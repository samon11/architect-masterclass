---
name: project-design
description: Design a software project from a system architecture using Juval Lowy's IDesign Method (Righting Software). Turns services into an activity network; computes the critical path, float and float-based dynamic staffing; and charts staffing, cost and the planned earned-value curve (shallow S). Also tracks a running project (planned vs actual progress vs effort, projected finish, and the symptom to fix). Use when the user asks how long a system will take or what it will cost, wants a staffing plan, critical path, project timeline, earned value chart, schedule options, or a status check against the plan.
---

# Project Design (IDesign Method)

Project design is the architecture of the project. It is the only objective way to answer
**how long will it take** (the critical path) and **how much will it cost** (the area under
the staffing curve). It flows from the system design: the components of the architecture
become the activities of the project.

> A project plan is not a Gantt chart. It is how you staff, size services, put one
> architect in command, and map team structure.

This skill ships a calculator, `scripts/plan_project.py` (Python 3.8+, stdlib only). **Never
compute the critical path, float, staffing or earned value by hand.** Build the network JSON,
run the script, then interpret its output.

## Workflow

### 1. Get the architecture

You need the static architecture: Clients, Managers, Engines, ResourceAccess, Resources and
Utilities, plus which component uses which. If the user has no architecture yet, use the
`idesign-method` skill first. If they give a feature list instead of components, say so. A
feature list can't be project-designed, because features come from integrating components
and aren't built by any single activity.

### 2. Build the activity list

Every component becomes one construction activity, sized so **one developer** can build it
in a reasonable time (roughly 1 to 4 weeks). Add the activities that aren't code:

| Category | Typical activities |
|---|---|
| Front end (`"role": "core"`) | Requirements and core use cases, architecture, project design |
| Planning (`"role": "tester"`) | System test plan, test harness |
| Infrastructure (start immediately after project design) | Utilities: security, logging, pub/sub, message bus; resources (DB schema) |
| Construction (`"role": "developer"`) | One activity per component. Each one already includes the service lifecycle: detailed design, test plan, construction, code review, unit testing |
| Clients | UI and API work. Can start early, because UI must not depend on the back end |
| Integration | Integrate per **slice** or use case, as you go. Never as one big-bang at the end |
| System test, release | System testing, a zero-duration release milestone |

### 3. Derive dependencies from the architecture

Dependencies come from the **call chains**, not from intuition:
- A component depends on the components it **calls**. A Manager depends on its Engines and
  ResourceAccess, an Engine on its ResourceAccess, a ResourceAccess on its Resource.
- Everything that logs, secures or publishes depends on **Utilities**.
- Clients depend on Utilities (and on Managers only for integration, not for construction).
- An integration activity depends on the Managers and Clients of its slice.
- Everything depends on project design, and system test depends on the test plan.

Check the network for these problems before you compute anything:
- **No cycles.**
- **One start and one end.**
- **Every activity leads to the end.** No dangling activities.
- **No god activities.** An activity much longer than the rest is a design smell. Split it.

### 4. Estimate (accurately, not precisely)

- Use **nominal** numbers in a fixed granularity: 5, 10, 15, 20 days (or 1, 2, 3, 4 weeks). Never 11 vs 12.
- Getting the network **topology** right matters far more than the estimates. With 30+
  activities, over- and under-estimates cancel out (law of large numbers).
- **Never pad.** Padding feeds Parkinson's law and gold plating. Underestimating feeds cutting
  corners. Both kill projects. If the plan needs slack, add float to the network, not to estimates.
- If the user doesn't have estimates, ask for them. Don't invent them. Treat the first number a
  developer gives as typing time, and have them itemize testing, learning curve, integration and docs.

### 5. Write the network JSON and run the calculator

Full schema: `references/input-format.md`. Worked example: `examples/network.json`.

```bash
python3 <skill-dir>/scripts/plan_project.py plan network.json --out <dir>
python3 <skill-dir>/scripts/plan_project.py plan network.json --developers 3 --out <dir>-3devs
```

Outputs in `<dir>`:

| File | Contents |
|---|---|
| `report.md` | Summary, activities sorted by float, Mermaid network (critical path bold, colored by float), Mermaid staffing, cost and planned-EV charts |
| `charts.html` | Self-contained page with SVG staffing/cost and earned-value charts (light and dark) |
| `activities.csv` | ES/EF/LS/LF, float, float band, scheduled start/finish, value share |
| `timeline.csv` | Per period: staffing, cost, cumulative cost, planned earned value % |
| `activity-network.canvas` | Obsidian JSON Canvas of the network. x = earliest start, color = float |

### 6. Interpret the plan with the user

Go through it in this order:

1. **Critical path.** The longest path is the fastest the project can *ever* be built. You
   can always go slower, never faster. Your best (most reliable) developers go on it.
2. **Float heat map.** Black = critical, red = low, yellow = medium, green = high. A cluster
   of black and red is the **nexus of pain**: staff it first and watch it closely.
3. **Staffing.** Assign people **by float, low to high**. If you staff a high-float activity
   ahead of a lower-float one, the lower-float one turns critical and derails the project.
   The script does this for you. Ask for the **lowest staffing level that lets the critical
   path progress unimpeded**, not "how many developers do we need?". The curve should go:
   core team, ramp up, peak, ramp down, system test. Flag feast-famine shapes.
4. **Cost.** Cost is staffing × time, the area under the curve. Report effort and
   efficiency. Efficiency is direct activity effort ÷ total effort, and the core team plus
   idle capacity make it well below 100%.
5. **Planned earned value.** Each activity is worth its share of total effort and counts
   only when its exit criteria are met. A viable plan draws a **shallow S**. If the script
   reports front-loaded, back-loaded or straight-line, the plan isn't viable as designed. Fix
   the network or the staffing, not the estimates.

### 7. Present options, not a single answer

Never take one plan to management. Run the calculator with several developer caps (and,
where it makes sense, compressed variants such as parallelized work or a better top
developer on the critical path). Show each option's duration, cost and risk side by side.
Let the decision maker pick one and sign off. That signed choice is the commitment.
Committing to numbers you know you can't meet isn't optimism, it's fraud.

A useful set of options:
- **Normal**: the lowest staffing that keeps the critical path unimpeded.
- **Constrained**: the user's actual headcount. The script warns when the cap stretches
  the schedule past the critical path.
- **Compressed**: more parallel work, at higher cost and higher risk (less float).

### 8. Track the project (once it's running)

The plan is a living document. Every week, collect a status report: which activities met
their exit criteria (binary, no "90% done"), optional partial credit by completed lifecycle
phase, and the total person-days spent. Then run:

```bash
python3 <skill-dir>/scripts/plan_project.py track network.json status.json --out <dir>
```

It plots **planned earned value**, **actual progress** and **actual effort** as three
independent lines, projects the finish date from the progress trend, and diagnoses the
symptom:

| Progress | Effort | Diagnosis | Remedy |
|---|---|---|---|
| On plan | On plan | Healthy | Do nothing. |
| Below | Above | Underestimation | Push the date out, or cut scope to hold it. Re-plan and re-sign. |
| Below | Below | Resource leak | Find who is taking your people and escalate. |
| Above | Above | Overestimation | Release people or pull scope forward. |

Effort and progress are unrelated. Never report one as the other. Base progress on
integration points and exit criteria, never on features. Look forward along the trend, not in the rear-view mirror.

## Guardrails

- If you have no architecture, there is no project design. Don't plan from a feature list.
- One developer per service at any time. If a service needs two people at once, it's too big.
- Before developers write code, give idle people the work that doesn't depend on the design:
  UI/API and infrastructure. Don't hand them features.
- Scope changes need a re-plan and a new sign-off, not absorption.
- Being over schedule is worse for the business than being over budget. Protect the critical path.

## References

- `references/input-format.md`: network and status JSON schemas
- `references/concepts.md`: definitions and formulas (critical path, float, staffing, earned value, tracking)
- `examples/network.json`, `examples/status.json`: a complete small system to copy from
