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
- [ ] Design Don'ts

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
> **Still undelivered — re-parked four times.** See [[Modules/Service Contract Design and Factoring#Sample Project II — The Real System (Resilient Energy)]] and [[Modules/Design Aspects#Self-Similarity and Fractal]]. The most recent attempt was yesterday's [[99-Resources/Transcripts/Sample Project — Resilient Energy|Resilient Energy]] lecture (*"the classic thing we're going to discuss tomorrow is inside each node"*), and today's [[99-Resources/Transcripts/The IDesign Method|The IDesign Method]] lecture **did not deliver it either** — the words `manager`, `client`, `utilit*`, `resource access` and even `service` do not appear once in 6,370 words. The only structural language is generic: *"the system is going to have layers. Inside layers you have components, you slice it."* Layers-and-components is **not** the four-node taxonomy.
>
> Nothing here yet. See [[Modules/Service Contract Design and Factoring#Sample Project]] for the v1→v4 contract evolution he uses to motivate it.

### Containing Changes

-

### Design Don'ts

-

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

## Related

- [[MOC — Course Overview]]
- [[Modules/Design Aspects]]
- [[Modules/Design Aspects/Fractal Architecture]]
- [[Modules/Agile and Design]]