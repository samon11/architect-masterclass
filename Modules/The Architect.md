---
title: "The Architect"
date: 2026-07-21
module: module-1
type: module
tags:
  - course/notes
  - module-1
  - juval-lowy
---

# The Architect

> [!summary] Module 1 — The Foundation
> Understanding software development as engineering, types of architects, the role of the architect, and the relationship between architects, technology, and business.

## Topics

- [x] Software development as engineering
- [x] Types of architects
- [x] The role of the architect
- [x] Architects and technology
- [x] Architects and the business

## Notes

### Software Development as Engineering

**The Crisis:**
- Software development is in a chronic crisis: projects run over budget, past schedule, with poor quality and unmet requirements
- This crisis has existed since 1972 — if there were a quick fix, it would have been applied by now
- It's an **uphill struggle**, not a quick fix. Quacks promise victory; the reality is a fighting chance that requires courage, integrity, and responsibility

**The Act of Maturity:**
- Every engineering discipline started chaotic, like a "mob trying to write software" — no standards, no repeatability, no structured knowledge
- **Civil engineering:** Cathedrals collapsed the first time. Only after universities formalized knowledge (12th century) did buildings stop falling down
- **Mechanical engineering:** Early trains had unique parts, different rail gauges, no interchangeability. Standardization enabled the Industrial Revolution
- **Software:** Hasn't had its act of maturity yet. We're still in the chaotic phase — "let it evolve organically" ("the only thing that evolves organically is the tumor")

**Key Insight:**
- Software just hasn't gone through the bloody reckoning that forced other disciplines to formalize their approaches
- The industry needs structured knowledge, not one-hero-dependency models

---

### Types of Architects

- Software solution architects are **not** domain experts — developers are
- The architect's value isn't in knowing more about the business domain, but in **how** they approach the system
- Different from engineers who focus on domain-specific problems; architects focus on **structural problems** that cut across domains

---

### The Role of the Architect

**Core Responsibility:**
- **Decouple the system** from the domain — make the architecture reusable across different business contexts
- Solve the interoperability problem before it becomes a mess (like standardizing rail gauges)
- Manage complexity so it doesn't become an excuse for poor quality

**Design Philosophy:**
- Write the **dumbest, simplest code** you can — future developers will butcher elegant code if they don't understand it
- Never write the smartest, most clever code; write code that a college grad with minimal experience could maintain
- Ask: "Could someone without programming experience understand this line?"

**Mindset:**
- Take personal accountability — "It's always your fault" when projects fail
- Don't repeat the same mistakes; if something isn't working, do something else
- Be in the **transformation business** — make a difference, don't just do "more of the same"

---

### Architects and Technology

**Complexity ≠ Poor Quality:**
- The **jumbo jet analogy** proves you can have insane complexity AND flawless quality
  - Millions of parts, thousands of components, millions of people, expected to fly for 100 years
  - Far more reliable than a toaster (toasters are murderer entities!)
- Complexity is just an **excuse** your mind wraps around to avoid admitting incompetence

**Gold Plating vs Core Functionality:**
- Gold plating = adding features/effort nobody asked for, driven by vanity
- Like a **short blanket** — pull to your chest, toes are cold; pull to toes, chest is exposed
- Every ounce of energy on gold plating is energy NOT spent on core functionality
- Example: Visual Studio's WPF editor forced into VMs without GPUs — nobody asked for it, made development painful

**The Toolbox:**
- Your techniques can build a mud hut or a paper airplane — you need techniques that can build a cathedral
- Simple techniques, not complex ones — but you still have to use them

---

### Architects and the Business

**Commodity vs Precious Resource:**
- HR treats developers as **commodities** — "one code monkey is the same as the next"
- Salary surveys = **commodity spot prices** (like copper, interchangeable from any mine)
- You don't want to be priced by a salary table; you want to be a **diamond** — unique, valuable, hard to replace

**The 1000:1 Spectrum:**
- World's best developer is 10x better than your best; your best is 10x better than your worst
- That's **three orders of magnitude** — one great developer beats a thousand monkeys
- But the best developers often leave, taking knowledge with them. The ones left behind butcher what remains
- Management overhead of a thousand monkeys is enormous

**Value Creation:**
- Organizations won't pay premium rates if they don't see premium value
- "When you pay peanuts, you get monkeys" — but also, "when we value you, we pay"
- To justify premium compensation, you must deliver premium results: on time, on budget, with zero defects
- Juval's track record: Every project he was personally involved in was on schedule, on budget, with zero defects — even world-changing, first-of-a-kind systems

---

### Types of Architects

-

### The Role of the Architect

-

### Architects and Technology

-

### Architects and the Business

-

## Reflections & Discussion

### Software in the Age of AI

**Key question:** How do these principles apply when AI makes software cheap and fast to produce?

**Tensions:**
- **Risk:** AI could accelerate gold plating and commoditization — more "code monkeys" with AI assistance, churning out unmaintainable code
- **Opportunity:** AI could democratize architectural thinking — making the "architect's mindset" available to more people, not just the elite few
- **The real value:** AI makes *writing code* a commodity, but *designing systems*, *decoupling domains*, and *solving business problems* remain human skills

**Connection to Lecture 1:**
- "Write the dumbest code" — AI-generated code is often the smartest, most complex code. Future maintainers will butcher it even more
- "Don't be a commodity" — If AI commoditizes code production, the scarce resource becomes **architectural judgment**
- "Complexity is an excuse" — AI doesn't remove complexity; it might enable more of it. The architect's job is to manage it

> [!tip] Open question
> AI might force the industry's "act of maturity" to happen faster — or it might deepen the crisis by enabling more chaos at scale.

---

## Review Questions — Lectures 1 & 2

1. Why does Juval say "it's always your fault" when projects fail?
2. What's the difference between gold plating and core functionality? Why is gold plating harmful?
3. What does Juval mean by "write the dumbest code you can"? Why is this important?
4. What does it mean to "not be a commodity"? How does HR/salary surveys treat developers as commodities?
5. How does the jumbo jet analogy disprove the "complexity = poor quality" excuse?
6. What historical evidence does Juval use to prove software development can succeed on time and on budget?
7. Why did the Roman Empire never build skyscrapers despite having better cement than modern times?
8. What does "decoupling the system" mean in the context of a software architect's role?
9. Why does Juval compare early train systems to modern software development?
10. What does Juval mean by "act of maturity" for an engineering discipline?

## Related

- [[MOC — Course Overview]]
- [[Modules/Microservices Development Process]]