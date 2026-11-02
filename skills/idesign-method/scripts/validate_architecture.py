#!/usr/bin/env python3
"""Validate an IDesign Method architecture and its call chains.

Stdlib only. Usage:

  validate_architecture.py architecture.json [--out DIR]

Checks the closed-architecture call rules, the method's "don'ts", naming,
component counts and the manager/engine ratio, and flags unused components and
asymmetric call chains. Writes report.md with a Mermaid static architecture
diagram and one Mermaid call-chain diagram per use case.

See ../references/architecture-format.md for the schema.
"""
import argparse
import json
import os
import re
import sys

LAYERS = ["client", "manager", "engine", "resourceaccess", "resource", "utility"]
RANK = {"client": 0, "manager": 1, "engine": 2, "resourceaccess": 3, "resource": 4}
ALIASES = {
    "clients": "client", "ui": "client",
    "managers": "manager",
    "engines": "engine",
    "ra": "resourceaccess", "resource_access": "resourceaccess", "resource access": "resourceaccess",
    "access": "resourceaccess",
    "resources": "resource", "db": "resource",
    "utilities": "utility", "util": "utility",
}
CALL_TYPES = {"sync", "queued", "async", "publish"}
CRUD_IO = re.compile(r"^(Select|Insert|Update|Delete|Create|Read|Write|Load|Store|Save|Seek|"
                     r"Fetch|Query|Get|Set|Put|Post|Open|Close)[A-Z_]?", re.I)
ABBR = {"client": "C", "manager": "M", "engine": "E", "resourceaccess": "RA",
        "resource": "R", "utility": "U"}
FIB_ENGINES = {1: (0, 1), 2: (1, 1), 3: (1, 2), 4: (2, 3), 5: (2, 3)}


def fail(msg):
    sys.exit("error: " + msg)


def layer_of(raw):
    key = str(raw).strip().lower()
    key = ALIASES.get(key, key)
    if key not in LAYERS:
        fail("unknown layer %r (use one of %s)" % (raw, ", ".join(LAYERS)))
    return key


class Findings:
    def __init__(self):
        self.items = []

    def add(self, level, rule, msg):
        self.items.append((level, rule, msg))

    def count(self, level):
        return sum(1 for i in self.items if i[0] == level)


def check_call(f, comps, uc, call):
    a, b = call.get("from"), call.get("to")
    kind = call.get("type", "sync")
    if a not in comps or b not in comps:
        f.add("error", "unknown-component", "%s: call %s -> %s references an undeclared component"
              % (uc, a, b))
        return
    if kind not in CALL_TYPES:
        f.add("error", "call-type", "%s: unknown call type %r on %s -> %s" % (uc, kind, a, b))
        return
    la, lb = comps[a]["layer"], comps[b]["layer"]
    where = "%s: %s (%s) -> %s (%s)" % (uc, a, la, b, lb)

    if kind == "async":
        f.add("warn", "async", where + " is an async call. Prefer sync or queued calls.")

    if kind == "publish":
        if lb != "utility":
            f.add("error", "publish-target", where + " publishes to something that is not a "
                  "pub/sub utility")
        if la != "manager":
            f.add("error", "dont-publish", where + ": only managers publish events "
                  "(clients, engines, resource access and resources never do)")
        return

    if la == "resource":
        f.add("error", "resource-calls", where + ": resources don't call anything "
              "(no triggers publishing events, no callbacks)")
        return

    if lb == "utility":
        return  # utilities are a vertical bar every layer may call

    if la == "utility":
        f.add("error", "utility-calls-business", where + ": a utility calls business components. "
              "Utilities must be usable in any system (the cappuccino-machine test)")
        return

    ra, rb = RANK[la], RANK[lb]
    if rb < ra:
        f.add("error", "call-up", where + ": calling up imports volatility into a lower layer")
        return

    if kind == "queued":
        if lb in ("engine", "resourceaccess"):
            f.add("error", "dont-queue", where + ": never queue calls to engines or resource "
                  "access. A queued call stands alone, and an engine or RA only means something "
                  "inside a manager's use case")
        elif la == "client" and lb == "manager":
            pass
        elif la == "manager" and lb == "manager":
            pass  # queued sideways call between managers is the sanctioned escape hatch
        return

    if la == lb:
        if la == "manager":
            f.add("error", "sideways", where + ": a sync call between managers makes the callee an "
                  "activity of the caller (functional decomposition). Queue it, or publish an event")
        elif la == "engine":
            f.add("error", "sideways", where + ": engines call engines. An engine is an activity; "
                  "everything about it should be inside it")
        elif la == "resourceaccess":
            f.add("error", "sideways", where + ": RA calls RA. It's no longer atomic. Have the "
                  "manager or engine call both")
        else:
            f.add("error", "sideways", where + ": sideways call")
        return

    allowed = {
        ("client", "manager"),
        ("manager", "engine"), ("manager", "resourceaccess"),
        ("engine", "resourceaccess"),
        ("resourceaccess", "resource"),
    }
    if (la, lb) not in allowed:
        hint = {
            ("client", "engine"): "business logic will move into the client",
            ("client", "resourceaccess"): "business logic will move into the client",
            ("client", "resource"): "the client depends on storage directly",
            ("manager", "resource"): "go through resource access",
            ("engine", "resource"): "go through resource access; a schema change would break the engine",
        }.get((la, lb), "skips layers")
        f.add("error", "skip-layer", where + ": " + hint)


def check_use_case(f, comps, uc):
    name = uc.get("name", "?")
    calls = uc.get("calls", [])
    if not calls:
        f.add("warn", "empty-use-case", "%s has no call chain. If you can't draw one, the "
              "design can't support the use case" % name)
        return
    for c in calls:
        check_call(f, comps, name, c)
    # A client should enter through one manager per use case.
    entry = {c["to"] for c in calls if c.get("from") in comps and c.get("to") in comps and
             comps[c["from"]]["layer"] == "client" and comps[c["to"]]["layer"] == "manager"}
    if len(entry) > 1:
        f.add("error", "client-stitching", "%s: the client calls %d managers (%s) in one use "
              "case. The client is stitching the workflow, so business logic is in the client"
              % (name, len(entry), ", ".join(sorted(entry))))
    # Zero-one-infinity: queuing to several managers means publish instead.
    for m in {c["from"] for c in calls if c.get("from") in comps and comps[c["from"]]["layer"] == "manager"}:
        queued = {c["to"] for c in calls if c.get("from") == m and c.get("type") == "queued"
                  and c.get("to") in comps and comps[c["to"]]["layer"] == "manager"}
        if len(queued) > 1:
            f.add("warn", "zero-one-infinity", "%s: %s queues to %d managers. When a manager "
                  "notifies more than one, publish an event instead" % (name, m, len(queued)))
    # Double-back smell: the same engine called first and last by the manager.
    seq = [c["to"] for c in calls if c.get("to") in comps and comps[c["to"]]["layer"] == "engine"]
    if len(seq) >= 3 and seq[0] == seq[-1]:
        f.add("warn", "double-back", "%s: %s is called first and last. Use cases may be "
              "commingled, or state management is broken" % (name, seq[0]))


def check_structure(f, comps, use_cases):
    by_layer = {l: [n for n, c in comps.items() if c["layer"] == l] for l in LAYERS}
    m, e = len(by_layer["manager"]), len(by_layer["engine"])
    if m == 0:
        f.add("error", "no-manager", "No managers. Something must encapsulate the sequence "
              "of the use cases")
    if m >= 8:
        f.add("error", "too-many-managers", "%d managers. With 8 or more the design has already "
              "failed: split it into a system of systems" % m)
    elif m >= 5:
        f.add("warn", "many-managers", "%d managers. That's a stretch, likely a system of "
              "systems" % m)
    if 1 <= m <= 5:
        lo, hi = FIB_ENGINES[m]
        if e > hi + 1:
            f.add("warn", "engine-ratio", "%d managers with %d engines (expected about %d-%d). "
                  "Engines may be functional decomposition: does each one encapsulate an "
                  "open-ended activity, or just a variable one (a switch statement)?" % (m, e, lo, hi))
    total = sum(len(by_layer[l]) for l in ("manager", "engine", "resourceaccess", "utility"))
    if total > 25:
        f.add("warn", "component-count", "%d services. A composable design is usually on the "
              "order of 10. Look for functional decomposition or speculative boxes" % total)
    for n in by_layer["manager"] + by_layer["resourceaccess"]:
        stem = re.sub(r"(Manager|Access)$", "", n)
        if re.search(r"ing$", stem) or re.match(r"^(Calculate|Process|Handle|Do|Create|Update|"
                                                 r"Validate|Send|Get)", stem):
            f.add("warn", "naming", "%s: managers and resource access should be named with nouns "
                  "(AccountManager, AccountAccess). A verb usually means functional "
                  "decomposition" % n)
    for n in by_layer["engine"]:
        if not n.endswith("Engine"):
            f.add("info", "naming", "%s: engines are usually named after their activity "
                  "(PricingEngine)" % n)
    for n in by_layer["resourceaccess"]:
        for op in comps[n].get("operations", []):
            if CRUD_IO.match(op):
                f.add("warn", "atomic-verbs", "%s.%s: resource access should expose atomic "
                      "business verbs (Credit, Debit), not CRUD or I/O" % (n, op))
    for n, c in comps.items():
        if c["layer"] in ("manager", "engine", "resourceaccess") and not c.get("volatility"):
            f.add("info", "volatility", "%s: record which volatility it encapsulates. If you "
                  "can't name one, it shouldn't be a block" % n)
    used = set()
    for uc in use_cases:
        for c in uc.get("calls", []):
            used.add(c.get("from"))
            used.add(c.get("to"))
    for n, c in comps.items():
        if n not in used and c["layer"] != "resource":
            f.add("warn", "unused", "%s isn't used by any core use case. Validate a use case "
                  "that needs it, or throw it away" % n)
    for uc in use_cases:
        for c in uc.get("calls", []):
            if c.get("from") in comps and comps[c["from"]]["layer"] == "client":
                break
        else:
            if uc.get("calls"):
                f.add("info", "no-client", "%s: no client call. Is something triggering it "
                      "(a queue, a timer)?" % uc.get("name"))


def symmetry(comps, use_cases):
    """Label-free shape of each use case: which layers call which, and how."""
    sig = {}
    for uc in use_cases:
        edges = sorted({"%s>%s:%s" % (ABBR[comps[c["from"]]["layer"]], ABBR[comps[c["to"]]["layer"]],
                                      c.get("type", "sync")[0])
                        for c in uc.get("calls", []) if c.get("from") in comps and c.get("to") in comps})
        publishes = any(c.get("type") == "publish" for c in uc.get("calls", []))
        sig[uc.get("name", "?")] = (" ".join(edges), publishes)
    return sig


def mid(name):
    return re.sub(r"[^A-Za-z0-9_]", "_", name)


def mermaid_static(comps):
    out = ["flowchart TB"]
    titles = {"client": "Clients", "manager": "Managers", "engine": "Engines",
              "resourceaccess": "Resource Access", "resource": "Resources",
              "utility": "Utilities"}
    for l in LAYERS:
        names = [n for n, c in comps.items() if c["layer"] == l]
        if not names:
            continue
        out.append('    subgraph %s["%s"]' % (l, titles[l]))
        out.append("        direction LR")
        for n in names:
            shape = '[("%s")]' % n if l == "resource" else '["%s"]' % n
            out.append("        %s%s" % (mid(n), shape))
        out.append("    end")
    order = [l for l in LAYERS if any(c["layer"] == l for c in comps.values())]
    for a, b in zip(order, order[1:]):
        if a != "resource" and b != "utility":
            out.append("    %s ~~~ %s" % (a, b))
    return "\n".join(out)


def mermaid_chain(comps, uc):
    out = ["flowchart TB"]
    seen = []
    for c in uc.get("calls", []):
        for n in (c.get("from"), c.get("to")):
            if n in comps and n not in seen:
                seen.append(n)
    for n in seen:
        l = comps[n]["layer"]
        shape = '[("%s")]' % n if l == "resource" else '["%s"]' % n
        out.append("    %s%s:::%s" % (mid(n), shape, l))
    for c in uc.get("calls", []):
        if c.get("from") not in comps or c.get("to") not in comps:
            continue
        kind = c.get("type", "sync")
        arrow = {"sync": "-->", "queued": "-.->", "async": "-.->", "publish": "-.->"}[kind]
        label = "" if kind == "sync" else "|%s|" % kind
        out.append("    %s %s%s %s" % (mid(c["from"]), arrow, label, mid(c["to"])))
    out += ["    classDef client fill:#dbe9f6,stroke:#2f6fb0,color:#1d1d1b",
            "    classDef manager fill:#f6e3c6,stroke:#c9821c,color:#1d1d1b",
            "    classDef engine fill:#e7dcf3,stroke:#8a5cc2,color:#1d1d1b",
            "    classDef resourceaccess fill:#d9eedf,stroke:#3a9a5b,color:#1d1d1b",
            "    classDef resource fill:#e6e4df,stroke:#6b6b66,color:#1d1d1b",
            "    classDef utility fill:#f3dada,stroke:#d64545,color:#1d1d1b"]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("architecture")
    ap.add_argument("--out", default="idesign-output")
    args = ap.parse_args()
    with open(args.architecture) as fh:
        arch = json.load(fh)
    comps = {}
    for c in arch.get("components", []):
        if "name" not in c or "layer" not in c:
            fail("every component needs 'name' and 'layer': %r" % c)
        if c["name"] in comps:
            fail("duplicate component %s" % c["name"])
        comps[c["name"]] = dict(c, layer=layer_of(c["layer"]))
    if not comps:
        fail("no components")
    use_cases = arch.get("use_cases", [])
    f = Findings()
    for uc in use_cases:
        check_use_case(f, comps, uc)
    check_structure(f, comps, use_cases)
    sig = symmetry(comps, use_cases)
    pub = [n for n, s in sig.items() if s[1]]
    if pub and len(pub) < len(sig) and len(sig) >= 3:
        f.add("info", "asymmetry", "Only %d of %d use cases publish an event (%s). Asymmetry is "
              "a red flag: confirm it's intentional" % (len(pub), len(sig), ", ".join(pub)))
    shapes = {}
    for n, s in sig.items():
        shapes.setdefault(s[0], []).append(n)

    os.makedirs(args.out, exist_ok=True)
    title = arch.get("system", "System")
    md = ["# %s — Architecture Validation" % title, "",
          "**%d errors, %d warnings, %d notes.** %s" % (
              f.count("error"), f.count("warn"), f.count("info"),
              "No rule violations. That doesn't make the design good, but violations would have "
              "made it bad." if not f.count("error") else
              "Every error is a closed-architecture or method violation. Fix the design, not "
              "the rule."), ""]
    counts = {l: sum(1 for c in comps.values() if c["layer"] == l) for l in LAYERS}
    md += ["| Layer | Count |", "|---|---|"] + ["| %s | %d |" % (l, counts[l]) for l in LAYERS]
    md += ["", "## Findings", ""]
    if f.items:
        md += ["| Level | Rule | Finding |", "|---|---|---|"]
        for lvl, rule, msg in sorted(f.items, key=lambda i: ["error", "warn", "info"].index(i[0])):
            md.append("| %s | `%s` | %s |" % (lvl, rule, msg.replace("|", "\\|")))
    else:
        md.append("None.")
    md += ["", "## Static architecture", "", "```mermaid", mermaid_static(comps), "```"]
    md += ["", "## Call-chain shapes", "",
           "Use cases with the same label-free shape are grouped together. A good design repeats "
           "a few shapes.", "", "| Shape | Use cases |", "|---|---|"]
    for s, names in sorted(shapes.items(), key=lambda kv: -len(kv[1])):
        md.append("| `%s` | %s |" % (s or "(empty)", ", ".join(names)))
    for uc in use_cases:
        md += ["", "## Call chain: %s" % uc.get("name", "?"), "", "```mermaid",
               mermaid_chain(comps, uc), "```"]
    path = os.path.join(args.out, "report.md")
    with open(path, "w") as fh:
        fh.write("\n".join(md) + "\n")
    print("\n".join(md[:3]))
    for lvl, rule, msg in f.items:
        if lvl != "info":
            print("  [%s] %s: %s" % (lvl, rule, msg))
    print("\nwrote " + path)
    sys.exit(1 if f.count("error") else 0)


if __name__ == "__main__":
    main()
