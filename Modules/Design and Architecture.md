---
title: "Design and Architecture"
date: 2026-07-21
module: module-5
type: module
tags:
  - course/notes
  - module-5
  - juval-lowy
---

# Design and Architecture

> [!summary] Module 5 — The IDesign Method
> The core architectural design methodology: volatility-based decomposition, universal design principles, the architect's challenge, axes of volatility, and practical design validation.

## Topics

- [ ] The IDesign Method
- [ ] Classic mistakes
- [ ] Volatility-based decomposition
- [ ] Universal design principles
- [ ] The architect's challenge
- [ ] Axes of volatility
- [ ] Design example
- [ ] Volatility and the business
- [ ] Open and closed architecture
- [ ] Structure with clients, managers, engines, resource access and utilities
- [ ] Design validation
- [ ] Containing changes
- [ ] Design Don'ts

## Notes

### The IDesign Method

-

### Classic Mistakes

-

### Volatility-Based Decomposition

-

### Universal Design Principles

-

### The Architect's Challenge

-

### Axes of Volatility

-

### Design Example

-

### Volatility and the Business

-

### Open and Closed Architecture

-

### Structure (Clients, Managers, Engines, Resource Access, Utilities)

> [!note] Parked reference — waiting for the SSM lecture
> In [[99-Resources/Transcripts/Service Contract Design|Service Contract Design]] Juval designs a contract for **resource access** (a barcode scanner acting as a resource to a POS system), then explicitly defers the meaning of the term: *"These two words resource access doesn't mean much, but tomorrow when we'll discuss the **SSM method**, it will mean a lot. So I'm parking these two bullets for future reference."*
>
> Nothing here yet — this is the landing spot for that payoff. See [[Modules/Service Contract Design and Factoring#Sample Project]] for the v1→v4 contract evolution he uses to motivate it.

### Design Validation

> [!note] Pointer — one idea, until the architecture lecture lands
> [[99-Resources/Transcripts/Contract Factoring in Practice|Contract Factoring in Practice]] contributes a reframe worth keeping: **"Design validation is a world-class contract factoring technique."**
>
> Validation is not a final act where you confirm the design holds water. Trying to validate *produces* factoring — the use case turns out incomplete, wrong, or a duplicate, so you change the use case, which uncovers something else, so you come back and validate again. Iterate simultaneously in **diagrams** and **code sketches** (a C# or Java interface).
>
> Mechanics live in [[Modules/Microservices Development Process#Requirements Design Validation]]. This note is empty pending the architecture/SSM session, still parked for "tomorrow".

### Containing Changes

-

### Design Don'ts

-

## Related

- [[MOC — Course Overview]]
- [[Modules/Design Aspects]]
- [[Modules/Design Aspects/Fractal Architecture]]
- [[Modules/Agile and Design]]