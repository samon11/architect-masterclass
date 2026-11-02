#!/usr/bin/env python3
"""Project design calculator for the IDesign Method (Juval Lowy, "Righting Software").

Stdlib only. Two commands:

  plan   network.json  [--out DIR]   critical path, float, float-based staffing,
                                     cost, planned earned value, charts
  track  network.json status.json [--out DIR]
                                     planned vs actual progress vs actual effort,
                                     projected finish, tracking-symptom diagnosis

See ../references/input-format.md for the JSON schemas.
"""
import argparse
import csv
import json
import math
import os
import sys

FLOAT_COLORS = {  # heat map: black critical, red low, yellow medium, green high
    "critical": "#1f1f1f",
    "low": "#d64545",
    "medium": "#e0a526",
    "high": "#3a9a5b",
}


# --------------------------------------------------------------------------- input

def load_json(path):
    with open(path) as f:
        return json.load(f)


def fail(msg):
    sys.exit("error: " + msg)


def normalize(net):
    acts = net.get("activities")
    if not acts:
        fail("network has no 'activities'")
    by_id = {}
    for a in acts:
        if "id" not in a or "duration" not in a:
            fail("every activity needs 'id' and 'duration': %r" % a)
        aid = str(a["id"])
        if aid in by_id:
            fail("duplicate activity id %s" % aid)
        by_id[aid] = {
            "id": aid,
            "name": a.get("name", aid),
            "duration": float(a["duration"]),
            "depends_on": [str(d) for d in a.get("depends_on", [])],
            "staff": float(a.get("staff", 1 if float(a["duration"]) > 0 else 0)),
            # "developer" draws from the capped developer pool. "core" work is done by
            # the core team (architect, PM), already counted via core_team, so it
            # earns value but adds no staffing. Any other role (tester, ...) adds
            # staffing but is not capped.
            "role": a.get("role", "developer"),
        }
    for a in by_id.values():
        for d in a["depends_on"]:
            if d not in by_id:
                fail("activity %s depends on unknown activity %s" % (a["id"], d))
    return by_id


def topo_order(acts):
    indeg = {k: len(v["depends_on"]) for k, v in acts.items()}
    succ = {k: [] for k in acts}
    for a in acts.values():
        for d in a["depends_on"]:
            succ[d].append(a["id"])
    ready = [k for k in acts if indeg[k] == 0]
    order = []
    while ready:
        ready.sort()
        k = ready.pop(0)
        order.append(k)
        for s in succ[k]:
            indeg[s] -= 1
            if indeg[s] == 0:
                ready.append(s)
    if len(order) != len(acts):
        cyc = sorted(k for k in acts if indeg[k] > 0)
        fail("dependency cycle among: " + ", ".join(cyc))
    return order, succ


# --------------------------------------------------------------------------- CPM

def critical_path(acts):
    order, succ = topo_order(acts)
    for k in order:
        a = acts[k]
        a["es"] = max([acts[d]["ef"] for d in a["depends_on"]] or [0.0])
        a["ef"] = a["es"] + a["duration"]
    finish = max(a["ef"] for a in acts.values())
    for k in reversed(order):
        a = acts[k]
        a["lf"] = min([acts[s]["ls"] for s in succ[k]] or [finish])
        a["ls"] = a["lf"] - a["duration"]
        a["float"] = round(a["ls"] - a["es"], 6)
    # Walk one critical chain from a zero-float start to a zero-float end.
    path = []
    cur = min((a for a in acts.values() if not a["depends_on"] and a["float"] == 0),
              key=lambda a: a["id"], default=None)
    while cur is not None:
        path.append(cur["id"])
        nxt = [acts[s] for s in succ[cur["id"]]
               if acts[s]["float"] == 0 and abs(acts[s]["es"] - cur["ef"]) < 1e-9]
        cur = min(nxt, key=lambda a: a["id"]) if nxt else None
    return order, succ, finish, path


def float_band(f, finish, thresholds=None):
    if f <= 1e-9:
        return "critical"
    lo, hi = thresholds or (0.1 * finish, 0.3 * finish)
    if f <= lo:
        return "low"
    if f <= hi:
        return "medium"
    return "high"


# --------------------------------------------------------------------------- staffing

def schedule(acts, succ, developers=None):
    """Event-driven list scheduling. Ready activities are staffed in ascending
    float order (critical first), ties by earliest start. Without a developer
    cap every activity starts as early as possible."""
    done_at = {}
    running = []  # (finish, id)
    started = set()
    free = float("inf") if developers is None else float(developers)
    t = 0.0
    while len(done_at) < len(acts):
        ready = [a for a in acts.values() if a["id"] not in started and
                 all(d in done_at and done_at[d] <= t + 1e-9 for d in a["depends_on"])]
        ready.sort(key=lambda a: (a["float"], a["es"], a["id"]))
        for a in ready:
            need = a["staff"] if a["role"] == "developer" else 0.0
            if developers is not None and need > developers:
                fail("activity %s needs %g developers but the cap is %g"
                     % (a["id"], need, developers))
            if need <= free + 1e-9:
                free -= need
                started.add(a["id"])
                a["start"] = t
                a["finish"] = t + a["duration"]
                running.append((a["finish"], a["id"]))
        if not running:
            fail("scheduler stalled at t=%g (check dependencies)" % t)
        running.sort()
        t = running[0][0]
        while running and running[0][0] <= t + 1e-9:
            _, aid = running.pop(0)
            done_at[aid] = t
            if acts[aid]["role"] == "developer":
                free += acts[aid]["staff"]
    return max(a["finish"] for a in acts.values())


def staffing_curve(acts, finish, core_team):
    periods = int(math.ceil(finish - 1e-9))
    rows = []
    for p in range(periods):
        lo, hi = float(p), float(p + 1)
        staff = core_team
        for a in acts.values():
            if a["role"] == "core":
                continue
            overlap = max(0.0, min(hi, a["finish"]) - max(lo, a["start"]))
            staff += overlap * a["staff"]
        rows.append(staff)
    return rows


def earned_value_curve(acts, finish):
    """Planned earned value: each activity is worth its share of total effort
    and is earned (binary) when it completes."""
    total = sum(a["duration"] * a["staff"] for a in acts.values()) or 1.0
    for a in acts.values():
        a["value"] = a["duration"] * a["staff"] / total
    periods = int(math.ceil(finish - 1e-9))
    curve = []
    for p in range(periods + 1):
        curve.append(sum(a["value"] for a in acts.values() if a["finish"] <= p + 1e-9))
    return curve


def shallow_s_check(curve):
    """Compare average slope of the first 20%, middle 60% and last 20%.
    A viable plan is a shallow S: gentle start, steep middle, gentle end."""
    n = len(curve) - 1
    if n < 5:
        return {"verdict": "too short to judge", "slopes": None}
    a, b = int(round(n * 0.2)), int(round(n * 0.8))
    s1 = (curve[a] - curve[0]) / max(a, 1)
    s2 = (curve[b] - curve[a]) / max(b - a, 1)
    s3 = (curve[n] - curve[b]) / max(n - b, 1)
    issues = []
    if s2 <= s1:
        issues.append("front-loaded: the start is as steep as the middle (no core-team ramp)")
    if s2 <= s3:
        issues.append("back-loaded: value piles up at the end (integration/'big bang' risk)")
    if s2 > 0 and s2 / max(s1, s3, 1e-9) < 1.3 and not issues:
        issues.append("nearly a straight line: weak S; check staffing ramp")
    return {"verdict": "shallow S" if not issues else "; ".join(issues),
            "slopes": [round(s1, 4), round(s2, 4), round(s3, 4)]}


# --------------------------------------------------------------------------- svg

def svg_chart(title, xlabel, series, y_max=None, y_fmt="{:g}", bars=None,
              width=760, height=340):
    """Tiny dependency-free SVG chart. series: [(label, color, [y...], dashed)],
    bars: (label, color, [y...]) drawn on a secondary right axis."""
    ml, mr, mt, mb = 60, 60 if bars else 20, 36, 46
    pw, ph = width - ml - mr, height - mt - mb
    n = max([len(s[2]) for s in series] + [len(bars[2]) if bars else 0])
    xs = lambda i: ml + pw * (i / max(n - 1, 1))
    ymax = y_max or max([max(s[2]) for s in series if s[2]] + [1e-9])
    ys = lambda v: mt + ph - ph * (v / ymax)
    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
           'font-family="system-ui,sans-serif" font-size="11">' % (width, height),
           '<text x="%d" y="20" font-size="14" font-weight="600" fill="currentColor">%s</text>'
           % (ml, title)]
    for k in range(5):
        v = ymax * k / 4
        y = ys(v)
        out.append('<line x1="%d" x2="%d" y1="%.1f" y2="%.1f" stroke="currentColor" '
                   'stroke-opacity="0.12"/>' % (ml, ml + pw, y, y))
        out.append('<text x="%d" y="%.1f" text-anchor="end" fill="currentColor" '
                   'fill-opacity="0.7">%s</text>' % (ml - 6, y + 4, y_fmt.format(v)))
    if bars:
        bmax = max(bars[2] + [1e-9])
        bw = pw / max(n, 1) * 0.8
        for i, v in enumerate(bars[2]):
            h = ph * v / bmax
            out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" '
                       'fill-opacity="0.35"/>' % (xs(i) - bw / 2, mt + ph - h, bw, h, bars[1]))
        for k in range(5):
            v = bmax * k / 4
            out.append('<text x="%d" y="%.1f" fill="%s">%g</text>'
                       % (ml + pw + 6, ys(ymax * k / 4) + 4, bars[1], round(v, 1)))
    step = max(1, n // 12)
    for i in range(0, n, step):
        out.append('<text x="%.1f" y="%d" text-anchor="middle" fill="currentColor" '
                   'fill-opacity="0.7">%d</text>' % (xs(i), mt + ph + 16, i))
    out.append('<text x="%.1f" y="%d" text-anchor="middle" fill="currentColor">%s</text>'
               % (ml + pw / 2, height - 8, xlabel))
    for label, color, ys_, dashed in series:
        pts = " ".join("%.1f,%.1f" % (xs(i), ys(v)) for i, v in enumerate(ys_))
        out.append('<polyline fill="none" stroke="%s" stroke-width="2.2" %s points="%s"/>'
                   % (color, 'stroke-dasharray="6 4"' if dashed else "", pts))
    lx = ml + 8
    legend = [(s[0], s[1]) for s in series] + ([(bars[0], bars[1])] if bars else [])
    for label, color in legend:
        out.append('<rect x="%d" y="%d" width="10" height="10" fill="%s"/>' % (lx, mt + 4, color))
        out.append('<text x="%d" y="%d" fill="currentColor">%s</text>' % (lx + 14, mt + 13, label))
        lx += 22 + 7 * len(label)
    out.append("</svg>")
    return "\n".join(out)


def html_page(title, sections):
    body = "\n".join("<section><h2>%s</h2>%s</section>" % (h, c) for h, c in sections)
    return """<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>%s</title>
<style>
:root{--bg:#fbfaf7;--fg:#1d1d1b;--muted:#6b6b66;--line:#e4e1da}
@media (prefers-color-scheme:dark){:root{--bg:#161615;--fg:#ecebe6;--muted:#a3a29b;--line:#2e2d2a}}
body{background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,sans-serif;margin:0 auto;max-width:900px;padding:24px 16px}
h1{font-size:22px}h2{font-size:16px;margin-top:32px}svg{width:100%%;height:auto;color:var(--fg)}
table{border-collapse:collapse;width:100%%;font-size:13px;display:block;overflow-x:auto}
td,th{border-bottom:1px solid var(--line);padding:4px 8px;text-align:left;white-space:nowrap}
.muted{color:var(--muted)}
</style></head><body><h1>%s</h1>%s</body></html>""" % (title, title, body)


def html_table(headers, rows):
    h = "".join("<th>%s</th>" % x for x in headers)
    r = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in row) for row in rows)
    return "<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>" % (h, r)


# --------------------------------------------------------------------------- outputs

def fmt(v):
    return ("%g" % round(v, 2))


def mermaid_network(acts, order, finish, path):
    lines = ["flowchart LR"]
    crit = set(path)
    for k in order:
        a = acts[k]
        label = "%s: %s<br/>d=%s float=%s" % (k, a["name"], fmt(a["duration"]), fmt(a["float"]))
        lines.append('    %s["%s"]' % (k, label.replace('"', "'")))
    for k in order:
        for d in acts[k]["depends_on"]:
            arrow = "==>" if d in crit and k in crit else "-->"
            lines.append("    %s %s %s" % (d, arrow, k))
    for band, color in FLOAT_COLORS.items():
        members = [k for k in order if acts[k]["band"] == band]
        if members:
            text = "#fff" if band in ("critical", "low", "high") else "#1d1d1b"
            lines.append("    classDef %s fill:%s,color:%s,stroke:%s" % (band, color, text, color))
            lines.append("    class %s %s" % (",".join(members), band))
    return "\n".join(lines)


def mermaid_xy(title, xlabel, ylabel, values, kind="line", y_max=None):
    n = len(values)
    step = max(1, n // 24)
    idx = list(range(0, n, step))
    if idx[-1] != n - 1:
        idx.append(n - 1)
    xs = ", ".join(str(i) for i in idx)
    ys = ", ".join(fmt(values[i]) for i in idx)
    top = y_max if y_max is not None else max(values + [1])
    return ('xychart-beta\n    title "%s"\n    x-axis "%s" [%s]\n    y-axis "%s" 0 --> %s\n'
            '    %s [%s]' % (title, xlabel, xs, ylabel, fmt(top), kind, ys))


def write(path, text):
    with open(path, "w") as f:
        f.write(text)


def canvas(acts, order, path, unit_px=40):
    """Obsidian JSON Canvas activity diagram: x by earliest start, colored by float."""
    color = {"critical": "1", "low": "1", "medium": "3", "high": "4"}  # red/yellow/green presets
    lanes, nodes, edges = {}, [], []
    for k in order:
        a = acts[k]
        col = round(a["es"], 3)
        lane = lanes.get(col, 0)
        lanes[col] = lane + 1
        nodes.append({"id": k, "type": "text", "x": int(a["es"] * unit_px),
                      "y": lane * 130, "width": 220, "height": 100,
                      "color": color[a["band"]],
                      "text": "**%s: %s**\nduration %s, float %s%s" % (
                          k, a["name"], fmt(a["duration"]), fmt(a["float"]),
                          "\n**critical**" if a["band"] == "critical" else "")})
    crit = set(path)
    for k in order:
        for d in acts[k]["depends_on"]:
            e = {"id": "%s-%s" % (d, k), "fromNode": d, "fromSide": "right",
                 "toNode": k, "toSide": "left", "toEnd": "arrow"}
            if d in crit and k in crit:
                e["color"] = "1"
            edges.append(e)
    return json.dumps({"nodes": nodes, "edges": edges}, indent=2)


def cmd_plan(args):
    net = load_json(args.network)
    acts = normalize(net)
    order, succ, cpm_finish, path = critical_path(acts)
    unit = net.get("time_unit", "days")
    rate = float(net.get("cost_per_unit", 0) or 0)
    core = float(net.get("core_team", 0) or 0)
    devs = args.developers if args.developers is not None else net.get("developers")
    thresholds = net.get("float_thresholds")
    for a in acts.values():
        a["band"] = float_band(a["float"], cpm_finish, thresholds)
    finish = schedule(acts, succ, devs)
    staff = staffing_curve(acts, finish, core)
    ev = earned_value_curve(acts, finish)
    s_check = shallow_s_check(ev)
    effort = sum(staff)
    cum_cost, run = [], 0.0
    for s in staff:
        run += s * rate
        cum_cost.append(run)
    peak = max(staff) if staff else 0
    avg = effort / len(staff) if staff else 0
    efficiency = (sum(a["duration"] * a["staff"] for a in acts.values()) / effort) if effort else 0
    name = net.get("project", "Project")
    out = args.out or "project-design-output"
    os.makedirs(out, exist_ok=True)

    # CSVs
    with open(os.path.join(out, "activities.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "name", "duration", "staff", "role", "depends_on", "es", "ef", "ls",
                    "lf", "float", "float_band", "scheduled_start", "scheduled_finish", "value_pct"])
        for k in order:
            a = acts[k]
            w.writerow([k, a["name"], fmt(a["duration"]), fmt(a["staff"]), a["role"],
                        " ".join(a["depends_on"]), fmt(a["es"]), fmt(a["ef"]), fmt(a["ls"]),
                        fmt(a["lf"]), fmt(a["float"]), a["band"], fmt(a["start"]),
                        fmt(a["finish"]), fmt(a["value"] * 100)])
    with open(os.path.join(out, "timeline.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["period", "staffing", "period_cost", "cumulative_cost", "planned_ev_pct"])
        for p, s in enumerate(staff):
            w.writerow([p + 1, fmt(s), fmt(s * rate), fmt(cum_cost[p]), fmt(ev[p + 1] * 100)])
    write(os.path.join(out, "activity-network.canvas"), canvas(acts, order, path))

    # Markdown report
    md = ["# %s — Project Design" % name, ""]
    md += ["| Metric | Value |", "|---|---|",
           "| Critical-path duration (unconstrained) | %s %s |" % (fmt(cpm_finish), unit),
           "| Scheduled duration%s | %s %s |" % (
               " (cap: %s developers)" % fmt(devs) if devs is not None else "", fmt(finish), unit),
           "| Critical path | %s |" % " → ".join(path),
           "| Total effort | %s person-%s |" % (fmt(effort), unit),
           "| Peak / average staffing | %s / %s |" % (fmt(peak), fmt(avg)),
           "| Efficiency (activity effort ÷ total effort) | %s%% |" % fmt(efficiency * 100)]
    if rate:
        md.append("| Total cost | %s |" % "{:,.0f}".format(cum_cost[-1] if cum_cost else 0))
    md.append("| Planned earned value shape | %s |" % s_check["verdict"])
    if devs is not None and finish > cpm_finish + 1e-9:
        md += ["", "> [!warning] Resource-constrained: the developer cap stretches the schedule "
               "%s %s past the critical path. Float was consumed; re-run the CPM on the "
               "scheduled network before committing." % (fmt(finish - cpm_finish), unit)]
    md += ["", "## Activities", "",
           "| ID | Activity | Dur | Staff | ES | EF | LS | LF | Float | Band | Start | Finish |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for k in sorted(order, key=lambda k: (acts[k]["float"], acts[k]["es"])):
        a = acts[k]
        md.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            k, a["name"], fmt(a["duration"]), fmt(a["staff"]), fmt(a["es"]), fmt(a["ef"]),
            fmt(a["ls"]), fmt(a["lf"]), fmt(a["float"]), a["band"], fmt(a["start"]),
            fmt(a["finish"])))
    md += ["", "_Sorted by float, low to high: this is the staffing priority order._", "",
           "## Network", "", "```mermaid", mermaid_network(acts, order, cpm_finish, path), "```",
           "", "## Staffing distribution", "", "```mermaid",
           mermaid_xy("Staffing", unit, "people", staff, "bar"), "```"]
    if rate:
        md += ["", "## Cumulative cost", "", "```mermaid",
               mermaid_xy("Cumulative cost", unit, "cost", cum_cost), "```"]
    md += ["", "## Planned earned value", "", "```mermaid",
           mermaid_xy("Planned earned value", unit, "% complete",
                      [v * 100 for v in ev], y_max=100), "```", "",
           "Slopes (first 20%% / middle 60%% / last 20%%): %s" % (s_check["slopes"],)]
    write(os.path.join(out, "report.md"), "\n".join(md) + "\n")

    # HTML with SVG charts
    sections = [
        ("Summary", html_table(["Metric", "Value"], [
            ["Critical path", " → ".join(path)],
            ["Duration", "%s %s (critical path %s)" % (fmt(finish), unit, fmt(cpm_finish))],
            ["Effort", "%s person-%s" % (fmt(effort), unit)],
            ["Peak / avg staffing", "%s / %s" % (fmt(peak), fmt(avg))],
            ["Total cost", "{:,.0f}".format(cum_cost[-1]) if rate and cum_cost else "n/a"],
            ["Earned value shape", s_check["verdict"]]])),
        ("Staffing and cost", svg_chart(
            "Staffing distribution and cumulative cost", unit,
            [("Cumulative cost", "#2f6fb0", [0.0] + cum_cost, False)] if rate else
            [("Cumulative effort", "#2f6fb0", [0.0] + [sum(staff[:i + 1]) for i in range(len(staff))], False)],
            bars=("Staffing", "#8a5cc2", [0.0] + staff))),
        ("Planned earned value", svg_chart(
            "Planned earned value (should be a shallow S)", unit,
            [("Planned EV %", "#2f6fb0", [v * 100 for v in ev], False)], y_max=100,
            y_fmt="{:.0f}%")),
        ("Activities by float", html_table(
            ["ID", "Activity", "Dur", "Float", "Band", "Start", "Finish"],
            [[k, acts[k]["name"], fmt(acts[k]["duration"]), fmt(acts[k]["float"]),
              '<span style="color:%s">●</span> %s' % (FLOAT_COLORS[acts[k]["band"]], acts[k]["band"]),
              fmt(acts[k]["start"]), fmt(acts[k]["finish"])]
             for k in sorted(order, key=lambda k: (acts[k]["float"], acts[k]["es"]))])),
    ]
    write(os.path.join(out, "charts.html"), html_page(name + " — Project Design", sections))
    print("\n".join(md[:12]))
    print("\nwrote %s/{report.md,charts.html,activities.csv,timeline.csv,activity-network.canvas}" % out)


# --------------------------------------------------------------------------- tracking

SYMPTOMS = {
    ("on", "on"): ("Healthy", "Do nothing. Don't disturb a healthy project."),
    ("below", "above"): ("Underestimation",
                         "Push the schedule out, or reduce scope to hold the date. "
                         "Re-plan and get a new sign-off."),
    ("below", "below"): ("Resource leak",
                         "Someone is taking your people. Find the 'vampire' and escalate to the "
                         "lowest common manager."),
    ("above", "above"): ("Overestimation",
                         "Release people (smaller teams are more efficient) or bring scope forward."),
    ("above", "on"): ("Ahead of plan", "Check for overestimation; consider releasing staff."),
    ("on", "above"): ("Effort overrun", "Watch for underestimation; progress may soon slip."),
    ("on", "below"): ("Under-staffed but on plan", "Verify effort is reported correctly."),
    ("below", "on"): ("Slipping", "Early underestimation signal; re-estimate remaining work."),
    ("above", "below"): ("Ahead with less effort",
                         "Overestimated work. Verify exit criteria are really met (no 90% lie)."),
}


def classify(actual, planned, tol):
    if planned <= 0:
        return "on"
    r = (actual - planned) / planned
    return "above" if r > tol else "below" if r < -tol else "on"


def cmd_track(args):
    net = load_json(args.network)
    status = load_json(args.status)
    acts = normalize(net)
    order, succ, cpm_finish, path = critical_path(acts)
    devs = net.get("developers")
    core = float(net.get("core_team", 0) or 0)
    finish = schedule(acts, succ, devs)
    staff = staffing_curve(acts, finish, core)
    ev = earned_value_curve(acts, finish)
    total_effort = sum(staff)
    unit = net.get("time_unit", "days")
    tol = float(status.get("tolerance", 0.05))
    reports = sorted(status.get("reports", []), key=lambda r: r["time"])
    if not reports:
        fail("status.json needs a non-empty 'reports' list")
    pts = []
    for r in reports:
        unknown = [c for c in r.get("completed", []) if c not in acts]
        if unknown:
            fail("report at t=%s lists unknown activities: %s" % (r["time"], unknown))
        prog = sum(acts[c]["value"] for c in r.get("completed", []))
        # Optional partial credit for in-progress activities, by completed phase weight.
        for aid, frac in r.get("partial", {}).items():
            if aid not in acts:
                fail("report at t=%s has partial credit for unknown activity %s" % (r["time"], aid))
            prog += acts[aid]["value"] * float(frac)
        eff = float(r.get("effort_to_date", 0)) / total_effort if total_effort else 0
        t = float(r["time"])
        i = min(int(math.floor(t)), len(ev) - 1)
        pv = ev[i]
        pts.append((t, pv, prog, eff))
    t, pv, prog, eff = pts[-1]
    key = (classify(prog, pv, tol), classify(eff, pv, tol))
    label, remedy = SYMPTOMS[key]
    # Projection: linear fit through the last up-to-3 progress points.
    recent = pts[-3:]
    proj = None
    if len(recent) >= 2:
        n = len(recent)
        mx = sum(p[0] for p in recent) / n
        my = sum(p[2] for p in recent) / n
        sxx = sum((p[0] - mx) ** 2 for p in recent)
        if sxx > 0:
            slope = sum((p[0] - mx) * (p[2] - my) for p in recent) / sxx
            if slope > 0:
                proj = mx + (1.0 - my) / slope
    elif prog > 0:
        proj = t / prog
    out = args.out or "project-tracking-output"
    os.makedirs(out, exist_ok=True)
    name = net.get("project", "Project")
    md = ["# %s — Tracking at %s %s" % (name, fmt(t), unit), "",
          "| Measure | Value |", "|---|---|",
          "| Planned earned value | %s%% |" % fmt(pv * 100),
          "| Actual progress | %s%% |" % fmt(prog * 100),
          "| Actual effort (of planned total) | %s%% |" % fmt(eff * 100),
          "| Planned finish | %s %s |" % (fmt(finish), unit),
          "| Projected finish (trend) | %s |" % ("%s %s" % (fmt(proj), unit) if proj else "n/a"),
          "| Diagnosis | **%s** (progress %s plan, effort %s plan) |" % (label, key[0], key[1]),
          "| Recommended action | %s |" % remedy,
          "", "## History", "", "| Time | Planned EV | Progress | Effort |", "|---|---|---|---|"]
    for p in pts:
        md.append("| %s | %s%% | %s%% | %s%% |" % (fmt(p[0]), fmt(p[1] * 100), fmt(p[2] * 100),
                                                   fmt(p[3] * 100)))
    write(os.path.join(out, "tracking.md"), "\n".join(md) + "\n")
    n = len(ev)
    # Sample actuals onto the period grid (step interpolation) for the SVG.
    prog_line, eff_line = [], []
    for i in range(n):
        known = [p for p in pts if p[0] <= i + 1e-9]
        if known and i <= t + 1e-9:
            prog_line.append(known[-1][2] * 100)
            eff_line.append(known[-1][3] * 100)
    series = [("Planned EV", "#2f6fb0", [v * 100 for v in ev], False),
              ("Actual progress", "#3a9a5b", prog_line, False),
              ("Actual effort", "#d64545", eff_line, False)]
    if proj and prog_line:
        last = prog_line[-1]
        k = len(prog_line) - 1
        proj_pts = [last + (100 - last) * (j - k) / max(proj - k, 1e-9)
                    for j in range(k, min(n, int(math.ceil(proj)) + 1))]
        series.append(("Projected", "#3a9a5b", [None] * k + proj_pts, True))
    sections = [("Status", html_table(["Measure", "Value"],
                                      [[r.split("|")[1].strip(), r.split("|")[2].strip()]
                                       for r in md[4:11]])),
                ("Progress vs effort vs plan", svg_tracking(series, unit))]
    write(os.path.join(out, "tracking.html"), html_page(name + " — Tracking", sections))
    print("\n".join(md[:12]))
    print("\nwrote %s/{tracking.md,tracking.html}" % out)


def svg_tracking(series, unit):
    """Like svg_chart, but series values may be None (not yet reported) and the
    y-axis is fixed at 0-120% so overruns stay visible."""
    cleaned = series
    width, height, ml, mr, mt, mb = 760, 340, 60, 20, 36, 46
    pw, ph = width - ml - mr, height - mt - mb
    n = max(len(s[2]) for s in cleaned)
    xs = lambda i: ml + pw * (i / max(n - 1, 1))
    ys = lambda v: mt + ph - ph * (min(v, 120) / 120.0)
    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
           'font-family="system-ui,sans-serif" font-size="11">' % (width, height)]
    for v in (0, 25, 50, 75, 100):
        out.append('<line x1="%d" x2="%d" y1="%.1f" y2="%.1f" stroke="currentColor" '
                   'stroke-opacity="0.12"/><text x="%d" y="%.1f" text-anchor="end" '
                   'fill="currentColor" fill-opacity="0.7">%d%%</text>'
                   % (ml, ml + pw, ys(v), ys(v), ml - 6, ys(v) + 4, v))
    step = max(1, n // 12)
    for i in range(0, n, step):
        out.append('<text x="%.1f" y="%d" text-anchor="middle" fill="currentColor" '
                   'fill-opacity="0.7">%d</text>' % (xs(i), mt + ph + 16, i))
    out.append('<text x="%.1f" y="%d" text-anchor="middle" fill="currentColor">%s</text>'
               % (ml + pw / 2, height - 8, unit))
    lx = ml + 8
    for label, color, vals, dashed in cleaned:
        pts = " ".join("%.1f,%.1f" % (xs(i), ys(v)) for i, v in enumerate(vals) if v is not None)
        out.append('<polyline fill="none" stroke="%s" stroke-width="2.2" %s points="%s"/>'
                   % (color, 'stroke-dasharray="6 4"' if dashed else "", pts))
        out.append('<rect x="%d" y="%d" width="10" height="10" fill="%s"/><text x="%d" y="%d" '
                   'fill="currentColor">%s</text>' % (lx, 8, color, lx + 14, 17, label))
        lx += 22 + 7 * len(label)
    out.append("</svg>")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("plan", help="design the project from an activity network")
    p.add_argument("network")
    p.add_argument("--out")
    p.add_argument("--developers", type=float, help="cap on concurrent developers (overrides JSON)")
    p.set_defaults(func=cmd_plan)
    t = sub.add_parser("track", help="compare status reports against the plan")
    t.add_argument("network")
    t.add_argument("status")
    t.add_argument("--out")
    t.set_defaults(func=cmd_track)
    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
