---
title: "Microservices Development Process"
date: 2026-07-21
module: module-2
type: module
tags:
  - course/notes
  - module-2
  - juval-lowy
---

# Microservices Development Process

> [!summary] Module 2 — Process & Delivery
> How architects lead teams through design, documentation, quality control, and the full project lifecycle in a microservices context.

## Topics

- [ ] Process leadership intro
- [ ] Design granularity effect on the project
- [ ] The design and the team
- [ ] System lifecycle
- [ ] Service lifecycle
- [ ] Project design
- [ ] AI and documentation
- [ ] Composable design
- [ ] Design hand-off point
- [ ] Architect and the team
- [ ] Developers onboarding
- [ ] Career of the architect
- [ ] AI and future of development
- [ ] AI and agility
- [ ] AI spec-driven development
- [ ] Quality assurance
- [ ] Quality control
- [ ] Design for performance
- [ ] Services simulation and emulation
- [ ] Peer reviews
- [ ] Development and design standards
- [ ] Metrics collection
- [ ] Management visibility
- [ ] Requirements Design Validation

## Notes

### Process Leadership Intro

- [Transcript](../99-Resources/Transcripts/Process Leadership Intro.md)
- [CMM Diagram](Microservices Development Process/CMM Diagram.md)
- Good process is invisible — it maximizes productivity, doesn't get in the way
- Process works for teams of ~7 or fewer; larger projects need hierarchical decomposition
- 85% of companies are at CMM Level 1 (Chaos); no project should fall below Level 2
- **Juval's definition of success**: *Meet your commitments*
- Modular services give us reusability + maintainability, but add inherent complexity
- **The only fighting chance**: ensure your modules are impeccable

#### CMM — Capability Maturity Model

The IDesign approach is compatible with CMM levels 2–3, with some elements from level 4.

| Level | Name | Key Elements |
|-------|------|-------------|
| 1 | Initial / Chaos | A mob writing software — no process |
| 2 | Repeatable ✓ | Requirements Management, Project Planning, Project Tracking (PDMC), Quality Assurance, Configuration Management, Subcontract Management |
| 3 | Defined ✓ | Organizational Process, Integrated Management, Software Engineering, Inter-group Coordination, Training Program, Peer Reviews |
| 4 | Managed ✓ | Metrics Management, Quality Management |
| 5 | Optimizing | Defect Prevention, Technology Change Management, Process Change Management |

- **85% of companies** are at **Level 1 (Chaos)**
- **No project should fall below Level 2** — the jump from 1→2 is hundreds of percent penalty; from 2→3 is only 20–30%
- Sweet spot for most projects: between Level 2 and Level 3 (buffet menu, not discrete)
- See [[Modules/Microservices Development Process/CMM Diagram]] for the visual reference

### Design Granularity Effect on the Project

-

### The Design and the Team

-

### System Lifecycle

-

### Service Lifecycle

-

### Project Design

-

### AI and Documentation

-

### Composable Design

-

### Design Hand-off Point

-

### Architect and the Team

-

### Developers Onboarding

-

### Career of the Architect

-

### AI and Future of Development

-

### AI and Agility

-

### AI Spec-Driven Development

-

### Quality Assurance

-

### Quality Control

-

### Design for Performance

-

### Services Simulation and Emulation

-

### Peer Reviews

-

### Development and Design Standards

-

### Metrics Collection

-

### Management Visibility

-

### Requirements Design Validation

- [Transcript](../99-Resources/Transcripts/Requirements Design Validation.md)

- **Capture required behavior, not required functionality.** Functional requirements ("system should do X") force developers to interpret *how* to implement it, and Murphy says they will always misinterpret. Always specify *how the system should perform a particular behavior.*

- **Use use cases, not user stories.** User stories look at things from the user's perspective, but "what the users see is the tip of the iceberg." Use cases capture the full system behavior — most of which is below the waterline.

- **Requirements must be captured graphically.** Reading is evolutionarily artificial (only ~5,000 years old). Half the brain is visual processing evolved over 5 million years. Use diagrams to leverage the brain's native strengths.

- **Never use flowcharts.** They have no notion of time — cannot express concurrent execution, blocking, or waiting. Use **UML activity diagrams** instead (the one genuinely useful part of UML).

- **A use case must fit on a single page.** If it doesn't, you don't understand it and nobody can code it. Large "use cases" are usually many use cases superimposed.

- **If a use case contains a nested if, it must be graphical.** No human can parse text with nested conditionals without misinterpreting. Graphically, even 17 nested ifs are trivial to follow.

- **Design validation before coding.** "Evolutionary design" (build → deploy → see if it works) is "incredibly wasteful" — like building a house, getting feedback, demolishing it, and rebuilding. No engineer would build a plane by putting passengers in and seeing if it flies.

- **How to validate: interaction diagrams per use case.** For each use case/activity diagram, draw an interaction diagram showing how your components/services collaborate to support that behavior. If you can do this for every use case, you have a **valid design**. Valid ≠ great, but it's the minimum bar.

## Quiz

> [!question]- 1. What is Juval's definition of success?
>!
> [!summary]- Answer
> *Meet your commitments.* If you committed to a year, you deliver in a year — not two, not three.

> [!question]- 2. Why does the process described in this lecture only work for teams of ~7 or fewer?
>!
> [!summary]- Answer
> Because communication overhead grows disproportional to team size. 1+1+1 ≠ 3 in software — marginal returns diminish after the 6th or 7th developer.

> [!question]- 3. What percentage of companies are at CMM Level 1 (Chaos)?
>!
> [!summary]- Answer
> 85%.

> [!question]- 4. What are the key components of CMM Level 2?
>!
> [!summary]- Answer
> Requirements management, project planning, project tracking (PDMC), quality assurance, and configuration management.

> [!question]- 5. What does "cargo cult culture" mean in software development?
>!
> [!summary]- Answer
> Blindly adopting practices (like Scrum, stand-ups, sprint boards) without understanding *why* they exist — performing rituals that suck productivity instead of enabling it.

> [!question]- 6. Why does Juval say good process should be invisible?
>!
> [!summary]- Answer
> Because good process maximizes productivity rather than getting in the way. You shouldn't be aware of it — just like you don't think about your daily morning routine.

> [!question]- 7. What is the "only fighting chance" against complexity in modular systems?
>!
> [!summary]- Answer
> Ensuring that every module is impeccable in quality. Without impeccable components, complexity devours the system.

> [!question]- 8. What does Juval compare modularity's tradeoff to?
>!
> [!summary]- Answer
> Getting "our cake and to eat it too" — modular services give us reusability and maintainability, but we must contend with inherent complexity that grows over time.

> [!question]- 9. Why should requirements capture *behavior* rather than *functionality*?
>!
> [!summary]- Answer
> Because functional requirements ("system should do X") force developers to interpret *how* to implement it. Murphy says they will always misinterpret. Behavior specifications remove ambiguity and prevent wasted iterations.

> [!question]- 10. Why does Juval say we should never use flowcharts for requirements?
>!
> [!summary]- Answer
> Flowcharts have no notion of time. They cannot express concurrent execution, blocking waits, or looping — all of which are paramount in describing required behavior.

> [!question]- 11. What does it mean to have a "valid design" according to Juval?
>!
> [!summary]- Answer
> You can draw an interaction diagram for each use case, proving your architecture supports all required behaviors.

> [!question]- 12. What is the relationship between use case complexity and graphical capture?
>!
> [!summary]- Answer
> If a use case contains a nested if, it must be graphical. No human can parse text with nested conditionals without misinterpreting. Graphically, even 17 nested ifs are trivial to follow.

## Related

- [[MOC — Course Overview]]
- [[Modules/The Architect]]
- [[Modules/Introduction to Service-Orientation]]
- [[Modules/Design and Architecture]]