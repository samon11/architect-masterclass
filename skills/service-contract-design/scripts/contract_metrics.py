#!/usr/bin/env python3
"""Service contract metrics analyzer (Juval Lowy, IDesign).

Stdlib only. Measures contracts from a JSON spec or from interface source code
(C#, Java, TypeScript) and reports the metrics that can falsify a design:

  operations per contract      target 3-5, reject at 12+, never 20+
  property-like operations     avoid (Get/Set pairs, properties on contracts)
  arguments per operation      ~0.7 or less, counting data-contract fields
  contracts per service        ~2 (rises toward platform/fractal scale)
  CRUD/I-O verbs on ResourceAccess, single-operation contracts,
  operations duplicated across contracts (factor-up candidates)

Optional history data ranks contracts best-to-worst (the sorting method).

Usage:
  contract_metrics.py spec.json [--out DIR]
  contract_metrics.py --source DIR_OR_FILES... [--out DIR] [--history history.json]

Meeting the metrics does not make a design good. Violating them makes it bad.
"""
import argparse
import json
import os
import re
import sys

# Case-insensitive prefix so camelCase (Java, TypeScript) matches too.
PROPERTY_LIKE = re.compile(r"^(?i:get|set|is|has)[A-Z]")
CRUD_IO = re.compile(r"^(?i:select|insert|update|delete|create|read|write|load|store|save|seek|"
                     r"fetch|query|get|set|put|post|open|close)(?=[A-Z_]|$)")



def fail(msg):
    sys.exit("error: " + msg)


# --------------------------------------------------------------------------- source parsing

def strip_comments(src):
    src = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
    return re.sub(r"//[^\n]*", "", src)


def balanced_body(src, start):
    """Return (body, end) for the {...} block whose '{' is at or after start."""
    i = src.find("{", start)
    if i < 0:
        return "", start
    depth = 0
    for j in range(i, len(src)):
        if src[j] == "{":
            depth += 1
        elif src[j] == "}":
            depth -= 1
            if depth == 0:
                return src[i + 1:j], j + 1
    return src[i + 1:], len(src)


def split_params(s):
    out, depth, cur = [], 0, ""
    for ch in s:
        if ch in "<([{":
            depth += 1
        elif ch in ">)]}":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur)
    return [p.strip() for p in out if p.strip()]


def param_type(p, lang):
    p = re.sub(r"\s*=.*$", "", p)          # default values
    p = re.sub(r"^\s*(@\w+(\([^)]*\))?\s*)+", "", p)  # Java annotations
    p = re.sub(r"^\s*(\[[^\]]*\]\s*)+", "", p)        # C# attributes
    p = re.sub(r"^(ref|out|in|params|final|readonly)\s+", "", p)
    if lang == "ts":
        m = re.match(r"\.{0,3}\w+\??\s*:\s*(.+)$", p)
        return m.group(1).strip() if m else "any"
    parts = p.rsplit(None, 1)
    return parts[0] if len(parts) == 2 else p


def base_type(t):
    t = re.sub(r"\[\]|\?$", "", t.strip())
    m = re.match(r"(?:Task|Promise|Optional|List|IEnumerable|IList|Array|ICollection|"
                 r"ReadonlyArray|Set|IReadOnlyList)<\s*(.+)\s*>$", t)
    return base_type(m.group(1)) if m else t


def parse_source(path, text, lang):
    """Very small heuristic parser: interfaces, their members, data types and
    which classes implement which interfaces."""
    src = strip_comments(text)
    contracts, types, impls = [], {}, {}
    for m in re.finditer(r"\binterface\s+(\w+)(?:\s*<[^>{]*>)?\s*(?:(?:extends|:)\s*([\w\s,<>.]+?))?\s*\{",
                         src):
        name = m.group(1)
        bases = [b.strip() for b in re.split(r",", m.group(2) or "") if b.strip()]
        body, _ = balanced_body(src, m.end() - 1)
        ops, props = [], []
        for stmt in [s.strip() for s in re.split(r";|\n(?=\s*\w)", body) if s.strip()]:
            stmt = re.sub(r"^\s*(\[[^\]]*\]\s*)+", "", stmt)        # [OperationContract]
            stmt = re.sub(r"^\s*(@\w+(\([^)]*\))?\s*)+", "", stmt)  # @WebMethod
            if lang == "cs" and re.search(r"\{\s*(get|set|init)", stmt):
                props.append(re.findall(r"(\w+)\s*\{", stmt)[0])
                continue
            mm = re.match(r"(?:[\w<>\[\],.?\s]+?\s+)?(\w+)\s*(?:<[^>]*>)?\s*\(([^)]*)\)", stmt, re.S)
            if mm:
                ops.append({"name": mm.group(1),
                            "params": [{"type": param_type(p, lang)}
                                       for p in split_params(mm.group(2))]})
                continue
            if lang == "ts":
                pm = re.match(r"(?:readonly\s+)?(\w+)\??\s*:\s*([^(][^;]*)$", stmt)
                if pm and "=>" not in pm.group(2):
                    props.append(pm.group(1))
                elif pm:
                    ops.append({"name": pm.group(1), "params": []})
        fields = len(props)
        types[name] = fields
        contracts.append({"name": name, "operations": ops, "properties": props,
                          "bases": bases, "file": path})
    # Data contracts: classes / records / structs, counting their fields/properties.
    for m in re.finditer(r"\b(class|record|struct)\s+(\w+)\s*(\(([^)]*)\))?([^{;]*)", src):
        kind, name, _, rec_params, tail = m.groups()
        impl = re.findall(r"\w+", re.sub(r"<[^>]*>", "", re.sub(r"^.*?(:|implements|extends)", "", tail)
                                        if re.search(r":|implements|extends", tail) else ""))
        impl = [i for i in impl if i not in ("implements", "extends", "where", "class", "new")]
        if impl:
            impls[name] = impl
        if rec_params:
            types[name] = len(split_params(rec_params))
            continue
        body, _ = balanced_body(src, m.end())
        if lang == "cs":
            n = len(re.findall(r"\{\s*get", body)) + len(re.findall(
                r"^\s*public\s+(?!.*\()[\w<>\[\],?\s]+\s+\w+\s*;", body, re.M))
        elif lang == "java":
            n = len(re.findall(r"^\s*(?:private|public|protected)\s+(?!static)[\w<>\[\],\s]+\s+\w+\s*(=[^;]*)?;",
                               body, re.M))
        else:
            n = len(re.findall(r"^\s*(?:public\s+|readonly\s+)*\w+\??\s*:\s*[^(;]+;", body, re.M))
        types.setdefault(name, n)
    # TypeScript `type X = { ... }`
    for m in re.finditer(r"\btype\s+(\w+)\s*=\s*\{", src):
        body, _ = balanced_body(src, m.end() - 1)
        types[m.group(1)] = len([s for s in re.split(r"[;\n]", body) if ":" in s])
    return contracts, types, impls


def load_source(paths):
    exts = {".cs": "cs", ".java": "java", ".ts": "ts", ".tsx": "ts"}
    files = []
    for p in paths:
        if os.path.isdir(p):
            for root, dirs, names in os.walk(p):
                dirs[:] = [d for d in dirs if d not in ("node_modules", "bin", "obj", ".git",
                                                         "dist", "build", "target")]
                files += [os.path.join(root, n) for n in names if os.path.splitext(n)[1] in exts]
        else:
            files.append(p)
    contracts, types, impls = [], {}, {}
    for f in sorted(files):
        lang = exts.get(os.path.splitext(f)[1])
        if not lang:
            continue
        with open(f, encoding="utf-8", errors="replace") as fh:
            c, t, i = parse_source(f, fh.read(), lang)
        contracts += c
        types.update(t)
        impls.update(i)
    names = {c["name"] for c in contracts}
    services = []
    for cls, ifaces in sorted(impls.items()):
        mine = [i for i in ifaces if i in names]
        if mine:
            services.append({"name": cls, "contracts": mine, "layer": guess_layer(cls)})
    # Interface data types are not data contracts unless they only hold properties.
    data_types = {k: v for k, v in types.items()
                  if k not in names or not next(c for c in contracts if c["name"] == k)["operations"]}
    for c in contracts:
        for op in c["operations"]:
            for p in op["params"]:
                p["fields"] = data_types.get(base_type(p["type"]))
    return {"contracts": contracts, "services": services}


def guess_layer(name):
    for suffix, layer in (("Manager", "manager"), ("Engine", "engine"),
                          ("Access", "resourceaccess"), ("Client", "client")):
        if name.endswith(suffix):
            return layer
    return None


# --------------------------------------------------------------------------- metrics

def ops_verdict(n):
    if n == 0:
        return "empty", "error"
    if n == 1:
        return "single operation: red flag (speculative, near-duplicate, or amalgam?)", "warn"
    if n == 2:
        return "thin: look for a home with its kinsmen", "info"
    if n <= 5:
        return "target (3-5)", "ok"
    if n <= 8:
        return "acceptable", "ok"
    if n <= 11:
        return "a lot: factor down or sideways", "warn"
    if n < 20:
        return "too many: you'll be hard pressed to justify it", "error"
    return "reject: 20 or more is never acceptable", "error"


def effective_args(op):
    """Arguments counted as fields: a data contract with 6 fields counts 6 (no cheating
    by bundling parameters into one structure)."""
    raw = len(op.get("params", []))
    eff = 0
    for p in op.get("params", []):
        f = p.get("fields")
        eff += f if isinstance(f, int) and f > 0 else 1
    return raw, eff


def analyze(spec, history):
    contracts = spec.get("contracts", [])
    if not contracts:
        fail("no contracts found")
    services = spec.get("services", [])
    by_name = {c["name"]: c for c in contracts}
    users = {c["name"]: [] for c in contracts}
    for s in services:
        for cn in s.get("contracts", []):
            if cn in users:
                users[cn].append(s["name"])
    ra_contracts = {cn for s in services if (s.get("layer") or "").lower() in
                    ("resourceaccess", "ra") for cn in s.get("contracts", [])}
    ra_contracts |= {c["name"] for c in contracts if re.search(r"Access$", c["name"].lstrip("I"))}
    findings, rows = [], []
    op_owner = {}
    total_ops = total_raw = total_eff = 0
    for c in contracts:
        name = c["name"]
        ops = c.get("operations", [])
        n = len(ops)
        verdict, level = ops_verdict(n)
        if level in ("warn", "error"):
            findings.append((level, "ops-per-contract", "%s, %d operation(s): %s" % (name, n, verdict)))
        props = c.get("properties", [])
        plike = [o["name"] for o in ops if PROPERTY_LIKE.match(o["name"]) and
                 (len(o.get("params", [])) == 0 or o["name"][:3].lower() == "set")]
        if props:
            findings.append(("error", "properties", "%s exposes properties (%s). Properties imply "
                             "state and betray implementation. Interact through behavior" %
                             (name, ", ".join(props))))
        if plike:
            findings.append(("warn", "property-like", "%s has property-like operations (%s). "
                             "Tell, don't ask" % (name, ", ".join(plike))))
        if name in ra_contracts:
            crud = [o["name"] for o in ops if CRUD_IO.match(o["name"])]
            if crud:
                findings.append(("warn", "atomic-verbs", "%s (ResourceAccess) exposes CRUD/I-O "
                                 "operations (%s). Expose atomic business verbs instead"
                                 % (name, ", ".join(crud))))
        c_raw = c_eff = 0
        for o in ops:
            raw, eff = effective_args(o)
            c_raw += raw
            c_eff += eff
            if eff >= 4:
                findings.append(("warn", "arguments", "%s.%s takes %d argument fields. The "
                                 "caller knows too much about the service" % (name, o["name"], eff)))
            op_owner.setdefault(o["name"], []).append(name)
        total_ops += n
        total_raw += c_raw
        total_eff += c_eff
        rows.append({"contract": name, "operations": n, "verdict": verdict,
                     "properties": len(props) + len(plike),
                     "args_per_op": round(c_eff / n, 2) if n else 0,
                     "implemented_by": users.get(name, []),
                     "bases": c.get("bases", [])})
    for op, owners in sorted(op_owner.items()):
        if len(owners) > 1:
            findings.append(("info", "factor-up", "Operation %s appears in %s. If it means the "
                             "same thing, factor it up into a shared base contract"
                             % (op, ", ".join(owners))))
    for c in contracts:
        if services and not users.get(c["name"]) and not any(
                c["name"] in o.get("bases", []) for o in contracts):
            findings.append(("info", "unused", "%s isn't implemented by any service. Is it a "
                             "placeholder? Record why it exists" % c["name"]))
    summary = {
        "contracts": len(contracts),
        "services": len(services),
        "operations": total_ops,
        "ops_per_contract": round(total_ops / len(contracts), 2),
        "args_per_op_raw": round(total_raw / total_ops, 2) if total_ops else 0,
        "args_per_op_fields": round(total_eff / total_ops, 2) if total_ops else 0,
        "contracts_per_service": round(sum(len(s.get("contracts", [])) for s in services)
                                       / len(services), 2) if services else None,
    }
    if summary["args_per_op_fields"] > 1.0:
        findings.append(("warn", "arguments", "Average %.2f argument fields per operation (target "
                         "about 0.7, under 1)" % summary["args_per_op_fields"]))
    cps = summary["contracts_per_service"]
    if cps is not None and cps < 1.5:
        findings.append(("info", "contracts-per-service", "%.2f contracts per service. Expect "
                         "about 2: a business contract plus a plumbing/diagnostics one" % cps))
    if cps is not None and cps > 3.5:
        findings.append(("warn", "contracts-per-service", "%.2f contracts per service is high "
                         "unless this is a platform or system of systems. Contracts may be "
                         "over-fractured" % cps))
    single = sum(1 for r in rows if r["operations"] == 1)
    if len(rows) >= 4 and single / len(rows) > 0.3:
        findings.append(("warn", "fracturing", "%d of %d contracts have a single operation. "
                         "Factoring down, sideways and up only makes contracts smaller, so the "
                         "design has fractured into an explosion of little things" % (single, len(rows))))
    ranking = rank(rows, history) if history else None
    return summary, rows, findings, ranking


def rank(rows, history):
    """Sorting method: weight several measurements, normalize, sort worst first.
    Higher complexity/defects/time/changes are worse; higher reuse is better."""
    keys = {"complexity": 1.0, "defects": 1.0, "implementation_days": 1.0, "changes": 1.0,
            "reuse": 1.0}
    keys.update(history.get("weights", {}))
    data = history.get("contracts", {})
    for r in rows:
        r.setdefault("reuse_calc", len(r["implemented_by"]))
    maxes = {k: max([float(data.get(r["contract"], {}).get(k, r["reuse_calc"] if k == "reuse" else 0))
                     for r in rows] + [1e-9]) for k in keys}
    scored = []
    for r in rows:
        d = data.get(r["contract"], {})
        bad = 0.0
        for k, w in keys.items():
            v = float(d.get(k, r["reuse_calc"] if k == "reuse" else 0)) / maxes[k]
            bad += w * ((1 - v) if k == "reuse" else v)
        scored.append((round(bad / sum(keys.values()), 3), r["contract"]))
    return sorted(scored, reverse=True)


# --------------------------------------------------------------------------- report

def report(summary, rows, findings, ranking):
    md = ["# Contract Metrics", "",
          "> Meeting the metrics doesn't make a design good. Violating them makes it bad.", "",
          "| Metric | Value | Guideline |", "|---|---|---|",
          "| Contracts | %d | |" % summary["contracts"],
          "| Services | %s | |" % (summary["services"] or "n/a"),
          "| Operations per contract (avg) | %s | 3-5 ideal, 12+ reject, 20+ never |" % summary["ops_per_contract"],
          "| Arguments per operation (params) | %s | |" % summary["args_per_op_raw"],
          "| Arguments per operation (fields) | %s | about 0.7, under 1 |" % summary["args_per_op_fields"],
          "| Contracts per service | %s | about 2 (more at platform scale) |" % (
              summary["contracts_per_service"] if summary["contracts_per_service"] is not None else "n/a"),
          "", "## Contracts", "",
          "| Contract | Ops | Verdict | Property-like | Args/op | Implemented by |",
          "|---|---|---|---|---|---|"]
    for r in sorted(rows, key=lambda r: -r["operations"]):
        md.append("| %s | %d | %s | %d | %s | %s |" % (
            r["contract"], r["operations"], r["verdict"], r["properties"], r["args_per_op"],
            ", ".join(r["implemented_by"]) or "-"))
    md += ["", "## Findings", ""]
    order = {"error": 0, "warn": 1, "info": 2}
    if findings:
        md += ["| Level | Rule | Finding |", "|---|---|---|"]
        for lvl, rule, msg in sorted(findings, key=lambda f: order[f[0]]):
            md.append("| %s | `%s` | %s |" % (lvl, rule, msg))
    else:
        md.append("No metric violations.")
    if ranking:
        md += ["", "## Ranking, worst to best (sorting method)", "",
               "| Rank | Contract | Badness (0-1) |", "|---|---|---|"]
        for i, (score, name) in enumerate(ranking, 1):
            md.append("| %d | %s | %s |" % (i, name, score))
        md += ["", "Worst: used in one place and changed every day. Best: never changed, "
               "and used everywhere all the time."]
    md += ["", "## Questions the metrics can't answer", "",
           "For each contract: is it **logically consistent**, **cohesive** (no more, no less), "
           "and an **independent facet**? Is it **reusable**? Does it support the core use "
           "cases (validation)? All four conditions must hold."]
    return "\n".join(md) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec", nargs="?", help="JSON contract spec")
    ap.add_argument("--source", nargs="+", help="source files or directories (.cs .java .ts)")
    ap.add_argument("--history", help="JSON with per-contract history for ranking")
    ap.add_argument("--out", default="contract-metrics-output")
    args = ap.parse_args()
    if bool(args.spec) == bool(args.source):
        ap.error("give either a JSON spec or --source")
    if args.spec:
        with open(args.spec) as f:
            spec = json.load(f)
    else:
        spec = load_source(args.source)
    history = None
    if args.history:
        with open(args.history) as f:
            history = json.load(f)
    summary, rows, findings, ranking = analyze(spec, history)
    os.makedirs(args.out, exist_ok=True)
    text = report(summary, rows, findings, ranking)
    with open(os.path.join(args.out, "report.md"), "w") as f:
        f.write(text)
    with open(os.path.join(args.out, "metrics.json"), "w") as f:
        json.dump({"summary": summary, "contracts": rows,
                   "findings": [{"level": l, "rule": r, "message": m} for l, r, m in findings],
                   "ranking": ranking, "parsed": spec if args.source else None}, f, indent=2)
    print(text.split("## Contracts")[0].strip())
    for lvl, rule, msg in findings:
        if lvl != "info":
            print("  [%s] %s: %s" % (lvl, rule, msg))
    print("\nwrote %s/report.md and metrics.json" % args.out)
    sys.exit(1 if any(f[0] == "error" for f in findings) else 0)


if __name__ == "__main__":
    main()
