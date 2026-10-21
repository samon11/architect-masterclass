---
title: "Design Aspects"
date: 2026-07-21
module: module-6
type: module
tags:
  - course/notes
  - module-6
  - juval-lowy
---

# Design Aspects

> [!summary] Module 6 — Deep Architecture
> Exploring complicated vs. complex systems, self-similarity, fractal architecture, and advanced design patterns.

## Topics

- [ ] Design aspects (overview)
- [ ] Complicated vs. complex
- [ ] Complex software systems
- [ ] Structure and interactions
- [x] Self-similarity and fractal
- [ ] Fractal examples
- [ ] Fractal design patterns
- [ ] AI modeling
- [ ] Fractal design guidelines
- [ ] Simulations
- [ ] Fractal detailed design

## Sub-Module

- [[Modules/Design Aspects/Fractal Architecture]] — Deep dive into fractal architecture specifically

## Notes

### Design Aspects (Overview)

-

### Complicated vs. Complex

-

### Complex Software Systems

-

### Structure and Interactions

-

### Self-Similarity and Fractal

> [!note] First real content — sourced from a Module 5 lecture
> This note is otherwise still empty. The material here arrives from [[99-Resources/Transcripts/Sample Project — Resilient Energy|Sample Project — Resilient Energy]] (MOC Module 5, recorded while discussing contract metrics), not from a Design Aspects session. Treat it as a real-system observation that happens to belong to this topic, not as the full Design Aspects treatment — the dedicated fractal lecture is still parked for *"Friday morning."*

**The claim, stated absolutely.** Resilient Energy aggregates systems tree-like — a system of systems, every node another tree of systems. *"There is no 'here is the box where the system is.'"*

> [!important] "Each node in the tree has four subsystems. Each node across the tree from the continent level to the appliance has **absolute self-similarity** — it is exactly, exactly, exactly, exactly, exactly the same code."

The line worth stealing:

> [!quote] "The system doesn't know it is the root of the world or it's actually a light bulb. It doesn't know."

**Self-similarity is mandatory, not aesthetic.** This is the strongest argument for it in the vault, because it is a failure argument rather than a purity argument:

> [!danger] "This is actually the only way to build this kind of a system, because **if you start doing it with if and else, you will fail.** There is no way of building this kind of a system using if and else."

With scale spanning *"not just a building, but imagine an appliance"* up to *"continent-wide"*, and *"every deployment going to be completely and utterly different"*, branching by context does not scale. The alternative is one code base that does not know where it sits in the tree.

**Structural detail:** each node uses the classic IDesign method internally — a manager plus services/engines — *"the classic thing we're going to discuss tomorrow."* → [[Modules/Design and Architecture#Structure (Clients, Managers, Engines, Resource Access, Utilities)]]

> [!warning] Two different "fractals" — do not conflate them
> 1. **Self-similarity** (this section) — the same code repeated across nodes of a tree of systems. He now uses *"the fractal"* as vocabulary for it: measuring contracts per service at 2.65, he explains the excess as *"a bunch of other interfaces here required just to manage the fractal and such."*
> 2. **The size totem pole** — program → system → platform → fractal, used to explain why metric thresholds are scale-relative. Documented in [[Modules/Service Contract Design and Factoring#Metric 3 — Contracts per Service ≈ 2.2]].
>
> Related ideas, **different claims**. The totem-pole usage is still parked for Friday morning.

### Fractal Examples

-

### Fractal Design Patterns

-

### AI Modeling

-

### Fractal Design Guidelines

-

### Simulations

-

### Fractal Detailed Design

-

## Related

- [[MOC — Course Overview]]
- [[Modules/Design and Architecture]]
- [[Modules/Agile and Design]]