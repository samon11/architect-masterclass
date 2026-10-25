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

> [!summary] Module 6 — The IDesign Method
> The core architectural design methodology: volatility-based decomposition, universal design principles, the architect's challenge, axes of volatility, and practical design validation.

> [!warning] Numbering
> This is **MOC Module 6**, but this note's frontmatter and tags say `module-5`. The vault's numbering is off by one from Module 4 onward — full table in [[Modules/Introduction to Service-Orientation#Numbering Discrepancy]]. Transcripts for this module use `module-5` to stay tag-consistent with this note.

> [!note] This note was empty until 2026-10-21
> For the vault's whole life this file was 435 words of bare stubs. [[99-Resources/Transcripts/The IDesign Method|The IDesign Method]] is the first real payload it has received, and it fills three sections: `The IDesign Method`, `Classic Mistakes`, and `Design Validation`. Everything else remains awaiting the SSM/architecture session.

## Topics

- [x] The IDesign Method
- [x] Classic mistakes
- [ ] Volatility-based decomposition
- [ ] Universal design principles
- [ ] The architect's challenge
- [ ] Axes of volatility
- [ ] Design example
- [ ] Volatility and the business
- [ ] Open and closed architecture
- [ ] Structure with clients, managers, engines, resource access and utilities
- [x] Design validation
- [ ] Containing changes
- [x] Design Don'ts

## Notes

### The IDesign Method

- [Transcript](../99-Resources/Transcripts/The%20IDesign%20Method.md)

> [!note] First real content in this note
> Everything below comes from [[99-Resources/Transcripts/The IDesign Method|The IDesign Method]], recorded 2026-10-21. It is a **meta-lecture about the method itself** — its philosophy, its mechanics, and its accountability model — plus one concrete technique (the vertical slice). It is **not** the SSM/taxonomy lecture; the word *service* does not appear once in 6,370 words.

#### The Anti-Fluff Thesis

His headline sentence, which he then dismantles word by word:

> [!important] "The IDesign method is a simple and effective analysis and design technique."
> *"Let's parse that sentence. Let's parse 'simple'."*

The inversion is the whole point:

> [!important] "There is less to the method than meets the eye. **There's less to it, not more to it.**"

People inflate methods; they never find hidden depth. And why:

> [!danger] "You're going to try and fluff it up… because **you're standing on nothing.**"
> *"Recognize your own depravity, your own incompetence, recognize that you had no idea what you were doing so far, and do something about it. **But that's hard.** So instead, you fluff it up."*

> [!quote] "The average software team is nothing but **a group of quacks holding hands, chanting some mantra around a cauldron of boiling pus**. Why? Because you got nothing."

He makes the same point three escalating ways: a 1970s South American general who has just concluded *"the 17th military coup of the week,"* chest full of ribbons — *"**Because there's nobody home**"*; a Jedi Knight in a robe who exudes more authority than the whole medal rack; and centuries-past coronations taking **three days of ceremony** to legitimate *"a hereditary despot whose genes are probably worse off than anybody else."* He refuses the softening: *"No, no, no, no. **I meant it exactly like I said it.**"*

#### It Is a Machine — and You Are the Input

The word *analysis* gets the ridicule: *"You've got a bunch of coins over here. You got design over there. How do you go from here to there?"* → **the analysis fairy**: *"Is the analysis fairy leaving your notes under the pillow a good idea?"* It is a **design** technique, not a magic transfer.

> [!important] "Emphasis is *technique*. It's literally a mechanical approach for design. **It is literally a meat grinder. You feed into it ingredients, you crank the handle, the design comes out.**"
> Operative word: **"mechanized"** — *"a highly, highly deterministic design effort."*
> Immediately qualified: *"Of course, if you feed into it garbage, garbage will come out."*

The objective:

> [!important] "The objective of the method is to **remove design and technology as a risk out of the project**."

Which yields an uncomfortable claim — design and technology are *technical solutions for technical problems*, and *"every technical problem has a technical solution"*:

> [!danger] "**If there is a solution, there is no excuse for failing.** No bridge should collapse because the engineer did not put enough steel in the bridge. No airplane should crash because the wings were not strong enough."

He keeps that honest with a counter-case: the pilot flying into the mountain, where **Lufthansa** overrode a psychiatric evaluation for staffing reasons. *"Everybody's going to die. But that wasn't a technical problem. It was an **integrity problem, an honesty problem, an accountability problem.**"* And the sting: *"I didn't hear about anybody in Lufthansa going to jail."*

> [!important] The pivot: "If your management is not committed to quality, you are going to fail. But you know what? **It's not a technical problem.** … **It's a conviction problem.**"

#### Runtime Behavior — the Architecture Trick Question

His standing design-review opener is a trick question he never explains:

> [!quote] "**Please show me the architecture.**" … *"Now like all my trick questions, it never sounds like a trick question."*
> He wants to see **your interpretation** of what architecture is.

What they show him is a block diagram with pictures of customers and servers. His verdict: **"That is not an architecture, that is a giant block diagram"** — *"it's a static image, while the system is by definition dynamic."*

The body-decomposition thought experiment: burn you, run a mass spectrometer, dump six litres of water, potassium, fat, sodium, phosphorus, protein and magnesium into a vat, **heat it to exactly 36.9 °C**, stir. *"But all the ingredients are there"* — and still no you.

> [!important] "**You are not the static composition of your composing elements, you're the dynamic composition of your composing elements.**"
> Therefore: *"Runtime behavior is not an afterthought, it's not something that emerges. **It's a result of specific guidelines and deliberate design effort.**"*

#### The Method Is Fast — Deliberately

> [!important] "The method doesn't take long to execute. **Three days will be more than enough. If you're doing five days, you're already too much.**"

He pre-empts the objection (*"this system is going to be in production for 10 years, let's spend another five days"*) and rejects it:

> [!quote] "**The time crunch is a facet of the method. It's absolutely essential.**"
> Human nature: two-hour meetings where *"two minutes in, you already know what should be the outcome, but you have to wait another 118 minutes for everybody to catch up."* Do it standing up — or *"outside on one leg in the rain"* — and it won't take two hours. **"When you put the screws on people, you force them to focus, to prioritize, and to deliver."**
> And the animal underneath: *"Why? **Monkey nature.** We've been monkeys for 100 million years… 23 and a half hours a day the monkeys are arguing and throwing feces. It's not in our nature to focus, to prioritize, to deliver. You have to overcome it."*

The larger reason is **design gold plating** — see [[#Classic Mistakes]].

#### Communication — "Architecture Survival"

> [!important] "**I call it architecture survival.**"
> Three things that do **not** count: a good design *"in your head"*; a good design *"on a whiteboard with a big DUNNO arrow next to it"*; a design *"in a document that nobody ever reads."*
> The one condition: **"It's only a good design if it survived through development without being butchered, ending up as working bits on customers' machines."**

How butchering happens: *"Why do we need all these layers? Let me just connect from the front end direct to the database, bam, see it, compile, ship it. I mean it works."*

The bar for developers is deliberately lower than you'd expect: he does **not** expect them to produce the correct design — *"that would make them architects"* — but *"I do expect them to be able to understand what you're calling for, to value it, and then **follow simple instructions**."*

Two levels must be transmitted:
1. The **general interaction rules** — *"these components are allowed to do this, I'm not allowed to do that."*
2. The rules **in the context of your specific component type.**

The construction-site model: *"I do expect the electrician to know the electrical code, and the plumber the plumbing code. But the architect says, run the power line here. Oh, okay, that's what the sign is calling for"* — and the tradesman runs it **to code**.

> [!danger] The verdict he gives architects who complain: *"Many times architects pull me by the sleeve and say, I gave them a good design and they butchered it. **They butchered it — you failed. You failed to have them value what you're calling for. You failed to communicate.**"*

The second channel is **between architects**: *"Nobody knows everything on every system. You need to get constructive criticism from other architects."* → **"Engineers communicate based on design diagrams."** A mechanical engineer doesn't *talk* about the widget, he sends the **AutoCAD** diagram. Because of the method's conventions, *"all if you do is send the diagrams to somebody who understands the method, immediately they give you feedback"* — evidenced, he says, **hundreds of times on alumni**: *"a perfect stranger who knows nothing about the domain, the business, the developers, the technology, gives you very valuable feedback instantly."*

#### Not a Silver Bullet — Full Accountability

> [!quote] "However, the method is not a silver bullet. First of all, **there are no silver bullets.**"
> The sports-car proof: drive a beautiful sports car into a tree — the tree's fault? the car's? his? **No, yours, because you are driving.**

> [!important] "You can never turn off your brain and delegate your thinking to something else, be it a methodology or process or convention. **All of these things are supposed to help you think, but they cannot replace the thinking.**"

And the meta-warning against formula-chasing: *"'So you always do it like this, right?' **No. No, you don't. You're already wrong.** … Reality is subtle. Reality is complex. There's usually, but it depends, and sometimes. What can you do? That's life."*

> [!danger] **The accountability triple:** "You are responsible for getting the right use cases. You are responsible for having the right decomposition. **You are 100% liable for getting it wrong.**"
> *"The method does not take away the need to be creative."* Get the decomposition wrong and *"you can then use all the fancy method words and call everything right, **it's still garbage.**"*
> Humility clause: *"The method does provide a good starting point. **You need to stand on the shoulders of giants.**"*

#### The Rhetorical Centre — Design Process vs Development Process

The argument the whole lecture is built to land:

> [!important] "How many years have you spent arguing passionately about development process — Agile.D, Scrum.dot, Lean.dot, SOLID.dot? **How much energy did you spend arguing about your DESIGN process? And the answer is zero. Hardcore zero.**
> What's the point of arguing about development process if you haven't discussed your design process? It's pointless."

Closing line, closing the loop on the meat grinder: **"So the method is a design process. Now, like any process, if you feed it garbage, you get garbage out. That doesn't go away."**

*(The cargo-cult critique itself is already in [[Modules/Project Planning#Agile Criticism: The Voodoo Metastasized Religion]] — same argument, different words. Cross-link.)*

### The Vertical Slice

The concrete technique of the lecture. He explicitly parks it: *"We're not going to talk more about the vertical slice. That's the only bullet I have on it… we're going to spend all of today on some other things."*

#### Why It Exists — Context, Not Intelligence

> [!quote] "The method produces a lot of design artifacts. **20, 30, 40 design diagrams is common** in our IDesign method project."

Hand those to your team and *"you are going to get a blank stare."* The insult, undelivered-apology-free: *"Your developers are dumber than the dumbest construction monkey."* Any site with a crane has a vinyl-covered table and 40 diagrams, and *"some gorilla with a hammer in his belt that barely finished high school knows to pick up the diagram… Your developers cannot even do that."*

Then the analogy that reframes the insult completely — **the caveman and the microwave**: push leaves into the power cord *"so the microwave can eat the leaves."* *"When things are out of context, you make these crazy conjectures."* He does **not** think the caveman is an idiot: *"You would not survive one day in an environment of a caveman."*

> [!important] "You have to put it in context. And **the context of developers is code. They need to see it first in code to understand what is going on.**"

#### Mechanics

The system has layers; inside layers you have components; **you slice it**. *"A good slice is relatively thin. **Don't go for a big slice.**"*

**The components in the slice do absolutely nothing.** Partly because you haven't designed yet, *"but that's not the point."* The point is the wiring is real — layers calling layers, and *"all the design aspects — security, transactions, so on — are actually done according to your architecture."* Only the work is stubbed. That is what proves the **architecture** rather than the code.

> [!quote] "**Now you demystify the diagrams.** You see this block over here, that's actually this attribute over here. See this line over here, that's this portion from the framework."

#### Three Purposes

| Purpose | What it does |
| --- | --- |
| **Context / communication** | Turns 40 abstract diagrams into attributes and framework portions the team can point at. Fixes a context failure, not an intelligence failure. |
| **Design discovery** | *"Don't kid yourself that you'll be able to get the design right in the first pass. **That never happens.**"* Attempting the slice reveals *"this is too big, split it"* and *"we never use that one, throw it away."* → **"It doesn't have to be perfect, and it can never be perfect. All it has to be is good enough."** |
| **Early stress test** | *"One week into it I must know if there's anything in this architecture that would preclude me from meeting my throughput, scalability, availability, responsiveness, performance goals."* |

The demolition of late performance testing:

> [!danger] "What's the point of doing an activity that has a **Boolean outcome** that regardless of the Boolean outcome **you're doing the same thing**?"
> **Rule: "The only way to meet the performance goals at the end of the project is to meet performance goals throughout the project, including at the beginning."**

> [!note] Different from sketching, though the same thesis
> [[Modules/Service Contract Design and Factoring#Rule 8 — Sketching, and Validation as a Factoring Technique|Rule 8 sketching]] is a **single code sketch** (one C#/Java interface) that validates **contracts**, aimed at the architect's own thinking. The vertical slice is a **thin runnable end-to-end slice** across all layers that validates **architecture**, aimed at the development team. Both rest on *validate early by building something* — keep them separate.

#### The Mini-Clinic Confessional

He used to cram five days of material into four (*"Thursday evening there was just a pile of corpses around me"*), freeing Friday for a **mini-clinic**: the audience describes their own system, he demonstrates how to interview a customer, *"steals the core use cases"*, does the architecture, and **live builds a full vertical slice of the entire system, soup to nuts, in one day** while answering questions.

Result: *"Amazing. Okay, we have no doubt that you know how to do it. **Me? Never going to happen.**"*

Why he stopped: *"You can't jump from zero to a hundred overnight. Being good at anything is a journey… it's **10,000 hours**."* Two reasons — it was **disparaging**, and *"this is not something you can learn by seeing somebody else doing it. **You have to go through the motions yourself.**"* (The second reason is the same conclusion reached independently in [[99-Resources/Transcripts/Contract Factoring in Practice#6. How to Learn It|Contract Factoring in Practice]].)

### Classic Mistakes

- [Transcript](../99-Resources/Transcripts/The%20IDesign%20Method.md)

> [!note] Partial coverage
> These are the mistakes this lecture names. Volatility-based decomposition, axes of volatility and the rest of the note's topics remain unrecorded.

#### Design Gold Plating

> [!danger] "If you think code gold plating is evil, **you haven't met design gold plating. Design gold plating is disastrous.**"

Parkinson's Law means extra time becomes extra work — so the fix is the time crunch, not more diligence. *(Code gold plating and Parkinson's-Law padding are already in [[Modules/The Architect#Architects and the Business]] and [[Modules/Project Planning]]. Here it is a **design** failure caused by removing the crunch — same law, new application.)*

**The pendulum effect** — why minimalism matters more than it looks:

> [!quote] "For you it's just another box, for somebody else, two years of effort."
> Therefore: *"You want to go with the **most minimalistic, bare-bones design you can possibly get away with**."* Which is against your grain, because you'll fluff it up. **"Less is more when it comes to architecture."**

#### Glorifying Evolutionary Design

> [!danger] "Design is not time consuming if you know what you're doing. Do most people know what they're doing? **No.** Therefore they need an infinite amount of time, and then they **glorify their incompetence** by saying, oh, it's evolutionary design."
> *"Nobody designing an airplane or a building or a laptop allows the design to emerge."*

#### Bubble Sort of the Design Decision Tree

The analytical centerpiece — the vault's first formal model of design ordering, and the root cause of analysis paralysis: *"some **downstream** decision is going to invalidate an **upstream** decision. And then you have to do it again and again and again."*

**The laptop example, in full.** Naive path: CPU → *"give me a fast one, I7, make it i9"* → the i9 gets hot, and *"the heat flux out of a modern CPU is **hotter than the surface of the sun**"* → fan → airflow → minimum box thickness → monitor size (15", wide) → box dimensions → battery in the back → done.

**Wrong**, because *"this was supposed to be actually a travel laptop,"* where the dominant decision is **weight** — and the heaviest component, the battery, was scheduled **last**. If it blows the weight budget it **invalidates every earlier decision**.

His rationale for why weight dominates: he doesn't intend to use it (*"If I have to use it, I'll be thankful that I actually have a laptop"*; the replacement is waiting at home), and he'll haul it across airports and hotels — *"by the time I'm done with it, I would have moved tons."* So: **"anything over two pounds, I stop reading."**

**Corrected chain:** weight budget first (battery ≈ 80% of it — *"I'm not selling a battery, I'm selling a laptop"*) → battery mass ⇒ capacity → power consumption, whose largest consumer is the **fan** (mechanical, *"little blades and sparks"*; everything else including the screen is milliamps) → fan **duty cycle** (say 50%) → desired runtime (two hours) → allowable fan power → the fan's rated **heat flux** → *then* pick **the hottest CPU that still fits under that heat flux**, at ~80% not 100%. **"Done this way, the last thing we do is a CPU, not the first."**

> [!quote] "What you're doing now is **bubble sort of the design decision tree**. And the complexity of bubble sort is **n²**."
> Twenty decisions → **roughly 400 iterations, or specifically 400 meetings.** *"Do you think any design team has time for 400 meetings? How about 200? How about 100? How about 40?"*

**The endgame:** *"At some point the boss is gonna look at that and say, these monkeys have no idea what they're doing, and put them out the door and say design is over, start coding. And now you're going to manufacturing with a **half-baked decision tree**"* — discovered *"at the worst possible time, once you've already put the code in."*

#### It Is a Tree, Not a String

The root decision for a laptop is **market**: gaming laptop → **graphics card**; travel laptop → **weight**; desktop replacement → **CPU, hard drive, monitor**. Each has a different subtree.

> [!important] "**Every system has a design decision tree.** If you're approaching it blind you will invalidate some upstream decision."
> **"The first act of wisdom in designing any system — or anything — is recognizing your own design decision tree."**
> What the method does is *recognize* it: *"Decide on this before that, on that before this. Do it in this order, you'll spend the least amount of energy designing things."*
> He labels his own model honestly: *"a somewhat cartoonish view… but good enough in principle."*

### Constraints — the Second Lever

- [Transcript](../99-Resources/Transcripts/The%20IDesign%20Method.md)

> [!quote] "The other thing the method lets you do is **increase the level of constraints on the problem**."

| Problem type | Example | Difficulty |
| --- | --- | --- |
| **Blank canvas** — the worst | *"Build me something. What should you do? You figure it out."* | *"Probably infinite ways of getting it wrong, one way of getting it right. **Do you like the odds? Infinite to one?**"* |
| **Fully constrained** — the easiest | *"Don't do this, do that."* | *"You spend no time designing anything… It is what it is. We're done."* |

Real life is gray — constraints are implicit, explicit, or **false**, and you must go discover all of them.

The part everyone misses, and the intuition inversion:

> [!important] "The more constraints you have, the easier the design gets. **It's exactly the opposite.**"
> People complain *"we can't do this and we have to do that"* → *"Why are you complaining? Don't do this, you have to do that. **You're done.**"*

> [!quote] "**My best design tool is putting constraints on the problem.** …It's like running the design through a funnel and the design converges, emerges immediately."
> And the method automates it: *"When you decide on this, it implies this and this and this. And those things imply that, and you're basically done. It's almost instantaneous. **That's actually the mechanical nature of the machine.**"*

### Design Validation

- [Transcript](../99-Resources/Transcripts/Contract%20Factoring%20in%20Practice.md)
- [Transcript](../99-Resources/Transcripts/The%20IDesign%20Method.md)

> [!important] "You need to know — **know with a capital K** — if this design is going to hold water."
> **"Engineers validate their design. And you're going to have to do it here as well."**

> [!quote] "Most people don't ever bother validating their design. They draw a few lines and hope for the best. Let me point out that **hope is not a good strategy.** Nobody designing a bridge says, well, I hope the bridge is going to hold the weight."

**Why the timing is brutal, not optional:** within roughly a week people are tasked and start building, so *"you're only going to have **a blink of an eye** to get it right and to know if it's going to hold water."* This is the clock behind the three-day limit — not a stylistic preference.

The two contributions this lecture makes beyond [[Modules/Microservices Development Process#Requirements Design Validation]]:
- the **timing constraint** above (one week, blink of an eye);
- the **bridge/hope** framing, which is the same theorem the Four Guarantees note already carries, in new words.

And the reframe from [[99-Resources/Transcripts/Contract Factoring in Practice|Contract Factoring in Practice]]: **"Design validation is a world-class contract factoring technique."** Validation is not a final act — trying to validate *produces* factoring, because the use case turns out incomplete, wrong or duplicated, so you change it, which uncovers something else, so you validate again.

### Volatility-Based Decomposition

- still empty — and [[99-Resources/Transcripts/Functional Decomposition|Functional Decomposition]] did **not** fill it.

> [!info] This is the other half of a session whose first half is now recorded
> The 2026-10-22 lecture is the **"what not to do"** half, and it ends exactly at the hinge: *"We have nailed to the ground the what not to do. Therefore, now we discuss the what to do."* **The word "volatility" appears zero times in those 10,471 words** — as do `axis`, `axes`, `encapsulation`, `cohesion`, `information hiding`, `Parnas`.
>
> What belongs here, and where it stands:
> - - **The positive principle itself — unrecorded.** Not one formulation of it appears anywhere in the 23 recordings so far.
> - **The [[#Axes of Volatility]] — unrecorded.**
> - The *anti-pattern* inventory is now complete: see [[#Design Don'ts]]. That is genuinely useful, but it is the negative half only.

### Universal Design Principles

-

> [!note] One candidate, from [[99-Resources/Transcripts/Functional Decomposition|Functional Decomposition]]
> *"I can prove to you that functional decomposition is the wrong way of designing any system **without using a single software argument.**"* — then the first law of thermodynamics. That is the *form* of a universal principle: a rule you cannot trade away, because it is not about software. See [[#The Physics Argument — No Software Premise At All]]. Same shape as [[Modules/Service Contract Design and Factoring#The Closing Thesis — Compliance Asymmetry|The Closing Thesis — Compliance Asymmetry]].
>
> The list itself is still unrecorded. Not filled.

### The Architect's Challenge

-

> [!note] Partially illuminated, not filled
> [[99-Resources/Transcripts/Functional Decomposition|Functional Decomposition]] never uses the phrase, but it is one long answer to a related question: **why do competent, informed people reliably produce bad designs?** His answer is not "they're careless" — it is *"human beings cannot resist the allure of the free lunch"*, and **"the nature of the architecture forces them."** See [[#Four Nails]] and [[#The Physics Argument — No Software Premise At All]]. Not filled.

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
> **Still undelivered — re-parked a FIFTH time.** The 2026-10-22 [[99-Resources/Transcripts/Functional Decomposition|Functional Decomposition]] lecture is the closest call yet and still a miss: **`client` appears 24 times, and every single instance means "the caller / the UI"** — the web page, the mobile device, the desktop, the browser. It is the *caller* sense, which is at least the first node of the taxonomy — but the taxonomy is never named. `manager` 1, `engine` 3 (all three are an **aircraft** engine, in the jumbo-jet fuel story), `utilit` **0**, `resource access` **0**, `SSM` **0**.
>
> Prior attempts: [[99-Resources/Transcripts/Service Contract Design|Service Contract Design]] (parked it), [[99-Resources/Transcripts/Sample Project — Resilient Energy|Resilient Energy]] (*"the classic thing we're going to discuss tomorrow is inside each node"*), [[99-Resources/Transcripts/The IDesign Method|The IDesign Method]] (`service` 0 times), and now Functional Decomposition. The only structural language anywhere remains generic: *"the system is going to have layers. Inside layers you have components, you slice it."* **Layers-and-components is not the four-node taxonomy.**
>
> **This is now the most strongly primed reference in the vault.** The next recording that says *managers*, *engines*, *utilitities*, *resource access*, or *SSM* closes it. See [[Modules/Service Contract Design and Factoring#Sample Project]] for the v1→v4 contract evolution it is meant to explain.

### Containing Changes

-

### Design Don'ts

> [!info] First real content — from [[99-Resources/Transcripts/Functional Decomposition|Functional Decomposition]] (2026-10-22, 10,471 words, ~70 min)
> This is the **"what not to do" half** of the Volatility-Based Decomposition session — the largest single anti-pattern argument in the vault, and the first note here that argues *decomposition itself* rather than a technique inside a design.
>
> **Note the split.** `volatility`, `axis`, `axes`, `encapsulation`, `cohesion`, `information hiding` and `Parnas` all appear **zero times** in this lecture. So it fills *Design Don'ts* and nothing else. The recording ends exactly at the hinge: *"We have nailed to the ground the what not to do. Therefore, now we discuss the what to do."*

#### The Method's First Move Is a Prohibition

> **The method actually starts by discussing what not to do.** … So we have to spend some time discussing what **not** to do, and only while you say "I can't take it anymore," we're going to discuss the what to do.
>
> **The method says: avoid functional decomposition.**

That ordering is the first architecture lesson, and it is about *how an architect learns*, not about decomposition. He is explicit that authority will not work on you: *"I can talk about the perils of functional decomposition till I'm blue in the face. You're still going to do it… that's the only thing you've ever seen. That's the only thing you know how to do."* So the method does not begin by teaching the right answer. It begins by **removing your confidence in the wrong one.** Compare [[Modules/Service Contract Design and Factoring#How to Learn Contract Factoring|How to Learn Contract Factoring]] — same pedagogy, opposite direction: there you learn by *doing* factoring badly; here you learn by *seeing* your own design in the anti-design.

#### The Definition, and the Verdict

> **Architecture is always and everywhere an act of decomposition.** You take a big [system] and you break it down into smaller building blocks — components, modules, services.
>
> **Functional decomposition is basing the decomposition on the required functionality of the system.** If the system needs to do A and B and C — you have an A block, a B block, a C block. If you need to do invoicing and billing and shipping: invoicing service, billing component, and so on.

> That is functional decomposition, and **that is death.** If you have functional decomposition, the project has already failed. **Past tense.** Before you hired the first developer, before anybody wrote the first line of code.

And the sentence that sets the shape of everything after it: *"I'll start poking [holes] and driving nails in its coffin. **Every one of the following nails is going to be enough to kill it. However, I will save the best nail for last.**"* These are **independent** fatal findings. Not a cumulative case.

#### Four Nails

| # | The nail | His words |
| --- | --- | --- |
| **1** | **Business logic lands in the client — and the architecture forces it there.** The client decides *A, then B, then for this customer D instead of C*, and that ordering **is** business logic. So every new client front-end duplicates it. | *"Every developer out there knows: do not pollute the client with business logic. **100% of developers are doing it.** Why? **It's the nature of the architecture. It forces them.**"* |
| **2** | **It is secretly *temporal* decomposition — and this is what kills reuse.** | *"You don't do A, B, C. You do A **and then** B **and then** C. So built into the very fabric of B is: it is called after A and before C."* → *"As soon as you lift the B from this system, **the A and the C are hanging off it.** Which means **kiss goodbye, reuse.**"* |
| **3** | **It pushes you to both ends of the cost curve at once** — an explosion of 300 blocks, or a few bloated monstrosities. Both are the canonical "what not to do." | *"Functional decomposition **always pushes you to the edges of the cost curve.** And no project can survive a non-linear cost."* |
| **4** | **It maximises points of entry** — three places to secure, scale, and keep available. | *"A good design should **minimize** the number of points of entry — arguably, just one. But functional decomposition **maximizes** [it]. Is the design that maximizes the number of points of entry a good design? **Probably not.**"* |

> [!note] The form of every one of these arguments — worth copying
> He never cites a framework, a paper, or a book. Every nail has the same three moves: **(1)** state a design invariant the room already accepts, **(2)** show the decomposition violates it, **(3)** ask the question and let the room answer. Nail 4 is the purest case — "minimize points of entry" is not controversial, and the violation is then obvious.
>
> And note who is *not* blamed. **Not** the developers — *"every developer knows do not pollute the client"*. The indictment is always of the decomposition. This is the exact inverse of [[Modules/Microservices Development Process#CMM — Capability Maturity Model|CMM]], where the individual hero saves the project. **Here the architecture dooms the individual, by making the violation inevitable.**

Nail 2 is the one to hold onto, because it is the only one that costs you the *mechanism* rather than money:

> **A block that silently requires a predecessor and a successor is not a component. It is a segment of a script.**

#### The Due-Diligence Artifact — "The Three Gas Giants and the Asteroid Belt"

The **only real production codebase** he has ever put in front of us — a due diligence on a company being acquired, on a contract where *"the sum of money had seven zeros in it."*

His procedure, verbatim:
- **Come clean first.** *"Show me all the skeletons in the closet, because **I will find every skeleton.** If I find something you didn't show me, I will have to conclude you're either trying to hide it from me or you had no idea. Either way it doesn't look too good for you."*
- **5 a.m. and 9 p.m.** *"I come to the office at **5 a.m.** and see who is working. I go to the **parking lot at 9 p.m.** and see who is working — and why."*
- **All code to my laptop. Stopwatch.** *"If you spend the whole day looking under the carpet for pieces of code, is this a good company?"*
- **Build it on my machine.** *"If it takes an act of God and **225 manual steps** to build the system, is this a good system?"*
- **Full-blown cyclomatic complexity analysis of everything.**

What it found — three surviving labels:

| Artifact | His expectation | What the metrics showed |
| --- | --- | --- |
| `main form` | a view | **"How many zeros are in `main form`?"** |
| `form setup` | a setup routine | *"Do you know what it takes to **stand up** this beast?"* |
| `resources` | *"a long table of strings or image references **with complexity of one**"* | *"Do you know what it takes to **change one string** here?"* |

> In my mind, **the client should be just a pretty face and an empty conduit to the system.**
>
> **I call this diagram "the three gas giants and the asteroid belt."** They got to enjoy the best of both: a few hideously complex components **and** an explosion of little things. What's not to like? Really. What's not to like?

**And the architect's reply:** *"I think you have functional decomposition on your hands."* — the architect had read Juval's material, knew where it was going, sighed: **"Ha. I don't think so."** — *"**I know so.** What do you think was my recommendation? If this was your money, would you like to buy this system?"*

> [!tip] "I don't think so" is the reason the anti-design exercise exists
> That is not a technical rebuttal. It is a man who knew the diagnosis and did not want it. **A diagnosis delivered by authority gets argued with.** Which is the whole lesson of the exercise below — and of [[Modules/Service Contract Design and Factoring#Rule 8 — Sketching, and Validation as a Factoring Technique|Rule 8]]: make the architect *produce* something checkable, because a produced artifact cannot be waved away the way a judgement can.

#### The Ratchet — How Services Hollow Out

> The moment you have the client stitching up the services, you always build the client with business logic. In fact, **it creates this ratchet motion — click, click, click, click, ratchet.** … So in no time at all, **all the so-called business services shrink into being do-nothing, pass-through services, and everything is in the client.**

> [!warning] This explains the anemic contract, from the other end
> [[Modules/Service Contract Design and Factoring#Rule 8 — Sketching, and Validation as a Factoring Technique|Rule 8]] warns against contracts that are one thin method per table. This is the *mechanism* that produces them. A ratchet moves one way only: nothing ever pushes business logic back into a service, because every step that de-duplicates the client also empties a service. **It is not drift and it is not laziness — it is a one-way mechanism, and each individual step is defensible.** Watch for it when a service you designed rich starts losing behaviour.

#### "Then the Services Will Call Each Other" — the n²

The obvious repair, granted and then destroyed. **A** must receive parameters it does not care about in order to call **B**, and must contain the *anti-B* if B fails. **B** likewise for **C**. And then **A** is bloated by **C** as well, because A must supply what B needs to call C — and if B fails to undo C, *"the last recourse is for A to undo the C."*

> **This is just three components. What if you have 17?** Let's assume every hop adds **one unit** of bloat to the predecessors. **It does not, but suppose.** How does 1 + 2 + 3 + 4 behave? **It behaves like n².** … And not assuming just one unit — what if it's ten units? **Good luck with that.**

> [!caution] He disclaims his own assumption, in the same breath
> *"It does not, but suppose."* **The n² is a floor, not an estimate.** Take the most generous assumption possible and you still get quadratic growth. Do not cite "n²" as a measured result — it is a lower bound under an assumption he immediately withdraws.

And then someone presses `async`, and the chain becomes: *"Do you really have three separate services here, or a **giant clique of doom**?"*

#### The Physics Argument — No Software Premise At All

> **I can prove to you that functional decomposition is the wrong way of designing any system without using a single software argument.** … **The first law of thermodynamics states that you cannot add value without sweating.**

He is scrupulous that this is an abstraction, and says so: *"I'm a bit abstracting the whole calculus-and-dq/dt-and-such, but just **bold** strokes. **Why is this the first law of thermodynamics? We do not know.** There is nothing in Newtonian physics that says it. However, we do know that **on this side of the big bang, this is the way the universe behaves.**"*

> Now suppose I give you a requirement spec: system should do A, B, C. And you say — **no sweat.** A block, B block, C block. **And that's the problem. You said "no sweat."** Because now you endeavour to **cheat the first law of thermodynamics.** … **This can never happen. It's impossible.**
>
> **There is no free lunch.** … But functional decomposition lets architects **pretend that there's a free lunch.**

> It never ceases to amaze me — people say "I should be a highly paid architect," and then you spend **easily a few lines, a few boxes — bam, no sweat** — and that's the architecture. Well, **if this is so easy, why do you think you should get the high paycheck?**

**And the proof that this is not an intelligence problem:**

> For **thousands of years**, people tried **alchemy**. The alchemists commanded a king's ransom. They were the most expensive people in the kingdom. **They produced exactly zero results. It has never worked even once.**
>
> **And this has nothing to do with intelligence. Who was the greatest alchemist of all time? Isaac Newton.** Newton spent **two years** on *Principia Mathematica* — the book that single-handedly ushered in the age of reason and evidence and science — and **22 years** trying to figure out the philosopher's stone.
>
> **Are your developers smarter than Isaac Newton?** … **Don't argue with me — argue with Lord Kelvin.**

> [!note] Why this is load-bearing, not decoration — and it belongs in [[#Universal Design Principles]]
> Everything before it was a *demonstration*, and demonstrations are negotiable: "not in my system." This claim is different in kind. It says functional decomposition is **precluded**, not disfavoured:
>
> > **It's not an accident that it's not working for you. It *cannot* work for you.**
>
> That is the move of a **universal design principle** — a rule you cannot trade away, because it is not about software. Same shape as [[Modules/Service Contract Design and Factoring#The Closing Thesis — Compliance Asymmetry|The Closing Thesis — Compliance Asymmetry]]. So this is the only part of the lecture that arguably contributes to [[#Universal Design Principles]], which stays formally unfilled.

#### The Two Houses

**House 1 — functional.** Cooking, sleeping, parking as separate blocks. So: a microwave in mid-air on a scaffolding, wired to the grid, a little pantry, a little roof. *"Sprint 1.0 is done. Cooking is done. High five."*

> **Is cooking really done?** … **Why did you lie to the customer?** … You deliver the skateboard. **The customer wants a car.**
>
> Anyone who tries to build your house this way, you're gonna find them. Because **they are clearly insane.** But in software, it's called [agile]. **How could it be that something so clearly insane is a best practice?** — It's because **in your world, the lunatics have taken over the asylum.**

**House 2 — domain. And it is worse.** *"If I had to choose between this and the previous, I choose the previous."* Building the kitchen is a proper job: foundation trench, rebar, bolts, cure, walls, bolt it down, connect **power, water, gas, sewer discharge**, ducts, stucco, drywall, roof, cabinets. **Milestone 1.0 — kitchen done.**

Then you add a bedroom, and he walks it in full. Bust the stucco. **Unbolt the kitchen. Lift it off the foundation on hydraulic jacks.** Disconnect all four services. Jack up and dump the old foundation. Pour a **new continuous foundation** with the kitchen's bolts **"at exactly, exactly, exactly the same place."** Lower it back. Reconnect. Tear out the kitchen's drywall and cabinets to route utilities *between* the rooms. Re-hang. **New continuous stucco across both** — *"nobody wants to see a big ugly crack in the middle of the whole thing."* **Tear the roof off** and re-roof both. **Milestone 2.0 — bedroom done.**

> **One** — an exterior wall is now an **interior** wall: security, insulation, and a bunch of other things.
>
> **But the real problem** is that when you said bedroom one was done, **the fact that you had to rebuild the kitchen was not disclosed to the customer.** And the fact that we're doing the kitchen the second time around was **way more expensive than doing it the first time around** — that is also not disclosed.
>
> **How many more times can you lift and shift the kitchen before all you have is a radioactive pile of construction debris that you're shifting around?**

> [!tip] The cost of the *second* change — a new idea in the vault
> Every other cost argument here is about complexity at build time. This is about **rework across milestones**, and it separates two costs the analogy makes distinct: the **physical** (lift the kitchen, repour, re-roof) and the **reporting** (the customer was told "bedroom done" and never told the kitchen was rebuilt, at higher cost, twice). He names the second as *the real problem.* See [[Modules/Project Planning#The Shallow S: Shape of a Viable Plan|Shallow S]] — the same lie, different mechanism: there the burn curve is hidden; here, **rebuilt work is reported as new work.**

Plus the duplication this cannot avoid: *"at the end of every cocktail party, **all the guests end up in my house in the kitchen**"* → duplicate entertaining. *"Fall asleep in the living room"* → duplicate sleeping. *"The wife banishes me into the garage, I get lonely and hungry"* → duplicate cooking. And the things with no home: **where do you barbecue? Where do you do your taxes?** *"In no time at all, **all domains duplicate all other domains.**"*

#### The Kill Shot — Domain Decomposition Is Functional Decomposition in Disguise

This is the nail he promised to save for last.

> Now all of that is **not** the real reason why domain decomposition is a failure. **The real reason is because a rose by any other name is still a rose.**
>
> **Domain decomposition is still functional decomposition — except it's in disguise.** Kitchen is where you do the cooking. Bedroom is where you do the sleeping. Garage is where you do the parking.
>
> Since we know that **by the nature of the universe** functional decomposition is precluded from ever working — **domain decomposition is precluded from ever working. The rest are just details filling in the blanks.**
>
> And **this** is your best practice? This is the best idea you could come up with? Really? **How is that working for you?** — *Poorly. That's how it's working for you.*

> [!important] Read the boundary of this claim precisely — it is narrower than it sounds
> He never says domains are useless, or that a decomposition should ignore the business. He says **a block named after a location of activity is still a block named after a function** — so it inherits the ordering coupling of Nail 2, and no amount of careful bounded-context work removes it.
>
> That is a claim about **what the boundary is keyed to**. Keep it there. Everything he demonstrated against House 1 — the duplication, the coupling, the undefined domains — is *contingent* and a team could argue they avoided it. **The identity claim is not contingent.** If X *is* Y in disguise, every disproof of Y is already a disproof of X. **Do not argue the implementation; argue the identity.** This is the single most transferable move in the lecture.
>
> And his gloss of the initials is labelled opinion in the sentence itself: *"I think that this should stand for **deranged**, or **delusional**, or **deceptive**, or **disparaging**. **But this is just my interpretation of the initials.**"* Record the hedge, or the note misrepresents him.

#### You Never Get to Do Either One — the Legacy Problem

> **The real problem is that you will never get the chance of doing the other one.** … I just told you you're standing on clean dirt with blue sky above you. **That doesn't exist anymore, because you have some kind of legacy system.**

Why you actually rebuild: *not* because computers can't add numbers. Because **"your system has reached end of life. It is so chaotic, so sclerotic, so calcified, you cannot change anything inside."**

> **Good career advice:** anytime somebody comes to you and says *"we have to do a new system"* — **fire them on the spot. Why should we let the same group of clueless code molesters who did not know how to do a good job in the first place do a good job in the second place? What has changed? Did they grow an extra brain? Or perhaps a conscience?**
>
> **Where's the refund for the bad system?** … **The basic expectation of professionals is that they provide some kind of warranty. They own the consequences of their malpractice.** Doesn't matter if it's a doctor or a plumber or a contractor. **Where's the consequence?** — Oh, there's no consequence, because we don't really hold anybody accountable. **Now — if somebody had integrity, they wouldn't have to be held accountable.**

**And the argument that should be printed above every migration plan — you cannot ship just the A:**

1. **No standalone value.** *"Invoicing alone has no business value. Invoicing **and** billing **and** shipping has business value."*
2. **Cannot straddle.** *"You cannot do the A in the new and the B and C in the old, because **every validation rule in the old system says: where's the A?**"* And users revolt — *"why should they do double the work and not get double the value?"*
3. **So you must extricate — and that is the trap.** *"What you're about to do is a serious lobotomy. **The task of extricating the A out of an old decrepit system where you can't change anything far exceeds, in complexity and cost, the task of just building the A. You will be solving a far worse problem** — and that's exactly what you're gonna do."*

> **Even the allure of the free lunch doesn't exist. Because first of all, it's not free. And second, it's not lunch.**

And the users: *"I'm going to build a dream house out on the other side of town, and the first thing we do is build the kitchen on the other side of town. Every time we have to do something, we go to the other side of town, use the kitchen, come back."* → **"Why are you abusing your users? Is it conducive to business to abuse your users?"** *Rhetorical.*

> [!tip] Note what is *not* here — no cure, only the cost
> **There is no migration prescription anywhere in this lecture** — no strangler pattern, no seam, no composition root. That is faithful: this is the "what not to do" half of a session and it stops at the hinge.
>
> What it does establish, sharply, is *why* incremental migration is harder than any plan says: **you cannot ship an A with no standalone business value**, so the first increment silently becomes "extricate the A from a system whose defining property is that nothing can be changed in it." **This is the cost, not the cure.**

#### "Unit Testing Is Completely and Utterly Unimportant"

> **You're asking the wrong question.** … Unit testing is **completely and utterly unimportant.**

**The jumbo jet** — every component passes *"unbelievably rigorous, from here to infinity"* unit testing, assembled, and that is the only testing done: *"**Would you dare set foot in that jumbo jet?**"* No — *"there are lots of problems that have nothing to do with any single component."* His worked example is a **causal chain through the fuel subsystem**, worth keeping whole:

> The **turn** creates **G-force** on the fuel in the tank → pulls it away from the pump → **sub-pressure** in the pump → a **cavitation bubble** appears → it hits the rotor, **implodes hypersonically** → **shatters the rotor** → debris reaches the injectors → **the engine is on fire.**
>
> **No amount of unit testing can discover this defect.**

> [!example] Note what that chain requires
> A *manoeuvre*, a *fluid*, gravity, and a pump. The defect exists only **in the interaction**, under a condition no single component is tested against. The unit tests are not weak here — **they are about different things.** Which is why the fix is a different *kind* of testing, not more of the same kind.

**Regression testing is the correct kind** — the defect may involve the interaction of every component, or some subsystems, or one subsystem, or several components inside it: *"at the very end of this regression, you get to a single component."* But:

> If your design looks like this, **do you think you can have regression testing? No.** Everything is so coupled to everything else, everything duplicates everything else. **You cannot do regression testing.** So you focus on the testing you *can* do, which is unit testing. **It's possible. It doesn't mean that unit testing is important.**
>
> **You are searching under the street light** — a cognitive bias all human beings have, **focusing on the things they can do as opposed to the things they should do.**

**Essential, but unimportant** — the distinction that keeps the claim honest:

> **Did I say it's not essential? Oh yes, it's essential — but it's unimportant.** Life is full of things which are **essential but unimportant.** For example: **breathing.** What would you say to somebody who enters the office saying *"I breathed today"?* **Nobody takes pride in doing essential things. I take for granted you do it. What's next?** — **That's developers taking pride in unit testing.** What's *your* regression testing?

**The verdict:**

> Because you cannot do regression testing in a function-decomposed system — **that's another way of saying your system is untestable. And if your system is untestable, you will forever have defects.** I understand why **every system you've ever seen had chronic defects. It's unavoidable. It has to be this way. It's the nature of the design that makes it so.**

> [!note] This supplies the missing *why* for [[Modules/Microservices Development Process#Project Design|Project Design]]
> There, the architect must plan **all** quality-control activities — regression testing, the harness, the test plan, test legs, simulators. This lecture says *why that plan can fail even when written*: regression testing is **structurally unavailable** unless the design permits isolation. So the QA plan is not an activity the architect schedules — **it is a property the design must first make possible.** You cannot schedule your way out of an untestable design.
>
> Keep it distinct from [[Modules/Microservices Development Process#Quality Control|Quality Control]]. Essential/important cuts across *one activity*; QA/QC separates catching from preventing.

#### The Stock Trading Example — Nine Ways the Canonical Design Comes Apart

He switches to software because someone will say *"I'm not designing houses or airplanes."* And he picks **deliberately** the trivial, ubiquitous example:

> System should enable traders to **buy and sell stocks.** *Buy me Johnson & Johnson.* It should **schedule trades.** It should **issue reports.** It should **analyze the trade.** Client is a **browser**. Send an **email** confirming what you did. **Store it in the database.**
>
> **This is a classic, classic system — you see it in every article, and blog, and book, and vendor example.** Buy stocks, sell stocks, schedule, analyze, report; web page on top, database at the bottom. **Bada bim, bada boom, we're done.**

Nine problems, in his order:

| # | Change that will definitely happen | What it costs you |
| --- | --- | --- |
| 1 | **Fund a buy by selling other stocks** — and the price moves between the two legs | *"Which one is it? **I don't know, nor do I care. I do know that however you resolve it is business logic. And that business logic now must reside in the client.**"* |
| 2 | **Add mobile, then desktop** | *"Could we just move the code from here to here? **No, the code is different.**"* → many copies, *"all going to be subtly different — **which of course is never going to confuse anyone.**"* |
| 3 | **"Email is so 90s — can we text?"** | *"That means visiting every box and saying: **not an email, text. Not an email, text.** Oh my god, what a sweeping change."* |
| 4 | **"Move it to the cloud"** | Locally you *"pay for the license once and then **go and party on the database**"* → **chatty** calls. In the cloud *"they will nickel-and-dime you on everything — number of connections, size of messages, number of messages, the time of day, **the colour of your cat.**"* So calls get **chubby** → *"visiting every box: **don't be chatty, be chubby.**"* |
| 5 | **Relational → not** | *"Most local databases tend to be relational… I personally think it's more along the lines of **'when all you have is a hammer, everything looks like a nail.'**"* Cloud-native is *"basically a giant table"* → **the way you think about the data changes**. → *"Boss, no, we cannot move to the cloud." / "**How can we get rid of these people? Why do they keep saying no?**"* |
| 6 | **"Make it asynchronous"** — traders are paid per trade and hate a blocked UI | *"I have this **magic pixie dust**. I put `async` and **bam**, everything becomes asynchronous. Right? **Wrong.**"* See below. |
| 7 | **"Can we trade bonds? Currencies?"** — nobody holds only stocks | *"Here it says **buying stocks**. It doesn't say **buying bonds**."* → a **never-ending stream**: bonds, currencies, commodities, options, futures, derivatives, *"combination of everything in between"* — and *"every one of these things has its respective business logic"*. **"What if I'm trying to buy stocks by selling commodities? Oh my god."** |
| 8 | **Reuters offers a better feed** | *"We're not going to do it. Why? Because it means visiting every box and saying **not Bloomberg — Reuters.**"* → *"**Bloomberg, by the way, loves it. Reuters not so much.** … **The design you have here has created a vendor lock-in.** Is that good or bad? **Well, it's good for the vendor.**"* |
| 9 | **Go international** — different trading rules per locale | *"There are things which are **considered fraud on Wall Street but perfectly legal in the city of London.** Which makes every American trading house open an office in London to do their fraud there — **and every once in a while they blow up the world.**"* Deploy one system in both → *"either the people in Wall Street go to **jail**, or the people in London **lose their job**."* So you fork a New York version, a London version. Then Singapore, Frankfurt. → **"Now you're a hindrance to your own business."** |

> **And yet this is the example you will see in every book, in every article, in every conference session, in every YouTube clip. That's how bad it is.**

##### Problem 6, expanded — the three fixes `async` does not give you

The most complete `async` argument in the vault, and the only one that gives **solutions** rather than a warning. Traders are paid per trade, so a blocked UI costs them money; they ask for async; the sell-then-buy of Problem 1 now **arrives out of order** — *"you try to buy, but you haven't sold yet."*

1. **Sequence tagging.** *"**A is 1 of 3, B is 2 of 3, C is 3 of 3.**"* When B arrives first: *"B is 2 of 3? **I never got the A. Put it in the buffer.**"* When A arrives: *"A is 1 of 3 — **execute the A**."* **You** restored the order, on the service side. *"Is async going to do this for you?"*
2. **Buffer watermark + positive NACK.** *"**Any size of a buffer you give me, I give you a volume of trades that maxes out the server.**"* So: a watermark; below it, accept; **punch through it on the way up → call back to all your clients: "stop calling me."** Don't wait until full — *"there could be messages **in route** to you already; those you want to accept."* And if you do max out: **"you actively NACK them to the client… I actually got it, but I say I didn't."** Drain to the watermark on the way down → **"start calling me."**
3. **Elasticity / load-shedding.** *"Suppose you can handle **100 calls per second, but not 101.**"* Because *"systems are not elastic… if you plot **response time as a function of load**, it's **linear, but then it snaps.** … **you can do 100, 101 — the system is dead.**"* Fix: monitor incoming calls, admit below a threshold, **buffer above it**, watch the load, drain when it drops. *"Is async doing this for you?"*

> [!important] "I actually got it, but I say I didn't"
> When the buffer is genuinely full, the service **lies** about messages it did receive — because a client that believes its message landed will never retry, and the message is going to be dropped regardless. **Backpressure is a protocol about honesty, and sometimes honesty has to be deferred.** And note the consequence for retry policies: **NACKing a delivered message means the operation may run twice — idempotency is a prerequisite for this technique, not an optional extra.**

**His concession — async's real territory**, stated fairly:

> **Most people that do very simple form-based data applications don't think about these problems, nor do they need this kind of fancy solution, nor could they do it if they ever had to. That is the sweet spot of `async`.** But anybody on this call — your customers expect this level of performance. **And you cannot solve this kind of problem with syntax. You have to design around the problems. The classic solution is either taking the calls or, even better, dealing with queues.**

And the case no client-side fix touches: *"suppose you're into the wire, up the other machine, and the machine blows up. **Should you call it again?** Or maybe it went through, actually — but it's about to return, and **the network is down. How do you know?**"*

> [!warning] This is the only WCF mention — and it is NOT the regression
> **The parked WCF→Web API regression does not land here.** WCF appears **exactly once** in 10,471 words, and the reference is to a *performance property of WCF-era systems*, not to the 2.5× throughput regression. It reads as a half-finished clause, so the exact claim may be garbled: **re-parked again.** The substantive point stands regardless — **elasticity is a design property, and the response-time curve has a cliff, not a slope.**

##### The vendor-lock-in observation — use it as a filter

> **Have you ever wondered why any example you've ever seen from any vendor about how to use the merchandise uses functional decomposition? Do you think any vendor will ever show you an example that makes it easy on you to swap them out? That's the last example you're going to see. Every example you will see will be an example that maximizes the lock-in on you.**

> [!tip] The checkable version of this — not "vendors are evil"
> The mechanism is narrow: **a tutorial that wires the vendor's SDK into every business box is a tutorial that makes the vendor hard to remove.** So the question for any example code is not *does this work*, but **where does the vendor's type appear, and how many boxes would I have to edit to swap it?** If the answer is "everywhere," the example is teaching you a lock-in, not a design.

##### What the nine have in common — the actual test of a decomposition

> [!tip] None of these nine is a bug
> Buy/sell, mobile, texts, the cloud, non-relational storage, async, more instruments, a better feed, another country — these are the **normal, expected, desirable future of any successful system.** He is not listing risks. He is listing **things that will definitely happen**, and showing that this decomposition makes each one a sweep across every box.
>
> **So the test of a decomposition is not "does it satisfy today's spec" — it obviously does. The test is: what does tomorrow cost?**

#### The Anti-Design Exercise

The only *management* tool in the lecture — and a technique, not an attitude.

> **I call that technique the anti-design exercise.** Announce to the team that you are going to do a **design contest** for the next generation architecture. **Split them in two halves**, two conference rooms. Say to the first half: **your goal is to come up with the next generation architecture.** Say to the second half: **your goal is to come up with the worst possible design. An anti-design. A design that would maximize our inability to maintain it, to extend it, to reuse it.**
>
> **Let them work on it for one afternoon, then you bring them together — and you see they did the same.** It's not going to be exactly the same, because the labels are going to differ. **But if you scrub away the labels, it's the same.**
>
> **Only now you come clean: you know, guys — you weren't really working on the same problem. What does it mean that those that did the worst did the same as those that did the best?** … **Now all of a sudden something would click in their head.** Maybe now they'll be open to seeing the right way of doing things.

> [!tip] Why this is the pedagogy of the whole lecture in miniature
> He cannot tell a room their design is wrong — he has spent 70 minutes trying, and says plainly it won't work. The contest **removes the labels**, and the team discovers the two rooms produced the same structure. The argument stops being *his* diagnosis of *their* work and becomes **two halves of their own team recognising each other.**
>
> **Generalisable:** when a team will not accept a criticism, construct an exercise where the criticism is **produced by the team about itself**, with identifying labels removed so nobody is defending a position.

#### The Barbican Flip Chart — and Where Authority Comes From

> A few years ago, I gave a session at a conference in London, in the **Barbican Centre**… architecture track. And on the stage there's a **flip chart on a stand** from the previous session, where the previous speaker did a live session on architecture. **I walked to the flip chart and I kid you not: invoicing, billing, shipping. Literally these three words. I take the flip chart and the stand and I throw it off the stage. Like Elijah on Mount Carmel, shattering the idols of Baal.**
>
> **That's what everybody is doing. That's what everybody recommends.** **You cannot listen to the experts. You cannot listen to the so-called scholars and consultants.**
>
> **You have to seek your own authority here. The best authority is of course your brain. If you think that something is true, then by God you do it.**

> [!note] "Invoicing, billing, shipping" — the archetype, now three times over
> It is this lecture's running example, it is the hypothetical for the extrication argument, and it is what a room full of working architects had written on a flip chart. **So when you catch yourself writing exactly those boxes, you are not doing something neutral — you are reproducing the flip chart he threw off the stage.**

**Then the child** — which is a transition, not a fifth nail:

> **Mr. T says: I pity the fool. I pity the fool who does functional decomposition.** … But there's a saying — **from the mouth of babes.** In *The Emperor's New Clothes*, **Hans Christian Andersen** has a **child** saying *"the emperor has no clothes."* **All the adults are insane** — *oh, the emperor has amazing gown, and the silk and the lace, and look at the hemline.* **The emperor is naked.**
>
> **Adults are always insane, always blind, go with the madness of the crowds. That's a natural state. But a child hasn't yet been corrupted by the nature of the world.**

He had promised *"I will save the best nail for last."* **It is never driven.** Either the payoff is next recording, or the "best nail" was the domain-decomposition identity delivered earlier. **Do not treat the child as a fifth nail** — it is a rhetorical handoff.

#### What This Lecture Does *Not* Say

- **No migration strategy.** This lecture is a pure diagnosis — no seam, no strangler pattern, no composition root. Do not record it as answering incremental-migration questions. See [[#You Never Get to Do Either One — the Legacy Problem]].
- **No positive method.** No volatility, no axes, no encapsulation, no cohesion, no information hiding, no Parnas. Not one word about what to decompose on instead. [[#Volatility-Based Decomposition]] and [[#Axes of Volatility]] stay empty, legitimately.
- **No SSM.** `client` appears 24 times and **every instance means "the caller / the UI"** — the web page, the mobile device, the desktop, the browser. `manager` 1, `engine` 3 (all an aircraft engine), `utilit` 0, `resource access` 0. **Re-parked a fifth time.** See the callout at [[#Structure (Clients, Managers, Engines, Resource Access, Utilities)]].
- **No WCF→Web API regression.** One WCF mention, on elasticity. **Re-parked.**
- **The recording starts mid-sentence** and ends cleanly at the hinge. Not truncated — a genuine section boundary.

---

## Quiz

> [!question]- 1. Juval says the method is "literally a meat grinder" and "highly deterministic." If so, why does he keep saying "garbage in, garbage out" — and what exactly is your job that the machine cannot do?
>!
> [!summary]- Answer
> Because determinism governs the *transformation*, not the *inputs*. The method reliably turns use cases and a decomposition into a design, but cannot generate either. He assigns three things to you personally: getting the right use cases, getting the right decomposition, and being creative — *"the method does not take away the need to be creative."* Get the decomposition wrong and *"you can use all the fancy method words and call everything right, it's still garbage."* Hence: **"You are 100% liable for getting it wrong."** The sports-car analogy makes the same point — drive a beautiful sports car into a tree and it is neither the tree's nor the car's fault, because **you are driving**. Hence "there are no silver bullets": a methodology helps you think but cannot replace thinking.

> [!question]- 2. Why is the time crunch "a facet of the method" rather than a stylistic preference? Give both arguments.
>!
> [!summary]- Answer
> **Three days is enough; five is already too much.** First, human nature: two-hour meetings where *"two minutes in, you already know what should be the outcome, but you have to wait another 118 minutes for everybody to catch up."* Standing up — or *"outside on one leg in the rain"* — removes the slack, because *"when you put the screws on people, you force them to focus, to prioritize, and to deliver."* Underneath it is *"monkey nature… 23 and a half hours a day the monkeys are arguing and throwing feces. It's not in our nature to focus, to prioritize, to deliver. You have to overcome it."* Second, **design gold plating**: Parkinson's Law means extra time becomes extra work, and *"if you think code gold plating is evil, you haven't met design gold plating. Design gold plating is disastrous."* Combined with the pendulum effect — *"for you it's just another box, for somebody else, two years of effort"* — the conclusion is **"less is more when it comes to architecture."**

> [!question]- 3. Explain the laptop example's failure mode and the two distinct ways it is expensive. Then give the general rule.
>!
> [!summary]- Answer
> Starting from the CPU (i9 → fan → airflow → box thickness → monitor size sets dimensions → battery last) fails because it is a **travel laptop**, where the dominant decision is **weight**, and the heaviest component — the battery — was scheduled last. If it blows the weight budget it invalidates every earlier decision. Two-part cost: (i) it isn't just the two decisions that must be reordered, *all the decisions in between* go out the window, so you are doing **bubble sort of the design decision tree**, complexity **n²** — twenty decisions implies roughly **400 meetings**, which no team has; (ii) the boss eventually aborts design and says "start coding," so you go to manufacturing with a **half-baked decision tree** and discover invalidations *after* the code exists, where changing the design is the most expensive thing in software development. General rule: **it is a tree, not a string** — the root decision is the *market* (gaming → graphics card; travel → weight; desktop replacement → CPU/HD/monitor) — and **"the first act of wisdom in designing any system is recognizing your own design decision tree."**

> [!question]- 4. What is "architecture survival", and why does Juval blame the architect rather than the team when a good design gets butchered?
>!
> [!summary]- Answer
> A design is real only if it survives implementation. Not a good design if it is good **in your head**; not on a whiteboard with a big DUNNO arrow next to it; not in a document nobody ever reads. **Only a good design if it survived through development without being butchered, ending up as working bits on customers' machines.** The threat is developers who don't value what you call for — *"why do we need all these layers? Let me just connect from the front end direct to the database, bam, compile, ship it, I mean it works."* He blames the architect because the transmission failure is theirs: *"They butchered it — you failed. You failed to have them value what you're calling for. You failed to communicate."* Two levels must be conveyed: the **general interaction rules** (which components may do what) and the rules **in the context of your specific component type** — the construction-site model, where the electrician knows the electrical code but the architect says *"run the power line here"* and the tradesman runs it **to code**. He does not expect developers to design correctly — *"that would make them architects"* — only to understand, value, and follow simple instructions.

> [!question]- 5. Give the three purposes of the vertical slice and state what must be true of the components inside it.
>!
> [!summary]- Answer
> **(a) Context/communication** — *"the context of developers is code. They need to see it first in code to understand what is going on."* Forty diagrams alone produce a blank stare, exactly as a microwave does for a caveman: a context failure, not an intelligence failure. **(b) Design discovery** — *"don't kid yourself that you'll be able to get the design right in the first pass. That never happens."* Attempting the slice reveals *"this is too big, split it"* and *"we never use that one, throw it away."* *"All it has to be is good enough."* **(c) Early stress testing** — one week in, you must know whether anything in the architecture precludes meeting throughput/scalability/availability/responsiveness/performance goals. Components **do absolutely nothing**, deliberately: the wiring, layers and design aspects (security, transactions) must be real and must follow your architecture; only the work is stubbed. That proves the *architecture*, not the code. Keep it relatively thin.

> [!question]- 6. "Architecture is always and everywhere an act of decomposition" — so what exactly is *functional* decomposition, and why does he date the project's failure to before the first line of code?

>!
> [!summary]- Answer
> **"Functional decomposition is basing the decomposition on the required functionality of the system."** A, B, C required → an A block, a B block, a C block. Invoicing/billing/shipping → invoicing service, billing component.
>
> It is dated to before the first line of code because his claim is not that it *tends* to fail — it is that it is **precluded**: *"that is death. If you have functional decomposition, the project has already failed. **Past tense.**"* And the physics argument is why: decomposing by function lets the architect say **"no sweat"** — i.e. **endeavour to add high value without sweating**, which he treats as a law-of-the-universe impossibility. *"It's not an accident that it's not working for you. **It cannot work for you.**"*

> [!question]- 7. Which nail costs you the *mechanism* rather than money — and what is the one-sentence test of it?

>!
> [!summary]- Answer
> **Nail 2: functional decomposition is secretly temporal decomposition.** *"You don't do A, B, C. You do A **and then** B **and then** C. So built into the very fabric of B is: it is called after A and before C."* Lift B into a system where nothing does A or C and it fails — *"the A and the C are hanging off it. Which means **kiss goodbye, reuse.**"*
>
> Money nails (business logic duplicated per client, cost-curve edges, points of entry) are recoverable. This one removes the unit of reuse. **Test: a block that silently requires a predecessor and a successor is not a component — it is a segment of a script.**

> [!question]- 8. He calls domain decomposition *worse* than the functional house, yet his own "lunatics have taken over the asylum" line targets today's best practice. Give his actual reason — and the limit of it.

>!
> [!summary]- Answer
> An **identity**, not a list of symptoms: *"a rose by any other name is still a rose. Domain decomposition is still functional decomposition — except it's in disguise. Kitchen is where you do the cooking, bedroom is where you do the sleeping, garage is where you do the parking."* Therefore the physics disproof transfers: **domain decomposition is precluded from ever working. "The rest are just details filling in the blanks."**
>
> **The limit:** he never says domains are useless or that you should ignore the business. He says a boundary named after a *location of activity* is still a boundary keyed to a *function*, so it inherits Nail 2. Also note the reporting point, which he calls the *real* problem of the second milestone: **"the fact that you had to rebuild the kitchen is not disclosed to the customer"** — and it cost more than the first time.

> [!question]- 9. "Unit testing is completely and utterly unimportant" but also *essential*. Hold both. Then: why is regression testing unavailable, and what makes the jumbo-jet defect unfindable by any unit test?

>!
> [!summary]- Answer
> **Essential but unimportant** is a general category — *"Life is full of things which are essential but unimportant. For example: breathing… Nobody takes pride in doing essential things."* So unit testing is table stakes, and pride in it is the tell.
>
> Regression testing is unavailable because **"everything is so coupled to everything else, everything duplicates everything else"** — you cannot isolate. So you fall back to what you *can* do: **searching under the street light.** Consequence: *"your system is **untestable**. And if your system is untestable, you will forever have defects."*
>
> The jumbo-jet defect is a **chain through the interaction**: turn → G-force pulls fuel off the pump → sub-pressure → cavitation bubble → implodes hypersonically → shatters the rotor → debris to injectors → engine on fire. It exists only under a condition no single component is tested against. **The unit tests are not weak — they are about different things.**

> [!question]- 10. Your CTO returns from a conference and says "move it to the cloud." Give the two distinct problems Juval raises — and what each forces you to edit.

>!
> [!summary]- Answer
> 1. **Pricing model changes call shape.** Locally you *"pay for the license once and then **go and party on the database**"* → many **chatty** calls. Cloud: *"they will nickel-and-dime you on everything — number of connections, size of messages, number of messages, the time of day, **the colour of your cat**."* So calls get **chubby** → *"visiting every box: **don't be chatty, be chubby.**"*
> 2. **Storage model changes how you think about data.** *"Most local databases tend to be relational… **when all you have is a hammer, everything looks like a nail.**"* Cloud-native is *"basically a giant table"* → *"forget about all those fancy queries, we're not doing that anymore."*
>
> Both are **sweeps across every box** — which is the point. And note the career trap he names: say no twice and the boss asks *"how can we get rid of these people?"*

> [!question]- 11. Give the three fixes `async` does not give you. Then explain the lie.

>!
> [!summary]- Answer
> 1. **Sequence tagging** — tag calls *1 of 3 / 2 of 3 / 3 of 3*; buffer out-of-order arrivals; execute when 1 lands. **You** restore order on the service side.
> 2. **Buffer watermark + NACK** — *"any size of a buffer you give me, I give you a volume of trades that maxes out the server."* So: below watermark, accept; punch through on the way up, tell all clients **"stop calling me"**; drain to the watermark on the way down, **"start calling me."**
> 3. **Load-shedding** — *"100 calls per second, but not 101"*, because **systems are not elastic**: response time vs load is *"linear, but then it **snaps**."* Admit below a threshold, buffer above it, drain when load drops.
>
> **The lie:** when the buffer is genuinely maxed, *"you actively NACK them to the client — **I actually got it, but I say I didn't.**"* Because a client that believes its message landed will never retry, and the message is being dropped anyway. **And it means the operation may run twice — so idempotency is a prerequisite, not an optional extra.**

> [!question]- 12. Design the anti-design exercise in four sentences, and say why it works when a design review does not.

>!
> [!summary]- Answer
> Announce a **design contest** for the next-generation architecture. Split the team into two rooms: half designs **the best** next-generation architecture, half designs **the worst possible design** — one that maximises your inability to maintain, extend, or reuse it. One afternoon. Bring them together.
>
> *"You see they did the same. It's not going to be exactly the same because the labels are going to differ, but **if you scrub away the labels, it's the same.**"* Then ask only: **what does it mean that the two rooms produced the same thing?**
>
> It works because he is explicit that authority fails — *"you're still going to do it; that's the only thing you've ever seen."* The review makes it **his** judgement of **their** work, which is arguable (see the due-diligence architect: *"Ha. I don't think so."*). With labels removed, **two halves of the same team recognise each other's output**, and nobody is defending a position.

## Related

- [[MOC — Course Overview]]
- [[99-Resources/Transcripts/Functional Decomposition|Functional Decomposition]] — **the [[#Design Don'ts]] payload**
- [[99-Resources/Transcripts/The IDesign Method|The IDesign Method]] — the previous lecture
- [[99-Resources/Transcripts/Contract Factoring in Practice|Contract Factoring in Practice]] — where "varying requirements ≠ what varies" comes from
- [[Modules/Service Contract Design and Factoring]] — the ratchet explains the anemic contract
- [[Modules/Microservices Development Process]] — cost curve, Shallow S, QA plan, extraction
- [[Modules/Design Aspects]]
- [[Modules/Design Aspects/Fractal Architecture]]
- [[Modules/Agile and Design]]