---
title: "Service Contract Design and Factoring"
date: 2026-07-21
module: module-4
type: module
tags:
  - course/notes
  - module-4
  - juval-lowy
---

# Service Contract Design and Factoring

> [!summary] Module 5 — Contract-Driven Design
> How to design service contracts, apply factoring techniques, measure contract quality, and walk through a sample project.

> [!warning] Numbering
> This is **MOC Module 5**, but this note's frontmatter and tags say `module-4`. The vault's numbering is off by one from Module 4 onward (Project Planning was inserted as Module 3 after the other notes were written) — full table in [[Modules/Introduction to Service-Orientation#Numbering Discrepancy]]. Transcripts for this module use `module-4` to stay tag-consistent with this note.

## Topics

- [x] Service contract design
- [x] Contract factoring techniques
- [x] Contract metrics
- [x] Contract factoring process
- [x] Sample project
- [x] Detail design — cost, conviction, and how to learn it

## Notes

### Service Contract Design

- [Transcript](../99-Resources/Transcripts/Service%20Contract%20Design.md)

> [!note] This is Wednesday
> The lecture opens by retracting Monday's answer. On Monday the area-of-minimal-cost question was answered with *"you get a qualified competent architect, and that's the architect's problem"* — see [[Modules/Project Planning#Service Sizing — The Area of Minimal Cost]]. Today: *"Unfortunately, it's Wednesday now, and we are wearing the architect's hat now, and we cannot keep dereferencing it to somebody else."*

#### The Method: Transformational Reduction

> [!important] "Whenever you encounter a question you cannot answer or answer easily, try and do some **transformations or reductions** on the question until you find a question that you can answer."

The whole lecture is *"a series of transformational reductions."* The first one converts **what is a good service?** → **what is a good contract?**

Assumption (immediately disowned): *"I know that's not the case. I know a service can support multiple contracts. I know you can have the same contract across multiple interfaces or multiple services. I know. But suppose it's one to one."*

Why it's safe: *"We're not really talking about units on these charts. It are just qualitative numbers. And if I have not one-to-one mapping, what it will do, it would move the chart up and down and right and left, and not gonna change the behavior. And what I'm really looking after here is the behavior. So it's a good enough reduction. It passes a smell test."*

This is also why the chart is **not** Monday's chart: *"what we have here is number of contracts, not number of services."* Same cost curve, different x-axis.

#### Contracts Are Formal Interfaces

The implementation construct is the interface. Then the inversion:

> [!important] "Are interfaces contracts? **Not necessarily.** Are contracts interfaces? **Yes.**"
> **"All contracts are interfaces, but not all interfaces are contracts."**

| Interaction | Formal? |
| --- | --- |
| Taxi / Uber | No — wave your hand, no paperwork. You pay at the end; they get you there safely and in time. |
| Post office | No — *"They're gonna give the best effort of trying to deliver it. They're not saying they're actually going to deliver it, they're gonna try."* |
| Employment | **Yes** — written contract. |
| Apartment rental | **Yes** — written contract. |

A service is formal *"because the clients are gonna program against it and rely on it and be dependent on it."*

#### Facet Theory

One person signs many contracts — employment, rent, marriage, loan. *"Each one of these contracts represents a **facet** of you to the outside world, you as a renter, you as an employee, you as an employer, you as a spouse."*

Refinement: *"It's actually insufficient to say that contracts are facets of the entity. Contracts are **independent** facets of the entity."*

#### The Three Attributes

**1. Logically consistent.** Would you sign an employment contract that also requires a home address? *"Where I live is irrelevant. So if I move, I have to quit."* Including it *"would make the contract logically inconsistent."*

Nuance: there is nothing inherently wrong with an address — in a **rent** contract it is essential. But a rent contract conditioned on *"you can only rent here if you work for Microsoft"* is inconsistent: *"You don't care how I'm making a living. As long as I'm making rent, it doesn't matter. **Even criminals can rent. Even politicians can rent.**"*

**2. Cohesive.** A contract that omits pay: everyone gets a paycheck, you get nothing, and the boss says *"I'm looking at this contract. It doesn't say how much you get. I thought you came here because you like it."*

> [!quote] "Cohesive means they contain all the things that actually are required to describe the interaction."
> Recurring formula: *"The contract has evolved to include all the things pertaining to the interaction, **no more, but no less**."*

**3. Independent.** A marriage contract with a "works at Microsoft" precondition: *"What happened to you for richer and poorer?"* *"Your marriage contract should be completely independent from your employment contract. And the employment contract should be completely independent from your mortgage contract."*

**Consolidated:** *"Good contracts are **logically consistent, cohesive, independent facets** of the entity."*

**The dictionary shortcut:** *"It turned out there's a word in English that combines consistent and cohesive… the word is **coherent**. When something is coherent, it is both consistent and cohesive."* → target: **coherent and independent contracts**.

#### Reuse — the Master Attribute

> [!important] "There's another attribute that groups everything together, and that is **reuse**… So the ultimate way of evaluating a contract is its degree of reuse or its potential for reuse. That is the **ultimate litmus test**."

**The HR test.** *"It's time to have the meeting with Cruella, the HR manager. And she gives you this crooked look that the spider gives a fly caught in the web, and she says to you, **we have crafted a contract just for you**."* → *"This is either very good news or very bad news. And **Murphy said it's always very bad news**."* You want **the same** contract everybody else got, not a better one: *"A contract was good for every other employee. Why would it not be good for me? …it doesn't include things like the name of my cat."*

**The apartment test.** Option A: real-estate lawyer at **$500/hour**. Option B: Google "apartment contract," download the first hit, *"don't even read the fine print on the boilerplate,"* put the address in. *"A contract that was good for a million other apartments… has honestly evolved to include all the important logically consistent things like the address and the rent. Does not include irrelevant things."*

**Three-way comparison:**

| Shape | Verdict |
| --- | --- |
| Thousands of methods, hundreds of arguments each | *"The chance that anybody else in the planet will ever need this contract again? A hard, cold **zero**. This monstrosity is so highly specialized, nobody will be able to reuse it."* |
| A tiny contract positioned as "red, underneath yellow, next to green, **not** the one next to blue" | Also zero: *"It is so incredibly specialized for its context and interaction with its neighbors… Nobody will have this particular constellation ever again."* |
| A third group | *"Are there any good? We actually do not know… But at least now there's hope. **Hope is better than no hope.**"* |

**Overlapping** the same contracts — same size, same count — is still bad: *"Now they're no longer independent facets… they're clearly tightly coupled to each other so it fails because of the independence aspect."*

**Potential ≠ degree.** *"I can design an amazing contract that nobody else in the universe is using besides me. So what? It doesn't mean it's a bad contract. It's **reusable**. It's not **reused**."* When he founded **IDesign** he asked his lawyer to craft terms *"not for me… good enough for any small boutique shop like IDesign… It doesn't matter that we are the only ones using it. That's irrelevant."*

> [!quote] The factoring mindset
> *"How about you do it once and be done with it? Think always in terms of reusable elements. The question is not good contract, bad. The question is **is it reusable**? Will anything here prevent it from being reused? To what degree can I already reuse it somewhere else?"*

Closing shape: *"Not too big, not too small, not too many, not too few, not too coupled, not too independent. Just here."*

### Contract Factoring Techniques

- [Transcript](../99-Resources/Transcripts/Service%20Contract%20Design.md)

> [!quote] "These are literally the **only three techniques** there are. There are factor down, sideways, or up."

| Technique | Telltale sign | What to do |
| --- | --- | --- |
| **Down** | An **offending operation** — works great in some contexts, feels miserable in others (`AdjustBeam` on a numeric keypad) | Break the contract into a hierarchy, push the offender down, keep the common operations upstairs |
| **Sideways** | A **weak logical relationship between operations** (`ReadCode` vs `OpenPort`/`ClosePort`) | Split into separate **independent facets** |
| **Up** | Operations **logically related but repeated** across multiple facets | Hoist into a shared base — *"not including them would make the contract less cohesive. Duplicating them would be just bad contracts."* |

The argument for completeness is that these exhaust the directions a relationship can point: **down** the hierarchy, **across** to a sibling facet, or **up** to a shared one.

Worked in full in [[#Sample Project]] below — the POS example is the only concrete design walkthrough in the lecture, and it is where all three techniques are introduced.

Two things worth pulling out:

- **A rare explicit stance on inheritance.** *"Now, all my problems with inheritance were inheritance of **implementation**. **Inheritance of interface is just fine.** Remember, all the problems with inheritance was the need to know the implementation detail of what happens upstairs, but there are no implementation details in an interface, which is perfectly fine."* This is the reconciliation with [[Modules/Introduction to Service-Orientation#Inheritance — "Absolutely Evil"]] — same author, same week, and the distinction that resolves it.
- **Splitting costs nothing.** *"A service can implement multiple contracts. So look now at the barcode scanner: it implements IScannerAccess **plus** ICommunicationDevice. Look at it from the perspective of the developer charged with implementing the barcode scanner: **the sum of work inside BarcodeScanner has not changed. We're not doing any more work.** However, the conveyor belt can also implement ICommunicationDevice. So now we can reuse it."*

#### The Design Law Behind It

> [!danger] "At this point you should strongly suspect there's a never-ending long list of peripheral devices like printers and everything else that the customer would want to throw at you. And every one of these things would start duplicating little parts of every other contract. And every time you introduce such a peripheral device, it will force a change to your system. And **that is a hallmark of a bad design**. A good design should be **resilient to changes in the user domain**. Here, every time there's a change in the user domain, all of a sudden there's a reflecting change in the system domain, and that's a hallmark of a bad design."

### Contract Metrics

- [Transcript](../99-Resources/Transcripts/Service%20Contract%20Design.md)

#### Why Metrics Exist — the 14-Year Dead End

*"The three techniques I showed you — down, sideways, or up — always result with contracts with **fewer** members. If you keep doing it, keep doing it, you'll end up with an **explosion of little things** which we know is not a good design. So it would be nice if you have a technique that results with **larger** contracts."*

*"The reason I didn't show it to you is because by now I'm convinced that the technique does not exist. I've spent **14 years** thinking about the question: what is a good contract. I'm not kidding."* Every technique he could devise produced smaller contracts, never larger. *"The pitfall there is that if you keep doing it, you keep fracturing and fracturing and fracturing, and that's no good. The way to counter it is using **metrics**."*

#### The Sorting Method

> [!quote] "You can actually measure and sort contracts from the worst to the best. In fact, I can go now to any one of your systems, **knowing nothing about your domain, your developers, your technology, anything**, I could say which one is the best and which one is the worst."

Five candidate measurements: (1) cyclomatic complexity of the service behind the contract; (2) number of defects logged against each service; (3) time it took to implement each contract; (4) number of times each contract was checked out and changed; (5) degree of reuse — how many services use it. *"Assign weight for each one of these categories, measure all of them, and sort your contracts."*

Honesty about the limit: *"Obviously your best may not be any good, but I said I'm gonna sort it from the worst to the best. I'm not gonna tell you which one is good."*

> [!important] Best and worst, verbatim
> **Best:** *"A contract that **nobody has ever changed**, and yet the system is using it **in every object of the system all the time**."*
> **Worst:** *"A contract that is used in **exactly one place** and everybody every day keeps **changing**."* — *"Everything else in between."*

*(The measurement vocabulary — cyclomatic complexity, defect counts — overlaps [[Modules/Microservices Development Process#Metrics — the full lecture]], but that note measures **code/services/projects**; this measures **contracts**. Cross-link, don't merge.)*

#### Metric 1 — Number of Operations

A single-operation contract compiles and won't get you arrested, *"but it's something to avoid."* Reason: *"If a contract represents a facet of the entity, it must be a **pretty dull facet** if you only have one thing to say about it. Almost always it's… an **amalgam of three different things concatenated back to back**, you're calling it one thing, not three separate things."*

| Diagnosis | Fix |
| --- | --- |
| **Speculative design** — *"in the next version we're doing ABC, so I'm doing A over here"* | *"No no no, we'll do the A with the B and the C. **Take it out.**"* |
| **Near-duplicate** — *"it's sort of like that thing over there, but not quite"* | *"You got anything else to say about it? No? Then put it over there with its other kinsmen. I know it's like the **redheaded stepchild**, but it's gonna be fine."* |
| **Sub-interface with one operation** | *"Hardly ever anybody's using the base interface. They only use the sub-interface. We can just **bump it upstairs** and fix it."* |

Posture: *"I cannot tell you what to do. I can tell you that **a single operation is a red flag**. You have to go and investigate. How you resolve it? It's up to you. It's your system."*

Cost of small contracts: *"Every one of these things is another endpoint, another container, another cluster… it's another entry point, it's another potential **security vulnerability**. Don't do it."*

**The tolerance ladder** — *"a range that gets **progressively less tolerant** because the underlying behavior is non-linear"*:

| Ops | Reaction |
| --- | --- |
| **3–5** | *"I'm smiling."* — the target |
| **6** | *"It's okay."* |
| **9** | *"It's a lot." / "I don't know."* |
| **12** | *"No no no no!"* — *"I'm most likely going to throw it out, but at least I'm listening… You're probably unlikely to make your case. I'm still gonna throw it out."* |
| **20** | *"At 20, I'm throwing it out. **At 20, I'm not even listening.**"* |

External standard: *"According to the design standard I showed you yesterday, clearly states **no more than 20**. No if, no butt, no nothing."* → [[Modules/Microservices Development Process#Development and Design Standards]]

Empirical back-fill: *"When I measured all of .NET, the good interfaces were exactly three to five… the histogram was an **equal bar for three, four, and five**."*

His own meta-caveat: *"Everything I say this week, it's all soft and mushy. I know you think I'm raising the bar too high. No no, I'm telling you all my numbers, my guidelines are **entry level**."*

#### Metric 2 — Avoid Property-Like Operations

> [!danger] "You think properties are good, therefore properties have to be bad? No… What I hope you were told is that properties are better than **public member variables**, and indeed they are. But in what twisted reality does 'better' make 'good'? I do not know. Properties are bad."

*"They always **imply state**. They **betray implementation**. **Why do I need to know how many hairs the dog has? I don't need to know. Fetch. Bark.**"*

**The coupling chain:** *"A good interaction between a service provider and a service consumer is always **behavioral**. Do something, do operation. How you go about doing it? I don't know and I don't want to know, because **the more I know, the more I care; the more I care, the more I'm coupled to you; the more coupled to you, the more you change, I change**."*

**The general principle:** *"What is better in life — **to tell or to ask**? Well, we know the answer for that. Why would you write your code any other way?"*

**Empirics:** *"If I look at every good code base, .NET and such — **no properties**. …If you look at **COM**, COM did not have properties, only interfaces with operations, as it should be."*

**The C# origin story.** Early C# had **no properties** *"because properties are bad."* Then the VB team went hat-in-hands to **Anders Hejlsberg**: *"our users — you see, we wouldn't even dignify them with the word **developers** — our users, all they do is **get and set all day long**."* Punchline: *"To pacify the VB **morts** *(short for mortals)*… Anders added get and set to C#. **Not because it was a good idea.**"* Properties entered the language as a political concession, not a design decision. *"Then WCF comes along, no get and set. **As it should be.**"*

**Property-like operations** is his coinage for the workaround — you want a `Name` property, there are none, so you add `GetName()`/`SetName()`: *"I call these things property-like operations. **Don't do it.**"* *"The fact that you could **cheat the WCF police** doesn't mean it's a good idea."* And: *"It's a **fiction** that you need properties."*

#### Metric 3 — Contracts per Service ≈ 2.2

*"It's slightly higher than two. So a typical service supports two contracts."* Why it feels right: *"You have the **business logic contract** and you have some kind of a **plumbing / connectivity / diagnostic / instrumentation / something** contract. Makes sense."*

> [!warning] Metrics are not scale-invariant — the totem pole of software
> *program → system → platform → fractal.* *"Things which are true in a simple program are not necessarily true at the scope of a system or platform or fractal."* As you go up the pole, **the number of contracts per service increases**. 2.2 is a mid-pole figure (*"somewhere in the middle of it, say system to platform"*) — locate your software on the pole before quoting it.
>
> **Do not confuse this "fractal" with self-similarity.** Here it is the top rung of a *size* totem pole, used to explain why thresholds are scale-relative. The self-similarity idea lives in [[Modules/Design Aspects#Self-Similarity and Fractal]] and is a different concept. He parks it: *"I know you never heard about that. We'll discuss it Friday morning."*

> [!note] First real datapoint — 2.65 on Resilient Energy
> In [[99-Resources/Transcripts/Sample Project — Resilient Energy|Sample Project — Resilient Energy]] he measures his own flagship project at **2.65 contracts per service**, above the threshold, and explains it with exactly this caveat: *"there's a bunch of other interfaces here required just to manage the fractal and such."* That is the first time he has **used** the totem-pole caveat rather than merely stated it — and the number stayed almost unchanged across two years of development. Treat 2.2 as a mid-pole figure and expect higher values in large systems of systems.

#### Metric 4 — Arguments per Operation ≈ 0.7

*"Somewhat under one."* Rationale is behavioral, not stylistic: *"Even passing a bazillion arguments means **you know too much about what is happening on the service side**. Ideally, I don't even want to pass arguments. I tell you to do something. **What kind of data you need? That's on you. I don't care.**"*

> [!warning] Anti-cheat caveat
> *"Suppose I have 25 arguments, I'll make one structure with 25 fields and pass it in, and that's now a single parameter. **You're cheating here.**"*
>
> The metric counts **individual fields**, not parameter slots — the same move he makes against the *"amalgam of three things concatenated back to back."*

> [!warning] First real datapoint — and it is not flattering
> Measured on Resilient Energy: **0.79** initially, drifting to **0.95** after two years. His explanation is a self-admitted lapse, not a scale argument — *"that's because I didn't quite insist on certain things. If I were to do it more, my weight would be slightly lower."* So his own flagship project lands **above** the threshold and moves the wrong way over time. The qualitative claim survives intact (85% of methods take zero or one argument, none more than four), but **do not quote this project as evidence that 0.7 holds in the wild.** See [[99-Resources/Transcripts/Sample Project — Resilient Energy#4. The Metrics — Initial Design]].

#### The Closing Thesis — Compliance Asymmetry

> [!important] "Super important: **complying with the metrics does not mean you have a good design. Violating the metrics means you have a bad design.**"

Proof by counterexample, callback to the sample project: `IScannerAccess` has four methods — *"smack in the center of three to five"* — yet was revealed to be *"an ugly dumping ground… not logically consistent, it's not cohesive, it's not independent facet. I mean it violates everything. **Yes, it has four methods. Doesn't mean anything.**"*

Upper-bound sanity check: *"If I show you a contract with four thousand methods, that's obviously a bad design."*

**The doctor/temperature analogy** — the lecture's final image: *"If the patient doesn't have a fever, doesn't mean the patient is healthy… you measure the temperature, it's exactly **36.9 centigrade**. Doesn't mean the patient is healthy. No, doesn't mean. Not at all. Now, if the patient has a fever, the patient is sick. That we agree, okay? It's exactly one of those things."*

**Net position:** the metrics are **one-way detectors**. They can only *falsify* a design, never *certify* it. Passing all of them buys you nothing.

> [!warning] This theorem is already written up
> [[Modules/Microservices Development Process#Metrics — the full lecture]] already carries it: *"the correlation runs both ways and is not one-to-one. It could be that the patient has a fever, doesn't have a fever, and the patient is still sick."* **Same theorem.** Only the **36.9 °C** figure and the explicit *comply ≠ good / violate ⇒ bad* framing are new here.

### Contract Factoring Process

- [Transcript — Service Contract Design](../99-Resources/Transcripts/Service%20Contract%20Design.md)
- [Transcript — Contract Factoring in Practice](../99-Resources/Transcripts/Contract%20Factoring%20in%20Practice.md)

The first pass at this section came out of the Wednesday lecture and was honest about being thin:

*"You constantly iterate over it and you evaluate: are they logically consistent? are they cohesive? are they independent facets? what else could change, in which case what would I do? and on and on."*

That is the **inner test** — the thing you check on every iteration. Two days later he gave the **outer discipline**: how to iterate, how long it takes, and why it fails in organisations. Both halves are below.

> [!warning] An envelope he deliberately leaves closed
> *"We are going to see that IScannerAccess, the first one we started with, had another really, really bad thing going for it, but we're not ready to acknowledge it now."*
>
> **Still unopened.** The follow-up recording never revisits the sample project. Do not guess what it is.

#### Rule 0 — Iteration Is Mandatory, Not Optional

> [!important] "Contract design, like any design, is iterative. **Never try to get the contracts right in the first pass.** Nobody — myself included — has ever done that. It's the height of hubris to think that it's possible. Nobody is smart enough."

He then removes intelligence from the explanation, which matters: it isn't that smart people could do it in one pass. *"There's an act of **discovery and maturity** that simply takes a **critical number of iterations**… You have to sweat on it."*

#### Rule 1 — Iterate Across Subsystems, Not Through Them

The technique most likely to be violated in practice.

In a small system you *can* take two or three services in isolation, design them, and hand them to manufacturing. Beyond a certain size — several subsystems, each a system in its own right, interacting with the others — you cannot, because of **crazy ripple effects**.

> [!danger] "Resist the temptation of taking the first subsystem, factoring the contract to perfection, moving to the second, factoring to perfection… **that will never work**, because as you do these things you validate what you did before and you have to go do it again."

Prescription: **iterate across all subsystems, bringing each to the same level of maturity as you go along.** Sketch subsystem 1, raise it one notch; immediately move to 2 and raise it to the same level; then 3, then 4; then go back round and raise them all again. His formulation of the discipline: **"I never do one of them to perfection."**

The cost is context switching, which is *incredibly* expensive in detail design — **several hours** to get back into the zone. Hence Rule 6.

> [!warning] Real-world test — confirmed, but the rule may be stricter than necessary
> On [[99-Resources/Transcripts/Sample Project — Resilient Energy|Resilient Energy]] he reports the exact payoff this rule advertises: *"two years later, we did massive changes, like moving things from this subsystem to that subsystem. There were **no ripple effects**, everything just works."* But three things complicate it, all in his own words:
>
> 1. **He deferred a subsystem** — *"the design of the large third subsystem was actually done on the go"* — so he did not bring every subsystem to equal maturity up front, and still got the clean result.
> 2. **Ripples were very real *during* design** (*"there were crazy ripple effects"*). "No ripple effects" is a property of the **mature** design, not of the process.
> 3. **Governance is a confounder** — *"even if you start with the best design and you allow developers to butcher it, they're going to butcher it"* — backed by a hard gate routing every detail-design and domain decision through the architect or an SME.
>
> So the rule's promise is real, but the outcome is **factoring quality + governance**, not factoring alone.

#### Rule 2 — The Second Round of Interviews Is a Different Interview

| Interview type | Uncovers |
| --- | --- |
| **Architecture** interviews | The **nature** of the business — the core use cases |
| **Detail-design** interviews | The **behavior** of the business — how it is supposed to behave |

This is the cleanest architecture/detail-design boundary in the vault, and it is what makes Rule 1 necessary: you don't know the behavior yet, because *"nobody ever gives you 300 UML activity diagrams of the project."*

#### Rule 3 — Detail Design Is an Active Process

*"You can't just sit and say mm-hmm, mm-hmm."* Always reflect your understanding back: *"Let me reflect back to you — I understand that this is like that. Is that true?"*

And refuse the wave-through: push hard enough and they'll say **"close enough"** — *"No, it's not close enough."* If it's sometimes ABC and sometimes ABD, you must know which, because **"these idiosyncrasies are exactly the things that would help you factor the contracts better."** Supported by: *"Understanding never lands in your lap on a silver platter."*

#### Rule 4 — Blockers Are Signals

> [!quote] "Typically blockers are not necessarily a bad thing — they indicate something. Go investigate what's hiding there."

If you have another architect, *drag them*. A blocker is usually *"some glaring ambiguity or some hidden landmine that the business people are not even aware of"* — and forcing them over it with you clarifies the point **even to the business people**, which is why it is worth surfacing rather than absorbing.

#### Rule 5 — Never Design for the Metrics ("Icing the Thermometer")

> [!important] "Never design for the metrics. I call this **icing the thermometer**." *Any doctor who does this is a quack.*

The image: a patient with a fever, and a doctor who wants good metrics puts an ice cube next to the thermometer. The temperature drops; the metric looks fine.

The inversion that replaces the compliance-asymmetry framing: **"Meeting the metrics is the result of a good design."** See [[Modules/Microservices Development Process#Metrics — the full lecture]] for the original theorem (*comply ≠ good, violate ⇒ bad*, patient at 36.9 °C). **Same theorem, new failure mode** — that note warns that passing tells you nothing; this one names the active sin of engineering toward the number.

Corollary — you may start from something obviously wrong. Either a *"giant ugly dumping-ground monster"* with everything in it, or dozens of tiny obviously-unrelated contracts. Both are bad, but *"at least you have all the operations. Then start iterating: factor up, down, sideways."* The operational question for sideways is **"what else in these things looks like it would fit here?"** — applied until it's cohesive. *"Eventually, if you do your work correctly, it will tend to land on the correct metrics."*

#### Rule 6 — Meticulous Notes, Because Context Switching Is the Real Cost

> [!danger] "In detail design, context switches are **incredibly expensive**."

The failure mode, described vividly:

> [!quote] "You actually forget what the insight was that made you decide to do it like this. You're staring at it and you have no idea why you did it. **You're afraid to touch it because maybe it was right, but you can't justify it now.** So do you continue with it or not?"

> [!important] "I cannot stress enough how important it is to take **meticulous notes**."

Record the *because*: *I'm doing this because of this, because of that.* And record placeholders honestly — *this operation is here, it's a placeholder, we didn't find a home for it yet, it's not supposed to be here.*

#### Rule 7 — Don't Jump Three Steps Ahead

Make iterations explicitly explicit. Two reasons:

1. **Hubris.** You may discover an additional insight on the intermediate step you skipped.
2. **Mentoring.** *"If you just jump to the end, they're going to say: how did you get from here to that? They don't see it. So what value is that? It just frustrates them."*

#### Rule 8 — Sketching, and Validation as a Factoring Technique

Start sketching; it doesn't have to be correct. Sequence: **name things** → draw **interaction diagrams** before you have operations (*"this service is going to do something with that service — we already have the name, so give it the name"*) → look at the use case and try to validate it.

> [!important] "Design validation is a world-class contract factoring technique."

Validation is not a final act where you confirm the design holds water. Trying to validate *produces* factoring: the use case turns out incomplete, wrong, or a duplicate, so you change the use case, which uncovers something else, so you come back and validate again. Iterate simultaneously in **diagrams** and **code sketches** (a C# or Java interface).

Two directions to check:
- **Don't just satisfy the use cases with the blocks you already have.** Spewing extra operations produces two big things. Ask instead: *"Am I actually even missing a contract? Am I missing operations? Am I even missing a service?"*
- **The other direction:** things you thought you'd need but never used — **throw them away.**

Early on there is enormous churn and *"clouds of dust"*; keep going and *"eventually the churning subsides and things start settling."* Visual corollary: *"Many times the key to a blocker is just **visualizing it differently**. It solves it instantly."*

#### Rule 9 — Consistency Is the Last Mile

Design integrity (all parts meshing, use cases validated) is not the end. The design must also be **consistent**:

> [!quote] "All the contracts have to look like they came from the same **cookie cutter**."
> If one takes this kind of data contract, they all do. If one has this operation shape, that's the shape for this type of component.

> [!important] "If you won't make design consistency a priority, **it's certainly never going to happen organically**." *"Once developers start, developers will **always** try and unravel things. So it needs to be at a very high level of integrity and consistency to begin with, to stand any chance of surviving through development."*

See [[Modules/Project Planning#Design Consistency — The Higher Level of Design Integrity]]. That note has the metaphor; what's new here is that it applies to **contracts specifically**, plus the two rules above.

#### What "Good Design" Requires — Four Conditions, All of Them

> [!important] "If they meet the metrics, and they are reusable, and they are valid — they support the use cases — then you can probably state you have a good design. **All conditions have to be met. In isolation, none of these things means much.**"

| Condition | Where it comes from |
| --- | --- |
| The contracts have the attributes — logically consistent, cohesive, independent facets | [[#Service Contract Design]] |
| They meet the metrics | [[#Contract Metrics]] |
| They are reusable | [[#Service Contract Design]] — the master attribute |
| They are **valid** — they support the use cases | Rule 8, this section |

This *sharpens* rather than contradicts the compliance-asymmetry thesis: meeting the metrics alone still means nothing, but it is now one of four necessary conditions rather than a free pass.

#### Working With the Domain Expert

The architect is *"not necessarily a domain expert,"* so factoring needs the expert's help at least as much as architecture does. The availability problem is structural, and it explains why detail design starves for input:

| | Architecture | Detail design |
| --- | --- | --- |
| Needs the expert | Continuously | Intermittently — a few hours, then a few days, then a few hours |
| Expert's disposition | *Interested* — they'll give you the week | *By definition very busy* — domain experts are the people who add the most value |

The fix is to make the commitment explicit and ongoing rather than episodic:

> [!important] "This will take me three or four months. I need these two domain experts **on call**. When I need them, it overrides everything else they do… In between, they can do whatever they want. But I raise my hand and they immediately have to help me. It's essential for success."

At least one. For a complicated domain with **multiple facets**, multiple domain experts.

### The Cost of Factoring — and Why Organisations Fight You

- [Transcript](../99-Resources/Transcripts/Contract%20Factoring%20in%20Practice.md)

> [!note] New section
> This material is about *why factoring is hard to get away with*, not about how to do it. It belongs here because the resistance is specifically to contract factoring — and because the answer to "why don't we just refactor" is a contract-design answer.

> [!important] "The real problem is that contract factoring is very time consuming."

Everything in this section follows from that sentence.

#### Why It Bites at the Junior Hand-off Point

> [!danger] "For them, one big thing with 7,000 methods is just fine. If you let them do it, of course they're going to butcher it. They are instantly going to go to **the edges of the curve** and then you're dead."

Mitigation when senior developers are available: design a few services with them, farm out **simple programming tasks** to the juniors, move to the next batch — the batching model quantified in [[Modules/Project Planning#The Hand Off Point: Senior vs Junior]]. When you *cannot* avoid designing the whole system yourself, the instruction is simply to accept the cost: *"20 services, let's say it's a week for each — that's six months."* (His own arithmetic; 20 × 1 week is nearer five months. Quoted as spoken.)

> [!important] "If you do not acknowledge the true nature of the hand-off point, you are going to fail… it instantly sends you to the edges of the curve, which is **non-linearly worse**, and then nothing really matters."

#### Detail Design — the Missing Third Discipline

The diagnosis he keeps returning to: **"These simple detail-design skills are what developers lack the most."** He walks the other two gaps and dismisses both as coverable — developers don't know architecture, *fine*, he can hire competent architects; developers don't know much coding, *fine*, he expects them to know the domain so he looks the other way. Detail design is the one he cannot outsource around.

> [!important] Detail design is **"separate and distinct from architecture, and separate and distinct from coding."** *"Nobody taught them, nobody trained them, and of course they don't know how to do it."*

The asymmetry that drives the whole cost argument:

| Discipline | Time |
| --- | --- |
| Architecture | *"A blink of an eye. An hour a day — if you're doing a week, you're already spending too much time on it."* |
| Detail design | *"Very time consuming. **Weeks, months.**"* |

*(Note this is a different sense of "architecture takes a day" from [[Modules/Project Planning#Terse Requirements at the Service Level]] — that one is about how much you write down. This one is about how much clock time the activity consumes.)*

#### The Organisational Problem — They Don't Think It's Possible

> [!danger] "The vast majority of organizations do not recognize the value **or even the feasibility** of contract factoring."

Note the second word. It isn't that they undervalue it — they don't believe it can be done. The root cause is biographical: *"Most people have seen nothing but mud their entire career."* Never having seen a contract factored correctly, nor having been required to re-do one, they generalise from their own experience. **For them, re-re-re-re is the only way to do things.** Tell such a person a contract can be got right up front and the reaction is *you're trying to do the impossible — they will fight you.*

> [!important] The fallacy, named: **"The fact that they know how to do something or have never seen it doesn't mean it cannot be done."**

> [!quote] "Tell an average person of the 1800s that within a few short years most people will have a standard of living higher than the king. *You're crazy. You're crazy.*"

#### The Cost and Morale Arguments

**Cost:** perpetual refactoring is *"**orders of magnitude** more expensive. It's not a little bit more expensive."* The multiplication is nullified testing effort, repeated rearrangement of the ball of mud, and solving a non-linearly worse problem each time.

**Morale:** *"What is it like to live in a perpetual construction site? People constantly going through mud and debris. Who wants to live like this?"* And quality cannot survive the environment: *"Testing is meaningless in such an environment, because every test is going to be changing next week."*

> [!important] "Those that do not invest in detail design live to regret it — either immediately or eventually."

#### Holding the Line

Because the resistance is epistemic rather than rational, technique alone is not enough:

> [!important] "Every single one of you must be able to say to the boss: **trust me or fire me. It's an illusion that there's anything in between.**"

Accompanied by his dismissal of the noise: *"It doesn't matter what all the howling, shrinking monkeys and knuckle-jugglers are saying."*

And how not to convert them: *"Calling somebody a lunatic monkey is not a good idea."* Ask an open question instead — *"How has this been working for you? You think that doing more of the same would solve it?"* → *"You catch more flies with honey than with vinegar."*

#### The Golden-Egg Story

The cautionary tale that justifies the above, and the reason conviction is required at all.

**Act one.** A strategically important internal system. **Three and a half months** of contract factoring — his own phrase is *"talking to myself."* Out of the corner of his eye, the managers are *"clawing the walls."* Their parody of him, reported without flinching: *"Is a dog really a dog? Or is it really a cat? Maybe a poodle. Oh, what is an iguana? Bunk, fetch, give me this, give me that."*

> [!important] His response: **"I know you don't understand. I know by your own admission you don't understand. Which is why I'm doing it. That's okay — that's my job."**

**Act two, roughly twenty years later** (he insists he doesn't know the exact figure). His older sister is at a holiday cocktail party, meets someone from that company, is recognised as his sister, and is told: *"I'm not a member of the fan club of your brother… What your brother did for us all these years ago is **a machine that keeps laying golden eggs**."* The rest of the report is the payoff: *"Over the years, a decade, every once in a while somebody lifts the lid. Then you think you know — it's fine, close it. **Technologies come and go, doesn't matter. We keep rolling with this.**"*

The moral is deliberately inward-facing:

> [!quote] "Were they surprised? No. Gratified? Of course. It doesn't matter what they think. **What matters is what you think. Who are you? What are your convictions?**"

Compromising your integrity is *"like drinking acid — you'll be burnt out and spit out like a yellow skeleton on the side."* With the callback: *"I already told you — **the cure for being burnt out is not compromising on your convictions.**"* See [[Modules/Project Planning#Career Advice: Trust Me or Fire Me]].

### How to Learn Contract Factoring

- [Transcript](../99-Resources/Transcripts/Contract%20Factoring%20in%20Practice.md)

> [!danger] "I wish I could tell you just read this book, read appendix A in **Righting Software**, you'll be fine. It doesn't work this way."

> [!important] "The best — and likely only practical — way of learning factoring and detail design is **from someone who knows how to do it**."

Concretely: somebody IDesign-trained, or who has watched it done, has the mileage of doing it on several systems, and feels confident doing it. *"This is a kind of muscle you have to actually hone in your brain."*

**What the mentor actually transfers** — and it isn't the techniques:

> [!quote] "The up-down-sideways is actually the easy part."

The process and the mindset, specifically: **how do you know this subsystem is done and we can move to the next? How do you know when enough is enough? When is good enough?**

Both mindset failure modes:

| Failure mode | His correction |
| --- | --- |
| Charge ahead and try to get everything done | *"You will fail."* |
| Get immediately disheartened by another three months of this | *"Every journey starts with a first step. Let's take the first step, examine where we are, revise the navigation if we need to. It's fine. Calm down. All you need is the determination, the mindset."* |

**The discovery anecdote.** The system is **Resilient Energy**, named two days later in [[99-Resources/Transcripts/Sample Project — Resilient Energy|Sample Project — Resilient Energy]]. A key aspect of a design he already knew how to solve, yet he spent two meetings walking the team through *different wrong solutions* so they would rule them out, *"controlling them into doing it correctly using a completely different mechanism that they had no idea about."* Worst possible starting point: an interface with only properties. End result: a **discovery-based mechanism**.

> [!quote] "If you've done it enough, you recognize the pattern — 'this kind of a problem we typically solve like this' — so you have an instant jumping over there. But again, don't cut the pauses short."

**The course.** A week-long immersion taught by his IDesign colleague **Monty** *(class name uncertain in the raw transcript — and **not** the Project Design Clinic recorded in [[Modules/Microservices Development Process#Architect and the Team]], which is presentation coaching and a different course)*.

> [!quote] "Monty is a hell of a lot less nice than me. He actually lets you fail a lot before he shows you how to solve it. A lot of tough love."

> [!quote] "In a week you will see like **fifteen different systems**, and they're all full of challenges. Every time you have to do something, you say: okay, this one is missing a leg and an eye — now what are you going to do?"

> [!important] The closing line: **"There's no substitute for you gaining your own experience and seeing how it's done on the real system."**

### The Empirical Study and the Business Case for Reuse

- [Transcript](../99-Resources/Transcripts/Service%20Contract%20Design.md)

> [!note] New section
> This material does not fit any of the five topic stubs — it is the evidence base behind the metrics plus the organisational argument for reuse. It is kept as its own section rather than buried under Contract Metrics.

*"I've been doing it for years. For years I measured contracts. I wanted to see what is good — **not by what I think is good, what passes the test of time**. What I really wanted to do is draw this chart. I wanted to have the formula."*

**The enterprise-architect privilege.** He calls a meeting with division architects: *"how many contracts do you have? I don't know. Okay, let's get me a dump of everything. All of the interfaces, good. How many lines of code are behind every one of them? I don't know. I've got this utility that measures it. What's the complexity? I don't know. Let's measure it too. How many developers work on this? 17? Oh, okay."*

**~60 projects interviewed.** Model assumed: *"y equals a times e to the power of b times x, plus c, plus a big constant at the end. It's basically some kind of a power function."* *(He says "five coefficients" and lists four — flagged, not silently fixed.)* The formulas were *"ridiculously non-linear… I had to actually plot it on a **log chart** to see what is going on."* Finding: *"there were **incredibly uniform metrics** between the contracts that resided in the area of minimal cost."*

**Why he bothered — the not-invented-here problem.** Ten divisions; nine want black, the tenth wants white. *"The tenth is gonna say I'm gonna change something on here and break my code because the other guys want to do the opposite. I cannot have that risk."*

> [!quote] *"Suppose I want you to do something for me and I'm at the bottom of your priority list and I have a dependency on you and I'm stuck. **I'd much rather invent the wheel on my own than take a dependency on you.** That's the normal inclination of most people. That's the fundamental drive behind the **not-invented-here syndrome**."*

**The lever, verbatim:** *"Look, I measured your code. Your project is here, it costs you this much. If you use our framework, I can get you to here. You will save this much money. **By the way, I'm sending a copy of this report to your boss too. Your call.**"* → *"Of course they wanted to use it. Now I can give them a tangible number."*

**Why no formulas are published:**

> [!important] "The behavior is universal, but the values are not."
> *"What I found is that they are actually **not universal**. They're highly dependent on the nature of the business, on the domain, on the technology. So unfortunately there is no generic formula here. We can talk about abstract behaviors in a qualitative way, but not in a quantified way. But for a while, I actually had these formulas."*

Corroboration base: *"the code and design of IDesign customers and measured systems of mine that have survived for decades."*

**The .NET survey:** *"When .NET itself came out, I used **Reflection** to measure all the interfaces in .NET and sort them from the best to the worst. There were **two thousand interfaces** in my survey. And when .NET 2.0 came along, now there were **2,200**. I wanted to see if things had changed. I did it again and I got **exactly the same results**."*

### Sample Project

- [Transcript](../99-Resources/Transcripts/Service%20Contract%20Design.md)

A point-of-sale register in a mall store. The POS connects to a **barcode scanner**, which *"is actually acting as a **resource** to the system."* Task: *"design a service contract for the **resource access**."*

> [!note] Parked for tomorrow
> *"These two words resource access doesn't mean much, but tomorrow when we'll discuss the **SSM method**, it will mean a lot. So I'm parking these two bullets for future reference."* → [[Modules/Design and Architecture#Structure (Clients, Managers, Engines, Resource Access, Utilities)]]

#### v1 — the scanner

Requirements: scan individual codes; adjust the scanning beam (barcodes print in different sizes — *"if it's a very large barcode, we have to widen the beam"*); open the port, scan, close the port.

```
IScannerAccess { ScanCode, AdjustBeam, OpenPort, ClosePort }
BarcodeScanner : IScannerAccess
```

Instant reuse payoff: *"Maybe a QR code and it even supports the same contract. So obviously this is a good contract because it's reusable, right?"* — the setup for the whole exercise.

#### v2 — the numeric keypad → FACTOR DOWN

Barcodes get scratched, so the operator types the code. *"There's some kind of distribution that 80% of the items, 80% of the time it's [on] 20% of the items"* — over time the operator knows the codes by heart, and typing beats bending down, picking up the gun, scanning, putting it back: *"You just look at it and type the digits. We do auto-completion, bam, that's it."*

The failure: *"You cannot use IScannerAccess… because it says **Scanner** over here and this is obviously a scanner, doesn't mean anything to a numerical keypad. And what does it mean to adjust the beam to a numerical keypad?"* Also: *"You can't just use half the interface. What do you do? Throw exceptions on the messages you don't implement. What are you gonna do?"*

Diagnosis: *"IScannerAccess assumes the device is an optical device."* → *"From a reuse perspective, it is much better to abstract the actual reading because fundamentally it's not really a **scanner**, it's a **reader**. It reads a value. Whether the reading is done optically or by typing is actually to a large extent irrelevant."*

**The two renames** (*"the first sleight of hand"*): `IScannerAccess → IReaderAccess`, `ScanCode → ReadCode`.

`AdjustBeam` is *"an **offending operation**. It works great on a scanner, it feels miserably on a numerical keypad."* → factor it down:

```
IReaderAccess   { ReadCode, OpenPort, ClosePort }
IScannerAccess : IReaderAccess { AdjustBeam }
```

Final implementations: `BarcodeScanner : IScannerAccess`, `QRCode : IScannerAccess`, `KeypadReader : IReaderAccess`, `RFReader : IReaderAccess` — *"this is a far better proper form of reuse."*

**What an RF reader is** (the one real-world aside): *"There are already stores today that there is no actual checkout line. The moment you take the item and put it in your cart, there's a little chip inside, there's some kind of a magnetic pulse inside, it zaps it, reads it inside the cart, or maybe when you take the shopping cart out of the store it actually rings you up automatically."*

#### v3 — the conveyor belt → FACTOR SIDEWAYS

Shoppers put items on a belt; the operator presses a pedal repeatedly to advance it; *"it gets very old."* Since the code already knows the item size, the system can advance it by the right amount. The belt *"acts as yet another resource."*

Why `IReaderAccess` collapses: *"IReaderAccess means absolutely nothing to the belt. What does it mean to read code? You cannot abstract away, you can just call it **DoSomething**. Because the belt also has start and stop. What does it mean?"*

Root cause is **logical consistency, not naming**: *"The root problem is IReaderAccess is a poorly factored contract."* `ReadCode` is the facet of the entity as a **reader device**; `OpenPort`/`ClosePort` are the facet as a **communication device**. *"These two therefore are not logically related. You could make the case that open and close ports are much more logically related to each other than they are to ReadCode."*

His verdict: *"It's actually an **ugly dumping ground, an ugly grab bag** of all the things you had to say. You just took all the requirements, shoved them on the contract, and it's basically much closer conceptually to **OOP** — much closer conceptually to a **one big thing** than it is to anything else."*

```
ICommunicationDevice { OpenPort, ClosePort }   // facet: communication device
IReaderAccess        { ReadCode }              // facet: reader device
IBeltAccess                                    // facet: belt
```
*"Know that all of these things are completely independent from each other."*

And the payoff: *"the sum of work inside BarcodeScanner has not changed. We're not doing any more work. However, the conveyor belt can also implement ICommunicationDevice. So now we can reuse it."*

#### v4 — safety and diagnostics → FACTOR UP

Kids pick up the laser gun and zap the next kid's eyes; *"there was this girl with long hair, it got caught in the conveyor belt, really bad things happened."* So: a giant red button that *"stops everything, aborts everything, disconnects the power to everything… in the interest of safety."* Plus diagnostics: *"ping all the devices and get diagnostic information so we can do some preventive maintenance, do some statistics."*

Why these belong everywhere: *"Logically aborting the conveyor belt is just as much an operation of the belt as aborting the laser gun. So both of them would not be logically consistent if you did not include the aborting operation."*

```
IDeviceControl { Abort, Diagnostics }
IReaderAccess : IDeviceControl
IBeltAccess   : IDeviceControl
```

*"The things that are required in all the other contracts."*

### Sample Project II — The Real System (Resilient Energy)

- [Transcript](../99-Resources/Transcripts/Sample%20Project%20%E2%80%94%20Resilient%20Energy.md)

> [!note] Two sample projects, not two versions of one
> The section above is a **pedagogical toy** — it teaches the factoring *moves*. This one is a **real consulting engagement that shipped**, and it shows whether the moves hold. Toy first (tutorial), real second (exhibit). Keep them separate; conflating them loses the distinction between *reasoning* and *measured evidence*.

> [!danger] The source transcript is truncated mid-sentence
> It ends: *"…because of the investment in data design is just right"* and then stops. Everything up to the arguments-per-method histogram is reliable; **everything after it is missing.** Do not reconstruct the ending.

**Company: Resilient Energy.** This resolves the "energy net" flag raised in [[99-Resources/Transcripts/Contract Factoring in Practice#6. How to Learn It|the previous lecture]] — same project, named: *"this is the energy project I keep referring to you here. It's what I'm leading now on the side."*

#### What Makes It Hard

A volatility stack where everything arrives at once: multidisciplinary (fintech, Nash-equilibrium economics, physics, EE/ME, psychology); **E-type** (*"the very introduction of the system would drastically change every environment it's going to be in"* — Lehman's taxonomy, a real term, not a garble); **illegal** (*"it is illegal to deploy this system in most places in the world"*, likened to transmitting data over phone lines before 1992); mission critical (*"if you are gonna do bad things, people are going to die"*); 40-year-old legacy utility code; *"a near endless variety of devices"*; scale from appliance to continent; and *"every deployment is going to be different. Not just a little bit — completely and utterly different."*

His analogy for the vault: **"the system is nothing short of the internet for energy."**

#### Architecture — Absolute Self-Similarity

The vault's first concrete self-similarity material, and it is not theoretical.

> [!important] "Each node in the tree has four subsystems. Each node across the tree from the continent level to the appliance has **absolute self-similarity** — it is exactly, exactly, exactly, exactly, exactly the same code."
> **"The system doesn't know it is the root of the world or it's actually a light bulb. It doesn't know."**

Self-similarity here is **mandatory, not aesthetic**: *"if you start doing it with if and else, you will fail. There is no way of building this kind of a system using if and else."* → [[Modules/Design Aspects#Self-Similarity and Fractal]]

Each node uses the classic IDesign method internally — manager plus services/engines — *"the classic thing we're going to discuss tomorrow"* → [[Modules/Design and Architecture#Structure (Clients, Managers, Engines, Resource Access, Utilities)]].

No off-the-shelf technology (not .NET Core, not Java): distributed transactions, reliable messaging, message security, discovery, message bus, long-running workflows, massive concurrency, offline and degraded-mode operation. *"You couldn't do these things with Web API."* **Three years spent building the technology itself**, guided by WCF/ServiceModel — *"my firm went off of WCF"* — producing *"a framework that is eerily familiar to WCF."* And the re-park: *"all they're trying to get you to do is use decrepit Web API. There's themselves, by the way — don't use it. **We'll get to it tomorrow.**"*

#### How It Was Actually Run

He says **"four stages"** and lists five (use cases, architecture, detail design, construction, integration) — flagged, not corrected.

**Green/green/green grading** — the answer to designing something nobody has done:

| Grade | Meaning |
| --- | --- |
| Single green | New system |
| Double green | New system, on technology you must invent |
| **Green-green-green** | **The use cases themselves don't exist.** *"There are no users. There's nobody you can talk to and ask, should it be like this or should it be like that."* |

Only input to the design team: **single core use cases of two words**, one being **"survive."** Which creates a specific composable-design problem — with 2–5 core use cases it's easy, but with a single highly abstract one *"there is literally an open-ended number of variations,"* so **"the next level down of use cases are actually the real use cases."** This is [[Modules/Project Planning#Core Use Cases vs. Fluff]] taken to its degenerate case.

**Artifacts:** ~100 activity diagrams for two of the four subsystems (many *"open-ended in variation"*, not locked); 100 pages per subsystem; ~100 sequence diagrams for those two, ~80 more for the others; many passes because *"there were crazy ripple effects"* between use cases and subsystems.

**The design objective, stated plainly:**

> [!important] "Not to nail down every last argument to every last method." → **"The real objective here is removing detail design as a risk out of the project."**
> Diminishing returns on finessing the last detail; what matters is that when you change something, *"there won't be ripple effects detonating everything else."*
> That is the strongest statement of detail design's purpose anywhere in the vault.

**Medium migration:** PowerPoint first, occasionally jumping to Visual Studio to demonstrate something; early VS sketches are *"only a grab bag of operations"*; over a month or two progressively more moves into VS, returning to diagrams only for multi-stage call/callback/event-from-queue flows where *"at this point you lost everybody."*

> [!important] Zero code. **"The design team did not produce a single line of code. This was purely a design effort."**
> He calls this *crucial in iterating quickly*: asking only *consistent? cohesive? independent facet? reusable?* while completing **no** implementation gives *"a much faster cycle time."*

**Team: five people, four months to the day, all remote** across Europe / US-East / US-West. One architect doubling as domain expert, one senior architect doubling as technology expert, two junior architects acting as senior developers, and the venture's **other founder** as domain expert. **36 conference calls, 126 total hours, 630 work hours** — self-consistent, since 630 ÷ 126 = 5 exactly. Calls averaged 3½ hours, plus 12 hours of overall review.

**The monkey wrench** — credited as causation, not colour:

> [!quote] "Every once in a while, once we figured out doing something, he would throw a monkey wrench into it." … *"There's this case over there where it's completely different and **the unicorns are flying backwards**."* … *"This is fantastic. This is like the best there is… it was constantly coming in and destroying what we did. **It was wonderful.**"*
> **"I think it is one of the core reasons we were successful — that kind of disruption."**

This is the empirical answer to the *"domain experts on call"* instruction — the expert was one of five named people and the disruption was institutionalised.

#### The Metrics — First Time He Has Published Real Numbers

| Metric | Initial | After ~2 years | His threshold | His explanation |
| --- | --- | --- | --- | --- |
| Contracts per service | **2.65** | almost unchanged | ≈ 2.2 | *"slightly higher… because there's a bunch of other interfaces here required just to manage **the fractal** and such"* |
| Interface reuse | **1.61** → 2.1 corrected | slightly increased | — | ~**35 mock-up services that do nothing**, wired only so services could connect. *"These things are not real services."* |
| Operations per interface | **3.09** | slightly under 3 | 3–5 | *"quite nice"* |
| Parameters per operation | **0.79** | **0.95** | ≈ 0.7 | *"that's because I didn't quite insist on certain things. If I were to do it more, my weight would be slightly lower."* |

Counts: **47 contracts** (+8 zero-operation placeholders), **145 operations** → **68 / 189** after two years. All operations behavioral; **exactly zero properties or property-like operations**; *"there isn't a single operation that corresponds to a feature."* His label: **"It's an extreme composable design."**

> [!warning] Read this honestly: the qualitative claims held, the thresholds did not
> Zero ripple effects. Zero properties. No feature-corresponding operations. Design style unchanged across two years. All spectacular.
> And two of his own numbers landed **above** his own thresholds — parameters per operation drifting *up* to 0.95, with a self-admitted lapse as the explanation, not a scale argument.
> **Do not quote this project as evidence that 0.7 holds in the wild.** The numbers were approximations he adjusted in his own favour, and he says so out loud.

**Contract heat maps** as a working tool: large and red = lots of contracts. *"As soon as you identify an outlier, you don't let it fester to have 700 operations on it. You go and start cleaning it up to reduce the heat and spread the heat across the map."* (Different quantity from [[Modules/Project Planning#Heat Map Color Coding by Float]] — cross-link, don't merge.)

**Complexity heat map:** **85% of methods are completely trivial** (0–1); yellow 2–10; very few red. **Most complex method = 25**, a single case — *"basically a complicated numerical simulator that does a lot of formulas and calculus."*

**Operations-per-contract:** green band 3–5; **no contract has more than seven operations**; **50% perfectly in the green**; the 1-operation ones are *"probably unripe — they will either get removed or mature."* And across service types: *"It's not like all managers were seven and engines were two. No, no, no. You had a mix of all of them across all of them."*

**Arguments per method:** 85% have zero or one; a few two or three; **none more than four**.

Then it cuts off.

#### The Empirical Proof — and Why It Is Weaker Than It Sounds

> [!quote] "Two years later, we did massive changes, like moving things from this subsystem to that subsystem. **There were no ripple effects, everything just works.**"

That is the exact payoff advertised by **Rule 1 — iterate across subsystems, not through them**. Stated by him as fact about a shipped system. But three complications, all his own words:

1. **He deferred a subsystem.** *"The initial design was just for two out of the three large subsystems… the design of the large third subsystem was actually done on the go."* Rule 1 says bring *all* subsystems along to equal maturity. He didn't — and still got the clean result. **The rule may be stricter than necessary.**
2. **Ripple effects were very real *during* design.** *"There were crazy ripple effects"* across many validation passes. So "no ripple effects" is a property of the **mature** design, not of the process. Rule 1's audience must not read this as *ripples don't happen*.
3. **Governance is a confounder he names himself.** *"The reason the design style and design direction didn't change is the result of the quality of the initial investment… and **the rigor in the process**. Because even if you start with the best design and you allow developers to butcher it, they're going to butcher it."* Backed by a hard gate: *"all detail design decisions and all domain decisions must go to the architect or a subject matter expert. The developers are not at liberty — and they were all senior, highly paid — to do any detail design changes without consulting with the architect, and that kept things honest."*

**Net:** factoring quality **+ governance**, not factoring alone. Report the anecdote that way.

## Quiz

> [!question]- 1. What are the three attributes of a good contract, and what single word combines two of them?
>!
> [!summary]- Answer
> **Logically consistent** (nothing in it whose presence would force an unrelated change — an employment contract that requires a home address means "if I move, I have to quit"), **cohesive** (it contains all the things required to describe the interaction, *"no more, but no less"*), and **independent** (a marriage contract must not depend on an employment contract). The word that combines consistent and cohesive is **coherent** — he shows a Merriam-Webster screenshot for it. So the target is *coherent and independent facets of the entity*.

> [!question]- 2. Name the three factoring techniques and the telltale sign for each. Why only three?
>!
> [!summary]- Answer
> **Factor down** — telltale sign: an **offending operation** that works in some contexts and feels miserable in others (`AdjustBeam` on a numeric keypad). Split into a hierarchy, push the offender down, keep the common operations upstairs. **Factor sideways** — telltale sign: a **weak logical relationship between operations** (`ReadCode` vs `OpenPort`/`ClosePort`). Split into separate independent facets. **Factor up** — operations that are **logically related but repeated** across facets; *"not including them would make the contract less cohesive. Duplicating them would be just bad contracts."* Hoist into a shared base. He claims completeness — *"These are literally the only three techniques there are"* — because they exhaust the directions a relationship can point: down the hierarchy, across to a sibling facet, up to a shared one.

> [!question]- 3. Your service exposes 2 contracts, its operations average 0.7 arguments, and every contract sits at 4 operations. Is that a good design?
>!
> [!summary]- Answer
> No — and the metrics were never on your side. *"Complying with the metrics does not mean you have a good design. Violating the metrics means you have a bad design."* His counterexample is `IScannerAccess`: four methods, "smack in the center of three to five," yet an "ugly dumping ground" violating consistency, cohesion and independence. *"Yes, it has four methods. Doesn't mean anything."* The analogy is a doctor taking a temperature: 36.9 °C doesn't mean the patient is healthy, but a fever definitely means the patient is sick. Metrics are **one-way detectors** — they falsify, they never certify.

> [!question]- 4. Why does Juval say "properties are bad," and what is the political history behind C# having them?
>!
> [!summary]- Answer
> Properties *"always imply state"* and *"betray implementation"* — "Why do I need to know how many hairs the dog has? I don't need to know. Fetch. Bark." Good service interaction is **behavioral**, and the coupling chain is "the more I know, the more I care; the more I care, the more I'm coupled to you; the more coupled to you, the more you change, I change." His correction to the obvious objection: properties are better than *public member variables*, but "in what twisted reality does 'better' make 'good'?" Historically early C# had no properties **because properties are bad**; the VB team went hat-in-hands to Anders Hejlsberg because their users "get and set all day long," and to pacify the VB *morts* he added get/set — "not because it was a good idea." WCF later shipped without properties, "as it should be." Hence his coinage *property-like operations* (`GetName`/`SetName`) — "Don't do it. The fact that you could cheat the WCF police doesn't mean it's a good idea."

> [!question]- 5. What is the "ultimate litmus test" for a contract, and how do the HR and apartment tests illustrate it?
>!
> [!summary]- Answer
> **Reuse** — specifically *potential* for reuse. "Reusable contracts are coherent and independent… the ultimate way of evaluating a contract is its degree of reuse or its potential for reuse. That is the ultimate litmus test." HR test: if Cruella in HR says "we have crafted a contract just for you," that's bad news — Murphy says always. You want **the same** contract everyone else got, not a better one, because a shared contract has *evolved* to include everything relevant and exclude everything irrelevant ("it doesn't include the name of my cat"). Apartment test: the $500/hour bespoke contract vs the boilerplate that "was good for a million other apartments." Note he insists on **reusable ≠ reused**: "I can design an amazing contract that nobody else in the universe is using besides me. So what? It doesn't mean it's a bad contract."

> [!question]- 6. Why did it take 14 years and metrics to solve the factoring problem?
>!
> [!summary]- Answer
> Because all three factoring techniques only ever make contracts **smaller**. "If you keep doing it, keep doing it, you'll end up with an explosion of little things which we know is not a good design." He spent 14 years looking for a technique that produces **larger** contracts and concluded it doesn't exist. Metrics are the counterweight: they stop the endless fracturing by telling you when you've gone too far. The empirical base was ~60 projects plus a .NET interface survey (2,000 interfaces, re-run on .NET 2.0's 2,200 with exactly the same results), and the headline finding was that **"the behavior is universal, but the values are not"** — the shape of the curve is general, the thresholds are domain-dependent, so no generic formula is published.

> [!question]- 7. What is "icing the thermometer," and how does it relate to the compliance-asymmetry thesis?
>!
> [!summary]- Answer
> Designing *for* the metric instead of for the design — the doctor who puts an ice cube next to the thermometer so a fever reads normal. *"Any doctor who does this is a quack."* The inversion: **meeting the metrics is the result of a good design**, not its target. It is the same theorem as the 36.9 °C passage in [[Modules/Microservices Development Process#Metrics — the full lecture]] — passing tells you nothing — but it names a new failure mode. That note warns that compliance is meaningless; this one names the active sin of engineering toward the number.

> [!question]- 8. Why does "factor subsystem 1 to perfection, then move on" never work, and what is the cost of doing it correctly?
>!
> [!summary]- Answer
> **Crazy ripple effects.** Each subsystem is a system in its own right and interacts with the others, so finishing one in isolation means that when you reach the next you validate — and invalidate — what you already did. *"That will never work."* Prescription: iterate across all subsystems, bringing each to the same level of maturity as you go along; sketch all four, raise each one notch, go round again. *"I never do one of them to perfection."* The cost is context switching, which in detail design takes **several hours** to recover from — *"you forget what the insight was… you're afraid to touch it because maybe it was right, but you can't justify it now"* — which is why meticulous notes recording the *because* are mandatory.

> [!question]- 9. Why do organisations fight contract factoring, and what does Juval say about the argument they make?
>!
> [!summary]- Answer
> They don't recognise the value **or even the feasibility** of it. The root cause is biographical: *"most people have seen nothing but mud their entire career"* — never a contract factored correctly, never required to re-do one — so *re-re-re-re* is the only way they know how to do things. His named fallacy: **"The fact that they know how to do something or have never seen it doesn't mean it cannot be done."** The analogue: tell someone in the 1800s that most people will soon have a standard of living higher than the king — *"You're crazy. You're crazy."* Because the resistance is epistemic, technique isn't enough: *"trust me or fire me. It's an illusion that there's anything in between."* But don't call them monkeys — ask *"how has this been working for you?"* instead.

> [!question]- 10. What are the four conditions for "good design," and why is well-factored not enough?
>!
> [!summary]- Answer
> (1) the contracts have the attributes — logically consistent, cohesive, independent facets; (2) they **meet the metrics**; (3) they are **reusable**; (4) they are **valid** — they support the use cases. *"All conditions have to be met. In isolation, none of these things means much."* Well-factored alone is condition 1 only, and history is full of elegant contracts that don't support the use cases, were never reused, or drifted into inconsistency. Note this sharpens rather than contradicts compliance asymmetry: meeting the metrics is still not a free pass, but it is now one of four necessary conditions.

> [!question]- 11. On his own flagship project, two of Juval's metric thresholds were missed and one was not. Which is which, and what does that tell you about how to use the numbers?
>!
> [!summary]- Answer
> **Contracts per service:** 2.65 against a threshold of ~2.2 — missed, but with a legitimate scale explanation (*"a bunch of other interfaces here required just to manage the fractal"*), and stable across two years. **Operations per interface:** 3.09 against 3–5 — clean hit, slightly under 3 later. **Parameters per operation:** 0.79 against ~0.7 — missed, drifting to **0.95**, and his explanation is a self-admitted lapse (*"I didn't quite insist on certain things"*), not a scale argument. So the qualitative claims held spectacularly (zero ripple effects, zero properties, no feature-corresponding operations, design style unchanged for two years) while the quantitative thresholds were approximations he adjusted in his own favour, and says so out loud. Use them as **one-way detectors** and as directional guidance, never as certification — and never quote this project as evidence that 0.7 holds in the wild.

> [!question]- 12. What is green-green-green, and why does a single two-word core use case make factoring harder rather than easier?
>!
> [!summary]- Answer
> A grading of newness: single green = new system; double green = new system on technology you must invent; **green-green-green = the use cases themselves don't exist** — no prior art, no users, nobody to ask. The input here was single core use cases of two words, one being "survive." Intuition says fewer use cases means easier; he says the opposite. With 2–5 core use cases the space is bounded, but with a **single highly abstract** one *"there is literally an open-ended number of variations"* — so the **next level down becomes the real use cases**, and the team had to invent ~100 activity diagrams out of whole cloth before detail design even started.

> [!question]- 13. Why is self-similarity on this project a correctness requirement rather than a design preference?
>!
> [!summary]- Answer
> Because branching by context does not survive the scale. Every node from continent level to appliance runs *"exactly, exactly, exactly the same code"* — *"the system doesn't know it is the root of the world or it's actually a light bulb."* With scale spanning an appliance to a continent and *"every deployment completely and utterly different,"* he states it flatly: **"if you start doing it with if and else, you will fail. There is no way of building this kind of a system using if and else."** Note this is the *self-similarity* sense of "fractal" — distinct from the program→system→platform→fractal *size* totem pole used to explain scale-relative thresholds.

## Related

- [[MOC — Course Overview]]
- [[Modules/Introduction to Service-Orientation]]
- [[Modules/Design and Architecture]]