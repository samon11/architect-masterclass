---
title: "Project Planning"
date: 2026-07-22
module: module-3
type: module
tags:
  - course/notes
  - module-3
  - juval-lowy
---

# Project Planning — Staffing, Design & Delivery

> [!summary] Module 3 — The Architecture of the Project Itself
> A project plan is not a Gantt chart: it's how you staff, size services, architect one person in command, and map team structure. Everything else is decoration.

## Topics

- [x] What is a Project Plan?
- [x] Service Sizing — The Area of Minimal Cost
- [x] The Single Architect Principle
- [x] Junior↔Senior Apprenticeship
- [x] One-to-One Staffing (Services ↔ Developers)
- [x] Loose vs Tight Coupling in Team Design
- [x] Staged Delivery
- [x] The Fuzzy Frontend (15–25%)
- [x] Clean Slate Projects
- [x] Killing Failing Projects Early
- [x] Multiple Options for Managers
- [x] Iterative Design / Incremental Build
- [x] Integration Cost (x!)
- [x] Progress Reporting on Integration Points
- [x] Service Lifecycle — Testing, Construction & the Waterfall Truth
- [x] Project Tracking — Earned Value, Shallow S, and Living Plans
- [x] Project Design — Critical Path, Float, and Dynamic Staffing
- [x] Composable Design — Core Use Cases, Components & Agility
- [x] Project Design — Critical Path, Float, and Dynamic Staffing
- [x] Hand Off Point — Senior vs Junior Handoffs, Team Models & the Architect's Role

## Transcript Sources

- [Raw transcript — Staffing](../99-resources/Transcripts/Staffing.md)
- [Raw transcript — Planning](../99-resources/Transcripts/Planning.md)
- [Raw transcript — Service Lifecycle](../99-resources/Transcripts/Service%20Lifecycle.md)
- [Raw transcript — Project Tracking](../99-resources/Transcripts/Project%20Tracking.md)
- [Raw transcript — Project Design](../99-resources/Transcripts/Project%20Design.md)
- [Raw transcript — Documentation](../99-resources/Transcripts/Documentation.md)
- [Raw transcript — Process Flow](../99-resources/Transcripts/Process%20Flow.md)
- [Raw transcript — Composable Design](../99-resources/Transcripts/Composable%20Design.md)
- [Raw transcript — Hand Off Point](../99-resources/Transcripts/Hand%20Off%20Point.md)

## Notes

### What Is a Project Plan?

A project plan is **how you staff the project**, how you run the product lifecycle, design it, estimate cost & schedule, and integrate services. It is *not* a Gantt chart.

- Juval calls a Gantt chart an **artifact of planning** — useful only for extracting key data points at one moment; afterwards it's pacification for "knuckle draggers" (stakeholders who demand visible plans)
- A screaming baby needs a pacifier: the Gantt is the pacifier. Take what you need, then set it aside
- The real substance of planning lives in sections that precede the schedule

---

### Service Sizing — The Area of Minimal Cost

The heart of project design is choosing the right granularity for services. Size matters non-linearly at both extremes.

**Two cost components (per service):**
| Component | Blue line (build per service) | Red line (integration between services) |
|-----------|-------------------------------|------------------------------------------|
| Trend     | Declines as # of services ↑   | Increases as # of services ↑             |
| Driver    | Fixed overhead amortized across more, smaller units | Network interactions — ~n² or worse (~nⁿ with ripple effects)|

**Area of Minimal Cost 🟢:**
- Every system has an optimal range where total cost is minimized — services are "not too big and not too many"
- This is **relative**: "every area inside this zone is good enough", never aim for the exact center (diminishing returns)
- Once outside the zone → **deterministic failure before first line of code** (linear tools like +1 month / +1 dev cannot overcome non-linear complexity)

**Why managers miss it:** they focus on environment, perks, and process — not design. The architect's career-long duty is keeping systems inside this zone and training the next generation to do it too.

---

### Why One Architect, Not a Committee?

Committees destroy design integrity: parts are excellent individually but the whole lacks cohesion (the "chimera" analogy from Greek myth).

| Criterion | Single Architect ✅ | Committees ❌ |
|-----------|---------------------|---------------|
| Design integrity | One mind holds full picture | Parts glued together → inferior at everything |
| Accountability | One person owns it all | Nobody accountable for the boundaries between parts |
| Communication cost | Zero mental split-brain | Constant negotiation across fragmented visions → worse, not better |

**Architect apprenticeship (Guild model):**
- Seniors don't get snatched from job markets — they're **grown internally** like cathedral builders in the Middle Ages
- Junior architects shoulder documentation, demos, code review; senior architect focuses on design thinking
- Apprenticeship = a sounding board for the lonely architect — "What if we do X vs Y?" back-and-forth with someone who understands

> [!tip] Key insight from Juval's own story:  
> *"The single best career move I ever made"* was swallowing his pride and doing another year as junior under a master he knew surpassed him. He then "earned himself free by earning the right to go."

---

### The One-to-One Staffing Principle (Services ↔ Developers)

**Rule:** Each developer works on *one* service, at any given moment — **and never two services simultaneously.** Cross-section of team at any time = exact 1:1 mapping.

The other options all predict failure:

| Option | Result | Why it breaks |
|--------|--------|---------------|
| 2 devs → 1 service (serial) | Worse than one person (3–5× longer) | Constant context-switching + re-entry cost each swap-back |
| 2 devs → 1 service (parallel) then integrate | Months of delays cascade into project | Integration is never trivial; code changes invalidate prior testing, requiring full regression |
| 1 dev → 2 services | Same as above — drops one to work on the other | Every switch kills both timelines and triggers management panic |

**Implication of 1:1 mapping:**
- System diagram ≡ Team diagram — isomorphic by design
- Design tightly coupled **services** means team talks should happen over the water cooler, not in formal meetings
- The only way to meet an impossibly aggressive deadline is good architecture; managers who toss "maintainability/extensibility/reuse" overboard are throwing away their last chance of success

> [!quote] Key reframing for executives:  
> Don't say *"We need maintainable, extensible code."* Say *"I'll show you how to meet the schedule."* Managers hear the first as delay; they hear the second as solution.

---

### Loose vs Tight Coupling in Teams

A **loosely coupled system** has *just enough* interaction — removing it kills functionality:
- The team that can resolve problems at the water cooler is more efficient than one locked behind boundaries
- A design where every service talks to every other (over-coupled) mirrors a team trapped in meetings — everyone's calendar is yellow (meeting blocks), nobody ships

**Rule of thumb:** When assigning developers, match architecture coupling with interpersonal closeness:
- Tightly coupled services → assign developers who *want* to talk constantly and have lunch together
- Loosely coupled services → independent developers; over-communication becomes wasted effort

---

### Staged Delivery & the Project Lifecycle

> [!abstract]
> The planning process is not about drawing Gantt charts — it's about managing risk through staged delivery, early constraint-setting, and continuous integration. Every phase exists to shrink the space of failure.

---

#### Staged Delivery

Deliver the system in **stages** (a.k.a. increments or drops), each producing a working, integrated subset of the final product. Each stage is a mini-project with its own planning, design, and integration.

- Each stage must be **end-to-end**: a slice that crosses all layers (UI → service → data) so that something actually *works* at the end of it
- Stages are **time-boxed** and **scoped to fit** — if a stage can't fit, the architecture is wrong, not the schedule
- The alternative — building everything in parallel and integrating at the end — is the "big bang" approach, which is a recipe for catastrophe

> [!danger] Big Bang Integration
> Integrating N components all at once at the end of a project produces a combinatorial explosion of failure modes. There is no place to hide, no incremental feedback, and no way to isolate which of the N! interaction pairs broke the build.

---

#### The Fuzzy Frontend (15–25%)

The **fuzzy frontend** is the initial, ill-defined phase of a project where requirements are unclear, constraints are being discovered, and the architecture is being sketched. This phase should consume roughly **15–25% of total project time** at the start.

- This is where you explore the problem space, establish constraints, and define the architectural vision
- Too short → no constraints, infinite failure modes (see: Clean Slate)
- Too long → analysis paralysis, missed market windows
- The goal is to **exit the fuzzy frontend with enough clarity** to start staged delivery confidently

> [!tip] The 15–25% Rule
> If your fuzzy frontend takes less than 15%, you're rushing into code with no guardrails. If it takes more than 25%, you're overthinking and delaying delivery. The sweet spot is where you can articulate the key constraints and the first stage's scope.

---

#### Clean Slate Projects — From Hell

Starting a project from a **clean slate** — with no existing constraints, requirements, or reference points — is one of the most dangerous situations in software development.

- With no constraints, there are **infinite ways to fail**: every architectural decision is a potential wrong turn, every design choice is unanchored
- You have no precedent to validate against, no existing system to learn from, no boundaries to keep you on track
- The absence of constraints means the problem space is unbounded, and the solution space is infinite

> [!warning] Clean Slate = Infinite Failure Modes
> "A clean slate project is from hell because there are infinite ways to fail due to lack of constraints and requirements." Without existing systems, domain knowledge, or stakeholder constraints to anchor decisions, the architect is free to wander into any of an infinite number of dead ends.

**Mitigation:** Introduce constraints early. Derive them from business objectives, non-functional requirements, stakeholder interviews, and any available legacy or adjacent systems. The fuzzy frontend exists precisely to create these guardrails before staged delivery begins.

---

#### Kill Failing Projects Early

> [!danger]
> **Your career can't afford to be on a failing project. Kill them as early as possible.**

- The cost of continuing a doomed project compounds: sunk cost fallacy, team morale erosion, and reputation damage
- Early detection and termination is not failure — it's **professional survival**
- If a project shows signs of non-linear complexity, missing constraints, or architectural drift beyond the area of minimal cost, recommend termination before significant resources are invested

> [!quote]
> "Projects outside the area of minimal cost have failed before anyone wrote the first line of code. It's deterministic failure."

This is why the fuzzy frontend and clean-slate warnings matter: they give you the tools to **recognize failure modes early** and kill the project before it kills your career.

---

#### Multiple Options for Managers

Always present **multiple options** to managers in your software development plan — and get their sign-off as a **life insurance policy**.

- Managers want to feel they have agency in the decision; giving them a single option makes them feel like passengers
- By presenting multiple options (each with trade-offs clearly articulated), you:
  - Give them the illusion of control (which they need for buy-in)
  - Create a paper trail of their decision (your life insurance policy if things go wrong)
  - Force them to engage with the technical trade-offs, not just the schedule

> [!example] The Life Insurance Policy
> Present 2–3 options: e.g., "Option A: Fast but risky (clean slate, 6 months), Option B: Conservative (staged delivery, 9 months), Option C: Hybrid (reuse existing, 7 months)." Get them to sign off on which they choose. If the project fails, you can point to their signed-off decision.

---

#### Iterative Design, Incremental Build

> [!abstract]
> **Design iteratively, but build incrementally.** These are two different axes of iteration.

- **Design is iterative**: you refine the architecture through repeated cycles of exploration, prototyping, and validation. The design should evolve as you learn more about the problem and constraints.
- **Building is incremental**: each increment delivers working, integrated code. You don't redesign from scratch each time; you add to a growing, working system.
- The key insight: **don't wait for the perfect design before building anything**. Start building early, let the design emerge, but always keep the system in a working state.

> [!tip] The Iteration Distinction
> Design iteration = rethinking architecture. Build iteration = delivering working slices. Confusing the two leads to either premature commitment to a bad design or endless redesign with no delivery.

---

#### Integration Cost = x!

> [!danger]
> **The cost of integration is x! (x factorial), where x is the number of components.**

- Each new component must integrate with *every* existing component, and each integration point can fail in multiple ways
- Adding component n requires n-1 new integration points, but each of those interacts with existing integration points, creating ripple effects
- The factorial growth means that integrating all components at once at the end of a project is **mathematically doomed**

> [!quote]
> "The cost of integration is x! where x is the number of components, so integrate incrementally over the course of the project instead of all at once at the end."

**Implication:** This is the mathematical foundation for staged delivery. Each stage integrates a small number of new components into the existing system, keeping x small at each integration point. The factorial explosion is tamed by keeping integration batches small and frequent.

---

#### Progress Reporting on Integration Points, Not Features

> [!danger]
> **NEVER BASE PROGRESS REPORTS ON FEATURES. BASE IT ON SMALL INTEGRATION POINTS.**

- Features are subjective, often vaguely defined, and can hide integration problems behind a "looks done" facade
- Integration points are concrete, measurable, and reveal the true state of the system: if components can't talk to each other, nothing works
- A feature that's 90% done but can't integrate is 0% done
- A feature that's 30% done but integrates cleanly is making real progress

> [!tip] What to Report
> Instead of "Feature X is 80% complete," report "Integration point between Service A and Service B is complete and passing tests" or "3 of 5 integration points in Stage 2 are verified."

This is the natural consequence of staged delivery and incremental integration: your progress metrics should mirror your integration strategy.

---

## Key Excerpts

> *"Projects outside the area of minimal cost have failed before anyone wrote the first line of code. It's deterministic failure."*

> *"The cost of integration is x! where x is the number of components, so integrate incrementally over the course of the project instead of all at once at the end."*

> *"Your career can't afford to be on a failing project. Kill them as early as possible."*

> *"A clean slate project is from hell because there are infinite ways to fail due to lack of constraints and requirements."*

> *"NEVER BASE PROGRESS REPORTS ON FEATURES. BASE IT ON SMALL INTEGRATION POINTS."*

> *"Always present multiple options to managers in software dev plan and get their sign off for life insurance policy."*

> *"A camel is a horse designed by a committee, and a whale is a horse designed by an ocean."* — Juval (referencing the old joke)

> *"The only thing that evolves organically is the tumor."*

> *"Complexity of this network grows like n²... with ripple effects we're actually talking n factorial… Sterling's formula reminds us: nⁿ. Not exponential. Hyper-exponential."*

---

> *"The purpose of testing is, therefore, to break it. There's a mathematical proof from 1936 that proved that you can never prove that something works."*

> *"Today, waterfall means anything that's not coding... By the time you start doing 20% or 30%, you started starving all the other activities. You're not doing enough documentation or testing or installation script, and you're going to fail."*

> *"You cannot design what you don't understand. The way people understand the nature of the problem facing them is by getting their hands dirty."*

> *"The waterfall lifecycle... works remarkably well in small delineated units of work like a service. It fails miserably at the system."*

> *"Good and bad are not absolute. Is water good or bad? A cup of water is fine. A bucket of water, probably not."*

## Quiz / Self-Check

> [!question]- 1. What does Juval say is the *only* fighting chance against non-linear complexity?
> [!summary]- Answer  
> A qualified, competent **single architect** — not a committee, not linear tools like "add two more months."

> [!question]- 2. Explain why the red integration-cost curve can behave hyper-exponentially (not just quadratically).
> [!summary]- Answer  
> Because each new service interacts with every existing one: adding n services adds roughly n² interactions, and ripple effects through changed modules turn that into ~n³, approaching nⁿ per Sterling's approximation.

> [!question]- 3. What happens if you use "linear tools" (more people, more months) on a non-linearly scaled problem?
> [!summary]- Answer  
> Nothing helps — the cost curve diverges faster than your inputs grow. Beyond one or two extra contributors to an already-overcommitted area of minimal cost, every new person makes things *worse*.

> [!question]- 4. Why does Juval compare a camel to a committee?
> [!summary]- Answer  
> Every part is built by experts individually (lion's head, ox's body, goat's hind legs, etc.) — but the resulting creature can't match any of its components' performance because no single entity held the whole design in one mind. Committees produce chimeras.

> [!question]- 5. Give the 1:1 rule and list *two* alternatives that Juval rules out with reasoning.
> [!summary]- Answer  
> One developer ↔ one service ↔ one time. Two devs on one service either serialize (destroyed by context switching) or integrate later (testing breaks, delays cascade). One dev on two services drops one to work on the other — same cascading delay problem.

> [!question]- 6. What is staged delivery, and why is it superior to "big bang" integration at the end of a project?
> [!summary]- Answer
> Staged delivery means delivering the system in end-to-end stages, each producing a working, integrated slice that crosses all layers (UI to service to data). It is superior because it keeps integration batches small (taming the x! cost), provides early feedback, and isolates failures to a single stage rather than the entire system.

> [!question]- 7. What percentage of total project time should the fuzzy frontend consume, and what goes wrong if it falls outside the 15-25% range?
> [!summary]- Answer
> The fuzzy frontend should take roughly 15-25% of total project time. Too short (<15%) means rushing into code with no constraints or guardrails, leading to clean-slate-style infinite failure modes. Too long (>25%) leads to analysis paralysis and missed market windows. The goal is to exit with enough clarity to begin staged delivery confidently.

> [!question]- 8. Why is a "clean slate" project described as "from hell"?
> [!summary]- Answer
> A clean slate has no existing constraints, requirements, or reference points. With no guardrails, there are infinite ways to fail — every architectural decision is unanchored, every design choice is a potential wrong turn, and there is no precedent to validate against.

> [!question]- 9. Why should you "kill failing projects as early as possible"?
> [!summary]- Answer
> Your career can't afford to be on a failing project. Continuing a doomed project compounds costs (sunk cost fallacy, morale erosion, reputation damage). Early detection and termination is professional survival, especially since projects outside the area of minimal cost fail deterministically before the first line of code.

> [!question]- 10. What is the "life insurance policy" approach to presenting options to managers?
> [!summary]- Answer
> Always present multiple options to managers in your development plan and get their sign-off. This gives them the illusion of agency (needed for buy-in) and creates a paper trail of their decision, so if the project fails you can point to their signed-off choice as protection.

> [!question]- 11. Explain the difference between "iterative design" and "incremental build."
> [!summary]- Answer
> Design iteration = rethinking and refining the architecture through cycles of exploration and validation. Build iteration = delivering working, integrated code in increments. The key is to not wait for a perfect design before building — start early, let the design emerge, but always keep the system in a working state.

> [!question]- 12. Why is integration cost x! (x factorial), and what does this imply for project execution?
> [!summary]- Answer
> Each new component must integrate with every existing component, and ripple effects compound the interactions. The factorial growth means integrating all N components at once is mathematically doomed. The implication is to integrate incrementally throughout the project — each stage adds a small number of components to the existing system, keeping x small at each integration point.

> [!question]- 13. Why should progress reports be based on integration points rather than features?
> [!summary]- Answer
> Features are subjective and can hide integration problems behind a "looks done" facade. Integration points are concrete and measurable — if components can't talk to each other, nothing works. A feature that's 90% done but can't integrate is 0% done; one that's 30% done but integrates cleanly is making real progress.

> [!question]- 14. What is the purpose of testing, and why is "to prove it works" the wrong answer?
> [!summary]- Answer  
The purpose of testing is to **break it**, not to prove it works. A 1936 mathematical proof shows you can never prove something works, so the only thing you can prove is that it *doesn't* work. Testing requires a maniacal mindset: hating the code, wanting to kill it, wanting to break it.

> [!question]- 15. Why should a test plan be forked *before* construction begins?
> [!summary]- Answer  
Before any code exists, developers have no emotional attachment and can think clearly about all the ways the service could fail. After development, the code becomes their baby and they do light "it works!" testing — completely useless.

> [!question]- 16. Explain the ~1000:1 ratio between terse service requirements and verbose test plans.
> [!summary]- Answer  
At the service level, requirements are terse (e.g., "pump fuel"). But the test plan must cover every edge case: hot fuel, cold fuel, contaminants, water, diesel, soap, pressure extremes, vibration, out-of-spec current, and dozens more. Test plans are inherently ~1000 times more verbose than requirements.

> [!question]- 17. What does "getting your hands dirty" mean in the lifecycle, and why is it NOT prototyping?
> [!summary]- Answer  
After reviewing and approving the requirements spec, you do throwaway construction — pure disposable code — to better understand the problem. This is NOT prototyping. It's exploration to gain understanding so you can then do proper detail design.

> [!question]- 18. Why is the waterfall appropriate for services but catastrophic for systems?
> [!summary]- Answer  
The service lifecycle looks like a waterfall and that's fine for small units. But applied to an entire system, cascading complexity and integration cost (x!) make it fail. The 1976 IEEE paper that named it explicitly warned this — yet it was adopted as the gold standard for systems for 30 years.

> [!question]- 19. What does "waterfall means anything that's not coding" imply about developer time?
> [!summary]- Answer  
Modern usage treats "waterfall" as code for "anything beyond pure coding." Developers spend about 10% of time coding. Labelling everything else as "evil waterfall" leads to 90% coding and 10% useless rituals.

> [!question]- 20. How does the water/salt analogy explain when a process tool is good or bad?
> [!summary]- Answer  
Good and bad are not absolute — they're questions of scale. A cup of water is fine; eight liters kills. A smidgen of salt is essential; four teaspoons are lethal. Same with waterfall: effective at the service level, catastrophic at the system level.

---

### Service Lifecycle — Testing, Construction & the Waterfall Truth

> [!abstract]
> A service lifecycle is not a one-size-fits-all process. At the service scale (small, delineated unit of work), the lifecycle works — requirements → test plan → throwaway construction → design → construction → code review → integration & testing. The same lifecycle applied at the system scale fails. Good and bad are not absolutes — they're questions of scale, quantity, and context.

---

#### Terse Requirements at the Service Level

Requirements at the service scope are extremely terse. The fuel pump in a jumbo jet has a requirement spec of two words: **"pump fuel."** Once you have the requirements, you review them — and immediately fork a test plan.

> [!tip] Test Plan Before Construction
> Developers tend to think about testing *after* they've written code. By then, the code is their baby — they do light "it works!" testing. The right approach: fork the test plan **before** any construction, when there's no emotional attachment to protect.

#### The Purpose of Testing Is to Break It

> [!danger] Testing Cannot Prove Something Works
> There is a mathematical proof from 1936 that you can never prove that something works. If your testing goal is "to prove it works," you're wasting time trying to do the impossible.

The **only** thing you can prove is that something **doesn't** work. The purpose of testing, therefore, is to **break it**. This requires a maniacal mindset — hating the code with a passion, wanting to kill it, wanting to break it.

- Constructive testing (during development): white-box, against the design, line-by-line with a debugger — examining every argument, every if, every try/catch
- Destructive testing (from the test plan): black-box, aims to destroy the code, covers edge cases you never would have imagined

#### Test Plans Are Verbose (∼1000:1 Ratio)

If requirements are terse (two words), the test plan is extremely verbose. The ratio between requirements and test plan is roughly **a thousand to one**.

An iDesign customer mandates that vendor test plans **weigh at least 15 pounds** — and they review page by page to ensure no copy-paste. For the fuel pump example, the test plan covers hot fuel, cold fuel, fuel with water, fuel with contaminants, fuel with diesel, fuel with soap, high/low/atmospheric pressure, vibration, current outside spec, and dozens more failure modes.

#### Get Your Hands Dirty After Reviewing Requirements

> [!tip] Throwaway Code Is Not Prototyping
> "You cannot design what you don't understand. The way people understand the nature of the problem is by getting their hands dirty." After reviewing and approving the requirements spec, do some throwaway construction — pure, disposable code — just to better understand the task ahead. Then go into detail design, review it, and then into real construction.

#### One-to-One Mapping Reapplied to the Lifecycle

Each service must be done by a **single developer** in a reasonable amount of time. If the lifecycle takes a year, the service is too big. The entire process (requirements → test plan → throwaway → design → construction → code review → integration & testing) probably takes about a month.

#### Waterfall: Good for Services, Catastrophic for Systems

> [!warning] The Great Irony
> The waterfall lifecycle was described in a 1976 IEEE paper whose **explicit point was that it works for small units (services) and fails for systems** — yet it was adopted as the gold standard for systems for 30 years.

The service lifecycle looks like a waterfall if you squint — and that's **fine**. The problem was never the waterfall at the service level; it was applying it at the system level.

> [!tip] Today's Waterfall Means Something Different
> "Today, waterfall means anything that's not coding." Developers spend about 10% of their time actually coding. Anything beyond pure coding gets labelled "evil waterfall" as a dog whistle to avoid necessary upfront work.

#### Scale and Context: Good and Bad Are Not Absolute

Like water (essential in moderation, lethal in excess) or salt (vital for survival, deadly in large quantities), the waterfall and every process tool is a question of **scale and quantity**, not absolute good or bad.

- A cup of water: fine. Eight liters: fatal.
- A smidgen of salt: essential. Four teaspoons: lethal.
- Waterfall at the service level: effective. Waterfall at the system level: catastrophic.

---

#### Service Lifecycle Diagram

![[../99-Resources/Images/service_lifecycle.png]]

### Project Tracking — Earned Value, Shallow S, and Living Plans

> [!abstract]
> Project tracking is not about reporting features or chasing a Gantt chart. It's about measuring **earned value** against a **shallow S** plan, tracking **effort** independently from **progress**, and treating the plan as a **living document** that requires constant, tiny corrections.

#### Earned Value: Measuring Throughput, Not Just Completion

**Earned Value** is both a project design tool and a tracking mechanism. The core idea: assign a value to each work item toward completion of the whole, then track it as a function of time.

- The **pitch (slope)** of the earned value curve represents the **throughput of the team** — the only fair way to compare two teams
- The **blue line** is the planned earned value; the **green line** is actual progress; the **red line** is actual effort
- A plan that produces an impossible curve (e.g., back-scheduled to hit an arbitrary deadline) is **dead on arrival** — no team can deliver on it

#### The Shallow S: Shape of a Viable Plan

A well-designed project always yields a **shallow S** curve:

1. **Start**: A small core team begins work (low throughput, low value)
2. **Ramp up**: Additional people are absorbed as the project is approved (throughput increases)
3. **Peak staffing**: Maximum team size, maximum throughput (steepest part of the curve)
4. **Ramp down**: Developers are phased out as construction finishes
5. **System testing & release**: The curve levels off as the final 100% is achieved

> [!tip] **The plan needs to look like a shallow S.** If the earned value curve doesn't look like a shallow S, the plan is not viable. This is the only way to answer the question: "Does the plan make sense?"

#### Binary Exit Criteria: Kill the 90% Lie

> [!danger] **"90% of the time, they're 90% done."**

Developers always report 90% — because there are no binary criteria. The fix:

- Define **exit criteria** for each phase of a service lifecycle (requirements review, design review, code review, etc.)
- A phase is **done** only when its review has occurred — not when the documents are written
- Assign **weights** to each phase (e.g., requirements 20%, design 30%, coding 50%)
- Sum up completed phases × their weights to get true progress
- The **law of large numbers** ensures over/under estimates cancel out across ~30+ activities

#### Effort ≠ Progress

> [!danger] **"Effort is completely unrelated to progress."**

You can spend 150% of estimated effort and still be only 30% on progress — or vice versa. Track both independently:

- **Progress** (green line): measured by completed phases with binary exit criteria
- **Effort** (red line): simply sum up days worked by each developer — completely independent of progress

#### Trend Analysis: Project Forward, Don't Look in the Rearview

> [!danger] **"If you don't project, you do not have a project. You know what you have? A bunch of lawless monkeys smearing code on monitors."**

- **Trend analysis** (projecting where the project is heading) is the essence of project management
- Most teams drive by looking straight down or in the rearview mirror — both are fatal
- You drive forward by looking where the car is **going to be**, not where it is now
- **Extrapolation**: Right-click on the progress line in Excel and project it forward — this tells you when the project will actually finish

#### Four Tracking Symptoms and Their Remedies

| Symptom | Diagnosis | Remedy |
|---------|-----------|--------|
| Progress on plan, effort on plan | Healthy project | **Do nothing.** Don't disturb it. |
| Progress below plan, effort above plan | Underestimation | Push the schedule out OR reduce scope (date-driven) OR over-deliver (add scope) |
| Progress below plan, effort below plan | Resource leak | Identify the "vampire" stealing your team and escalate to the lowest common manager |
| Progress above plan, effort above plan | Overestimation | Let go of people — smaller teams are more efficient |

> [!tip] **The one exception to Brooks' Law**: At the origin (start of project), adding people is OK because onboarding is paid wholesale, not retail, and everyone is on the same clueless footing.

#### The Plan Is Alive

> [!quote] **"A project plan is not something that you design and review and then you sign off and put in a drawer never to see the light of day again. A good plan is a plan that five minutes before the release is still revising the plan to see if you can release five minutes from now."

- The plan is a **living document** — constantly revised as reality diverges
- **Von Moltke's** famous quote was twisted: it advocates a **system of options**, not abandoning planning. "A plan means nothing. Planning is everything."
- Projects are **dynamically unstable chaotic systems** (like the F-16 or the human body) — they require constant, tiny corrections to stay on course
- **Feature creep** must be handled with a new sign-off: every change requires revising the entire plan, reassigning people, and getting a new signature

#### Cost vs. Time Failure

> [!danger] **"Going over budget is failing management 101. Going over schedule is called Tuesday."**

- Managers are branded into never going over budget (next cycle gives you 2/3 of what you ask)
- Schedule slips are normalized as "software is always late"
- **Over budget is better than over schedule** — most companies can afford $2M instead of $1M, but wasting a year misses the market window
- The only way to meet the deadline is to be on time **throughout** the project, not heroically at the end

#### The Two-Minute Manager

> [!tip] **"Literature will tell you that if you're within 5%, you are God. Let me assert here, there was no divine intervention. What was here was a highly structured, highly engineered approach."**

- Project management can be **completely mechanized** — sixth-grade math, nothing more
- Every Friday, generate the charts, compare progress vs. plan, and send a pre-written email with the recommended remedy
- If nobody objects by Monday, execute the remedy
- This eliminates aggravation, builds trust, and makes the architect also the project manager without spending extra time — because success comes from method, not heroism

## Quiz

> [!question]- 1. What does the pitch (slope) of an earned value curve represent?
> [!summary]- Answer
> The throughput of the team. Steeper curves indicate higher throughput. This is the only fair and equitable way to compare two teams.

> [!question]- 2. What shape should a viable project plan's earned value curve take, and why?
> [!summary]- Answer
> A shallow S. It reflects proper staffing: a small core team starts, ramps up as people are absorbed, reaches peak throughput, then ramps down as developers are phased out, finally leveling off for system testing. If it doesn't look like a shallow S, the plan is not viable.

> [!question]- 3. Why can't you ask a developer "where are you?" and trust the answer?
> [!summary]- Answer
> Because 90% of the time they'll say they're 90% done — there's no binary criteria. The fix is to use review-based exit criteria: a phase is either done (review held) or not done (no review yet).

> [!question]- 4. Explain the difference between tracking progress and tracking effort. Give an example of how they can diverge.
> [!summary]- Answer
> Progress (green line) is measured by completed phases with binary exit criteria. Effort (red line) is simply days worked by developers. They are completely independent: you could spend 150% of estimated effort (15 days on a 10-day task) and still be only 30% on progress if the design review hasn't happened yet.

> [!question]- 5. What does it mean to "project" in project management, and why is it essential?
> [!summary]- Answer
> To project means to extrapolate the trend line forward to predict where the project is heading. It's essential because driving a project by looking at where it is now or where it's been (rearview mirror) is like driving a car by looking straight down or in the rearview mirror — you'll crash. If you don't project, you don't have a project.

> [!question]- 6. You detect that progress is below the plan and effort is below the plan. What's the diagnosis and what should you do?
> [!summary]- Answer
> This is a resource leak — people assigned to your project are working on someone else's project. Find the lowest-level manager who manages both projects, show them the chart, and force them to choose which project is more important, with consequences.

> [!question]- 7. Why is adding people to a late project almost always wrong, and what's the one exception?
> [!summary]- Answer
> Adding people to a late project is like putting out a fire with gasoline (Brooks' Law) — onboarding steals productivity from existing team members. The one exception is at the origin (project start), where onboarding is paid wholesale, not retail, and everyone is on the same clueless footing.

> [!question]- 8. What did Von Moltke the Elder actually mean, and how was his quote twisted?
> [!summary]- Answer
> His quote "no plan survives contact with the enemy" was twisted to mean "don't bother planning." He actually meant the opposite: since plans don't survive, you need a system of options — a plan for each possible enemy action. "A plan means nothing. Planning is everything."

> [!question]- 9. Why is over-budget failure better than over-schedule failure for an organization?
> [!summary]- Answer
> Most companies can afford to pay $2M instead of $1M, but wasting a year misses the market window. Over-budget is "failing management 101" (you get cut next cycle), while over-schedule is "Tuesday" (software is always late).

> [!question]- 10. How did Juval make project management "mechanic" and why does this matter?
> [!summary]- Answer
> He mechanized it by generating charts every Friday, pre-writing email templates with recommended remedies for each symptom, and sending them to all stakeholders. If nobody objects by Monday, he executes. This eliminates aggravation, builds trust, and lets the architect be project manager without spending extra time — because success comes from method, not heroism.

## Reflections & Discussion</arg_value></tool_call><tool_call>edit<arg_key>path</arg_key><arg_value>/Users/michael/Desktop/Projects/personal/juval-masterclass/Modules/Project Planning.md</arg_value><arg_key>edits</arg_key><arg_value>[{</arg_value></tool_call><tool_call>edit<arg_key>path</arg_key><arg_value>/Users/michael/Desktop/Projects/personal/juval-masterclass/Modules/Project Planning.md</arg_value><arg_key>edits</arg_key><arg_value>[{

**On Management Realities:**
Juval's framing here makes it unambiguously clear that "design" isn't a side concern about reuse or elegance — it's the only lever managers can pull when facing impossible deadlines and shrinking resources. The reason managers resent design is exactly what Juval identified: **N+1 benefits, deferred out of sight** during execution.

The one-to-one rule also reframes HR problems as engineering problems. You don't "hire more agile"; you **size services carefully**, then map a single owner to each one, and treat the architecture diagram as your org chart.

**Tensions:**
- *Team politics:* The lecture assumes developers can be assigned by coupling affinity — but in real companies, team dynamics may not align that way (e.g., people on leave, skill mismatches). Juval addresses this implicitly via apprenticeship grooming and senior oversight.
- *The apprentice model only works if leadership commits to it.* Grown-from-inside architects aren't going to appear overnight; Juval's candid admission ("it wasn't solved next Wednesday") means companies need a multi-year talent pipeline strategy, not a hiring fix.

> [!tip] Open question for the learner:  
> How would you pitch the **Gantt-as-pacifier** framing to your current boss without sounding dismissive of their planning process? Try scripting the conversation — what language turns "I don't need that" into "Here's how I'll meet *your* commitments"?

---

**On Project Process:**
The planning process takeaways reveal Juval's deep skepticism of traditional project management — Gantt charts, feature-based progress, big-bang integration, and clean-slate starts are all failure modes, not best practices. The common thread is **non-linearity**: complexity, integration cost, and failure modes all grow factorially or worse, while linear tools (more people, more time, more features) cannot keep up.

The **fuzzy frontend (15-25%)** is the antidote to clean-slate chaos: it's the phase where you deliberately introduce constraints, derive requirements, and establish enough architectural clarity to make the remaining journey tractable. Skipping it or rushing through it is the fastest path to a project that fails deterministically.

The **life insurance policy** framing is a masterclass in stakeholder management. Rather than fighting managers' need for control, Juval gives them options to choose from — but frames the choice as a documented decision they own. This is not cynicism; it's professional risk management. When the project fails, the paper trail proves you warned them.

**On Progress Reporting:**
The directive to report on integration points, not features, is perhaps the most counterintuitive and valuable insight. Features are a mirage — they look like progress but can mask fundamental integration failures. Integration points are the truth serum of a project: they either work or they don't. This aligns perfectly with staged delivery — each stage's success is measured by its integration points, not its feature count.

> [!tip] Open question for the learner:
> Think of a project you've worked on that failed or struggled. Which of these principles was violated? Was it a clean-slate start? Big-bang integration? Feature-based progress reporting? How would staged delivery have changed the outcome?

---

### Project Design — Critical Path, Float & Dynamic Staffing

> [!abstract]
> Project design is the architecture of the project itself — not a Gantt chart, not a feature list. It is the only way to answer *how long will it take* and *how much will it cost*, and the only way to staff a project efficiently, quickly, and safely.

---

#### Estimation: Accurate, Not Precise

Estimates don't matter nearly as much as most people think. The single most important thing is getting the **topology of the network** right — the architecture and dependencies between services. Individual estimates should be rough models (5, 10, 15, 20) — not precise (11 vs 12). The law of large numbers ensures over- and under-estimates cancel out across many activities.

**Two deadly estimation mistakes:**
| Mistake | Result |
|---------|--------|
| **Overestimation** (padding) | Work expands to fill allotted time (Parkinson's Law) → gold plating → increased complexity → even more time → project killed |
| **Underestimation** (rushing) | Developer cuts corners → "quick and dirty" → actually slower and worse → project destroyed |

Both are equally destructive. The only correct approach is **nominal estimation** — honest, un-padded estimates based on real understanding.

> [!danger] "Quick and dirty" Does Not Exist
> *"Quick and dirty is a figment of your sick imagination. Only deranged lunatics can come up with something called quick, dirty. Quick and dirty does not exist."* There is no version of quick and dirty that is acceptable in any aspect of life — yet software development treats it as a best practice.

---

#### The Critical Path

**James Kelly published the critical path paper in 1959. For 60 years, nobody improved on it.** This is the *only* way mankind has figured out to answer the question: **how long will it take?**

The critical path is the longest path through the activity network (longest in time, not necessarily in hops). It represents the **quickest possible way** the project could ever be built. You can always do it slower, never faster.

**How to compute it:** Work backward through the network. For each activity, its duration = its own effort + the maximum of all successor paths. The longest of these is the critical path.

> [!tip] Visual Encoding
> Highlight the critical path in bold/orange in your network diagram. This makes the project's true constraint immediately visible.

---

#### Float and Resource Assignment

Every non-critical activity has **float** — the amount of time it can be delayed without affecting the project end date. Float is *not* the same for every activity: some may have 5 days, others 60.

**The only correct way to assign resources to a project is based on float, low to high:**
1. Assign the critical path first (float = 0)
2. Then assign the next-lowest-float activity
3. Continue up the float spectrum

If you assign an activity with insufficient float before a lower-float activity, that lower-float activity becomes critical, the critical path shifts, and you **derail the project**.

> [!warning] The Float Insight
> *"Not one in a million project managers knows that you should only assign to a project based on float. Not one in a million."* Microsoft Project desktop can calculate float, but Microsoft dropped the feature from the online version because virtually nobody used it — even though it's the most basic thing a project manager should know.

---

#### Dynamic Staffing: The Wrong Question vs. The Right Question

**Wrong question:** "How many developers do we need?" (implies a static number)
**Right question:** "What is the lowest level of staffing that would allow you to progress unimpeded along your critical path at any moment in time?"

Staffing is **dynamic**, not static. It follows a curve:

```
Staffing
   ↑
   │        ┌──────┐
   │       ╱        ╲
   │      ╱          ╲____
   │     ╱   Peak       \
   │    ╱   Staffing     ╲______
   │   ╱                        \
   │  ╱  Core  Float→Ramp→Ramp  \
   │ ╱  Team    In   Out  Release\
   └─┴────────────────────────────→ Time
```

1. **Core team** on day one (PM, product manager, architect) — gathering constraints, doing project design
2. **Initial staffing** — just enough developers for the most enabling activities
3. **Ramp up** — absorb additional staff as enabling activities complete
4. **Peak staffing** — maximum team, maximum throughput
5. **Ramp down** — let go of developers as construction finishes
6. **System testing & release** — curve levels off

**Why lowest staffing?** Smaller teams are more efficient. A team of 4 costs two-thirds of a team of 6 *and* is more productive.

**Feast-famine cycles** (everyone working overtime, then nothing to do) are highly demoralizing and must be avoided by proper float-based staffing.

---

#### The Best Developer Always Goes to the Critical Path

Your best developer is not the one who types fastest — it's the **most trustworthy one**, the one that's reliable and going to deliver. The critical path is where the risk lives. Doing things faster off the critical path does nothing for the project. Slowing down the critical path slows down everything.

With one developer: assign to the critical path activity.
With two: first to critical path, second to the next highest-value activity.
With three or more: the third developer often **harms** the project by pestering the critical-path developer (context disruption).

---

#### Cost = Staffing × Time (Area Under the Curve)

The cost of a software project is **labor** — staffing times time. The area under the staffing-distribution curve is the total cost. Once you draw the curve, you can calculate cost with simple addition in Excel.

This is the **only way** to answer the question: how much will it cost?

---

#### Heat Map Color Coding by Float

Color-code activities by float to instantly see risk:
| Color | Float | Risk |
|-------|-------|------|
| **Black** | 0 (critical) | Highest — any delay kills the project |
| **Red** | Low | Urgent — must be staffed soon |
| **Yellow** | Medium | Watch — can float a bit |
| **Green** | High | Safe — plenty of room |

This reveals the **nexus of pain** — the cluster of black and red activities that demand immediate attention.

---

#### Pumping Float, Not Padding Estimates

Never change individual estimates to relax the project. Instead, **pump float along the critical path** — relax the project as a whole by adjusting the network structure, not by inflating individual numbers. This is the correct alternative to padding estimates, though Juval notes it's discussed in the advanced Project Design Clinic.

---

#### Roles: Architect vs. Project Manager

| Role | Responsibility |
|------|---------------|
| **Architect** | Produces the project design — the network, critical path, float analysis |
| **Project Manager** | Provides insight on constraints, priorities, and resource availability |

The architect and PM must work together, just as the architect works with the product manager on architecture. The PM knows what resources are actually available; the architect knows how to deploy them optimally.

---

#### Asking for Estimates: The Right Way

| Wrong | Right |
|-------|-------|
| "You have two weeks for this." | *Don't ask at all — this is a CLM* |
| "It's going to take two weeks." | *Setting them up for a CLM* |
| "How long will it take?" | *Open question, no bias* |
| "Two weeks!" | *A CLM — committing without analysis* |
| **"Please let me get back to you."** | ✅ *The only responsible professional answer* |

When someone gives you an estimate, **always check the first number** — it's completely bogus. Force them to itemize: testing, learning new SDKs, integration, documentation, manual, etc. The first number is just typing time.

---

#### The Boss Argument: No Good Outcomes

> [!warning] Never Argue With the Boss
> Every argument has three outcomes: you win, you lose, or it's a stalemate.
> - **You win** → you undermine the boss's power position → they'll get you eventually
> - **You lose** → you prove you're an idiot
> - **Stalemate** → you're labeled difficult, nobody can work with you
> 
> *"The boss is always in a position of power. People in position of power like power. They crave power."*

The solution: present **multiple options** with trade-offs. Empower the boss to choose. This is both effective stakeholder management and **life insurance** — if the project fails, the signed-off decision is your protection.

> [!danger] Legal Liability
> Signing a contract without proper time/cost analysis = being an idiot (legal).
> Signing a contract **knowing** you can't meet the numbers = **fraud** (criminal offense).
> This is why presenting multiple options with real numbers is essential — it eliminates the liability.

---

#### Agile Criticism: The Voodoo Metastasized Religion

Juval makes three definitive claims about what most people call "agile":
1. It can **never** be the fastest way of building any system (ignores critical path)
2. It can **never** be the cheapest way (ignores float-based staffing)
3. It can **never** be the safest way (ignores float analysis)

> [!quote]
> *"The voodoo metastasized religion you call agile will always be solving a non-linearly worse problem. Even that they will not be doing the slowest, the cheapest, the most efficient or the safest. And Murphy says they're going to be doing it the most expensive, the riskiest, the longest, the most painful, the least efficient."*

The compensation for not doing proper project design is **crazy levels of overcapacity** — throwing bodies at a Kanban board and hoping something hits the critical path. This is not engineering; it's a mob.

---

#### Physical Engineering Analogies

In every other engineering discipline, project design is natural:
- **Refineries**: You don't start chipping pipes in the desert. You design the order in which every pipe is welded, the crane access, the roads, the foundations.
- **Microchips**: Intel doesn't take sand and make a CPU appear. Design and manufacturing engineers work out every photolithography layer in sequence.
- **Cars**: Toyota designs the entire supply chain, the shipping order, and the factory before building a single car.

In software, the perception of "no physical waste" leads to the delusion that project design isn't needed. But **the waste is your energy, your prospects, your use**. You become the waste product.

---

#### Astronaut Architects

> [!warning] Don't Be an Astronaut Architect
> *"Floating in space, holding the architecture. It sounds like this: 'Yeah, it's a good design. I can afford to build it. I don't know.'"

Nobody should fly blind. The critical path exists whether you acknowledge it or not. Better to understand it, understand float, and work from reality.

---

#### Career Advice: Trust Me or Fire Me

> [!tip] The Only Professional Stance
> *"Trust me or fire me. It's an illusion that there's anything in between."*
> 
> *"Never wait for the boss to give you permission for doing these things. In life, you do the right things because they're the right things to do. Not because somebody gave you permission for doing it."*
> 
> *"Nobody argues with success. That's why."*

First time around, it's hard. Second and third time, easy. The medicine for making it work the first time will be discussed in the advanced class (Thursday).

---

#### Organization Incentivizes the Worst Behavior

> [!danger] The Trap
> A top manager gives you a dream project: unlimited budget, perfect requirements, a time machine showing it takes one year. What do you do?
> 
> **Right answer**: Hire an architect first, spend 3–4 months on proper design. Result: empty offices, manager looks bad.
> 
> **"Smart" answer**: Hire developers immediately, assign features. Result: architect's design comes 3–4 months later and is irrelevant — developers built something completely different. Project is late.
> 
> *"Organizations incentivize managers for working the worst possible way."*

Developers want to code. Methodologies like agile let them pretend they're doing good work while actually just code-molesting. Managers get to gloat about "agile." It's marriage made in hell between the code monkey and the knuckle dragger.

---

### Composable Design — The Architecture of Permanence

> [!abstract]
> Composable design is a design methodology where you identify a small set of core components (typically ~10) that you can combine in various ways to satisfy **all** use cases — present, future, known, and unknown. The key insight: never design against requirements. Design against a small set of building blocks that can be recomposed when requirements change.

---

#### Core Use Cases vs. Fluff

Requirements are almost always **fluff**: variations of things, happy/sad/incomplete cases, one-off customer requests. Separate requirements into:

| Type | Characteristics | Example |
|------|----------------|---------|
| **Core use cases** | Essence of the system, essence of the business, what brings customers to the door | Federal Express shipping packages |
| **Fluff** | All variations, edge cases, one-offs | Customer-specific tweaks, edge cases |

**The order of magnitude of core use cases is 1 (typically 2–3).** Rarely 4, almost never 5, Juval has only seen 6 once. If your product manager puts 10 bullets on a brochure, they get fired.

---

#### The Mission of the Architecture

The mission: **support all use cases, present and future, known and unknown.** This is where the bar is set. Never lower it to meet your inadequacies.

> [!danger] Never Lower the Bar
> *"Stop making excuses. Start thinking about it structurally like an engineer. Don't lower the bar to meet your inadequacies. You always, always lower the bar. I can't do it, so maybe I should lower the bar to what I can do. No. No. The bar must be exactly where I set it."*

---

#### Composable Design — The Core Idea

Your mission is to come up with a **smaller set of components** that you can put together to satisfy each of the core use cases. Other use cases represent different **interactions** between building blocks, not different decompositions.

**Key principles:**
- **Never design against requirements** — it's suicidal. Requirements change.
- Design against a small set of building blocks that can be **recomposed**.
- When requirements change, put components together in **different ways** — the design doesn't change.
- The **smallest set** is best: architects suffer from extreme pendulum effect (tiny swings at origin = monster swings downstream).

> [!quote] The Definition
> *"Composable design is a design that doesn't try to satisfy any use case in particular. What's the point? These use cases are going to change. Never, ever try and satisfy any use case in particular. It's suicidal. It's a death wish."*

---

#### The ~10 Components Rule

The optimal number of components is approximately **10** (order of magnitude). This isn't arbitrary — it's driven by **combinatorics**:

| # Components | Combinations (n!) | Use Cases Supportable |
|-------------|-------------------|----------------------|
| 2–3 | 6 | Too few |
| **10** | **~3.6 million** | **Bazillion — enough for all use cases** |

Real-world examples converge on ~10:
- Car: gearbox, fuel pump, engine block, radiator, battery ≈ 10
- Laptop: CPU, hard drive, motherboard, memory, GPU ≈ 10
- Human body: kidneys, liver, heart, lungs, brain ≈ 10
- Immune system: ~10 proteins
- Organic chemistry: ~10 elements

> [!tip] Economics Drives the Number
> No vendor (artificial or natural) can afford too few components (can't respond to changes) or too many (overly complex, overpriced, goes out of business). ~10 is the smallest set that gets away with.

---

#### Composable Design Enables True Agility

> [!warning] Agility ≠ Rituals
> *"You know what it takes to be agile. All you've been doing your entire career was rituals, useless pagan rituals, practicing a voodoo metastasized religion at the altar of doom. That's what you've been doing. The rituals cannot replace essence."*

True agility = ability to respond quickly to changes in requirements. Composable design provides this because:
1. Components stay stable
2. Only the interaction/composition changes
3. Change cost is minimized

---

#### The 85% Statistic — Bugs Are in Requirements

> [!danger] The Hard Truth About Requirements
> *"85% of all the cases where systems that were thought to have zero bugs were deployed and then still were found to have bugs, 85% of all of those bugs were traced directly to the requirements."*

- Requirements bugs can't be detected in advance
- If you design against requirements, a wrong requirement means the whole system is wrong
- **Composable design is the only practical way** to address system-level defects in requirements

---

#### The Business Architect — A Missing Role

There's a missing role in software development ecology:

| Role | Domain | Skills |
|------|--------|--------|
| **Software Architect** | Software domain (architecture, interaction diagrams) | Analytical, abstract, systems thinking |
| **Business Architect** | Business domain (requirements, use cases, operational concept) | People-oriented, analytical, abstract |

The business architect:
- Wines and dines customers
- Derives requirements
- Captures quiet behavior in diagrams
- Creates the small set of components
- Owns the use cases (not developers!)

InfoWorld named this the **#1 hottest new job in IT**. The role requires a rare combination: right-brain + left-brain. Leonardo da Vinci would be one such person — and there are approximately zero of them per generation.

---

#### Workflow Engines — The Unfulfilled Promise

The vision: business people capture required behavior in a visual tool → system composes components → code is generated automatically. This would give **extremely fast cycle time** because the business side never crosses into the software world.

**Why every workflow tool failed:**
1. Targeted the wrong audience (developers instead of business people)
2. Microsoft's WF team (WCF team!) understood the need but made a developer tool
3. The tool required code-behind, connection strings, serialization — "wicked visual programming"
4. The startup that built a real business-person tool went out of business (no customers because the business architect role doesn't exist)

---

#### AI and Artificial Agility

AI can now solve what the workflow engine couldn't: **exploring the combinatorial space** of component interactions to find optimal compositions.

- With ~10 components and ~3.6 million possible combinations, no human can evaluate all options
- AI can: simulate inputs, use Bayesian logic, genetic algorithms, run all combinations in parallel
- **Spec-driven development (SDD)**: you focus on correctly specifying use cases, AI composes the solution
- Linux Foundation announced **Doclang** — a formal industry standard for specifying use cases that AI can understand natively

> [!tip] The Architect Becomes the Enabler of AI
> *"The architect becomes the enabler of the AI... Your documentation now serves as the super prompt from hell. That is how you enable it."*

---

#### Context Rot — Writing Documentation for AI

> [!danger] Longer Prompts = Worse Results
> *"Recent research has identified a phenomenon called context rot. Where increasing the prompt's length degrades the result, especially the accuracy of the results."*

For documentation (which will serve as AI prompts):
- **Focused and short** — one focused prompt per topic
- **Cover all relevant details, but no more, no less**
- **Avoid repetitions** — saying the same thing in multiple ways makes AI worse
- **No passive voice** — passive voice is "the refuge of those who don't want to say exactly who or what or when something happens"
- **Avoid distractors** — irrelevant content degrades accuracy
- **Answer all possible questions** — imagine a reader who knows nothing about the domain

---

#### The Future: Software Industrial Revolution

| Before Industrialization | After Industrialization |
|-------------------------|------------------------|
| Every system handmade by absolute experts | Factories with assembly lines |
| Every system a one-off | Interchangeable, maintainable components |
| Insanely expensive | Mass production |
| 97% of population toiled fields | 3% work fields (tractors + fertilizer) |

**The software equivalent:**
- Composable design + AI = software factories
- Fewer developers needed (machines do the coding)
- **Much higher demand for architects** (nobody says we have enough engineers)
- The architect who can "crank the handle" will be worth their weight in gold

> [!tip] Career Advice: Hide the Elephant
> *"If you are walking down a trail in a jungle and an elephant is standing behind you, there are three options: step out of the way (give up), get trampled (be a mediocre developer), or run faster (become an exceptional architect). The best option is to hide the elephant — deploy composable design + AI."*

---

### Composable Design — Key Excerpts

> *"You will never get anything but garbage for requirements. But every cloud has a silver lining."*

> *"How many core use cases are you going to have? ... It could be two or three. We find the number two and three to be incredibly common across most systems. Rarely we see four. I hardly ever saw five. And I've only seen six once."*

> *"Your mission in life is to come up with a smaller set of components that you can put together to satisfy each of the core use cases."*

> *"Composable design is a design that doesn't try to satisfy any use case in particular. What's the point? These use cases are going to change. Never, ever try and satisfy any use case in particular. It's suicidal."*

> *"If you have 10 components, the factorial of 10 is bazillion, bazillion, bazillion. Somewhere around 10, there's such an explosion of possible interaction, you can now satisfy all the use cases, present and future, known and unknown."*

> *"85% of all the cases where systems that were thought to have zero bugs were deployed and then still were found to have bugs, 85% of all of those bugs were traced directly to the requirements."*

> *"Composable design is the only practical way of addressing system-level defects that are in the requirements."*

> *"You know what it takes to be agile. All you've been doing your entire career was rituals, useless pagan rituals, practicing a voodoo metastasized religion at the altar of doom."*

> *"The person doing this side of the machine, we should call the business architect. So it turns out that we are actually missing a role here in the ecology of the software project."*

> *"I call this idea artificial agility. And I've been waiting for this for a very long time."*

> *"Your documentation now serves as the super prompt from hell. That is how you enable it."*

> *"In such a world, we're not going to need as many developers. However, what about the demand for architects? Before the industrial age, what demand was there for engineers? Practically none. With industrial age, no country in the world says we have enough engineers."*

---

## Quiz — Composable Design

> [!question]- 1. What is the difference between core use cases and fluff, and what order of magnitude should core use cases be?
> [!summary]- Answer  
> **Core use cases** represent the essence of the system and the nature of the business — they're what bring the customer to the door. **Fluff** is all the variations (happy case, sad case, incomplete case, one-off customer requests). Core use cases are almost always **1–3** (order of magnitude of 1). It's rare to see 4, almost never 5, and Juval has only seen 6 once in hundreds of systems.

> [!question]- 2. What is "composable design" and why does Juval say never to design against requirements?
> [!summary]- Answer  
> **Composable design** is designing a smaller set of components that you can put together in different ways to satisfy each use case. Requirements change → you put components together differently → the design doesn't change. Designing against requirements is "suicidal" and a "death wish" because when requirements change, your entire design and code must change, making change maximally painful.

> [!question]- 3. Why does Juval say the ~10 components rule exists? What mathematical principle supports it?
> [!summary]- Answer  
> Because of **combinatorics**: the number of use cases you can support is proportional to the combinations of your components. Factorial of 2–3 ≈ 6 use cases (not enough). But factorial of 10 ≈ bazillion combinations — an explosion of possible interactions that can satisfy all use cases, present and future, known and unknown. This is reinforced by real-world examples: cars (~10 components), laptops (~10), the human body (~10), immune system (~10 proteins).

> [!question]- 4. According to the transcript, 85% of bugs in deployed "bug-free" systems trace back to what source, and why is composable design the only practical solution?
> [!summary]- Answer  
> **85% of bugs** trace directly to **the requirements**. The problem is you can't tell in advance that requirements are wrong. Composable design is the only practical solution because when requirements change (or were wrong), you just put components together in different ways — you don't have to redesign the entire system.

> [!question]- 5. What is the "business architect" role that Juval says is missing from software development?
> [!summary]- Answer  
> The business architect owns the business side of the machine: wine and dine customers, derive requirements, capture quiet behavior in diagrams, come up with the small set of components, capture operation concept and interfaces. The role is a **right-brain/left-brain combination** — both people-oriented AND analytical/abstract. InfoWorld later named this the #1 hottest new job in IT. Without this role, developers end up owning the use cases (which is wrong — they can't possibly understand the business deeply enough).

> [!question]- 6. Why does Juval say workflow engines have "horrible execution" despite "amazing potential"?
> [!summary]- Answer  
> Every vendor targeted the wrong audience (developers instead of business people) and made the tool part of the software world instead of the business world. The result: tools full of code-behind, connection strings, serialization — "a wicked visual programming" approach that's far worse than raw programming. Microsoft's WF team (WCF team, of all people!) understood the need but targeted developers. The startup that actually built a business-person tool went out of business because the fundamental problem is that the **business architect role doesn't exist** to use it.

> [!question]- 7. What is "artificial agility" and how does AI enable it?
> [!summary]- Answer  
> **Artificial agility** is AI exploring the combinatorial space of component interactions to find the best way to compose them for any given requirement. With ~10 components and ~bazillion possible combinations, no human can try all of them — but for AI, it's "a Tuesday afternoon." AI can simulate inputs, use stochastic/Bayesian logic, try genetic algorithms, and run all combinations in parallel to find optimal compositions.

> [!question]- 8. What is "context rot" and what does it mean for software documentation?
> [!summary]- Answer  
> **Context rot** is a phenomenon where increasing prompt length degrades AI accuracy, especially with high signal-to-noise ratios. The result: documentation must be **focused, clear, concise**, and answer all possible questions without redundancy. Adding more information or saying the same thing in multiple ways makes AI results worse. No passive voice, no distractions, no needles-and-haystacks.

> [!question]- 9. What is the "industrial revolution" analogy Juval uses for the future of software development?
> [!summary]- Answer  
> Today, software is built pre-industrialized: every system is handmade by absolute experts, each system is a one-off, nothing is interchangeable or maintainable. The future: software factories with assembly lines, where AI/composable design tools enable **continuous delivery** with machines doing the coding. Just as industrialization reduced farming from 97% to 3% of the population, AI+composable design will reduce the need for developers dramatically while dramatically increasing demand for architects (who design the components).

> [!question]- 10. How does composable design enable "extreme agility" for software products?
> [!summary]- Answer  
> By maintaining a fiction that all customers use the same version, you can **embed composable design in the end product**. Every customer can then customize their own version of the software by composing components differently. Every user can have their own version. Even time-based versions (e.g., weekend vs. weekday workflows). This is what Juval's own Energy product does — customers run different behaviors based on time and events without bothering the engineering group. The cycle time becomes extremely short because business people capture required behavior on the business side, not the software side.

## Related

- [[MOC — Course Overview]]
- [[Modules/The Architect]]
- [[Modules/Agile and Design]]
- [[Modules/Microservices Development Process]]
- [[Modules/Design and Architecture]]
- [[Transcripts/Staffing.md|📜 Staffing Lecture (raw)]]
- [[Transcripts/Planning.md|📜 Planning Lecture (raw)]]
- [[Transcripts/Service Lifecycle.md|📜 Service Lifecycle Lecture (raw)]]
- [[Transcripts/Project Tracking.md|📜 Project Tracking Lecture (raw)]]
- [[Transcripts/Project Design.md|📜 Project Design Lecture (raw)]]
- [[Transcripts/Composable Design.md|📜 Composable Design Lecture (raw)]]
- [[Transcripts/Documentation.md|📜 Documentation Lecture (raw)]]

## Reflections & Discussion

**On Project Tracking:**
The Project Tracking lecture introduces a fundamentally different approach to project management — one that treats the plan as a living, breathing entity rather than a static artifact. The key insight is that **projects are dynamically unstable chaotic systems** (like the F-16 fighter jet or the human body) that require constant, tiny corrections to stay on course. This reframes project management from "heroic end-game rescue" to "continuous micro-adjustment."

**On Earned Value as a Design Tool:**
Earned Value is not just a tracking mechanism — it's a project **design** tool. By plotting the earned value curve, you can immediately see if a plan is viable (shallow S) or dead on arrival (impossible curve from back-scheduling). The slope of the curve represents team throughput, making it the only fair way to compare teams.

**On the Two-Minute Manager:**
Juval's mechanization of project management is perhaps the most liberating idea: if you structure the process correctly, project management becomes sixth-grade math that can be fully automated. Generate charts every Friday, pre-write email templates with recommended remedies, and let the system run itself. This eliminates aggravation, builds trust, and frees the architect to focus on design.

**Tensions & Questions:**
- *The "communal lie" is deeply entrenched.* Most organizations have managers reporting 60%, 80%, 90% done — all bogus. Introducing binary exit criteria requires cultural change, not just process change.
- *Resource leaks at 50% are endemic.* The technique of escalating to the lowest common manager is powerful, but requires organizational authority that many architects don't have.
- *The F-16 analogy is elegant but incomplete.* Software projects are chaotic systems, but unlike the F-16 (which has a computer constantly correcting), most projects have no equivalent automated control system. Who plays the role of the computer?

> [!tip] Open question for the learner:
> Think of a project you're currently on (or recently worked on). What would the earned value curve look like? Is it a shallow S, or something impossible? What would the four-symptom diagnosis tell you about the project's health?

---

### Documentation — The External Documentation Mandate

> [!abstract]
> Juval is vehemently **against inline code documentation** but equally vehemently **for external documentation**. Good code reads like natural language — if you *need* comments to understand it, the code isn't good enough. But the best form of external documentation — the STD (Software Design Document) — is non-negotiable. Without it, architecture benefits vanish, new developers can't be onboarded, and management can't trust your work.

---

#### No Inline Code Documentation

> [!warning] If You Need to Document It, It's Not Good Code
> Good code must be self-explanatory: short meaningful functions, everything passes the spell checker, every variable has a meaningful name (`customerBalance` not `val`), everything reads like natural language. If you need to document your code, it's not good code. And if you don't have good code, all hope is lost.

- Step into .NET itself or any Java object — there is **no inline documentation**. The code speaks for itself.
- Juval is NOT saying "don't document." He is very much **in favor of external documentation**.
- The distinction: inline comments on code vs. comprehensive external documentation (the STD).

---

#### The STD (Software Design Document) — The Best Form of External Documentation

The iDesign STD doesn't just document "the second parameter is an int." It covers:

| Section | What It Covers |
|---------|---------------|
| **Project Overview** | Why are we here? Business objectives, not "it's cool" |
| **Vision & Mission** | The system's purpose and direction |
| **Operational Concept** | How all pieces of code operate together — how it comes from the cloud, goes to the queue, starts processing. Can't be understood by looking at individual code. |
| **Onboarding** | What does it take for a new developer to understand the system? |
| **Assumptions** | "We always do this, we never do that" — if it's only in folklore, it doesn't exist |
| **All Interfaces & Parameters** | Meaningful documentation: what are the allowed values? Pre/post conditions? Sample code? |
| **Scenarios** | How interactions between components solve particular use cases |
| **Language Extensions** | How custom language features work in the system |
| **Subsystem Documentation** | Detailed documentation for each subsystem, often dozens of pages per component |
| **Context Maps** | Execution context: who hosts whom, concurrency, security boundaries, transaction propagation |

> [!danger] The State of Documentation Industry Today
> Most .NET framework documentation says "the second parameter is an int" and nothing more. Developers have stopped pressing F1 because the docs are so bad (perhaps AI-generated). This is exactly the standard you should **not** replicate.

---

#### The Operational Concept — Can't Be Understood From Code Alone

The operational concept describes **how the entire system operates** — it's the forest, not the trees. No single file of code contains it.

- Without it, new developers must nag everyone for understanding
- At worst, they misunderstand the system and **butcher it**
- At best, they spend months getting up to speed
- The operational concept is impossible to extract from individual code files

---

#### Documentation Must Be Part of the Lifecycle — Not an Afterthought

There are only three options for documentation timing:

| Option | Reality |
|--------|---------|
| Write it at end of project | **Never happens.** No project in history has had time to write world-class docs at the end. Saying "we'll write docs at the end" = saying "we won't have documentation." |
| Write it once during lifecycle | **Doesn't happen.** On average, everything changes at least once. You'll write the STD at least twice. On one project Juval measured, developers wrote it **three times**. |
| Make it part of the lifecycle (review cycles) | ✅ **The only viable option** |

> [!danger] "We'll write documentation at the end" = "No documentation" = "No architecture"
> If you don't document to an exceptional degree, you can kiss goodbye any benefit of architecture. Architecture without documentation is meaningless — nobody can maintain it because nobody can understand it.

**Lifecycle integration:**
- Make documentation contribution the input for design reviews (not code or sketches)
- Developers initially resent it, but it drastically reduces their stress
- Forces crystallization of understanding — thinking in plain language is harder than thinking in code, which makes the design stronger
- "Forcing somebody to write down in clear plain language what is this doing and why is forcing them to truly crystallize it"

---

#### Design Consistency — The Higher Level of Design Integrity

> [!warning] Design Integrity Is Not Enough
> Even if you have perfect design integrity (all parts work flawlessly together), it's not enough. If all 20 services look and feel different, maintenance is absolute hell.

**Design consistency** means all services look as if they came from the same mint — cookie-cutter uniformity. Maintaining "this" is easy; maintaining "these 20 different things" is error-prone and confusing.

---

#### Great Documentation = Professional Trust Signal

> [!tip] Management Can't Tell Design from Orange Juice
> Most managers/investors cannot distinguish good design from bad, good developers from bad. They reward what they *can* evaluate — and nothing conveys excellence like great documentation.

- Great documentation signals: "I'm trustworthy, I know what I'm doing, I'm a stickler for quality and detail"
- Juval's anecdote: spent 10 days designing, 8-10 days documenting, handed the boss a beautifully printed folder. The boss looked at it, put it on the shelf, and said "I'll start documenting it. I know it's good."
- **Great documentation is your career insurance.** It's the one thing management can actually evaluate.

---

#### Context Maps — The Most Important Thing You'll Ever Document

> [!danger] Context Maps Are Non-Negotiable
> These capture the execution context of the system and **cannot be inferred by looking at code**, no matter how long you study it.

Context maps document:
- **Hosting**: Who hosts whom?
- **Concurrency**: What executes concurrently with what?
- **Security boundaries**: Where do authentication/authorization happen?
- **Transaction propagation**: How do transactions flow across the system?
- **Queuing patterns**: How do messages flow through queues and listeners?
- **Concurrency conflicts**: Which resources create deadlocks, and how to resolve them?

A simple diagram showing transaction boundaries, security zones, and message flows is worth more than weeks of code reading. Without context maps, you cannot convey design intent, you cannot get design review, and you cannot onboard anyone.

---

### Documentation — Key Excerpts

> *"Good code must be self-explanatory, short, meaningful functions, everything passes spell checker... if you need to document your code, it's not good code and if you don't have good code all hope is lost."*

> *"I'm very much in favor of external documentation."*

> *"If you don't document to an exceptional degree your handiwork, you can kiss goodbye any benefit of architecture."*

> *"Saying you're writing documentation at the end of the project is the same as saying we're not going to have documentation, and saying we're not going to have documentation is the same as saying no architecture."*

> *"On average everything changes at least once, so on average you're not going to write the STD once, you're going to write it twice."*

> *"Nothing conveys excellence like great documentation."*

> *"Most management, most decision makers, owners, investors, cannot tell design from orange juice."*

> *"Perhaps the most important thing you will ever document is what I call context maps."*

> *"I cannot understand how everything works together... context maps tend to be in a free format way so there shouldn't be any problem in anybody just looking at it intuitively."*

---

## Quiz — Documentation

> [!question]- 1. What is Juval's position on inline code documentation vs. external documentation? Explain the distinction.
> [!summary]- Answer
> Juval is vehemently **against inline code documentation** — good code must be self-explanatory, read like natural language, have meaningful names, and short functions. If you need to comment it, it's bad code. But he is equally **in favor of external documentation** (the STD). The distinction: code should speak for itself, but comprehensive external documentation (project overview, operational concept, interfaces, scenarios, context maps) is non-negotiable.

> [!question]- 2. What does the STD cover beyond "parameter is an int"? Name at least five sections.
> [!summary]- Answer
> The STD covers: (1) Project overview / business objectives, (2) Vision and mission, (3) Operational concept (how all pieces operate together), (4) Onboarding requirements, (5) Assumptions, (6) All interfaces and parameters with meaningful documentation (allowed values, pre/post conditions, sample code), (7) Scenarios / use cases, (8) Language extensions, (9) Subsystem documentation, (10) Context maps.

> [!question]- 3. Why does Juval say the operational concept cannot be understood from code alone?
> [!summary]- Answer
> The operational concept describes how the entire system operates — it's the forest, not the trees. No single file of code contains it. Without documenting it, new developers must nag everyone for understanding, and at worst they misunderstand the system and butcher it.

> [!question]- 4. Juval says there are only three options for documentation timing. What are they, and which is the only viable one?
> [!summary]- Answer
> (1) Write it at the end of the project — never happens, no project in history has had time for this. (2) Write it once during the lifecycle — doesn't happen, on average everything changes at least once so you write it twice or more. (3) Make it part of the lifecycle — ✅ the only viable option, integrated into design review cycles.

> [!question]- 5. Why does Juval say "saying you'll write documentation at the end" is equivalent to "no architecture"?
> [!summary]- Answer
> Because without documentation, nobody can understand or maintain the code. If nobody can maintain it, the architectural benefits (maintainability, extensibility, reuse) are meaningless. Architecture without documentation = nobody can benefit from it = no architecture.

> [!question]- 6. What is design consistency, and why is it a higher level than design integrity?
> [!summary]- Answer
> Design integrity means all parts work flawlessly together. Design consistency means all services look and feel the same — as if they came from the same mint, like cookie cutters. Even with perfect design integrity, if 20 services all look different, maintenance becomes hell. Consistency makes maintaining one thing easy instead of maintaining 20 different things.

> [!question]- 7. Why does great documentation matter for your career, according to Juval?
> [!summary]- Answer
> Most managers/investors cannot tell good design from bad or good developers from bad — they can't tell "design from orange juice." The one thing they *can* evaluate is documentation quality. Great documentation conveys: "I'm trustworthy, I know what I'm doing, I'm a stickler for quality and detail." It's the ultimate professional trust signal.

> [!question]- 8. What are context maps, and why does Juval call them "perhaps the most important thing you will ever document"?
> [!summary]- Answer
> Context maps capture the execution context: who hosts whom, what executes concurrently, security boundaries, transaction propagation, queuing patterns, and concurrency conflicts. They cannot be inferred by looking at code no matter how long you study it. Without them, you cannot convey design intent, get design review, or onboard anyone.

> [!question]- 9. Why does Juval argue that documentation should be part of design reviews, not just code reviews?
> [!summary]- Answer
> Forcing developers to write in clear, plain language what the design is doing and why forces them to truly crystallize their understanding. Thinking in code is not a good idea — you need to express design intent before implementing it. Documentation reviews catch misunderstandings earlier and produce stronger designs than code reviews alone.

> [!question]- 10. What was Juval's anecdote about the boss and the documentation folder, and what does it illustrate?
> [!summary]- Answer
> Juval spent 8-10 days documenting his design, produced a beautifully printed folder with diagrams and interactions, handed it to the boss. The boss looked at it, put it on the shelf, and said "I'll start documenting it. I know it's good." It illustrates that great documentation speaks for itself — management doesn't need to understand the technical details to recognize professional excellence.

---

## Quiz — Project Design

> [!question]- 1. What are the two deadly estimation mistakes, and why are they both destructive?
> [!summary]- Answer  
> **Overestimation (padding):** Work expands to fill allotted time (Parkinson's Law), leading to gold plating, increased complexity, and even more time — project killed.
> **Underestimation (rushing):** Developer cuts corners into "quick and dirty," which actually takes longer and produces worse code — project destroyed.
> Both are equally destructive. The only correct approach is nominal estimation — honest, un-padded estimates.

> [!question]- 2. Why does Juval say estimation "don't matter nearly as much as what you think they do"?
> [!summary]- Answer  
> Because the single most important thing is getting the **topology of the network** right — the architecture and dependencies between services. Good estimates should be accurate but not precise (5, 10, 15, 20 is fine; 11 vs 12 doesn't matter). The law of large numbers ensures over- and under-estimates cancel out across many activities.

> [!question]- 3. What is the critical path, and why is it the only way to answer "how long will it take?"
> [!summary]- Answer  
> The critical path is the longest path through the activity network (longest in time, not hops). It represents the quickest possible way the project could ever be built — you can always do it slower, never faster. Kelly published it in 1959; for 60 years nobody improved on it. It's computed by working backward: each activity's duration = its own effort + the maximum of all successor paths.

> [!question]- 4. What is float, and why must resources be assigned based on float low to high?
> [!summary]- Answer  
> Float is the amount of time a non-critical activity can be delayed without affecting the project end date. Resources must be assigned low-to-high by float because if you staff an activity with insufficient float before a lower-float activity, that lower-float activity becomes critical, the critical path shifts, and you derail the project. Only one in a million project managers knows this.

> [!question]- 5. What is the right question to ask about staffing, and what does the staffing curve look like?
> [!summary]- Answer  
> Wrong question: "How many developers do we need?" (static). Right question: "What is the lowest level of staffing that would allow you to progress unimpeded along your critical path at any moment in time?" The curve: core team starts, initial staffing for enabling activities, ramp up, peak staffing, ramp down, system testing & release.

> [!question]- 6. Why is the third developer often harmful on a project with just a critical path?
> [!summary]- Answer  
> The third developer will pester the critical-path developer (context disruption). With one developer, assign to critical path. With two, first to critical path, second to next highest-value. With three+, the third often harms the project by disrupting the critical-path developer.

> [!question]- 7. What is the "life insurance policy" approach to presenting options to managers, and what is the legal liability behind it?
> [!summary]- Answer  
> Present multiple options with trade-offs and get the manager's signed-off choice. This is life insurance because if the project fails, the paper trail proves you warned them. Legally: signing a contract without proper analysis = being an idiot (legal). Signing a contract **knowing** you can't meet the numbers = **fraud** (criminal offense). Presenting real options eliminates this liability.

> [!question]- 8. Why does Juval call what most people call "agile" a "voodoo metastasized religion"? Give three specific reasons.
> [!summary]- Answer  
> 1. It can **never** be the fastest way (ignores the critical path — developers pluck stories organically, zero chance they hit the critical path).
> 2. It can **never** be the cheapest way (ignores float-based dynamic staffing — constant overcapacity is the only compensation).
> 3. It can **never** be the safest way (ignores float analysis — no visibility into which activities are at risk).
> The result: most expensive, riskiest, longest, most painful, least efficient.

> [!question]- 9. What does the "astronaut architect" analogy mean, and what should you do instead?
> [!summary]- Answer  
> An astronaut architect floats in space, holding the architecture, saying "Yeah, it's a good design. I can afford to build it. I don't know." Nobody should fly blind. The critical path exists whether you acknowledge it or not. Better to understand it, understand float, and work from reality.

> [!question]- 10. In the dream-project trap scenario, why do organizations incentivize managers to work the worst possible way?
> [!summary]- Answer  
> If you hire an architect first and spend 3–4 months on design, the manager sees empty offices and looks bad. If you hire developers immediately and assign features, the architect's design comes 3–4 months later and is irrelevant — developers built something completely different. Either way the manager loses. So organizations incentivize the worst behavior: skip design, hire bodies, blame methodology when it fails.

> [!question]- 11. What is the correct professional answer when someone asks "How long will it take?"
> [!summary]- Answer  
> "Please let me get back to you." This is the only responsible professional answer. It's neither yes nor no, not flipping a number. Any immediate answer is a CLM (career-limiting move) — either you committed without analysis, or you sound like a quack.

> [!question]- 12. How does the cost of a software project relate to the staffing curve?
> [!summary]- Answer  
> Cost = staffing × time, which is the **area under the staffing-distribution curve**. Once you draw the curve, you calculate cost with simple addition in Excel. The cost of your laptop is noise; the cost of software is labor.

> [!question]- 13. What are the three outcomes of arguing with the boss, and why is every one a CLM?
> [!summary]- Answer  
> 1. **You win** → you undermine the boss's power position → they'll get you eventually (bosses crave power and surround themselves with yes-men).
> 2. **You lose** → you prove you're an idiot.
> 3. **Stalemate** → you're labeled difficult, nobody can work with you.
> The solution: present multiple options and let the boss choose — this empowers them rather than undermining them.

> [!question]- 12. What physical engineering analogies does Juval use to show that project design is natural everywhere except software?
> [!summary]- Answer  
> - **Refineries**: You don't start chipping pipes in the desert. You design the weld order, crane access, roads, foundations.
> - **Microchips**: Intel doesn't take sand and make a CPU appear. Every photolithography layer is designed in sequence.
> - **Cars**: Toyota designs the entire supply chain, shipping order, and factory before building a single car.
> In software, the perception of "no physical waste" leads to the delusion that design isn't needed — but the waste is your energy, prospects, and use.

> [!question]- 14. What is "pumping float" and how does it differ from padding estimates?
> [!summary]- Answer  
> **Padding estimates** = inflating individual activity durations → Parkinson's Law → gold plating → project killed.
> **Pumping float** = adjusting the network structure to relax the project as a whole, without changing individual estimates. This is the correct alternative, though Juval notes it's discussed in the advanced Project Design Clinic.

> [!question]- 15. What is the color-coded heat map for float, and what does it reveal?
> [!summary]- Answer  
> | Color | Float | Risk |
> |-------|-------|------|
> | Black | 0 (critical) | Highest — any delay kills the project |
> | Red | Low | Urgent — must be staffed soon |
> | Yellow | Medium | Watch — can float a bit |
> | Green | High | Safe — plenty of room |
> This reveals the **nexus of pain** — the cluster of black and red activities demanding immediate attention.

> [!question]- 16. Why does Juval say "trust me or fire me" is the only professional stance?
> [!summary]- Answer  
> There's nothing in between. Never wait for permission to do the right thing. In life, you do right things because they're right, not because someone gives permission. "The boss told me" is not a valid defense. Nobody argues with success — that's why. First time around it's hard; second and third time, easy.

---

### Process Flow — The Two-Domain Model and the Curse of Requirements Change

> [!abstract]
> Every software project spans two domains: the **business domain** (requirements, use cases, product decisions) and the **software domain** (static architecture + dynamic interaction diagrams). The core insight: **never design against requirements** — design against interaction diagrams instead. When requirements change, only the mapping changes, not the design.

---

#### The Two Domains

Every software project has **two domains**:

| Domain | Contents | Characteristics |
|--------|----------|-----------------|
| **Business domain** | Marketing requirements → derived requirements → use cases | Mutable, comes from customers/product managers |
| **Software domain** | Static aspect (architecture, STD) + Dynamic aspect (interaction diagrams) | Stable once designed |

- The **business domain** starts with marketing requirements — what customers say over golf
- **Derived requirements** are what you actually build: not what the customer asked for, but what they *really* need
- The **software domain** has two sub-aspects:
  - **Static**: architecture, layers, components, STD
  - **Dynamic**: interaction diagrams showing how components interact
- **Code** = "the act of marrying the interaction diagram to the STD" — give me this using this

---

#### Marketing Requirements vs. Derived Requirements

Marketing requirements are **not** derived requirements. They overlap, but neither is a subset of the other.

**Why derived requirements differ from marketing requirements:**
1. **Innovation**: Customers won't innovate for you (Henry Ford's "faster horse" — nobody asked for the iPhone or cloud infrastructure)
2. **Internal requirements**: Infrastructure, logging, diagnostics — nobody asked for these, but they're essential
3. **Dumbing down**: Customers may settle for less than what they asked for (the "Swiss cheese" vs "the moon" analogy)

> [!danger] The MVP Misconception
> *"The MVP for a car is not a skateboard."* Agile's MVP concept is wrong. The customer always wants the real product — a 2025 Mercedes Class 3. If they settle for a 20-year-old rusty Kia, that's the requirement. The MVP is still a car. Customers can't design skateboards into cars.

**Process**: Marketing requirements → derived requirements → expressed as **use cases** (still in the business domain)

---

#### The Architecture ↔ Requirements Feedback Loop

Requirements and architecture exist in a **mutual feedback loop**:

1. Start with requirements (even nebulous ones)
2. Express them as use cases
3. Try to map use cases to interaction diagrams using your architecture
4. Discover issues: *"I need to split this component"*, *"I thought I needed this but I don't"*
5. Requirements shape architecture AND architecture shapes requirements

**Key patterns that emerge:**
| Pattern | How it manifests | Resolution |
|---------|-----------------|------------|
| **Duplicate requirements** | Two use cases produce the same interaction diagram | One disappears — it was a product manager misunderstanding |
| **Mutually exclusive requirements** | Can implement one but not the other | Must be resolved at the **business level**, not the software level |
| **Emergent requirements** | Architecture enables something no use case described | Show it to the product manager — they'll say "yes, the customer mentioned it" |

> [!warning] Business Decisions, Not Software Decisions
> Mutually exclusive requirements can never be resolved in software. If nine customers want "A" and one wants "B" — and B is the future of the business — this is a **business resolution**, not a software one.

---

#### The Curse (C) — Requirements Change

The single biggest objection to the iterative requirements↔architecture process is what Juval calls **the Curse**:

> *"Of course I'd like to operate this way... but these evil customers keep changing requirements, and the time it takes to cycle through the machine far exceeds the time it takes them to change things. So I cannot actually do it."*

**Juval's response: This is not a curse. It's a blessing.**

- If requirements were static, someone would write the application once and nobody would need us
- **We exist precisely because requirements change**
- More requirements change → higher demand for our services → better compensation
- People resent the hand that feeds them

> [!tip] The Real Reason It Feels Like a Curse
> The pain isn't from requirements changing. It's from **designing against requirements** — when requirements change, your design and code must change too, and that's the most expensive thing in software.

---

#### The Core Solution: Never Design Against Requirements

> [!quote] **"Never, ever, ever, ever, ever, ever design against requirements. That's it."**

**The problem:** If you design against requirements (reflect them directly in your architecture/design), then every requirement change forces a design change — and changing design after code is the most expensive activity in software.

**The solution:** Design against the **interaction diagram** (the dynamic aspect), not the requirements (the static input).

- Interaction diagrams capture *how components interact*, not *what the requirements say*
- When requirements change, you only update the mapping from requirements to interaction diagrams
- The architecture itself remains stable
- **Changing design before code is basically free. Changing design after code is catastrophically expensive.**

> [!tip] The Machine Analogy
> Feed garbage requirements into the project machine → garbage comes out. Adding "Agile" (the Holy A) to the machine doesn't change its nature. The solution isn't better requirements — it's a design approach that doesn't depend on them.

---

#### The Iterative Process

The correct process is **iterative** between the two domains:

```
Requirements ←→ Use Cases ←→ Interaction Diagrams ←→ Architecture
     ↑                                                              │
     └────────────────────────── feedback loop ─────────────────────┘
```

1. You have some requirements (even nebulous)
2. Express them as use cases
3. Write interaction diagrams to support those use cases
4. Architecture reveals issues: *"I need to split this component"*
5. Requirements evolve based on architectural discovery
6. Architecture evolves based on requirements evolution
7. Eventually the dust settles — but it never truly stops

---

#### The Integrity Challenge

> [!danger] Human Nature: Always the Worst Possible Way
> *"People are always, always doing things the worst possible way. This is just how life is. It's not an accident."*

Juval's blunt diagnosis:
- Humans naturally choose the worst possible approach (credit cards vs. living below means, ignoring health vs. exercising)
- Software developers always design against requirements because it's all they've ever seen
- **The right move**: "This is always painful. This never works. I'm going to step away from the keyboard until I figure out what I should really do."
- Most don't do it because of the paycheck — but that's not an honest day's work

> [!quote] *"Your customer is not paying you to do it the worst possible way. Your customer is paying you to do the best possible way."*

> [!warning] Sanity vs. Insanity
> *"It is one thing if everyone knows why it works. All you've seen is pain and misery all around you. And you didn't stop to say, well, I guess I'm not going to do it."* People who keep inflicting the same pain on themselves are not sane — they're insane.

---

#### Key Takeaways

| Concept | Summary |
|---------|---------|
| **Two domains** | Business (requirements) and software (static architecture + dynamic interaction diagrams) |
| **Code** | Marrying interaction diagrams to the STD |
| **MVP** | Still a car, not a skateboard |
| **Architecture ↔ Requirements** | Mutual feedback loop; both shape each other |
| **The Curse** | Requirements change is a blessing, not a curse |
| **The solution** | Never design against requirements — design against interaction diagrams |
| **Garbage in, garbage out** | Agile rituals don't fix a broken approach |
| **Human nature** | Default is the worst possible way; integrity means choosing the right way |

---

> [!question]- 1. What are the two domains in every software project, and what lives in each?
> [!summary]- Answer
> **Business domain**: marketing requirements → derived requirements → use cases. **Software domain**: static aspect (architecture, layers, components, STD) and dynamic aspect (interaction diagrams showing component interactions). Code is the act of marrying the interaction diagram to the STD.

> [!question]- 2. What is the MVP misconception, and what is the correct MVP for a car?
> [!summary]- Answer
> Agile's MVP concept wrongly suggests you can grow a simple thing into a full product (skateboard → car). The customer always wants the real product (a 2025 Mercedes Class 3). If they settle for less (a 20-year-old rusty Kia), that's the requirement. The MVP is still a car.

> [!question]- 3. What is the feedback loop between requirements and architecture?
> [!summary]- Answer
> Requirements shape architecture (you discover you need to split components) AND architecture shapes requirements (you discover duplicate or mutually exclusive requirements, or emergent requirements the architecture enables). It's a continuous back-and-forth, not a one-way street.

> [!question]- 4. What is "the Curse" and why is it actually a blessing?
> [!summary]- Answer
> The Curse is the complaint that requirements change too often, making the iterative process impractical. It's a blessing because: if requirements were static, someone would write the application once and developers wouldn't need jobs. Requirements change creates demand for our services.

> [!question]- 5. What is the single most important principle Juval teaches about design and requirements?
> [!summary]- Answer
> **Never, ever design against requirements.** Design against interaction diagrams instead. When requirements change, you only update the mapping — not the design. Designing against requirements means every change forces a design+code change, which is the most expensive thing in software.

> [!question]- 6. What's the cost difference between changing design before vs. after code is written?
> [!summary]- Answer
> Changing design **before** code is basically free. Changing design **after** code is the single most expensive activity in software. This is why the solution is to design against interaction diagrams, not requirements — so requirement changes only affect the mapping, not the design.

> [!question]- 7. What are the three patterns that emerge from the requirements↔architecture feedback loop?
> [!summary]- Answer
> 1) **Duplicate requirements** — two use cases map to the same interaction diagram, so one disappears. 2) **Mutually exclusive requirements** — can implement one but not the other; must be resolved at the business level, not software level. 3) **Emergent requirements** — the architecture enables something no use case described; the product manager confirms it was mentioned by a customer.

> [!question]- 8. What does Juval mean by "garbage in, garbage out" in the context of project requirements?
> [!summary]- Answer
> If you feed garbage (unvalidated, contradictory, unrefined) requirements into the project machine, garbage comes out. You can paint the "Holy A" (Agile) on it — user stories, Kanban, sprints — but the nature of the machine doesn't change. The problem isn't the process; it's the approach of designing against mutable requirements.

> [!question]- 9. What is Juval's diagnosis of why developers keep "designing against requirements" despite it being painful?
> [!summary]- Answer
> Human nature defaults to the worst possible way. Developers keep doing it because: (1) it's all they've ever seen, (2) they need the paycheck, (3) they tell themselves it's honest work. Juval's prescription: stop, acknowledge the pain, and step away until you find the right approach. The right move requires integrity, not permission.

> [!question]- 10. What does "code is the act of marrying the interaction diagram to the STD" mean?
> [!summary]- Answer
> Code is simply: "give me this using this." The STD defines what components exist (static), interaction diagrams define how they communicate (dynamic), and code is the implementation that connects them. The interaction diagram is the contract between architecture and implementation.

---

### Hand Off Point — Senior vs Junior Handoffs, Team Models & the Architect's Role

> [!abstract]
> The **hand off point** is where the architect's design work ends and developers' detail design begins. Whether that point is senior or junior determines team ratio, project duration, cost, and even the architect-to-project ratio. This lecture also covers team models (star, top-down, matrix), why the architect must never adopt coding responsibility, and why architects must be business experts but not domain experts.

---

#### Senior vs Junior: It's Detail Design That Separates Them

Juval rejects the HR definition of seniority (years of experience):

- Experience is **negatively correlated** with success in software — most developers and architects have **negative knowledge**: "They're very good at doing it bad." The receptionist knows more about software design than you do, precisely because she knows nothing
- **Juval's definition**: *"Senior developer can do detail design. Junior developers cannot."*

**Architecture vs detail design** (analogies):
| Analogy | Meaning |
|---------|---------|
| Mouse vs grasshopper | Similar size, **different architecture** — so size isn't architecture |
| Mouse vs elephant | **Same architecture**, completely different detail design — architecture scales |
| Humans vs chimpanzees | Same architecture *and* same detail design (<0.2% genetic difference), different implementation |
| You vs me | Same architecture, detail design, and implementation — different **instances** |

- Architecture is the **grosser model** (two livers, one heart, the spine) — straightforward and easy once you know how; the devil is in the details
- Detail design is where the pain lives; the HR department can't salute Juval's definition because it's not about years

---

#### The 2:1 Ratio — Why Teams Aren't All Senior

| Team makeup | What it can handle |
|-------------|--------------------|
| **2 seniors : 1 junior** ← ideal | A new application *while* tackling a new technology |
| Real life (1:10, one senior ten juniors) | At best the same application on the same technology; anything modestly different → failure |

- An all-senior team fails too: every project has big-picture lofty ideas *and* mundane boring fluff — seniors forced to do the fluff grumble ("Why do I have to do this?")

---

#### The Hand Off Point: Senior vs Junior

The hand off point is the depth at which the architect stops designing:

**Senior handoff** — architect hands off at **top-level design**: decomposition, architecture, drill down to the service, maybe interface level, possibly outline a pattern. That's it.
- Senior developers *resent* being drilled further: "Stop baby feeding me. Tell me what you want."

**Junior handoff** — detail design all the way down to **parameter level**: `heights` and `widths` arguments, etc.
- Juniors will get it wrong: a class with 7,000 methods — "Look, it compiles"; a base class with 17 subclasses — "Look, it works." If there is a way of messing it up, they will find it
- The junior handoff means **galactic-scale extra work for the architect**: 10–40 services × ~1 week of detail design each = 40 weeks added to a single person — or 40 weeks added to the project's front end

> [!danger] The Failure Mode
> *"Not recognizing the hand off point is a classic reason for failure."* — Juval, quoting Monty of iDesign: *"It's always a junior hand off point. I don't care what the customer says. I don't care what the self image is."* Most people think they know how to do detail design; they don't.

---

#### The Senior Handoff as the Safest Way to Compress a Project

- With a senior handoff, **a week or two after the SDP review** you can start handing services off — detail design gets baked into each service's lifecycle instead of the front end
- This modifies the project lifecycle with the proviso: **"yes, with a senior handoff point"** — impossible with junior developers
- No project can be accelerated beyond its **critical path**, but the **fuzzy front end** can be trimmed as much as you like: cutting 20–40 weeks of front-end detail design and baking it into individual service lifecycles shortens the project **without extra risk, headcount, or critical-path changes** — the safest compression technique Juval knows
- **Shorter projects are always cheaper**: you pay the product manager, project manager, architect, HR, IT, and cloud time for the whole duration, so cutting 10 weeks easily outweighs the senior/junior salary gap

> [!tip] The Counterintuitive Conclusion
> **Senior developers cost less than junior developers.** "Not one in a million managers knows this." They don't type faster — juniors type feverishly; seniors think, diagram, look things up, then write some code. They cost more *because they enable the senior handoff*, and the bottom line is still lower. "My grandmother used to say she was too poor to pay cheap." Three bad developers never make up for one good developer — these things are **not additive**.

---

#### Junior Architects — Compensating for a Junior-Heavy Team

If you have a few seniors but mostly juniors, don't use the seniors as senior developers:

- Turn them into **junior architects**: they do the detail design, then farm out **simple programming tasks** to the juniors
- Call them "senior staff software engineer, principal level two" — people always go for the longer title
- **Stagger the batches**: while juniors construct batch N, junior architects detail-design batch N+1

**Simple programming task lifecycle:** detail design by the senior → review with the architect → construction → **code review (with a senior, never a junior)** → integration & testing

> [!danger] Any Design Refinement Requires a Senior
> The word *any* means any. Example: changing a method's parameter order (height/width swap) detonates **every call site** — and refactoring tools can't save you: Resharper only fixes open projects (developers only load their subtree), never reflection/late binding, never generated proxies. "Then you're going to code review with a senior developer, not with a junior developer. If you want to learn something wrong, ask a junior developer for opinion about something."

---

#### The Framework Abstraction Handoff

Even regular teams need a framework for shared concepts — currency types, security, logbook, instrumentation, diagnostics.

**The false dilemma:** abstract (everyone can use it immediately, but they must customize → little value) vs specific (immediate value, but you go against the grain → regret).

> [!tip] The Real Tension: Infrastructure vs Domain
> Practical frameworks are **abstract on the domain, specific on the infrastructure**:
> - Keep the **domain abstract** — currency, not dollars or euros
> - Make the **abstract infrastructure specific** — security, not "you know what I mean"; provide concrete mechanisms (authentication, message security, transport security)

**Ownership handoff:** infrastructure (transaction management, security) goes to **senior developers** — juniors never get it right; the domain (currency, interest rate) can go to **junior developers**.

---

#### The Star Model — Architect at the Center

Because of the skill gap, the architect tends to become the technical lead — "you smack your forehead once a week" — and the team collapses into the **star model**: the architect at the center, "puppies" around (two managers literally framed it in canine terms: "the rest are a bunch of dogs / lost puppies" — top dog, bunch of dogs, lost puppies).

**Why our eyes deceive us:** height follows a Gaussian distribution (tails are nonsense — nobody is two kilometers high), but **wealth and IQ behave like the tail**: Warren Buffett or Elon Musk *is* two kilometers high. The architect is 10×, 100×, 1000× better — conceptually 20 or 60 feet tall.

**Beam-carrying asymmetry:** two equal people carry half each — until one is taller (the shorter carries more), or you go uphill (the lower one carries most), or three people carry (one carries the beam *plus* two people — laziness, free riders). With real skill disparity you don't have a team: "you've got the sun and a bunch of asteroids orbiting it."

**The four problems with the star model:**
1. **Moral**: developers believe they're good, but the code is full of defects; working daily beside someone two kilometers high kills motivation — "What's the point?" Their meager productivity vanishes
2. **Joyride**: the "day in the life of a puppy" — architect works while puppy attends meetings, lunch, home. A joyride is corrosive: the good people quit, the bad stay ("I don't have to do a day of labor again")
3. **Cost**: the team is limited by the architect's throughput — ~2,000 usable hours/year of one person while paying for the whole team
4. **Risk**: the architect leaves → "a bunch of lost puppies." Do you really have a team?

---

#### Wasting the Architect: "Design Is Over, Start Coding"

Organizations are chronically short of good developers, so the temptation to employ the 1000× architect as a developer is enormous. When it happens:

- Everything else the architect owns — detail design, re-planning, reviews — has **no owner** → architect overload
- The architect must become a **domain expert** to code — directly contradicting the architect's proper (removed-from-domain) posture
- When pressure mounts, managers say "design is over, start coding" — and you're wasting the architect. The mechanical engineer sent to the metal shop to "pound on it" resigns on the spot

> [!quote] Architects Are a Seller's Market
> **"Architects don't look for a job. We choose a job."** Demand far exceeds supply — every architect in the class is one phone call and one email away from their next job. Architect turnover exceeds developers' (constantly "on the chair," looking for the next big opportunity); professional architects don't aspire to be developers — employ someone in a capacity they don't aspire to and they will quit when they get the chance.

---

#### Fix 1: The Top-Down Model (Architect as PM)

Make the architect also the project manager: "there's no way that this guy is going to say to this guy, design is over, start coding" — same guy. Usually a **defensive maneuver**: the architect assumes the PM role to defend the architecture and the team from a PM who would butcher it with "feature A, feature B, feature C" edicts.

**Problems:** requires as many projects as architects (rarely true), and leads to architect overload (two positions). **Mitigation:** mechanize project management — the Project Design masterclass shows how to manage a project in ~two minutes a week (Juval was almost always both architect and PM as a "two-minute manager").

---

#### Fix 2: The Matrix Model — The Best Approach

Factor the architects into a **separate part of the org chart**, recognizing architect as a profession distinct from developer (as testers separated from developers 50 years ago):

| Advantage | Why |
|-----------|-----|
| Company best, not project best | Architects report to **engineering managers**, not project managers — cross-project help flows (siloed projects say "hell no" to helping the other side; matrix architects do it because it makes their life easier) |
| Career path without management | The Peter Principle (people rise to their highest level of incompetence) forces 100× developers into paper-pushing management; matrix orgs enable a **chief architect** path — having the option to move is good enough for most people |
| Dedicated dev manager | Project managers spend 70%+ on "he took my crayon" people issues; a dedicated "mommy goose" handles people, so the PM focuses on a single objective: **meeting commitments** |
| Phasing in/out is designed | Developer ramp-up/ramp-down is laid out and planned — "nothing should be left to chance" |
| Enterprise agility | A corporate architecture body can give marching orders to matrix architects instead of having 60 evangelism meetings |

**Economy of scale:** Adam Smith recorded (1776, *The Wealth of Nations*) that maximizing every farm does *not* maximize total yield — Lagrange explained it 100 years later (optimization theory, Lagrange multipliers). The combine harvester example: two neighbors sell one of two $4M combines, split the income, stagger planting by a few days (risk one day of frost/rain each) — massive bottom-line gain *by moving away from the optimum*. A third farmer? Diminishing returns (per-farm savings drop from 50% to 16%) with diabolical complexity (weather, lot size, breakdown probability) — Lagrange's work was the catalyst. Matrix architects push common architecture, standards, and frameworks, which makes phasing devs in/out even easier — powerful positive feedback loops.

> [!tip] The Architect-to-Project Ratio Depends on the Handoff
> Junior handoff → must be **1:1** (a dedicated architect per project). Senior handoff → **up to 1:3** (seen at iDesign; never 1:4), and it requires infrastructure investment (same standards, same frameworks) to work. One-to-three is a *design decision*, not an accident.

---

#### Business Expert ≠ Domain Expert

- **The architect must be a business expert — not optional.** On iDesign engagements Juval spends day one–two meeting business people (head of marketing, VP of business development): "If I don't understand your business, I cannot help you." Most people don't even understand their own business — the outsider's privilege is saying "I'm the idiot, explain it to me" and watching them argue with each other
- **The architect need NOT be a domain expert.** Insurance example: policies, collections, risk, payments = *business*; the exact statistical algorithm that calculates risk = *domain* — you don't need that to design the system ("there's a box: risk"). Knowing too much domain *degrades* the design: you get coupled to the current way of thinking and produce more of the same
- Architect: **design first, domain second** (domain by osmosis over years is fine). Developers: domain **perfectly** — "if you don't understand the domain, you cannot code it"

---

#### Forward-Looking Design: E-Type Systems & the Jevons Paradox

A forward-looking design answers: **"How would the introduction of the system change the requirements against which it is written in the first place?"**

- **E-type systems** (IEEE paper, 1970s): the microprocessor's birth put computers into factories; the widget factory that converts from manual to computerized production finds that the *solution changes the requirements* — build capacity for 2,000 widgets when demand was 500, and demand now exceeds 2,000 (a legacy system at 2,000; overcapacity drops the price point; market share grows)
- **The Jevons paradox** (William Jevons, late 19th century): efficiency improvements in coal production (pumps, power tools, mine railways, safety lamps) made coal *more* expensive — availability increased demand so much that price exploded. Same pattern: adding interchanges makes traffic worse; the "paperless office" raised paper consumption 500%
- You cannot have this perspective if you're too coupled to the current domain — another reason architects stay removed from it

**Developers: application experts, not technology experts.** Proof: the unmanaged→managed migration (C++/VB → Java/.NET, ~2002–2005) — companies almost universally **retrained** developers rather than firing and hiring, because the domain knowledge in developers' minds outvalued technology knowledge. Technologies come and go; the application (and domain) stays. Developers also get the big compensation for domain work — nobody gets a bonus for logbook or security.

---

#### The Architect, Coding Responsibility, and the Technical Lead

Volunteering for coding responsibility is **worse** than being ordered into it. Three classic reasons architects adopt it:
1. A pet idea nobody was for or against — "now you're stuck with it"
2. Legacy attachment — Bill Gates still mucking with the VB compiler years after
3. "I want to keep my hands dirty" — the fear that losing coding responsibility means losing the touch

> [!danger] Keeping Your Hands Dirty Is Backwards
> **"The absolute surest way of losing the touch is adopting coding responsibility."** Coding overtakes other responsibilities because **urgent trumps important** — every piece of code is a deadline tacked on top. Once you code, nobody owns reviews, planning, or re-planning, and the project likely fails.

**Becoming a technical lead:**
- Be technically proficient — Juval's books are *studied*, not read ("I write with a chisel. Every punctuation matters."); learn on the job
- When someone asks for help: **drop everything** (“I'll be right with you” is not acceptable); don't "bloop solve it and run back" — spend two hours making them better; the message is "I care about you" and it creates reciprocity
- Own the endless design reviews: test plan, requirements, code, and design review of every service in the team
- Own planning and re-planning

> [!quote] The Definition
> **"I require the architect to be the best developer in the team, but no coding responsibility."** Juval never worked as a developer a day in his life — but published ~100 articles, 8 books, wrote the C# coding standard and the C# 2.0 white paper, and helped design the language. "You do not need a deadline chasing you to do anything. You need to decide to be good. It's a switch you need to flip in your head."

---

> [!question]- 1. How does Juval define senior vs junior developer, and why does he reject the HR definition?
> [!summary]- Answer
> HR defines it by years of experience — Juval rejects it because experience is negatively correlated with success in software ("negative knowledge": being very good at doing it bad). His definition: a **senior developer can do detail design; a junior developer cannot**.

> [!question]- 2. Fill in the analogy: mouse vs grasshopper = different \_\_\_\_\_; mouse vs elephant = same \_\_\_\_\_, different \_\_\_\_\_\_; humans vs chimpanzees = same \_\_\_\_\_\_, different \_\_\_\_\_\_\_\_\_\_\_\_\_.
> [!summary]- Answer
> Mouse vs grasshopper: different **architecture**. Mouse vs elephant: same **architecture**, different **detail design**. Humans vs chimpanzees: same architecture *and* same **detail design** (under 0.2% genetic difference), different **implementation**.

> [!question]- 3. What is the ideal senior-to-junior ratio, what can such a team handle, and why is an all-senior team also wrong?
> [!summary]- Answer
> **2:1** (two seniors, one junior) — such a team can handle a new application while tackling new technology. An all-senior team is wrong because someone must do the mundane fluff, and seniors forced to do it grumble and quit caring — plus real-world 1:10 teams at best repeat the same app on the same technology.

> [!question]- 4. What is the hand off point, and what does a *junior* handoff do to the architect's workload and the schedule?
> [!summary]- Answer
> It's the depth at which the architect stops designing and developers take over. A junior handoff means the architect must do detail design all the way to parameter level for every service — ~1 week × 10–40 services = galactic-scale extra work for one person (up to 40 weeks) added to the project's front end. With a senior handoff, detail design is baked into each service lifecycle a week or two after the SDP review.

> [!question]- 5. Why can the senior handoff compress a project *safely*, and why does it make senior developers *cheaper* than juniors?
> [!summary]- Answer
> You can't accelerate beyond the critical path, but you can trim the fuzzy front end: baking detail design into individual service lifecycles cuts weeks with no extra headcount, no critical-path change, and no added risk — the safest compression. And shorter projects are always cheaper (PM, product manager, architect, HR, IT, cloud paid for the whole duration) — the savings from cutting ~10 weeks dwarf the salary gap. Seniors don't type faster; they enable the senior handoff and still cost less overall. "Three bad developers don't make up for one good developer."

> [!question]- 6. Scenario: a junior changed a method's parameter order (height/width). Why must a senior handle the fallout, and why can't refactoring tools save the team? Name two cases tools miss.
> [!summary]- Answer
> "Any" design refinement means any: the change detonates every call site. Tools fail because Resharper only fixes projects you have opened (devs only load their own subtree) and never fixes **reflection/late binding** or **regenerated proxies** from code-gen/web services. Code review must therefore be with a senior, never a junior.

> [!question]- 7. How should a practical framework treat the domain vs the infrastructure, and who owns each part?
> [!summary]- Answer
> The real tension isn't abstract vs specific — it's domain vs infrastructure. Keep the **domain abstract** (currency, not dollars) and make the **infrastructure specific** (security → concrete mechanisms: authentication, message security, transport security). Infrastructure parts (transactions, security) go to **senior developers**; domain parts (currency, interest rates) can go to **junior developers**.

> [!question]- 8. List the four problems with the star model (architect at the center).
> [!summary]- Answer
> 1) **Moral**: developers lose motivation next to a "two-kilometers-high" architect; 2) **Joyride**: the day-in-the-life-of-a-puppy corrosive ride — good people quit, bad people stay; 3) **Cost**: the team's throughput is capped by one person's ~2,000 hours/year while the whole team is paid; 4) **Risk**: the architect leaves and you have "a bunch of lost puppies" — you never really had a team.

> [!question]- 9. Compare the top-down model with the matrix model. What problem does each solve, and what problem does each create?
> [!summary]- Answer
> Top-down (architect = PM): solves "design is over, start coding" because the same guy owns both — usually a defensive maneuver; creates architect overload and requires as many architects as projects (mitigated by mechanizing PM to ~2 minutes/week). Matrix (architects in a separate org unit, reporting to engineering managers): solves the star model and gives architects a career path without management (beating the Peter Principle); enables cross-project help, dedicated dev managers ("mommy goose" for crayon issues), designed phasing, and economy of scale.

> [!question]- 10. What's the difference between business expertise and domain knowledge, and which do architects vs developers need — plus, why does this connect to forward-looking design?
> [!summary]- Answer
> Business = the industry and its operations (insurance policies, payments); the architect **must** be a business expert. Domain = deep specialty (the exact risk-calculation algorithm); the architect should *not* over-invest there — it degrades design (coupling to current thinking). Developers must master the domain to code it. Forward-looking design asks "how does introducing the system change the requirements it was written against?" (E-type systems, Jevons paradox) — impossible if you're too coupled to the current domain.

---

### Reflections & Discussion
