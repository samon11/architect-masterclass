# Project design concepts and formulas

## Critical path (Kelley & Walker, 1959)
- Forward pass: `ES = max(EF of predecessors)`, `EF = ES + duration`.
- Backward pass: `LF = min(LS of successors)`, `LS = LF - duration`.
- **Total float** `= LS - ES`. Activities with zero float form the critical path, the longest
  path through the network. It is the fastest the project can be built.
- Duration of the project = length of the critical path, as long as staffing never starves it.

## Float
- The float heat map: **black** critical (0), **red** low, **yellow** medium, **green** high.
- Assign resources **by float, low to high**. Starting a high-float activity before a
  low-float one consumes the low-float activity's slack, so it turns critical.
- Float is the project's safety margin. Compressing the schedule removes float, which raises risk.
  If the project needs more slack, add float along the critical path. Don't pad estimates.

## Staffing
- One developer per service at any one time.
- Ask for **the lowest staffing level that lets the critical path progress unimpeded**,
  not for a static team size.
- Expected curve: core team → ramp up → peak → ramp down → system test.
- With 1 developer: the critical path. With 2: the critical path, then the next lowest float.
  More people than the network can absorb slow the critical path down (interruptions,
  Brooks' law). The exception is the very start, where onboarding is paid in bulk.
- Before construction starts, keep people busy with work that doesn't depend on the design:
  client UI/API and infrastructure (utilities).

## Cost
- Cost is labor: `Σ staffing(t) × rate`, the area under the staffing curve.
- Efficiency = direct activity effort ÷ total effort. Core team and idle capacity lower it.
  A plan claiming close to 100% isn't credible.

## Earned value
- Each activity's value = its share of total effort, earned **only** when its exit criteria
  are met (no "90% done").
- **Planned earned value** = cumulative value of activities planned to be complete by time t.
- The planned curve of a viable plan is a **shallow S**: gentle start (core team), steep
  middle (peak staffing), gentle end (ramp down, system test). The slope is team throughput.
- A curve that's steep from day one, a straight line, or one that piles up at the end means
  the plan is not viable.

## Tracking
Three independent lines: planned earned value, actual progress (completed value), actual effort
(person-time spent ÷ planned total). Effort is not progress.

| Progress vs plan | Effort vs plan | Diagnosis | Remedy |
|---|---|---|---|
| on | on | healthy | do nothing |
| below | above | underestimation | move the date or cut scope; re-plan and re-sign |
| below | below | resource leak | find the drain, escalate to the lowest common manager |
| above | above | overestimation | release people or add scope |

Project forward along the progress trend. Report weekly, mechanically: chart, diagnosis,
recommended remedy, and act if nobody objects.

## Estimation
- Nominal, not padded and not squeezed. Keep a consistent granularity (5/10/15/20 days).
- Topology matters more than estimates. Errors cancel across many activities.
- "Let me get back to you" is the only professional first answer to "how long?".

## Options and sign-off
- Show several options (normal, constrained, compressed) with duration, cost and risk.
- Management picks one and signs it. Scope change means re-plan and re-sign.
- Over budget is a management failure. Over schedule usually costs the business more.
