---
name: idesign-method
description: Design or review a software system's architecture using Juval Lowy's IDesign Method (Righting Software). Covers volatility-based decomposition, the layered taxonomy (Clients, Managers, Engines, ResourceAccess, Resources, Utilities), closed-architecture call rules, and validation with call chains for the core use cases. Includes a validator that checks an architecture JSON and draws Mermaid diagrams. Use when the user asks to design a system, decompose it into services or components, review an architecture, spot functional decomposition, apply "the Method", or validate a design against its use cases.
---

# The IDesign Method: System Design

The Method is deliberately simple. It produces the smallest set of components that, combined
in different ways, satisfy **all** the use cases, present and future. Decomposition is driven by
**volatility**, not by functionality. Volatility is the areas likely to change over the
system's lifetime.

> Features are always and everywhere aspects of integration, not implementation.
> You never map a feature to a component.

The output of this skill feeds `project-design`. The components become the project's activities.
Service contracts for the components are handled by `service-contract-design`.

## First: what not to do

Watch for **functional decomposition** (A, B, C requirements → A, B, C blocks) and **domain
decomposition** (Sales, Shipping, Billing "services"). Domain decomposition is functional
decomposition in disguise. The symptoms:
- Business logic gets pulled into clients, which stitch services together.
- Services quietly assume what runs before and after them, so reuse is lost.
- The design swings between an explosion of tiny services and a few giant ones.
- Services call each other in chains ("the staircase"), with coupling that grows like n².
- There are many points of entry.

If the user's current design looks like this, say so plainly and show which symptom gives it away.

## Workflow

### 1. Gather requirements as core use cases
Most use cases are variations. Find the **core use cases** (usually 2 to 6) that express the
**nature** of the business. Ask for them as activity flows, not feature lists. If the user only
has features, interview them: who does what, in which order, what varies by customer, region
or channel?

### 2. Identify areas of volatility
For each candidate, ask:
- **What could change over the life of this system?** Use the horizon test. If it changes
  every 10 years and the system lives 3, hard-code it. If it changes every 5 years and the
  system lives 10, encapsulate it.
- **Design for your arch-competitor.** Why couldn't a competitor run your system? Each answer
  (how they insure, route, price, notify, ...) is a candidate volatility.
- Check **both axes**: the same customer over time, and different customers at the same time.

Sort every candidate:

| Kind | Action |
|---|---|
| Not volatile within the horizon | **No block.** Hard-code it |
| Volatile within the horizon | **Encapsulate** it in a component |
| A change to the *nature* of the business | **Never encapsulate.** That's speculative design: rare, and always done poorly |

Watch for the opposite failure too. A new convert says "this could change, and this, and
this" and ends up with an explosion of boxes. Something that is **variable** isn't
necessarily **volatile**. Three fixed ways to calculate interest is a switch statement, not an engine.

### 3. Map volatilities onto the layers

| Layer | Encapsulates | Notes |
|---|---|---|
| **Clients** | Client technology and UI churn ("who") | Users, apps, other systems. Normalize them so there's one point of entry |
| **Managers** | The **sequence** of a family of related use cases ("what") | Nouns: `AccountManager`. Almost expendable, but never a pass-through |
| **Engines** | An **activity**, a business rule that varies ("how") | Named after the activity: `PricingEngine`. Rare. May be shared across managers |
| **ResourceAccess** | **How** a resource is accessed | Exposes **atomic business verbs** (`Credit`, `Debit`), never CRUD or I/O. Noun names |
| **Resources** | Where state lives ("where") | DB, queue, file, cache, another system |
| **Utilities** | Cross-cutting infrastructure | Security, logging, diagnostics, pub/sub, message bus. Must pass the **cappuccino-machine test**: usable in any system |

A use case can change in only two ways: its **sequence** (Manager) or its **activities**
(Engine). Expect roughly a Fibonacci ratio of managers to engines: 1 → 0, 2 → 1, 3 → 2, 5 → 3.
Five managers is already a stretch, and eight means a system of systems. A typical composable
design has on the order of **10** services.

### 4. Apply the closed-architecture rules
- Call **down one layer** only. Never **up**, never **sideways**, never **skip** a layer.
- Allowed relaxations: anyone may call **Utilities**. Both Managers and Engines may call
  **ResourceAccess**. A Manager may **queue** a call to another Manager, which is semantically
  a separate use case.
- The method's don'ts:
  - A client calling several managers in one use case.
  - Queued calls to engines or ResourceAccess.
  - Anything except managers publishing events.
  - Engines subscribing to events.
  - Engine→Engine or RA→RA calls.
  - Resources (DB triggers) publishing.
- A manager queuing to more than one manager is zero-one-infinity, so **publish an event** instead.
- When developers want to break a rule, there's a real problem underneath. Find it. A
  manager calling a client becomes a pub/sub event. A manager calling a manager becomes a queued call.

Full rule table: `references/rules.md`.

### 5. Validate with call chains
For each **core** use case, draw the call chain over the components. If you can draw a call
chain for every core use case, the design is valid. Validation is also a design technique.
It turns up missing operations, missing components, and components no use case ever uses (throw those away).

Write the architecture as JSON (`references/architecture-format.md`, example in
`examples/architecture.json`) and run:

```bash
python3 <skill-dir>/scripts/validate_architecture.py architecture.json --out <dir>
```

It writes `<dir>/report.md` with the findings, a layered static-architecture diagram, one
call-chain diagram per use case, and a table of label-free call-chain **shapes**. It exits
non-zero when there are errors.

Read the shapes:
- **Stick figure.** Client → manager → engines and RA on both sides. Healthy.
- **Fork.** The client fans out to many services. Functional decomposition.
- **Staircase.** A → B → C chains. Functional decomposition.
- **Glove.** A manager shuttles data between tiny engines and RA. The engines are too small.
- **Double-back.** The same engine is called first and last. Use cases are commingled.
- **Symmetry.** Good architectures look the same once you strip the labels. If three use
  cases publish after RA and the fourth doesn't, that's a red flag.

### 6. Check the design is ripe
- Volatility **decreases** going down the layers, and reuse **increases**. The design should look like a pyramid.
- Changing a use case should change a Manager and nothing below it. When the team hears
  about a manager change, the right reaction is "OK, for that use case we'll queue first...",
  not "whatever" (the manager is pass-through) and not "we can't, it's too expensive" (the manager is bloated).
- Extend the system by adding **slices**, not by refactoring. Pick a middle-complexity slice
  as the first **vertical slice**: wire every layer with stubbed work to prove the architecture early.

### 7. Deliver
1. A list of volatilities, each with the component that encapsulates it, plus the rejected
   candidates and why (not volatile within the horizon, or the nature of the business).
2. The static architecture diagram.
3. One call chain per core use case.
4. The validator report, with every error resolved.
5. Open questions for the domain expert.

Then offer to continue with `service-contract-design` (contracts) or `project-design`
(duration, cost, staffing).

## Guardrails
- Don't design against the requirements. Design for the core use cases and the volatilities.
- If it isn't volatile, there's no block, however much people want a "reporting service".
- Passing the validator doesn't prove the design is good. A violation does prove it's bad.
- Your best design may not be very good. Iterate, but stop when you can't find a smaller set.

## References
- `references/rules.md`: call rules, don'ts, naming, smells, with rationale
- `references/architecture-format.md`: JSON schema for the validator
- `examples/architecture.json`: a clean three-use-case example
