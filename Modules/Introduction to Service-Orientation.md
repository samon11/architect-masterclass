---
title: "Introduction to Service-Orientation"
date: 2026-07-21
module: module-3
type: module
tags:
  - course/notes
  - module-3
  - juval-lowy
---

# Introduction to Service-Orientation

> [!summary] Module 3 — Service Foundations
> Understanding why service orientation matters, service-oriented architecture, and service-oriented applications.

## Topics

- [x] Why service orientation
- [x] Service-oriented architecture
- [x] Service-oriented applications
- [x] The evolutionary arc of software (Enigma → .NET)

## Notes

### Why Service Orientation

- [Transcript](../99-Resources/Transcripts/The History of Software.md)

> [!warning] Only the opening frame is filled by this recording
> `history_of_soa.webm` contains **no service-oriented content** despite its name. It is the *preamble* — "the only way to understand where we are going with this is to understand where we came from" — and ends mid-thought at *".NET, again, from an evolutionary standpoint, is nothing but clean COM."* The SOA half of the lecture is a **separate, not-yet-recorded session**. Do not populate the two remaining stubs from this material.

Juval opens by asking the class what a service is: *"Not a single one of you can even come up with a definition of what is a service. Interesting, isn't it?"*

**Vendors commit two sins:**

1. **They equate whatever they are trying to sell with whatever you are talking about.** Cloud services, professional services, databases, message buses — all "service-oriented." Self-refuting: *"If they're all equating their stuff with service orientation, they can't all be right. Which means at least some of them are wrong — and Murphy says they're all wrong."*
2. **They claim service orientation exists only in the enterprise.** Motivated by **margin**: *"There's actually no money or margin in retail software."* Data points — *"Microsoft makes more money from Android than Google"*; *"when Coca-Cola is buying 100,000 licenses of Azure, Microsoft is printing money."* → *"The software industry has always been and forever will be fighting for the enterprise. That's the battleground."*

His promise: *"By the time I'm done with you, you'll be entirely convinced that this has nothing to do with enterprise environments."* He speaks as an **independent analyst**, grounding the argument in a trend spanning **the last 90 years** of software development — which is the whole of the rest of this recording.

### The Evolutionary Arc of Software: Enigma → .NET

- [Transcript](../99-Resources/Transcripts/The History of Software.md)

> [!important] What this section is for
> This is software archaeology, and it is the *argument* for service orientation rather than a description of it. One move repeats across every generation: **each abstraction decouples one axis of coupling and introduces a worse coupling on the next axis.** The endpoint — proven by the mouse, the chair, and Parnas — is that **only the interface is reusable**. That is the bridge into [[Modules/Service Contract Design and Factoring|Service Contract Design]].

#### Enigma (1920s–1945) — Machine #1: Purpose-Built, Not General Purpose

The world's first modern computer appeared **in Poland in the late 1920s**: a typewriter-like enciphering machine, sold to the Germans in the early 1930s, adopted by the German military — **Enigma**.

**Mechanism.** Keyboard keys at the bottom; the top three rows are **light bulbs, not keys**. Pressing a key sends current through an electromechanical maze and lights one bulb. The maze is dictated by **three rotors chosen out of a set of eight**, inserted in a **specific order**, at a **specific initial position**. Each rotor has **26 notches** and a "hellhole of copper wires" mapping letters in "some wacky way." Every keystroke also *clicks* the rotors, changing the maze.

**Why it mattered.** Enigma was the first enciphering technique immune to **frequency analysis**, because every keystroke re-scrambles. Brute force is out — **a five-letter word ≈ 30 million combinations**; a page of text has *"enough combinations to uniquely name every quark in the universe."*

> [!quote] "The Germans rightfully assumed that no human could ever break Enigma. And with that, they were absolutely correct."

So the British built **the second computer ever** — by **Alan Turing** — at **Bletchley Park**, to run anti-Enigma machines.

- **German mistake #1 — the key-sharing problem.** They sent **tomorrow's keys on today's ciphertext**: *"the one thing you're not going to do is send the key on the very channel you're trying to protect."* **"If you're even once in, you're always in."**
- **German mistake #2.** U-boat keys were **preloaded for 90 days** (RF doesn't penetrate water), so the British just needed *a* submarine plus *an* Enigma machine.
- **The heist.** A **faked raid on the port of Trondheim, Norway**: blow up every boat, burn every building, grab one Enigma, then **blow it up too** so the Germans never knew it was missing.
- **Codebook recovery.** A destroyer task force trained to drop depth charges *"just enough to hurt the submarine, but not to kill it,"* so the crew would surface and ditch; commandos jumped aboard a burning, sinking boat and ran to the radio room. Countermeasures: codebook paper that **dissolves in salt water**, countered by a **special leather pouch**; Germans lined the keel with **explosive chargers** and a long fuse. *"How many British commanders got the Victoria Cross was mostly on that one."* **1942** — submarine captured. Around **1944** the Germans added a **fourth rotor**; the British captured a second submarine.
- **Ian Fleming.** The whole operation was conceived by **Lieutenant Commander Ian Fleming, Royal Naval Intelligence** — the man who wrote the James Bond books. *From Russia With Love* is a transposition of this story. Fleming couldn't disclose it: stories were held under the **Official Secrets Act until 1975 — 30 years later**.

> [!important] Engineering takeaway
> Enigma is an *electromechanical computer designed to solve a specific problem*. Can you add numbers on it? No. Decipher/encipher? Yes. **"It is absolutely not a general-purpose computer."** Changing the "code" meant **changing the mechanical design of the computer** — *"an enormous level of coupling."*

#### ENIAC (late 1940s–1950s) — Machine #2: General Purpose, Never Used That Way

First electronic **general-purpose** computers; the most famous is the **ENIAC**. *"And yet they were never used in a general-purpose way."*

**Driver: the US hydrogen bomb program.** Unanswerable-by-experiment questions: how big must the atomic detonator be to reach fusion temperature/pressure? How much deuterium and tritium in the Teller device? The Manhattan Project hit the same wall finding plutonium's **critical mass**. Answer: **numerical simulation**.

**"Computer" in 1940 was a profession, not a machine** — like doctor, lawyer, accountant. *"Somebody with a white shirt and a green cardigan and a slide rule."* **Los Alamos ran three aircraft hangars, each with 200 human computers on long tables using slide rules, for three years.**

**Feynman and von Neumann.** **Richard Feynman** (the O-ring guy) walked down a Los Alamos street with **John von Neumann** and said: *"Even if every person on the planet had a slide rule, it would not be enough to solve the equations."* Von Neumann: *"Let's build a machine."* He had already read **Turing's** paper on general-purpose computers. (Juval notes Turing himself never built one — *"he was ousted and then forced to commit suicide."*)

The ENIAC was *"a monster, the size of a three-floor building, full of vacuum tubes, consuming more power than a town."* Scale just moved: *"What is the largest data consumer in the world today? Data centers."*

**Programming = physically flipping vacuum-tube states and placing zeros and ones by hand.** Requires intimate familiarity with the exact tube layout, so code that runs on *this* ENIAC won't run on *that* ENIAC. **"The notion that the code works on my machine is a time-honored tradition."** At the time it didn't matter — **the world had four computers**: two at Los Alamos, one at Oak Ridge, one at Lawrence Livermore. *"You cannot make the statement that your code works on 25% of all computers in the world."*

**Famous predictions, delivered with sarcasm:** IBM chairman **Watson** — *"the world will never need more than six computers"*; **Bill Gates** — *"no computer will need more than 640K."* Juval: *"Why are you listening to these guys? They have a perfect track record of getting everything wrong."*

> [!important] The software-engineering point
> If you program by setting individual tubes, **is there any difference between software and hardware? No.** The word **"software" only entered the English dictionary in 1958**, long after the ENIAC. What you actually have is **machine-specific language coupled to very specific hardware**.

#### Assembly Language (1960s) — Decoupling Code from the Machine

Transistors came *between* vacuum tubes and microchips, cutting the cost of ownership **from that of a small city to that of a large appliance** — computers shrank to "several refrigerators back to back."

**Assembly is not programming — it is an *abstraction* of programming.** You write against an abstraction of a computer (program counter, registers), and an interpreter maps that onto the specific places in the specific hardware.

**Payoff:** *this simple idea enabled the private sector to own computers.* Before that, computers lived only in hardcore defense — and in defense **cost doesn't matter**, because "the future of the world is at stake."

**Limitation:** assembly is still coupled to machine architecture. Code for a 5-bit machine never runs on an 8-bit machine; even 8-bit-to-8-bit fails if register counts or program-counter addressing differ. In the '60s architectures improved in rapid succession, so **every new computer type meant throwing away your code and starting over.**

#### COBOL (Late 1960s) — The Abstraction of an Abstraction

**COBOL is not programming — it is an *abstraction of an abstraction* of programming.** You write a higher-level language; a compiler emits assembly, and **you tell the compiler the target architecture**, so the same source compiles for every machine. *"COBOL is what enabled rank-and-file businesses to own computers."*

> [!note] Second Law of Software Engineering
> Where was COBOL developed? **The US Navy, San Diego.** Where was the internet? **DARPA net.** *"Do you see a pattern here?"* → **"All good things come from the Department of Defense."** *"It's an unbroken rule."*

**COBOL's problem.** To make the first-generation compiler's job easier, programmers used **go-to, go-to 10, go-to 20**. The compiler turns a go-to into a branch and life is good — but it creates **enormous coupling between the code and its own structure**. Maintenance scenario: can I change this line? **Yes. Should I? Oh my god, no.** Whoever go-tos into the line above you is affected; whoever go-tos into *that* go-to is affected.

> [!important] Core principle — the spine of the entire lecture
> **"In software, the cost of analysis far exceeds the cost of synthesis."** Hand someone a piece of C# and they spend three weeks concluding *"it just adds two numbers."* Ask them to *write* that code and it's trivial. Writing is synthesis; **debugging is analysis** — which is why writing code is easier than debugging it.

Corollary: *"Most developers are completely ill-qualified to debug their own code."* Therefore **"developers should never write the smartest possible code — developers should only write the dumbest possible code. No compound statements, no concatenation, short lines."** (See [[Modules/Microservices Development Process#Development and Design Standards]].)

The tempting shortcut — a fresh module on the side that nothing jumps into — *is* locally insulated, but *"at some point, somebody, somehow, somewhere always has to figure out what all the go-tos are doing"*, and you've made that task **non-linearly worse: not +1, but +N.**

**Result:** COBOL maintenance is *"armies of ants pouring over all these go-tos."* On histograms of developers per language, **the largest bar is still COBOL** — bigger than Java, bigger than C, mostly 1970s banks and government agencies. Juval's tip: *"If you want to make a lot of money, learn COBOL. You will be dipping your toes into a river of money."*

Net: COBOL decoupled code from architecture, but **introduced massive coupling against its own internal structure**.

#### 1972 — The Hinge Year

Three things happened, and Juval insists the coincidence is not accidental:

1. **Structured programming** emerges (**C in 1973**, Pascal later). The rule: **don't use go-to; write functions.** If nobody go-tos into the body of your function, you can examine it **in isolation** — a drastic reduction in the cost of analysis. Such languages are called "structured" precisely because they **decouple code from its structure**.
2. **David Parnas** publishes a **five-page paper: "On the Criteria To Be Used in Decomposing Systems into Modules."** *"This five-page paper contains every element of modern software engineering — information hiding, encapsulation, decoupling. It's absolutely astonishing."* Asking *"what would make this more reusable?"* is an **engineering question** — **"the birth of modern software engineering."** Parnas is **"the granddaddy of all software engineers."**
3. **The term "software crisis" was coined.**

> [!quote] "1972 is the most important year in the history of software. It's like *Back to the Future* and 1955, where all the timelines connect."

His thesis: the birth of SE and the coinage of the crisis aren't coincident — **the crisis is attacked by applying engineering principles.** He also promises *"another thing happened in 1972 — we'll see it Friday morning"* (unresolved in this capture) — **now resolved in part 2**: it is **Parnas's 1972 paper**, cited as the origin of *both* "service boundaries are explicit" and "services are autonomous." See [[#The Four SOA Tenets]].

**1978:** Parnas publishes **"Designing Software for Ease of Extension and Contraction,"** talking about software as *a family of programs*. Translation: **he's talking about interfaces, but in 1978 he lacked the vocabulary to say "interface."** *"David Parnas was decades ahead of his time."*

#### Structured Programming's Next Problem: Global Data

A C function *is* an element of reuse. But functions manipulate data, which lives as **global variables floating everywhere** — hundreds, maybe thousands.

You see `g_MyFlag`. Can you use it? Yes. Should you? **Oh my God, no** — you must first analyze what everybody is doing with every other global variable. So you add `g_MyFlag2`, which solves *your* problem but makes theirs **non-linearly worse. You doubled it, or worse.**

> [!important] "C maintenance is nothing short of neurosurgery"
> Figuring out what all the neurons in a patient's brain are doing.

**Silver lining:** not all functions touch all globals. So **group the functions with the globals they manipulate and call it an object** — and make the data **private**. Now the scope of analysis shrinks to a single object.

*(C still permits globals, for porting old code; new code shouldn't use them. Same reason C still has go-to: for porting COBOL.)*

#### Object Orientation (1980s) — "The Single Biggest Failure in the History of Software"

OO is **an attempt to encapsulate data and decouple code from data.** In C++/Smalltalk the mechanism of reuse is no longer a function but **a whole class hierarchy**: derive, specialize, reuse everything upstream. Two classes exposing the same public members are **polymorphic** — the term comes "from botany of all things."

> [!quote] "Everybody wanted to reap the benefit of reuse. Object orientation was the single biggest failure in the history of software. It was such a colossal disaster it set our industry back decades. And yet you all think it's good. … Anyone have any doubt? In less than two minutes I'll prove myself correct and you wrong again."

**Why it failed: it failed on its single promise. Nobody in the history of software has ever reused an object.**

- **Proof #1 — the mouse.** Take a Lenovo mouse and do OO analysis à la **Ivar Jacobson's *Object-Oriented Software Engineering* (1988)** — the title is *"an oxymoron, or just a moron."* Objects: left button, right button, wheel, case, optical sensor. Pry the **case** off and try to mount it on a Logitech/Microsoft/Dell mouse. Extremely unlikely — those 3D curves and the tang groove are **incredibly specific to this mouse**.
- **Proof #2 — the chair.** Unscrew the seat and try to mount it on the chair you're sitting on. Won't work — screw spacing and curvature differ.
- **Proof #3 — the stone-axe image.** The interface is really **"mouse–hand–tool."** You can't reuse the quartz crystals from Stonehenge inside the mouse, nor the mouse's electronics inside Stonehenge.

> [!important] The general law — the thesis of the whole course
> **"In any given entity, the only reusable thing is the *interface* to the thing — never the thing itself. Once you realize that, you start seeing it everywhere."**
>
> The interface *is* reusable: you can drive my mouse, I can drive yours; you can sit on my chair, I can sit on yours.

**Verdict:** *"By focusing on the object as the mechanism of reuse, OO absolutely guaranteed that nobody is ever going to reuse anything."* Since **reuse is the most fundamental aspect of engineering**, calling a book "object-oriented software engineering" is an oxymoron. The 1990s farce: every interview sounded like proving who knows OO better — *"and it was all for nothing, because nobody ever reused anything."*

#### The C++/C Team-Coordination Pathology

Building in C++ requires access to the actual `.cpp` files. Two teams exchanging code must **share a build** — and *"the moment two teams share a build, they are for all intents and purposes the same team."* Larger teams are inefficient, so **C has inefficiency built into its very fabric**, inherited from the size of the teams it forces.

- **Locking:** you go to grab `MyClass.cpp`, somebody else has it checked out, you can't work. **This violates the directive of teamwork: "Never prevent others from doing their work."**
- **The workaround:** copy `MyClass.cpp` locally, flip the write-permission field, make your one-character change, check it in as **`MyClass2.cpp`** — *"Don't give me this look, I had to do it, I was on a deadline."*
- **The interrogation:** *"There are a hundred lines, I just put one `i++`, why are you upset?"* → *"How many neurons in your brain? A trillion, and about ten trillion relationships. Would you mind if I went into your brain and rewired one neuron? … So if a one-in-ten-trillion change is not okay, why is one-in-a-hundred okay? What kind of nonsense is calling it `MyClass2.cpp`? Is it `MyClass2.cpp`, or is it **my completely different class, not to be confused with `MyClass.cpp`**? Which one is it?"* And did the evil code molester **redo every test, every integration, every regression** ever done on that class? Of course not.
- Then `MyClass3`, `MyClass4`, `MyClass4.2`… developers declare **"we have to do some refactoring."** *"Really? The two wrongs make a right."*

**Uniformity chain:** one giant compilation unit → **uniformity of language** → **uniformity of skill.** C is hard, so everyone must be a genius. You can't hire only geniuses; you hire along a normal distribution, and the rest of the team drowns.

**Uniformity of language destroys economy of scale.** Four people: no economy of scale. Four hundred: you must find commonalities and put them somewhere shared. But if 200 use Smalltalk and 200 use C++, **your economy of scale is zero.** Corporate architecture bodies are pure cost, pure overhead, no invoice, no revenue — so the chief architect must constantly evangelize "motherhood and apple pie… think of the children… maintainability, accessibility, reuse." Once is hard. **Twice — once for the Smalltalk crowd and once for the C++ crowd — is never going to happen.** *"Goodbye to any attempt at having Adam Smith working for you."*

#### Inheritance — "Absolutely Evil"

- **Base-class flags.** You look upstairs, see `m_MyFlag`. Can you use it? Yes. Should you? **Absolutely no.** So you add your own flag at your level in the hierarchy — possibly **with the same name**. *"That's not going to confuse anybody."* Except someday somebody must figure out what all these members do across the entire hierarchy: you've made the analysis job you refused to do **non-linearly worse for someone else.**
- **Virtual methods.** A defines a virtual method and implements it; both A and B use it. You're in C (A ← B ← C). **Overriding A provides different behavior — may that not break A and B?** Liskov says *may*, but **"you would."**
- **The combinatorial mess.** Should you call the base implementation? **Which** base — B's or A's? Is B overriding A or not? Is B calling A too? Who calls A? Call it **before or after** your code? All answerable only by analysis.
- **Pointer swapping.** A holds a pointer to the root of another hierarchy (A′ ← B′ ← C′). C reaches back into A and swaps the pointer from A′ to B′. B′ is polymorphic with A′ but provides **different behavior** — may that not break the code inside A and B? Yes. *"You may therefore have to go and analyze it."* → **"Ha ha ha ha ha — that word again. What do you think now about inheritance?"**

> [!quote] "If I could wave a magic wand and make all inheritance of implementation go away, I would. Inheritance is an absolute evil mechanism."

Escalated verdict: if C maintenance is neurosurgery, **C++ maintenance is neurosurgery, blindfolded, at night, at the top of an active volcano, surrounded by a minefield.** The need for intimate knowledge of base-class internals is *"an unbelievable killer."*

#### What C++ Says About Deployment — Nothing

> [!quote] "Miraculously, the code appears on the customer machine. Really? Which version? There's no support for versioning. You're on your own. Good luck."

- **Size.** His first industry project shipped a **40 MB .exe** when the average hard drive was **20 MB**. Today's drives are **4 TB** — but could you download an 8 TB file even today? No. Deploying 40 MB on floppies and then wanting to change one `+`: you can't patch it, you redeploy the whole 40 MB. *"That sounds very agile to me."* Actual advice: **"You postpone changes as much as you can, but the business wants to change, because the world is dynamic."**
- **Security.** One giant compilation unit = one giant process ⇒ **client and object share the same security token.** Ideally clients are *demoted* and objects *elevated*, so clients must go *through* the object to reach expensive resources. Instead clients land inside your object and bypass it. Would you run all your users as admin/root? **Absolutely not — but that's what C++ forces. "You cannot write secure code in C++."**
- **Fault isolation.** Client and object share the same address space. Client calls the object, object goes *poof* — so does the client. Users typing the great novel about to hit Save. The client should *detect the object is not home*, shut down gracefully, save local work. *"Poof you're gone: jumbo jet falls from the sky, nuclear reactors go into meltdown."* Also true of two objects from two vendors that never spoke, side by side in one process.
- **Scaling.** Single machine, single process, one contiguous address space ⇒ **you cannot scale.** You *can* do sockets/RPC/DCOM — *"I didn't say you couldn't scale, I said you couldn't scale **in C++**."*
- **Serialization.** C++ has `>>` and `<<`, **but you must write the serialization code yourself**, then maintain **perfect affinity between the serialization logic and the object's metadata**. Rename/add/remove a member ⇒ update the serialization logic. *"The moment you mention the word discipline in the context of software development, you know bad things are going to happen."* Deeper killer: the deployed customer machine holds an **older dump**; feed it to the new serialization logic and it **chokes and dies**. Conclusion: **a serializable object must remain immutable for the end of time once deployed.** *"Is that conducive to innovation? Agility? Probably not."*

> [!quote] "It failed on its single promise of reuse and introduced all these problems. The word success would not be the first to come to mind to describe this disaster."

> [!warning] Escalation warning — do not guess the sequel
> He used to call this the biggest disaster in software history, but *"there's an up-and-coming contender that's going to be an even bigger disaster. We'll discuss that disaster tomorrow. That disaster, I fear, is going to make this disaster look like a walk in the park."* **He does not identify it in this recording.**

#### The 1980s Attempts to Patch C++

**Header/source split (`.h` + `.cpp`).** Often the consumer only needs the class's *metadata*. Helps, but *"it's like taking an Advil — it doesn't solve things, it just makes you feel better."* Doesn't stop the `i++` problem or `MyClass2.cpp`.

**`.lib` files.** Compile `.cpp` files into a **binary** `.lib`, hand it over with a header that *"supposedly, with the hope and a prayer, describes what's inside."* "How do we know it's what's inside?" — **"Trust us."** Now nobody *can* create `MyClass2.cpp` because you never got the `.cpp`; teams and vendors partially separate. Downside: **it made the giant-exe problem worse** — hundreds of `.lib`s link into a near-undeployable monstrosity.

**`.dll`.** *Rename* the `.lib` (content unchanged) and write code that **links at runtime** — stubs that pretend to call the library but call into empty space; load the DLL, get its base address, patch the stubs with function pointers. Result: a tiny `.exe` next to a bunch of DLLs, deploy one DLL instead of the monolith. Solved the problem — at the cost of hefty programming.

**1988: `LoadLibrary`.** *"This sounds like just the sort of thing the operating system should do for you."* Give it the location, it links on the fly. *(Nostalgic aside: in the early 90s his interview question was "write me the code for LoadLibrary in C on a whiteboard." **About half got it right.** "As a testament to the degradation in the caliber of developers today.")*

**The DLL deployment problem.** If everyone calls `LoadLibrary`, you must be in the same folder as everyone else — and you don't know the folders on the target machine. Microsoft's fix: `LoadLibrary` **first looks in the one folder every machine must have — the folder where Windows itself executes.** Great for the **DLL vendor**, **awful for the app vendor**: every installer squirts its DLLs into the global folder, **overwriting whatever was there**, forcing every new DLL to be **backward compatible**.

**The compatibility lie.** *"New DLL is 100% backward compatible"* is **a bold-face lie. You can never prove something is backward compatible.** At best: *"we did so much testing we couldn't tell it wasn't"* — which is a **moose rule**.

**DLL hell, one concrete flavor.** App A against v1, app B against v2. Deploy B → v2 squirts into the global folder, smashing v1. Then someone installs app A, dropping in its 1.0 DLL. **App A is fine; app B blows up** — because the vendor guaranteed **backward** compatibility and **said nothing about forward compatibility**.

**The registry idea.** The root problem is that **file names aren't unique enough**. So: **unique identifiers per version (GUIDs)**, a **global dictionary** mapping key → file location, all versions on disk. Client code never does a blind `LoadLibrary` (*"that is suicidal"*) — the required GUID is **baked into the code**, it looks up the location, force-feeds that to `LoadLibrary`, which goes nowhere else. Enables **side-by-side** versions. Juval remembers **copying his first GUID onto a piece of paper**.

*"This is a lot of work. This is the sort of thing the operating system should do for you."* → **1994: Microsoft introduces `CoCreateInstance` — and COM was born.**

#### Component Orientation (Early 1990s) — The Fix Nobody Credits

> [!important] "Component orientation is what replaced object orientation, fixed all the problems, and got none of the credit."
> *"None of you have been using OO for a very long time. You have all been using component orientation without even being aware."*

**COM's central insight: the only element of reuse is the interface — therefore everything in COM is based on interfaces.** When you use COM you *only* see an interface; there is no way to get to the underlying class. It's irrelevant.

- **Binary metadata — type libraries.** Header files imply C/C++ ⇒ uniformity of language. COM replaced them with **language-agnostic binary metadata**: "suck it into Java, it looks like Java; into C, it looks like C; into VB, it looks like VB."
- **Productivity explosion.** Without uniformity of language, you can have really smart developers writing sophisticated multi-threaded COM objects, and people who *"basically were driving a bus yesterday"* dropping them onto a form and shipping it — as genuinely qualified developers. **"The very first app store was the ActiveX marketplace of Microsoft,"** with tens of thousands of vendors worldwide.
- **COM's virtual machine.** COM introduced **the first virtual machine**. *"People think the JVM was the world's first virtual machine. No — it was the second."* COM never called it that; it called it **apartments**, which provided **life-cycle management, memory access, and even security.**
- **Hot patching.** Because `CoCreateInstance` does the unique-identifier dance every time, **you can patch a machine while the application is running**. *"Astonishing. We don't have to shut down anything."*

> [!quote] "COM was an absolute marvel of engineering. Fixed all the problems of OO and introduced the benefit of separating interface from implementation."

**COM's own problems:**

1. **The language (C++) knew nothing about components.** COM's fundamental concept — *interface* — had **zero language support**. `new`/`delete` don't hold water: with binary components loaded by several clients in a process, the component loads **once** and you maintain a **reference count** — bump it when you pass it around, decrement when done, and at zero **the object commits suicide with the immortal line `delete this`.** Developers couldn't fight reference counting.
2. **The apartment was bolted on top of Windows, and Windows knew nothing about it.** COM had to allocate a **hidden window with a message pump** that converts Windows messages into real calls on the object — *"really nasty things."*
3. **Cross-apartment calls.** A reference is only meaningful in *your* apartment. To pass one you marshal into a stream, serialize, unserialize, get a neutral reference, check the interface into the **Global Interface Table**, get a **cookie**, carry it to the other apartment, look it up in the GIT, normalize the reference. *"Oh my god — what level of complexity? It's all because the OS knew nothing about this."*

**Result:** *"COM hit the nail perfectly on the head as far as the methodology; the execution was so-so. Most people couldn't handle it."*

**COM vs DLL hell.** *"You told us to use COM, we used COM, we got DLL hell."* → *"No, calm down. COM bears the scars of DLL hell. If you're using COM you cannot have DLL hell. But COM is notorious for enforcing the COM view of the world, and if you violate that you have **COM hell** — you've replaced one hell with another."*

**Two companies that made it work.** **Microsoft:** *"Microsoft has a simple rule: everything is a COM object."* Spell checker, split sheet, the cell in a split sheet, the button on a form. Fix or extend `ISpellChecker` and **PowerPoint, Word, Excel, Internet Explorer all benefit immediately**; write a text editor as a COM object and drop it into Word, Visual Studio, the browser (which it did). Hence a new Office and Visual Studio release every six months in the second half of the '90s. **The company he was chief architect of:** same guideline — *"Everything is a COM object. I know it's wacky — all those IDL files, type libraries, proxies — get over it."* Plus a key and a COM development standard. But those were **the exceptions indicating the rule.**

#### The Cleanup (~1997–98): C# and the CLR

It was clear to Microsoft that COM's methodology was right and its execution mediocre. Two fixes:

- If the language knows nothing about components → **invent a component-oriented language** with interfaces as first-class citizens, interop support, metadata persistence, and versioning. They called it **"Cool"** — *"because it's not even cool"* — today known as **C#**.
- If the OS knows nothing about components → **invent a component-oriented operating system**: the **CLR**.

**".NET is indistinguishable from COM" — bit for bit:**

| COM | .NET |
| --- | --- |
| Reference counting, managed by the **developer** | Reference counting, managed by the **garbage collector** |
| Global dictionary: unique IDs → file location, in the **registry** | Versioning via unique IDs → file location, in the **GAC** |
| **GUIDs** | **Strong names** |
| **Apartment** | **App domain** |
| Security blanket on **proxies** | **Code access security** |
| Type libraries | Type libraries |

*"Tid for tad, they did it exactly the same way."*

**"In .NET, everything is a COM object."** Define a class in C# and you did *not* define a C-style class — you defined a **full-fledged binary COM object** with GUIDs, type libraries, registry entries, everything. *"All of .NET to this day is still wired up using COM — except you never see any of that."*

**"You think the `integer` is not a COM object?"** .NET's `System.Int32` is **a monster structure exposing 17 different interfaces**. Why bother? **Composability.** The payoff: `MessageBox.Show("2 + " + 3)` — **two lines in C#, fifteen lines of kung fu in C**: allocate a buffer for the integer, a buffer for `"2 + "`, print into the buffer, allocate a third buffer sized as the sum of the first two minus one, shuffle all the characters, present the message box (eleven parameters), then free three buffers. *"That's only because the integer exposes those 17 interfaces."*

Closing line of the recording: **".NET — again, from an evolutionary standpoint — is nothing but clean COM."**

#### The Meta-Argument (the Actual Spine of the Lecture)

Every step is the same move:

> **coupling to a specific machine → coupling to an architecture → coupling to internal structure → coupling to global state → coupling to base-class internals → coupling to the OS**

Each generation's abstraction is *an abstraction of the previous abstraction* (assembly abstracts programming; COBOL abstracts assembly).

- **The recurring failure mode, stated four different ways:** you dodge the analysis cost locally and make it **non-linearly worse globally**, because *"at some point, somebody, somehow, somewhere always has to figure out what all the [go-tos / globals / members] are doing."*
- **The recurring correct answer**, foreshadowed by Parnas in 1972 and proven by the mouse/chair/stone-axe: **separate interface from implementation.**

> [!success] Why this matters for the rest of the course
> If the *only* reusable element of anything is its interface, then the interface — not the object, not the class, not the assembly — becomes the primary design artifact. That is exactly the claim [[Modules/Service Contract Design and Factoring|Service Contract Design and Factoring]] is built on, and the reason service contracts are the unit of reuse in a service-oriented architecture.

### Service-Oriented Architecture

- [Transcript](../99-Resources/Transcripts/Service%20Orientation.md)

> [!important] Read part 1 first
> This section is the second half of the session that produced [[#The Evolutionary Arc of Software: Enigma → .NET]]. It presupposes that history and applies the same abstraction ladder one more time. It opens mid-argument on the *consequences* of the COM/.NET mapping table that closed part 1.

#### Serious Issues With Component Software

*"Don't talk to me today about core. First of all, core for the longest time didn't exist. And second, where's WCF?"* Full-fledged power of the platform = **Windows**. Linux/Android force interop layers, which *"creates coupling in your code against the nature of the interop mechanism."* Even if you always run on Windows: *"can you have .NET talking to Java? Probably not. You could solve these things, except there's enormous plumbing required to do this."*

Six problems, stated as **"Serious issues with…"**:

| Problem | Why it breaks |
| --- | --- |
| **Concurrency management** | *"I have to assume that **all clients are forever concurrent**."* So you put a lock inside — and application-wide, locks stack: **"If I say locks, what do you hear? You hit deadlocks."** → *"Component software is inherently susceptible to deadlocks."* Solvable by sharing/managing the lock, **"but it's not in the box."** |
| **Transactions** | A component in a transaction spans all components in the system: *"Where is that transaction? Who begins it? Who commits it? Who aborts it?"* *"Not impossible. You can write your own transaction coordinator, but it's an unbelievable amount of programming."* |
| **Communication protocols** | Cross-platform requires interop, and interop is itself a coupling. |
| **Communication patterns** | *"Both COM and .NET use the call stack. So you push your stack frame into the stack of the caller, jump to the object."* Across a machine? Asynchronously? The call-stack mechanism itself breaks. |
| **Versioning** | *"Both COM and .NET bear scars of DLL hell"* — the runtime gives you *"exactly what you were compiled against."* Ship a better, stronger, faster, defect-free component: *"you know what actually happens? Absolutely nothing. Everybody gets the old one."* Both offer escape hatches into virtual resolution policy, *"except both of these mechanisms risk some degree of DLL hell."* |
| **Security** | *"Do I know it's not going to be called by malicious clients? No… I have to assume **all clients are malicious**."* Authorization is meaningless without authentication: *"answering what Joe is allowed to do without being sure it's really Joe is kind of pointless."* Identity mechanisms enumerated: username/password, mapped back to a Windows token, token directly, credentials from a database, biometrics, smart cards, certificates, distributed single sign-on. |

> [!danger] "HTTPS is not secure"
> *"HTTPS is not secure. I know you think it does… It's not secure. If you disagree, look up somebody called Edward Snowden… HTTP is absolutely not secure, it's an illusion of security."*
>
> What you need is **message security**: *"you have to encrypt a message and can send it even over non-secure or compromised channels."*

#### Aside: Async, and Why Syntax Cannot Fix a Design Problem

*"Async and await is something that **Anders Hejlsberg** promised me in 2004 he's not going to do,"* because Juval had asked him for something else; *"he sighed and said to me in his soft Danish accent…"* Then:

> [!quote] "When languages do this, they show their age. Twenty years later, they're scraping the bottom of the barrel for wicked, useless anti-features."

- **Why async ever appeared:** *"The level of care has changed."* Early business computing in VB / classic Windows: *"If you had to press a button and wait 10 minutes, it was better than going to the file room downstairs and use the Xerox machine."* Today *"nobody expects to have blocking applications."*
- **Razor blades to babies.** When .NET opened a multithreaded environment to former VB6 developers, Juval told Microsoft *"this would be like giving razor blades to babies."* Not a knock on razor blades: *"we just don't give it to babies… It's not that the C guys were any better off. They were just more accustomed to blood."*
- **Who async is actually for:** *"The vast majority of all applications out there are simple forms over data. So to solve that problem, you have async. However, **async is not for you**."* You have failures, distribution, retries, transactions — *"It doesn't do any of these things for you."*

> [!danger] The kill shot on async-as-syntax
> *"The problem of the asynchronous concurrent call is fundamentally a **design** problem. Can you solve a design problem using syntax? You know the answer for that. You cannot solve it. It requires a different design."*

#### It Is All Plumbing

Interoperability, hosting, activation, concurrency management, transactions, communication protocols, buffering, communication patterns, versioning, security —

> [!quote] "Is this business logic? Is this added value to customers? No. **This is plumbing. This is the gray glue that holds everything together.**"

**The measured number:** *"This was actually measured. The average application has between three and seven percent business logic and the rest is plumbing. You average that, you get five percent. So it's **95% plumbing, 5% business logic**."*

**Why the number is bad — stated as cost, not lines:** *"It's not so bad because of the number of lines of code. Lines of code could be 50-50, 60-40. The problem is **cost of ownership**."* Business logic: *"I should have inserted into this table, then into that table."* Plumbing: *"I'm coming on this before I started the transaction, if I haven't authenticated yet."* → *"Which would you rather debug? Which would you rather own? Again, it's always about cost."*

**Nobody cares:** *"Anybody here has a customer that cares about plumbing? No. Managers that care about plumbing? No — managers care about features, budget, deadlines, and if you're very fortunate, they care about quality."*

**The expertise inversion:** *"Anyone here is a world-renowned security expert? No? Unfortunately, **the hackers are world-renowned security experts**."* Distribution transactions: *"I can show you issues involving two lines of transactions that make blood shoot out of your eyes."* → *"By your own admission, you suck at it. So let's count our blessings: you're going to spend 95% of the effort on something that nobody cares about, and you're going to suck at it."*

**The duct-tape escalation** — a direct application of part 1's analysis-vs-synthesis law: *"Nobody's ever going to give developers enough time to do good plumbing… Developers are always given enough time to do the dirtiest piece of plumbing they can possibly get away with."* → *"In no time at all, the system becomes a giant ball of duct tape."* → **"What is the cost of analysis of a giant ball of duct tape? It's astronomical."**

*(Observed bottom-up in [[Modules/Microservices Development Process]]: the same claim appears there as the fractal view of code — lots of asserts, then a little business logic at the bottom.)*

#### Don't Do Plumbing — But Have It

> [!important] The one lesson of the module
> *"Don't do plumbing. That's it. If there's nothing you learn in this module, it is that you shouldn't do plumbing. Because every time you do plumbing, you commit a **sin of productivity** — against your customer who doesn't care, against your manager who doesn't care, against your future colleagues."*
>
> **"What part of 'nobody cares' don't you understand?"**

> [!success] The hinge of the whole lecture: have ≠ do
> *"You've all heard something I never said. I didn't say you shouldn't **have** plumbing. I said you shouldn't **do** plumbing."*
>
> → *"How about use ready-made off-the-shelf plumbing?"* → **"Reuse? Absolutely."**

Plumbing is genuinely required — security, transactions, synchronization. What is a sin is hand-rolling it.

#### Twenty Years of Ready-Made Plumbing, Unused

| Year | Thing | Juval's verdict |
| --- | --- | --- |
| **1994** | `CoCreateInstance` / COM born | Premise for everything below — see **The Cleanup (~1997–98): C# and the CLR** above |
| **1996** | **MTS — Microsoft Transaction Server** | *"The world's very first application server platform."* *"An awful name… there is nothing called a transaction server. It doesn't exist."* It was *"like a warm blanket wrapping the code,"* managing concurrency, transactions, security, activation, versioning. |
| **1998** | **J2EE** | *"A clean copycat of MTS down to copying the names of the APIs. And then they had the audacity of claiming to invent it in the first place."* → *"If you base your entire business model on plagiarizing other people's work, eventually go out of business."* |
| **2000** | **COM+** (Windows 2000) | *"Which had nothing to do with COM or with Plus."* MTS plumbing integrated into Windows. |
| **2002** | **Enterprise Services** | *"Probably the least known namespace in all of .NET."* Did all of it **declaratively**, available from .NET 1.0. |

*"Ever since the middle of the '90s, like clockwork, every two years, a release of ready-made off-the-shelf plumbing. By and large, **nobody used it**."*

**The three-copies anecdote, used as evidence not vanity:** his COM+/Enterprise Services book *"sold three copies"* (wife and mother bought the first two); the next book, **Programming .NET Components**, was *"the number one programming book in the world in sales"* — on the Amazon general reading list where *Harry Potter* was #1, *"my book was 140 for a year."* O'Reilly made "an unbelievable killing"; it paid for his house in California. *"So it wasn't the author. Same author. Same writing style. Same vain attempt at slipping the word 'monkey' past the editor."*

#### The Boundary Problem

*"No system is completely an island."* COM+ ↔ J2EE: *"Could you have a COM+ transaction going to J2EE? No."* So at the boundary you **dummy down**; then the neighbouring component dumbs down too, because whoever it speaks to "doesn't speak its flavour of the plumbing."

> [!important] "The boundaries creep from the outside in, preventing you from using ready-made off-the-shelf plumbing."
> Verdict: *"Ready-made off-the-shelf plumbing is very useful, except it's useful **in isolation**. And no system is that isolated. Close but no cigar."*

#### The Second Idea: Standardize the Plumbing

If COM, .NET and Java all use the call stack, can a .NET stack frame jump into Java? No. *"Ah, you can send them a message."* Then standardize the message: structure, header, payload.

**Standardizing even the data types.** A string is: null-terminated string, `BSTR` in VB, `CString` in MFC, `string` in .NET, `String` in Java, `_bstr_t`/`_ustr` in ATL and STL. An integer: 16-bit, little-endian, 64-bit, signed, unsigned. *"They basically started a massive effort of standardizing the world."*

> [!note] "WS" does not mean web services
> The standards are incorrectly called "the WS things" — WS-SecureConversation, WS-SecureMessaging, WS-Transaction, WS-Reliability. **"WS incorrectly stands for web services. This has nothing to do with web services. The correct interpretation of WS is *wire spec* — what goes on the wire."** A monumental effort.

**The architecture, in one paragraph:** *"Inside your node, your little piece of heaven, you can use whichever technology you use as your native plumbing. And when you reach the brink of your system, you use some kind of technology to create the message, put the plumbing aspects — your transaction ID and security token — in the message and send it to the great beyond. The great beyond intercepts that message, de-messages it to their native representation, starts a transaction with that ID, authenticates the call, executes it natively with their plumbing,"* with a response message and everything in reverse on the way out.

**Result:** keep the boundaries where the boundaries are **and** get ready-made shared plumbing.

#### The Definition of Service Orientation

> [!quote] "And if you understand that, you understand service orientation. **Service orientation is simply the next step in this journey. It's the attempt of decoupling the code from the plumbing aspects and providing standard ready-made plumbing.**"

**Purpose of the history lesson:** *"The main purpose for the history lesson of today is that you actually understand this very long-term trend so you can actually see what is coming and look around corners."*

**The chain, verbatim:**

> [!quote] "**The service is the evolution of the component, and the component is the evolution of the object, and the object is the evolution of the function, and the function is the evolution of the go-to, and you can trace it all the way back to the rotors of the Enigma.**"

**Anti-marketing frame:** *"Service orientation is, to the best of our knowledge, the best way of building any system."* But: *"Vendors always try to portray everything as an unbelievable quantum leap. It's not — it's just the next step in a very long journey. It's been going on for almost a century."*

**The book.** He believes he wrote *"the world's very first"* book on services: **".NET Component Services"** (O'Reilly, **2001**). He wanted to call it ".NET Services"; the editor insisted on "Components" because *"nobody knew what services were, so everybody knew components."*

**The pattern broke — and is still parked.** *"This pattern was actually broken in recent years, because the move from **WCF to Web API** is definitely not a step forward."* Cause: *"another very long-term trend that lasted 50+ years [is] also broken. So that triggers breaking of this."* Then: **"We're gonna discuss why demonic. For now, just park that thought."**

> [!warning] Still unresolved — and this is part 1's warning, unresolvable from either recording
> Part 1 warned of *"an up-and-coming contender that's going to be an even bigger disaster."* **It is not named here either.** The WCF→Web API remark is the closest adjacent material, and he explicitly parks it. Do not resolve the warning from either recording.

#### The Four SOA Tenets

*"They came up with a set of principles and called them tenets. I don't like the word tenets because it's presumptuous. Have you heard about aeronautical engineering and tenets?"* He covers them **"just to prove to you that it's not actually new — that all of these things are just modern manifestations of the same idea, again and again and again."**

| Tenet | The old idea | Credit |
| --- | --- | --- |
| Service boundaries are explicit | encapsulation is good | **Parnas, 1972** |
| Services are autonomous | loose coupling is good | **Parnas, 1972** |
| Services share an operational contract and data schema | separate interface from implementation | **Lowy, 2001** — *not* Parnas |
| Services are compatible based on policy | the C header file, extended into plumbing | the metadata ladder |

**1. Service boundaries are explicit** → *encapsulation is good.* What's newly encapsulatable: in .NET C-to-C you *know* the other party is .NET — you cannot encapsulate that. With services *"who knows who the other party is?"* So betraying **technology** on the service interface is *"probably not a good idea."* Same for **location**: *"If I'm calling a C object, I know it's running in my process. But if I'm calling a service, it could be the other side of the planet."*

**2. Services are autonomous** → *loose coupling is good.* Things you *cannot* decouple in C#: share the address space ⇒ **no security isolation**; share the address space ⇒ **no fault isolation**; same process ⇒ **you loaded the same version of .NET**. Services must not reintroduce that: *"the object should not be at the mercy of its client as far as securing it — the service is secure regardless of what the client wants to do."* Faults: *"the server should be able to handle its faults independently; the client doesn't need to reach down and clean up things. That's just an awful idea."* Plus independent versioning/evolution and different configuration/devices.

**3. Services share an operational contract and data schema** → *separating interface from implementation.* **Parnas did not write about this — "Mr. Lowy" did, in the 2001 book**, as *the core principle of component orientation*. The contract says **what** the server is supposed to do, not how, not what's under the covers, not the technology, not the platform. *"Then you can evolve the implementation separately from everybody else, and everybody is happy."*

> [!note] The 1972 payoff, delivered
> Part 1's promise — *"another thing happened in 1972 — we'll see it Friday morning"* — resolves here. Tenets 1 and 2 are each introduced with **"David Parnas wrote about it in 1972."** The whole point of the tenets section is to show they are not new. He never says "and *that* was the other thing"; the two Parnas call-backs **are** the payoff. Note he explicitly **excludes** Parnas from tenet 3 and credits himself.

**4. Services are compatible based on policy** — the modern incarnation of the C header file. The ladder: **C header file → binary metadata / type library → .NET or Java metadata embedded in the assembly.** Assembly metadata's advantage: **no hope and a prayer, because the compiler forces compatibility** (publish a signature and the compiler rejects passing a string where an int is expected).

But signature compatibility covers only **one axis**. There is a second axis: **plumbing**. If the object wants security and the client says *"no, we don't need any security, allow me in,"* that call is signature-compatible and *plumbing-incompatible*: *"it's the modern equivalent, plumbing-wise, of having no type safety."* If the object checks it itself, *"all of a sudden it starts polluting the object code with plumbing, which is the one thing you don't want to do."*

**Fix:** publish **plumbing metadata**, visible to the client, so the client knows what plumbing to send; put interception code in front of the object that inspects the message — *"the object says security, you're trying to call without security, deny the call. And the object doesn't even know the call is denied."* Compatible messages reach the object, which *"just executes business logic, rest assured that all its expectations of the runtime have already been met."* Conceptually: **expanding the concept of metadata into plumbing.**

> [!note] Inside vs between
> *"Inside services, you can still have old concepts of languages, technologies, .NET, 8, 7, and all these things. But **between** services, all you should see is standard policies and messages."*

**Business framing:** *"We are not in the methodology business, we are in the application business: on time, on budget, and with zero defects, of course."*

> [!tip] Contract material lives elsewhere — but not in this lecture
> Tenets 3 and 4 — the operational contract, data schema, and the plumbing-metadata mechanism — are **service contract design**, not intro-to-SOA. They are kept here because that is where Juval teaches them.
>
> **Status check after importing the contract lecture:** [[99-Resources/Transcripts/Service Contract Design|Service Contract Design]] does **not** supply this material. That lecture is about contract *quality* (facets, coherence, independence, reuse, factoring, metrics); this material is about the *runtime compatibility mechanism*. Different vocabulary — no `schema`, `metadata`, `policy`, `type library`, `header` or `Parnas` anywhere in it. So this remains an **open gap**: nothing has been migrated, and there is no recording yet that closes it.
>
> What the contract lecture *does* provide is the **payoff** of the premise promised here: if the interface is the only reusable element, then contract quality becomes the whole design problem. See [[Modules/Service Contract Design and Factoring#Service Contract Design]].

### Service-Oriented Applications

- [Transcript](../99-Resources/Transcripts/Service%20Orientation.md)

#### What a Service Is

> [!quote] "A service is a **unit of functionality exposed to the world over standard plumbing**."
>
> Immediately followed by: *"I really, really, really hope that when I said unit of functionality you did not hear **feature**. God help you."*

**The jumbo jet test.** A jumbo jet has a single **feature**: fly from A to B. Look inside: *"Is there any component in my jumbo jet that's doing the flying from A to B? No. But I do have a lot of services."* The **fuel pump** is a unit of functionality — *"What is functionality? Pump fuel. It doesn't have a feature, by the way."* *(Same example, different lesson, in [[Modules/Project Planning#Terse Requirements at the Service Level]] — cross-link, don't re-tell.)*

**The definitional ladder — same sentence, three dates:**

| Year | Definition |
| --- | --- |
| **1973** | *"A **function** is a unit of functionality exposed to the world."* |
| **1994** | *"A **component** is a unit of functionality exposed to the world."* |
| **Now** | *"A **service** is a unit of functionality exposed to the world **over standard plumbing**."* |

*"Get it? Nothing has changed. It's just the next step in a very long journey. **What is new here is that how you expose it is over standard plumbing.**"*

#### Composition, Recursion, and the Integer

Take a bunch of services, glue them together, that's your application or system — *"Isn't that the same diagram we started Monday morning? Yes, the same diagram."* Expose the aggregation as a service to the outside world. Double-click any service to see its comprising services, all the way down.

> [!important] "Taken to the ultimate conclusion, the integer must be a service. Why? Because **plumbing is evil regardless of scale**."
> At the enterprise, system, subsystem, class, and primitive levels — *nobody cares.* *"Do you enjoy synchronizing your integers? Do you enjoy securing your streams?"* Imagine transactional integers, transactional arrays, inherently secured strings, never having to synchronize booleans. *"And this is why this has nothing to do with enterprise programming. **Nothing.**"*

This is the direct answer to the vendors' **second sin** in [[#Why Service Orientation]] — that service orientation is an enterprise-only affair.

#### The Ten Principles

##### Practical — the design-review gate

*"If I'm doing design review and I don't see these things, **you fail**."*

1. **All services are secured.** *"No if, no but, not in our case. You are secured. Always."* Caveat: *"Did I say you provide the security? No. But you have to be secured."* Parenthetical: **"(HTTPS is not security.)"**
2. **All services leave the system in a consistent state.** *"Once a call returns, there's no debris to pick up, no leftovers."* Why: if there is, the callee already returned, so the **client** must clean up — *"think about the insane level of coupling you now enforce on the client that has to know the inner workings of the service"* — and you may have **millions of clients**.
3. **All services are thread safe.** *"You can and you will be accessed by concurrent clients."* The point is that **you** provide the synchronization, not the platform.
4. **All services are reliable.** *"Every call has exactly two outcomes: the call gets there and you know about it, and the call doesn't get there and you also know about it."* The forbidden third: *"Maybe the call got there."* → *"How would you program against these cases?"* Parenthetical: **"(Is HTTPS or HTTP reliable? Since the answer is no, you know what the inescapable conclusion is.)"**
5. **All services are robust.** *"It's not okay to blow up and take down the system with you. Proving you are gone is not a good way of building a system."* Whatever happened inside, you handle it and isolate your own faults.

##### Operational — "really nice to have"

*"You can make up a story why you don't have it, and maybe that's okay. But between you and me, you really need to comply."*

1. **Interoperable.** You can say *"I'm holding both ends of the stick, I don't care."* True — but *"when you write your services as if it's another technology, another party, you gain another degree of decoupling, which is also very nice internally."*
2. **Scaling-variant.** *"It's the same service code if I have one client or ten thousand clients. It's the same service code if I have one client making one call or one client making 10 million calls."* Excuse: *"I have two calls a minute, my cell phone can do it."* Counter-benefit: it makes **queuing and transactions** easier.
3. **Available.** *"When a client makes a call and sends a message, there's somebody home to handle it."* If nobody is home, the **client** must deal with it — *"if you think plumbing on the service is bad, what about plumbing on the client?"* Bar: *"Always available. 24 by 7. I'm not talking about six sigma, I'm talking **infinite sigma** here. Now put aside the fact that you have no idea how to do it — I'm just telling you where the bar is set."*
4. **Responsive.** *"Suppose you're 100% available, but it takes you two days to start processing the call. Good or bad? Probably bad."* Because the client **cannot tell the difference between unavailable and merely unresponsive**, and has to guess. *"Call comes in, bam, you start processing it."*
5. **Disciplined.** *"You don't block the client for long."* You can be 100% available and 100% responsive and still take two days to return — and the client can't distinguish unavailable / unresponsive / undisciplined. *"I'm not saying don't do lengthy processing. Do every lengthy processing you like, just do not block the client while you're doing it."*

> [!tip] Why the distinction matters
> The **practical** five are correctness guarantees about *your* service. The **operational** five are qualities the *client* can rely on. They matter because unavailable / unresponsive / undisciplined are **indistinguishable to the client** — and any ambiguity pushes plumbing onto the client, which is the one thing the whole module forbids.

#### Vendors: The Drug-Doctor Analogy

*"You never ask the vendor for advice on using their stuff. Ever."* Car dealer: *"Is today a good day to buy a car?"* Drug company vs. doctor: *"The doctor is not going to tell you to take the drug… What is the doctor going to tell you? How about you shed some pounds and start exercising. We are probably at least a century away from having any drug that will come even close to how important it is to exercise."* So: *"Before you run for the chemistry, how about you exercise?"*

*"I'm not even talking about the fact that apparently we need more than 640K and apparently the browser is important. I'm looking at you, Billy Gates."*

#### The SOA Vendor Clip

He shows (and decodes) the well-known skit mocking vendor SOA marketing:

- **The red blazers** — *"SOA's all in the database, dude."*
- **The blue suits** — *"You will migrate to our software, hardware, and professional services. That's IBM, Big Blue."*
- Running gags: *"SOA? No problem. All you have to be is migrate to our hardware and software. And services. And hardware."* / *"Sounds like these guys have a strategy. But so did the Borg."* / *"Too much SOA for one man… Sounds like architectural overdose."* / *"Maybe we should send out an SOA SOS."*

**The moral:** *"Notice how all the vendors are trying to sell you something. They're all equating whatever you want with whatever they're selling."* — the **two-sins thesis** from [[#Why Service Orientation]], restated. *"You can imagine the level of frustration that made somebody produce that clip."*

## Numbering Discrepancy

> [!warning] The vault's module numbering is off by one from Module 4 onward
> The MOC lists this as **Module 4**, but this note's frontmatter says `module-3`. The same off-by-one affects every note from here on, because **Project Planning** was inserted as Module 3 after the other notes were written:
>
> | Module note | Frontmatter says | MOC says |
> | --- | --- | --- |
> | Introduction to Service-Orientation | `module-3` | **4** |
> | Service Contract Design and Factoring | `module-4` | **5** |
> | Design and Architecture | `module-5` | **6** |
> | Design Aspects | `module-6` | **7** |
> | Agile and Design | `module-7` | **8** |
> | Groupthink | `module-8` | **9** |
> | Architect in Age of AI | `module-9` | **10** |
> | What Comes Next | `module-10` | **11** |
>
> Notes 1–3 (`The Architect`, `Microservices Development Process`, `Project Planning`) are correct. Transcripts for this module use `module-3` to stay tag-consistent with this note.

## Quiz

> [!question]- 1. Juval claims vendors commit "two sins" when discussing service orientation. What are they, and what economic incentive drives the second?
>!
> [!summary]- Answer
> **Sin 1:** vendors equate whatever they are selling with whatever you are talking about — cloud services, professional services, databases, message buses are all "service-oriented." Self-refuting: they can't all be right, so at least some are wrong ("Murphy says they're all wrong"). **Sin 2:** claiming service orientation only exists in *enterprise* environments. The driver is **margin**: retail software has essentially no margin ("Microsoft makes more money from Android than Google"), whereas "when Coca-Cola is buying 100,000 Azure licenses, Microsoft is printing money." Hence the industry "has always been and forever will be fighting for the enterprise — that's the battleground."

> [!question]- 2. State the "analysis vs. synthesis" principle, and trace how it explains the failure of COBOL go-tos, C global variables, and C++ inheritance in one unified argument.
>!
> [!summary]- Answer
> **"In software, the cost of analysis far exceeds the cost of synthesis"** — you can spend three weeks analyzing a snippet only to conclude "it just adds two numbers," yet writing that same code is trivial. Writing is synthesis; debugging is analysis, which is why developers should write "the dumbest possible code." Applied uniformly: go-tos couple code to its own structure; global variables (`g_MyFlag`) require analyzing every other user of every other global; inheritance requires knowing base-class internals, override chains, and swapped root pointers. The common shortcut — a new module on the side, `g_MyFlag2`, a shadow member in your subclass — is *locally correct* but makes the global picture **non-linearly worse: not +1, but +N**, because "at some point, somebody, somehow, somewhere always has to figure out what all of them are doing."

> [!question]- 3. What is the "lift, shift, and drop" test, and what does the mouse/chair/stone-axe analysis establish about the *mechanism* of reuse?
>!
> [!summary]- Answer
> The test: take business objects written in one system, lift-shift-drop them into another, and everything works. **Nobody has ever done it.** Prying the *case* off a specific mouse fails because its curves and tang groove are specific to that mouse; unscrewing a *seat* fails because screw spacing and curvature differ. **The only reusable element in any entity is the interface to the thing, never the thing itself** — you can drive my mouse and yours, sit on my chair and yours; the interface is really "mouse–hand–tool." Since reuse is the most fundamental aspect of engineering, OO — which made the *object* the mechanism of reuse — "absolutely guaranteed that nobody is ever going to reuse anything," which is why *Object-Oriented Software Engineering* (Jacobson, 1988) is an oxymoron.

> [!question]- 4. Walk the deployment ladder: `.lib` → `.dll` → `LoadLibrary` (1988) → `CoCreateInstance` (1994). What problem did each solve, and what did each break?
>!
> [!summary]- Answer
> **`.lib`** (binary + header, "trust us") stopped `MyClass2.cpp` by withholding the `.cpp` and partially separated teams/vendors — but made the giant-exe problem *worse*. **`.dll`** is a *renamed* `.lib` plus runtime linking (stubs patched with function pointers after loading) — tiny exe, deploy one DLL — but required hefty hand-written linking code. **`LoadLibrary` (1988)** moved that into the OS. Great for app vendors, terrible for DLL vendors: installers squirt DLLs into the **Windows folder** (the one folder guaranteed to exist) and overwrite whatever is there, forcing **backward compatibility** — which cannot be proven, only "we tested so much we couldn't tell." App A (v1) + App B (v2) → the older DLL smashes the newer and **app B blows up**, since backward compatibility says nothing about forward compatibility: **DLL hell**. **`CoCreateInstance` (1994)** fixes it: **GUIDs** identify versions, a global dictionary (registry) maps GUID → path, the required GUID is baked into client code, and lookups are force-fed to `LoadLibrary` — enabling **side-by-side** versions and hot patching. That is COM: the fix is *interfaces and binary metadata*, not better linking.

> [!question]- 5. Why is 1972 "the most important year in the history of software"?
>!
> [!summary]- Answer
> Three things converged. (1) **Structured programming** emerged — don't use go-to, write functions, so a function can be examined **in isolation**, drastically cutting the cost of analysis. (2) **David Parnas** published the five-page *"On the Criteria To Be Used in Decomposing Systems into Modules"*, which contains information hiding, encapsulation and decoupling — **the birth of modern software engineering**. (3) **The term "software crisis" was coined.** Juval's thesis is that the coincidence isn't accidental: the crisis is attacked by applying engineering principles. He adds that Parnas's 1978 *"Designing Software for Ease of Extension and Contraction"* describes **interfaces** decades before the vocabulary existed. (The "another thing happened in 1972" promise resolves in part 2: it is Parnas's 1972 paper, credited for two of the four SOA tenets.)

> [!question]- 6. Juval's slogan is "Don't do plumbing." What exactly does he say he did *not* mean, and what follows from the distinction?
>!
> [!summary]- Answer
> He did **not** say you shouldn't **have** plumbing — he said you shouldn't **do** plumbing. *"You've all heard something I never said. I didn't say you shouldn't have plumbing. I said you shouldn't do plumbing."* The follow-up: *"How about use ready-made off-the-shelf plumbing?"* — i.e. **reuse**. The distinction matters because plumbing is genuinely required (security, transactions, synchronization); what is a sin is hand-rolling it, since you'd spend 95% of the effort on something nobody cares about and that, by your own admission, you suck at.

> [!question]- 7. What is "the boundary problem," why did it kill twenty years of application-server plumbing, and what is the fix?
>!
> [!summary]- Answer
> No system is an island, so at the edge you cannot flow your proprietary plumbing to the other side: *"Could you have a COM+ transaction going to J2EE? No."* You therefore dummy down — and then the *neighbouring* component dumbs down too. Result: **"the boundaries creep from the outside in, preventing you from using ready-made off-the-shelf plumbing."** Ready-made plumbing is useful *only in isolation*, and no system is isolated — *"close but no cigar."* The fix is to **standardize** the plumbing and move it into a **message** instead of a call: at the edge of your system, put transaction ID, security token etc. into a standardized message; the far side intercepts, de-messages it into its native representation, starts the transaction with that ID, authenticates, executes natively, and replies with everything in reverse. Boundaries stay where they are, and both sides keep ready-made plumbing.

> [!question]- 8. Give the definition of a service, and explain the jumbo jet / fuel pump example and the 1973→1994→now ladder. What is actually new about services?
>!
> [!summary]- Answer
> **"A service is a unit of functionality exposed to the world over standard plumbing."** He immediately warns against hearing *feature*. A jumbo jet's single *feature* is fly from A to B, yet not one internal component flies from A to B — but it has many *services*, e.g. the **fuel pump**, whose functionality is simply "pump fuel." The ladder shows nothing changed in the definition, only in the exposure mechanism: **1973** — a *function* is a unit of functionality exposed to the world; **1994** — a *component* is; **now** — a *service* is, **over standard plumbing**. The new part is purely *how* it is exposed. Pushed to the limit, the aggregation of services is itself a service, recursively, **down to the integer — because plumbing is evil regardless of scale**, which is why this "has nothing to do with enterprise programming."

> [!question]- 9. Name the five practical and five operational principles, and say what distinguishes the two groups.
>!
> [!summary]- Answer
> **Practical (mandatory — "if I'm doing design review and I don't see these things, you fail"):** secured; leaves the system in a consistent state; thread safe; reliable (exactly two outcomes — never "maybe it got there"); robust (never take the system down with you). **Operational (optional at review, but comply):** interoperable; scaling-variant (same code for 1 or 10,000 clients, 1 or 10M calls); available (somebody home, 24×7, "infinite sigma"); responsive (start processing immediately); disciplined (never block the client while processing). **Distinction:** the practical five are correctness guarantees about *your* service; the operational five are qualities the *client* can rely on — and they matter because unavailable / unresponsive / undisciplined are **indistinguishable to the client**, so any ambiguity pushes plumbing onto the client, which is the one thing the whole module forbids.

> [!question]- 10. Which SOA tenet does Juval *not* credit to Parnas, and why is "compatible based on policy" the header file expanded rather than invented?
>!
> [!summary]- Answer
> **"Services share an operational contract and data schema"** — separating interface from implementation. *"David Parnas did not write about it. However, Mr. Lowy wrote about it in his book published in 2001,"* as the core principle of component orientation. (Parnas, 1972, is credited for the other two: explicit boundaries = encapsulation, autonomy = loose coupling.) Policy-compatibility is the latest rung of a long ladder: **C header file → binary metadata / type library → assembly metadata**, where assembly metadata's win is that the **compiler forces compatibility** instead of "hope and a prayer." But signature compatibility covers only one axis: **plumbing** is the other. A call that passes an int but carries no security is *"plumbing-wise, the equivalent of having no type safety."* Letting the object check that itself pollutes business logic with plumbing. So publish **plumbing metadata** visible to the client and intercept the message in front of the object: deny incompatible calls without the object ever knowing, and let compatible ones through to pure business logic. Same idea as the header file, extended into plumbing.

## Related
- [[MOC — Course Overview]]
- [[Modules/Microservices Development Process]]
- [[Modules/Service Contract Design and Factoring]]