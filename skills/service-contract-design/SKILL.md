---
name: service-contract-design
description: Design, factor and review service contracts (interfaces) using Juval Lowy's IDesign approach. Covers the attributes of a good contract (logically consistent, cohesive, independent facets, reusable), factoring down, sideways and up, and the contract metrics (operations per contract, property-like operations, arguments per operation, contracts per service, atomic business verbs). Includes an analyzer that measures contracts from a JSON spec or from C#, Java and TypeScript source. Use when the user asks to design or review an API, interface or service contract, factor a fat interface, check contract metrics, rank contracts best to worst, or spot CRUD-style ResourceAccess.
---

# Service Contract Design and Factoring

Good services are hard to evaluate directly, so evaluate their contracts instead. A
contract is a formal interface that clients program against and depend on. Every contract
is an interface, but not every interface is a contract.

> Good contracts are **logically consistent, cohesive, independent facets** of the service.
> The ultimate litmus test is **reuse**.

Contracts come after the architecture. If there are no components yet, start with the
`idesign-method` skill. Contract count and size feed the effort estimates in `project-design`.

## The attributes

| Attribute | Question | Failure example |
|---|---|---|
| **Logically consistent** | Does every operation belong to this interaction? | An employment contract that requires your home address |
| **Cohesive** | Does it hold everything the interaction needs, no more and no less? | An employment contract that doesn't mention pay |
| **Independent facet** | Can it change without the service's other contracts changing? | A marriage contract conditional on your employer |
| **Reusable** | Could another service implement it, or another consumer use it, unchanged? | A contract "crafted just for you" |

Consistent + cohesive = **coherent**. A contract can be reusable without being reused yet,
and that's fine. Too big (a dumping ground) and too small (fitted to its neighbors) both
reduce reuse to zero. Overlapping contracts fail independence.

## Factoring techniques (the only three)

| Technique | Telltale | Action |
|---|---|---|
| **Down** | An operation that fits some implementers but feels wrong in others (`AdjustBeam` on a keypad) | Build a contract hierarchy. Push the offending operation into a derived contract |
| **Sideways** | Operations only weakly related to each other (`ReadCode` next to `OpenPort`/`ClosePort`) | Split into independent facets (`IReader`, `ICommunicationDevice`) |
| **Up** | The same related operations repeated across facets | Hoist them into a shared base contract |

Interface inheritance is fine. It's implementation inheritance that causes trouble. A service
can implement several contracts at no extra cost: the work inside it doesn't change, and
each facet becomes reusable.

A design law to keep in mind: if every new device or user-domain variation forces a contract
change, the design isn't resilient to changes in the user domain. Factor until new variants
only **implement** existing contracts.

## Metrics: they can only falsify

All three techniques make contracts **smaller**. Without a counterweight they splinter into an
explosion of little things. Metrics are that counterweight:

| Metric | Guideline |
|---|---|
| Operations per contract | **3 to 5** ideal. 6 is fine. 9 is a lot. 12 almost certainly rejected. **20 or more: never.** 1 is a red flag (speculative design, a near-duplicate, or an amalgam of several things given one name) |
| Property-like operations | Avoid. No properties on contracts and no `GetX`/`SetX` pairs. They imply state and expose implementation. Tell, don't ask |
| Arguments per operation | About **0.7**, below 1. Bundling 25 arguments into one struct is cheating: count the fields |
| Contracts per service | About **2**: a business contract plus a plumbing or diagnostics contract. Higher at platform scale |
| ResourceAccess operations | **Atomic business verbs** (`Credit`, `Debit`, `Reserve`), never CRUD or I/O (`Select`, `Insert`, `Read`, `Write`) |

> Meeting the metrics doesn't make a design good. Violating them makes it bad.
> (Normal body temperature doesn't prove you're healthy. A fever proves you're sick.)

**Never design for the metrics.** That's icing the thermometer. If you factor well, good
metrics follow.

## Workflow

### 1. Collect the contracts
Pick whichever input the user has:
- **Code:** run the analyzer on their source (C#, Java, TypeScript interfaces). It finds
  interfaces, operations, properties, data types (to count fields), and which classes
  implement which interfaces.
- **A design:** write the contracts as JSON (`references/spec-format.md`, example in `examples/contracts.json`).
- **Nothing yet:** start from the components and core use cases. Name things, sketch
  interaction diagrams, then write rough interfaces as code sketches. It's fine to begin with
  one ugly dumping ground, or many tiny obviously-unrelated contracts, as long as every operation exists somewhere.

### 2. Measure

```bash
python3 <skill-dir>/scripts/contract_metrics.py --source src/ --out <dir>
python3 <skill-dir>/scripts/contract_metrics.py contracts.json --out <dir>
python3 <skill-dir>/scripts/contract_metrics.py contracts.json --history history.json --out <dir>
```

It writes `<dir>/report.md` (summary, per-contract table, findings) and `<dir>/metrics.json`,
and exits non-zero when it finds errors. The source parser is heuristic. If a count looks
wrong, write a JSON spec instead.

With `--history` (cyclomatic complexity, defects, implementation days, change count, and
reuse per contract) it applies the **sorting method**: it ranks contracts from worst to best
without knowing anything about the domain. Worst = used in one place and changed every day.
Best = never changed, and used everywhere all the time.

### 3. Judge what the metrics can't
For each contract, ask the attribute questions above, plus "what else could change, and
what would that do to this contract?". The course's own counterexample: `IScannerAccess` had
4 operations, right in the target range, and was still a dumping ground.

### 4. Factor and iterate
- Use **down**, **sideways** and **up**. For sideways moves, ask "what else here looks like
  it belongs together?".
- **Iterate across subsystems, not through them.** Bring every subsystem up to the same
  maturity, round by round. Never finish one to perfection first, or the ripple effects will undo it.
- **Validate as you go.** Run each core use case through the contracts. Look for missing
  operations, contracts and services, and throw away whatever no use case uses. Validation is
  itself a factoring technique.
- Show every step. Don't jump three steps ahead. A skipped step loses insight and loses the
  people you're mentoring.
- Write down the *because* for each decision, and label placeholders honestly.
- **Consistency comes last.** All contracts should look like they came from the same cookie
  cutter: the same operation shapes and the same data-contract conventions per component type.

### 5. Deliver
1. The metrics report, with every error fixed or consciously justified.
2. The factored contracts as code (in the user's language), with base contracts shown.
3. For each contract: what facet it represents, and why it passes the four attribute tests.
4. A before/after table of the metrics.
5. Open questions for the domain expert. Treat blockers as signals: there's usually a hidden
   ambiguity worth surfacing.

## A good design needs all four
The contracts have the attributes, **and** meet the metrics, **and** are reusable, **and**
are valid (they support the core use cases). Any one of these on its own means little.

## References
- `references/spec-format.md`: JSON spec and history schemas
- `references/factoring-walkthrough.md`: the point-of-sale example factored step by step
- `examples/contracts.json`, `examples/history.json`, `examples/csharp/Contracts.cs`
