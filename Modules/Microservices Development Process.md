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
- [x] Architect and the team
- [x] Developers onboarding
- [x] Career of the architect
- [ ] AI and future of development
- [ ] AI and agility
- [ ] AI spec-driven development
- [x] Quality assurance
- [x] Quality control
- [x] Design for performance
- [x] Services simulation and emulation
- [x] Peer reviews
- [x] Development and design standards
- [x] Metrics collection
- [x] Logging and the flight recorder
- [x] Management visibility
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

> [!note] Pointer — the substance lives in Project Planning
> The hand-off point is quantified in [[Modules/Project Planning#Hand Off Point — Senior vs Junior Handoffs, Team Models & the Architect's Role]]: senior-vs-junior team models, ~1 week per service across 10–40 services, and the batching pattern where senior architects detail-design the next batch while juniors implement simple programming tasks.
>
> [[99-Resources/Transcripts/Contract Factoring in Practice|Contract Factoring in Practice]] gives the same argument from the other side — *what happens when you don't acknowledge it*. Two things worth knowing from there:
>
> - **The failure is instant, not gradual.** *"For them, one big thing with 7,000 methods is just fine. If you let them do it, of course they're going to butcher it. They are instantly going to go to the edges of the curve and then you're dead."*
> - **The missing skill is detail design**, which he insists is *"separate and distinct from architecture, and separate and distinct from coding"* — and which is where developers lack the most, because *"nobody taught them, nobody trained them."* Architecture is *"a blink of an eye, an hour a day"*; detail design is *"weeks, months."*
>
> See [[Modules/Service Contract Design and Factoring#The Cost of Factoring — and Why Organisations Fight You]].

### Architect and the Team

- [Transcript](../99-Resources/Transcripts/The Architect's Career.md)

- **The architect is a salesperson.** You sell yourself to management who must trust you, sell your design to developers who must follow it without understanding every last insight, and sell your work to other architects who will critique and review it.

- **The architect must be an extrovert**, even though developers are introverts by roughly **2 out of 3**. The joke: talk to an introvert developer and he looks at the tip of his shoe; talk to an extrovert developer and he looks at the tip of *your* shoe.

- **Evidence for introverted developers.** *Bell Labs (1980s):* ask team leads who their best developers are, then run personality studies. Common attributes (ratio 2:3) — affinity to **music** (love listening or play an instrument); affinity to **languages** (eloquent in English, especially writing, or multilingual); **lower tolerance to BS** than average but **higher ethics**; and they **prefer family to work**. *Myers-Briggs study:* a Pascal program seeded with **24 defects**, developers sorted by how many they found (almost all found 6, many 12, few 16/20, a handful 24), then MBTI'd → **INTJ**. Juval dislikes the criterion: being good at *finding* defects ≠ the qualifiers of developers who *never have* defects.

- **Design-review body language, two caricatures.** Slumped shoulders, turned away, mumbling "this design… maybe… the best we could, I mean, maybe." Versus looking **30 degrees over the horizon** — "you are a man of vision, you see things mere mortals do not see" — open body: "come, come with me into the light. This design is the best thing since sliced bread. Maintainable, extensible, reusable. **The competition is already dead. D-E-A-D.**"

- **Management "cannot tell design from orange juice."** They judge you on what they do understand: confidence, body language, inspiration.

- **"You're never gonna get a second chance to give a good first impression. Every interaction has to count."** Rehearse it in your mind, have ready-made answers for everything, see around corners — anticipate what they'll ask and why.

- **Why developers resent reviews** (especially design reviews): a review **exposes the way your mind works** — for an introvert it's "like exposing yourself in public," so they'll make every excuse to avoid it. Architects **thrive on review and criticism**: "Oh my god, I didn't think about that. Thank you so much. Imagine we would have gone to production with this."

- **"Salesperson" does not mean** tweed jacket, grease in the hair, selling a used car with no tires. It means: *"Is the team better off with this design or without it? With. Why? Because of this and that. Then say so."* **Inner conviction is what makes the sale. If you're not convinced, they're not going to be convinced.**

- **Self-training drill:** put the portable video studio in your pocket in front of you, explain in a few sentences why an idea is good, watch it. It made you cringe? Fix it. Do it again. His **Project Design Clinic** works the same way: the winner starts as a bumbling idiot and, after about **three and a half hours** of coaching (overall message of the presentation, message of each slide, how to say it), delivers a TED talk that gets applause. When he started in the industry you did dry runs weeks in advance with devil's advocates and pre-planted questions to show teamwork. **"Leave nothing for chance."**

- **Board presentations:** nice jacket, and once a year a tie. Then he realized: **"They're not reviewing my design, they're reviewing me. Who is this kid we're going to trust with the future of the company?"**

- **Never ask permission to do things. Start doing them. Lead by example.** Don't explain how — do it. Once it's successful, *then* ask "how is this working for you?" and explain. Start by doing, not by converting people.

- **The elevator pitch works** because as the doors close the manager runs a calculation: what's more expensive — asking you to shut up, or enduring it in silence for two floors? Silence is cheaper, so they endure. He has also stalked managers down hallways to walk them out of the building.

- **Y2K story (late 1990s).** Y2K was "the monster hiding under the bed of the software industry"; well-run companies began 4–5 years early. Juval, then division architect, had his sights on enterprise architect and a cross-division architecture that transposed relationships, commoditized the high-end front end, broke the silos, and made things horizontally open. Given 20 minutes at the company-wide Y2K meeting with every manager and architect present, slide 1 reported the Y2K scan (two time-related API usages, both relative; PDB binaries also clean), then he pivoted: *"Yes, it is a Y2K meeting. And we did talk about Y2K. Except we have another 18 minutes until the next speaker comes up. You all need to know this. Let's make the most of the time."* Years later people greeted him as "Y2K boy" — they remembered the hijack, not the content, which gave him a hook to re-open the conversation later. **"The selling never stops."**

- **"Every meeting, you are on review. Not the code — you."**

- **Only three ways to get any other person on the planet to do something: authority, power, influence.** Authority: "I'm the boss." Power: "if you don't do this for me, I won't do that for you." Influence: "do it because it's good — think of the children." **Architects are chronically short on power and authority** (no authority over developers); what they have is **influence** — the big boss turns and asks "so what do you think about that?" **"Stop yearning for the sticks you don't have."** If "selling" bothers you, say *evangelizing* or *influencing*; it amounts to the same thing.

- **"Nobody is minding the code"** — a worrying industry trend: nobody monitoring every line, ensuring consistency and design integrity, developers doing whatever they want. The counter is to be **hands-on in the trenches**: helping people with the code and reviewing their work is your **top priority**.

- **Prime directive of teamwork: never prevent others from doing their work.** If a code review is requested, drop whatever you're doing and do it.

- Being in the trenches sends the message: "I'm not some ivory-tower… I'm with you shoulder to shoulder." Developers secretly know they're delivering mud, so you must **spawn confidence** — "we're gonna work this way and it's going to work; keep up the good work and stay the course." Hedging ("maybe we should cut a corner here") produces instant dismay.

- Don't just tell — **show them how to do it. Lead by example.** "You can smack your ass once a week, but if they want to be better, absolutely educate them."

- **Basic team dynamic: criticize in private, praise in public.** Public praise makes everyone else ask, "What do I have to do to be that good?"

- **The design test.** Every technical decision must satisfy *"could somebody maintain this code several years from now, having never been in this room or heard these meetings?"* If no, you're not doing it right.

- **Natural doubt:** you inherit "lawless monkeys / code monkeys," shape them into formation, correlate them into structure, instill culture, discipline, quality. You will always remember how bad they were before you, so you fear they'll revert when you leave. Address it proactively.

### Developers Onboarding

- [Transcript](../99-Resources/Transcripts/Onboarding%20Developers.md)

- **Never prevent others from doing their work** — the prime directive of teamwork. Untrained onboarding makes developers "pull on the sleeve" of key team members; if that person is on the critical path, you just derailed the project. Corollary: **never help the new guy** — you don't do anybody a favor there.

- **The lightning rod is not the answer.** Designating one person for everyone to ask just gets that person bombarded with the same questions until they write an FAQ/wiki — the same repeated, wasteful, haphazard process.

- **Design the onboarding process.** "The only thing that grows organically is a tumor. Everything else in nature has a plan." Unstructured onboarding leaves hidden gaps, cartoonish first approximations, and neglected "boring" aspects (testing, documentation, design practices) that "will always come back to haunt you." If a developer inside the domain introduces a bug, it's because you onboarded them incorrectly.

- **Structure it by categories, ordered.** Domain first, then software design principles, system requirements, system architecture, detail design, framework, technology, process/cultural issues, standards, operations. Order categories by logical dependency (design principles before system specifics, technology before DevOps).

- **3–10 elements per category.** Fewer than 3 → merge into another category; more than 10 → split into subcategories.

- **Assign one owner per element** (two only when there are genuinely divergent opinions). The onboarding developer is *only* allowed to approach the owner — a single source of truth.

- **Estimate and track the effort** for each element. Track for two reasons: (1) variance detection — three hours planned but three weeks spent means you're missing information; three days planned but three hours spent means they missed something; (2) you can pit people against each other — "everybody is at 60–70%, you're still at 15%."

- **Post-onboarding interviews** — in-person, with both the architect and the domain expert, in groups and individually. Purpose: improve the process itself (find remaining gaps, refine onboarding) and transfer soft/folklore knowledge that resists documentation.

- **Documentation is key.** Good STD, operational concepts, recorded design meetings (transcription + AI summaries). Every onboarding element links to a resource (document, webcast, YouTube clip, meeting recording). Example: Juval's current project runs a 260-hour guided onboarding.

- **Onboarding is a primer, not the end.** "The onboarding must not be the sum of the learning. The objective is to kickstart the learning effort." It must dispel misconceptions (e.g., the "voodoo metastasized religion they call agile"), point developers at areas of expertise, and set the expectation: bare-minimum knowledge, know it "by heart and cold," resources there to revisit.

- **Establish rapport with the domain expert** — onboarding forces the developer to bridge the power distance and ask the executive/owner directly. "Don't guess. Go and ask the expert."

- **Domain cutters.** Short weekly sessions where a domain expert floats a question that forces research — not something you can Google. Good cutter questions attack the system's core value: "Why are we here in the first place? What's the market differentiator?" Track participation (tapering off is not okay) and correct answers to spot above-average developers. Compile solved cutters into a document and add to the onboarding — a growing "short book on the domain."

- **Culture of deductive knowledge sharing.** When somebody figures out something interesting about the domain, they can't keep it to themselves — shared knowledge is what adds the most value for the business.

### Career of the Architect

- [Transcript](../99-Resources/Transcripts/The Architect's Career.md)

- **"Charity starts at home. Don't try and fix the world if your own room is messy."** If architecture is all about design, **the very first thing you need to design is yourself** — who are you, where are you going, how will you get there, what if it doesn't work, what once you get there, where do you go from there.

- Even a grand design won't happen on its own: **"Nobody's gonna one day tap you on the shoulder and say, *Rise, you mighty architect.* Never gonna happen."** You must proactively plan ahead and execute that plan. For developers it doesn't work that way — "this project, that project, yeah, whatever." That is not a career.

- **"How do you become an architect?" — what Juval really wants to answer is "if you have to ask, it's already too late."** Nobody will let an architect be an architect unless they are *already* architects. Would you be the first patient of a doctor just out of med school, or fly with a pilot who just got licensed? "I want to be patient 10,000."

- **Three obstacles to becoming an architect.** (1) No credentials, no track record. (2) You were hired *as a developer* and have a contract saying so — leaving creates a developer shortage, so the company resists; companies love pigeonholing people. (3) If the company doesn't value architecture, they will never let you be one — **and you cannot learn to be an architect in a company that doesn't value architects**.

- **Everything has to be aligned. It starts by choosing the right company:** "Don't be an architect in a place that doesn't value architects. Don't be an architect where nobody can mentor you."

- **Strategic vs. tactical decisions.** Strategic: what to study, who to marry, whether to have kids. Tactical: practically everything else — where you work, where you live, what you do in your free time. **"The tactical should always be at the service of the strategic."** Strategic = **what**, tactical = **how**.

- Because it is strategic it takes time to execute (you don't marry the first person you date). Your career horizon is short — **you can't afford false moves**. If there are no architect opportunities where you live ("Boondoggle County"), *move*. Juval moved to Silicon Valley because in Flower Mound "you find four companies that need one" corporate architect. Remote work makes this easier today, but the question still applies: "Which job did you apply for? If you applied for a job as a developer, why surprised you're not working as an architect?"

- **Resolving the paradox of the "first chance":** for most people the only way to become an architect is to **start doing the job of the architect without the title, benefits, or authority**. The ideas are so transformative that opportunities appear, people notice, and the title follows. (His own always-being-the-architect case is "the exception that indicates the rule.")

- **Demand for architects far exceeds supply** — and this is *before* the industrialization of software, "which we know is around the corner." After this class "you will be the one in a million."

- **Interview reality:** a two-hour interview, and **two minutes in the interviewer has already made up their mind**. So don't shy from asking the right questions — they want you more, and "when they want you more, are they going to offer you more or less? … It's best for you, it's best for them." Repeated anecdote: people report **getting a promotion during the interview** ("Bob, can you come in a second? I think I found that VP position…").

- **It is often easier to succeed as an architect where you already are:** you know the players and the business. The grass-is-greener belief is an illusion — **"It's always giant balls of mud. It's always knuckle draggers. It's always code monkeys. It's everywhere."**

- Moving jobs is ranked roughly the **third most disruptive life event**, after death in the family and divorce. The fundamental reason you want to move is that **you have given up trying to affect change where you are** — "that means you are the problem, not the environment… the one thing you cannot get away from is yourself. If you are the problem, fix yourself, don't move."

- **The only legitimate reason to move: align your career phase with the environment.**

- **Career-phase map.** (1) Start in the most **pristine, immaculate environment** — no defects, standards, structure, rigor — to learn how to work correctly. Great learning, poor advancement, because there you cannot make a difference. (2) Then move to the most **decrepit environment** — "sh*t hot bottom," code full of defects, nobody can compile it, "a giant ball of mud on fire," developers jumping out of windows — because there **even a little bit of hygiene goes a long way**; "even just a little bit of light in the darkness chases away the shadows." (3) Then a senior position in a clean environment; then VP/director; then perhaps join a VC, identify opportunities, set up the environment correctly, get a card, move on. The fame you earn in the decrepit environment is "nothing but common sense" — never design against the requirements, basic project design, basic hygiene. That alone gives you enormous notoriety.

- **"That is the only reason to move. Not because it's bad where you are. It's always going to be bad."** And: **"Every move must count. You cannot afford sidewalk moves that don't move you ahead."**

- **Proof that planning works:** he knew he would found IDesign **eight years** before founding it; knew he'd be chief architect of a fortune-management company **two years** before, and was already doing the job two years before the title. As a mere division architect he convened meetings with peer division architects: "Show me what you're doing. Good. How can I help you do your job better?" Parking-lot story: a peer asked, "Juval, why are you doing this? This has nothing to do with your job." Answer: **"I've got my own agenda."** The alternative is "being a leaf in the hurricane."

- **Interviewing an architect: only attitude matters.** Integrity, accountability, responsibility, maturity, honesty — the same list always. **Competence is a distant second.** "I can teach a monkey to design systems. It's very difficult to teach integrity." Teaching attitude is expensive; people learn the hard way. Socrates: people only learn via pain — pain = time and money. Good attitude starts when you're four years old; too late to do much about it.

- **Screening protocol.** Every architect job description floods you with hundreds of pretenders and impostors — "there's nobody home." Tell every candidate to read **chapters 2, 3, 4 and Appendix B of *Righting Software***. Reject immediately those who don't read it — and arguably reject those who read *only* the assigned chapters ("how could you get to chapter 4 and not continue to chapter 5?"). Next gate: ask what they think of the book. **Disagree → reject.** Agree → ask: *"Whose fault is it that in the current project and all the previous ones you didn't follow these ideas?"* **Hire only those who admit it was their fault** — "they should have known better; it was their job to be the architect." Anyone blaming the scrum master, the customer, the manager, the boss, the environment, the legacy, the culture → reject. "Excuses. Stop saying *in my environment*, *in my case*." Proof: "Imagine I were to trade shoes with any one of you. You think I would have any problem working correctly? If the answer is no, then you're the problem. It's as simple as that." Counter to "why didn't I take this class 20 years ago?" — "when the student is ready, the master appears."

- **Leading questions about their recent project:** Was there a schedule? Did you meet the deadline? Was there a budget, a plan, any notion of time and cost? "If you didn't have any notion, then how could you expect anything good to ever happen?" Are there defects? Is that OK? What did you do about it?

- **Agility grill:** they start paying homage to "a voodoo-like masquerading religion called Agile." Ask: "Do you feel you can quickly respond to changes in your current project?" If no — "Then why do you call it Agile? Isn't the essence of agility the ability to respond quickly to changes?" Ask "What is Agile?" and you get rituals; ask for the essence and you get a blank stare — cargo-cult culture. **Reject everyone doing rituals for the sake of rituals.**

- **The portfolio question:** "Can you please show me your portfolio?" Juval keeps a whole shelf of folders, one per successful project: project plan, tracking, earned-value tracking, project post-mortem, architecture, project design. "Are you embarrassed or ashamed of your past record? If you've got anything to hide, it wouldn't be on the portfolio." Ask about schedule/budget/quality track record, how many times they shipped without defects, how long their architectures survived (a year? two? nobody makes a decade).

- **Avoid technical competence questions entirely** — irrelevant and immaterial. Pretenders divert the conversation to how many serverless expressions they know in AWS. "Technology is irrelevant here." Ask competence questions only if you have ample supply of good-attitude candidates — which you won't.

- **A deeper effect of the right questions: asking them attracts the right people.** "The right people crave quality. They are dying to work correctly. They are dying to take pride in their handiwork. They are sick and tired of the waste and the insanity and the ball of mud." Show them your documents, standards, and how far they can go and "they're gonna work there for free" — people offer to *pay* to be a fly on the wall for a week. Developers tell headhunters, "You cannot pay me enough to move away from here." **High standards attract high-standard people. Quality attracts quality. Success breeds success.** (Side effect to be aware of: asking the right questions also "sets in the mind a decision that won't work for you.")

- **CV inflation:** they claim every three-letter acronym; in interviews "there's nobody home." Juval measured **30:1** — thirty interviews to find one developer he wanted to hire, at which point everyone else in the Valley was trying to hire that person. Conclusion: look for **non-technical qualifiers**. The ideal developer interview is "what's the name of your cat? Here's a guitar, play a few chords." HR's verdict: he'd be sued and fired in rapid succession.

- **Disengagement / how to end a project** — the opposite of the hand-off point. Staying on one project forever is a career-limiting move; you need more feathers in your cap. Classic pitfall: sticking around to **control** people instead of making them better. **"If the project cannot survive without you, you've failed as an architect."**

- Many software managers and executives have **contempt for developers** — "every commitment was written on ice, promised agility and delivered mud." So when a trustworthy, business-fluent architect shows up, "there's a responsible adult in the room." Management then resists the architect leaving, and the role **devolves** from addressing real architecture and process needs to being "the guy they trust." That is not a good sign.

- **Groom your replacement.** Constantly look in the trenches for junior architects. Pigeonholing prevents mobility because "whenever the pigeon leaves the hole, it creates a vacuum behind it, and the organization doesn't like vacuums." Counter it with: "I've mentored Junior for two years; Junior is perfectly ready to take over."

- **Master puppeteer technique** when taking over a broken team: direct from the shadows, pulling every string invisibly. To each developer privately: "I don't care what happened so far, it's blood under the bridge, but this cannot continue. I've talked to everybody else on the team and they're all in favor of working correctly. I like you personally, but this isn't good. I'm going to help you — but you have to do it the way I'm telling you. Your suggestions, of course. On the way out, can you tell Bobby to come in?" Each person sees individual help; collectively they see a **phase shift — "yesterday despair, today delivery."** Once you cut the strings, they keep doing things correctly, and only then can you leave: *"Your work here is done."*

- **From day one, tell the team you are going to leave.** Classic technique: **"I'm going to leave the day you tell me you don't need me anymore."** It puts the onus on them to raise their game instead of you nudging them. Say it often — otherwise, "you haven't said it in the last three hours, so maybe you changed your mind."

- **Overcoming fear and doubt is career-accelerating: anyone can design a system, very few can turn around and transform an environment.** Once an organization learns you do that, they keep you in that capacity — you get the fun work (architecture, project design, building teams) and hand the long-term churn to somebody else, with better compensation.

- **"Even your exit out of the project you have to design. Nothing is left to chance."**

### AI and Future of Development

-

### AI and Agility

-

### AI Spec-Driven Development

-

### Quality Assurance

- [Transcript](../99-Resources/Transcripts/Quality%20Assurance.md)

- **"They are not quality assurance. They are test monkeys."** Do not confuse software *quality control* with *quality assurance* — and most organizations don't even have quality control.

- **QA is typically a single person**, even in a large organization. You don't need a QA department or an army of QA — "you just need one."

- **The QA person is a special person:** the unique combination of **interpersonal skills + analytical skills** — good at resolving conflicts, approaching people, influencing them; and simultaneously good at cause analysis and crafting remedies.

- The presence of a QA person is almost always an indication of **commitment to quality** — the organization understands quality doesn't happen on its own, you must actively pursue it, be incredibly proactive, and *manage* quality. A sign of maturity Juval "hardly ever" sees: among the better companies IDesign gets called into (with self-selection bias) he sees real QA "maybe once a year, maybe once every few years." Yet "there is nothing when it comes to ROI like QA — this is the **highest ROI you can get in software development**."

- **What QA actually is:** examining, auditing, and tuning **the process**. Step back from the minutiae and the day-to-day, look at the entire way you develop software, and ask "How can we tune this to assure quality? How can we make sure that **problems don't happen in the first place**?" This is "completely different than going and playing whack-a-mole with defects."

- Often when you start QA work, all you have for a process (or project) is **"a smoldering crater."** A good person rolls up their sleeves and starts designing the process.

- **Extend standards beyond code and design into Standard Operating Procedures (SOPs):** "Here's how we do release. Here's how we manage change."

- **QA must report to top management.** "When QA says to do something, it's as if God said to do something."

- **QA owns procedural variants.** The process says A→B→C, but maybe here you can go A→C. Who decides? Not the monkey who wants to jump to Z and start coding. Good processes are adaptive; don't be too regimental.

- **Root cause analysis (the C in CAPA).** The symptom chain: (1) you didn't put `i++` — that's the *symptom*, not the bug; (2) the developer didn't understand what the code should do — still a symptom; (3) the developer didn't understand the domain; (4) no time to understand the domain; (5) no project design, schedule/cost/resources mis-accounted, the whole thing became a pressure cooker; (6) no point doing project design against a giant ball of mud — there's no architecture; (7) no architect; (8) "because we don't really value software development as a profession. For us it's just a bunch of monkeys smearing code on monitors." → **That's the bug: your rotten culture.** Everything above it is symptoms.

- **CAPA — Corrective Action, Preventive Action** — a tool manufacturing environments evolved over decades. Corrective action starts with root cause analysis: go up and up until you reach the root. Then ask: could this root cause, or any intermediate step, have caused **other problems we haven't discovered yet**? Yes — "go and hunt them, kill them now before they destroy anything else." From one little `i++` you may fix a bunch of other things.

- **Enforce the medicine.** A doctor prescribes 10 days; after three days the patient feels wonderful and stops. "The minority of patients will take the full dose. That's how bad it is." Many fixes are not once-and-done but must be done habitually **every time, every time**.

- **Post-mortem immediately, even on successes.** High five, you made all the commitments — first question: **"Was it because you were lucky? Do you feel lucky, punk?"** Then: how repeatable is it; could another team do what you did; what's different from what everybody else is doing; how do we replicate it; could you have done it faster/cheaper; what risks did you take that luckily didn't materialize and what mitigations should you have had; in hindsight what should we not do again; and what would it take to **sustain** the good things?

- **Worked incident example.** A developer optimized something while evaluating a standard; the defect was caused by **several violations of SOPs** — not one, several — which led to uncovering additional process errors. Key lessons documented as a one-page doc:
  - **Regression testing must account for all possible states.**
  - **You must solely test even the most innocuous change.** ("I told you — walk over every line of code with a debugger.")
  - **Do not optimize.** An SOP explicitly forbids it.
  - **All domain changes go through me** (the domain expert).
  - **Avoid organic efforts.**
  - **Do not tamper with the tools.**
  - When changing multiple files, **break it down into smaller, simple PRs.**

  Consequence: "We cannot trust the tools." They use their own set of development tools, not just Visual Studio — break the tools and you break everything. To regain trust you must document exactly how to produce the defect. Immediate fix: reject all of it. Long-term fix: do the effort properly. Result: "We only had one after that, in all the years we've been doing it" — for one little bug that should not have happened.

- **The Swiss cheese failure mode.** Every directive is a **guardrail**. You can bypass one, but hopefully the next catches you. Defects happen when you somehow bypass **all** of them. Each guardrail is a slice of cheese with holes; no guardrail is perfect. Defects manifest when across multiple slices **the holes align** — "and then poof, the defect goes through."

- **Preventive action — the P in CAPA. "Having an architect is a world-class QA activity."** A qualified, competent architect produces the most loosely coupled design → reduced complexity → minimal cost → project affordable → easier to understand, more approachable, easier for mere mortals to wrap their brains around → "once they understand it, they're probably not gonna make mistakes."

- **Project design is a world-class quality assurance mechanism.** It is the architect's responsibility to account for *all* quality-control activities: not "silly unit testing," but full-blown regression testing, developing the regression test harness, writing the test plan, standing up test legs, simulators and emulators — everything that enables diagnosing and isolating problems. All of this is part of the plan. And it won't happen without a competent, qualified architect.

- **"Boys and girls, I have news for you. You are not in the design business. You're in the quality business."**

- **Are you using the right tools?** Not just the compiler — the whole ecosystem: writing code, reviewing it, managing versions. Tool vendors' chronic problem is the **disparity in skills**: in the average team it's **10 to 1**, the overall spectrum can be **1000 to 1**. Design for the top dog and nine-tenths of the team can't make sense of it; design for the meekest monkey and anybody needing more power cannot operate. So vendors compromise and **aim for the middle**.

- Modern Visual Studio is far too complex for low-end developers. Compare it to old VB: "drag the button on the form and ship it." People who yesterday drove buses and today draw buttons on phones cannot jump from a bus to Visual Studio. And where is your **design surface** in VS? It doesn't exist.

- **To compensate, vendors offer hooks** — reach into the tool and extend it. "Any team that even contemplates the word QA must extend and customize their tools for the specific environment." Developers are **not at liberty** of designing folder structures or project settings — everything must be enforced (e.g. the C# standard enforcer). **"The tools are not driving — you are driving."**

- **Standards are a world-class preventive maneuver.** If you follow the standard, whole sets of problems don't happen. "You don't even understand half the things in the standard. Doesn't matter. Follow it."

- **The three-headed monster.** Because prevention is so hard to drive, it cannot be just the QA person's or the architect's problem — **QA, the architect, and engineering management must collaborate**. Runs on the **trifecta of influence, power, and authority**: **authority** resides within engineering management; **power** resides within quality assurance; **influence** is with the architect. A QA person can easily fail a release — "not up to code, not releasing it" — that's a lot of power.

- **Engineering management is all about quality assurance.** In many organizations engineering management is "nothing but glorified slave drivers or perhaps highly paid project managers." That is not engineering management. The only people who report directly to engineering management are the QA people or the managers of the quality-control people — and sadly most people don't understand that.

- **Great job-interview question:** "Do you have QA?" (everyone says yes, of course they don't). Then: "How many times has QA failed the release?" **Never** → paper tigers, no teeth, not the right place for you. **All the time** → also not the right place for you. **"Once or twice, we had to do it, and we didn't like it"** → that's a great answer.

- **Proximity is key at enterprise scale.** You can't have QA on one continent and the architect on the moon. "They're literally a **three-headed monster** — a single body with three heads, each owning a different part of the puzzle." When Juval was chief architect he shared an office wall with the company's QA person, and the VP of Software / engineering manager was two doors down. Strategies at that scale are like **slicing the salami**, slice after slice, planned and thoughtful, with contingency.

- **Closing jab:** "Given this definition of QA, how many of you would say you have QA? **Why do you call something that is not QA, QA?** Oh, but you are the one that also calls slow, expensive, and full of defects *agile*. And you also think that remaking, remaking, remaking in perpetuity the ball of mud into another ball of mud is best practice. **Everything you know is upside down. Everything doesn't mean what it means. You cannot make this stuff up.** At best what you have is quality control."

### Quality Control

- [Transcript — Quality Control](../99-Resources/Transcripts/Quality%20Control.md)
- [Transcript — Smoke Test](../99-Resources/Transcripts/Smoke%20Test.md)

- The topic is **deploy and test** — the practical discipline behind quality control: the **daily build** followed by the **daily smoke test**.

- It is rare to find companies without *a* build, but what you actually need is a **daily build** — and it is "not that rare" to find companies that do not do it daily.

- **Definition — daily build:** every day, regardless of how much progress was made, take *all* the code to a machine that has **never seen the code before** and has never seen a development tool. Install all development tools, libraries, and everything else, and perform a **full-blown build**. Once the build passes, deploy to target machines and run the smoke test.

- **Reason 1 — silent breakage.** A modern service-based system is **large and not reference-based**, so a change in one sub-project can silently break something else: "maybe I'm doing something over here that breaks something else, but I don't even know that I'm doing it." Excuses like "I'll do continuous integration, I'll check in, you'll do it" don't hold — there are ways of overriding or bypassing CI checks, "and that's not okay."

- **Reason 2 — you are not reference-bound when consuming a service.** You pull in an assembly/DLL/package; everything is "based on the call that goes out." If the protocol or messages change, "you have no way of knowing it." So you must **stand up everything** to find out.

- **The cost argument for cadence.** Build only occasionally (say monthly) and when it fails there is **no way of reconciling the various pieces of code** — no way to get it to work. You roll back to the last stable build a month ago and start again: "you lost a month… this is unacceptable." With daily builds the worst case is going back to yesterday: "I'm not happy about losing a day, but I can survive losing a day. I'm probably not going to survive losing a month."

- **The real reason** for the daily build is that it **enables the daily smoke test** — the build is what creates the opportunity for the smoke test.

- **Definition — smoke test:** the term comes from **electronics**. On a breadboard circuit the very first test has nothing to do with correctness of logic: you power up the board and see if **smoke comes out**. "Not a good sign." Software has no physical smoke, so the equivalent is to **bring up the whole system, energize all the components and all the plumbing, and see if there is any smoke**.

- **Where defects hide** (revisiting the composable-design blocks): (a) inside individual blocks, (b) in the **interactions between** blocks — really a bug in the requirements, handled by composable design — or (c) in **the "roads"**: the way things are put together.

- **The roads are "diabolically complex."** A modern service has aspects of hosting, activation, instantiation, queuing, security, transaction, synchronization, discovery, timeouts — each one "like a little dialogue" affecting the services. **"The number of roads is n squared"** — roughly **100 roads for 10 services**, and far more with 10, 20, 30, 40 services. Each road has dials and knobs that can be misconfigured.

- **The combinatorial spectrum is astronomical;** "there may not even be a combination… that lets you work." You cannot debug this analytically — you must **exercise** it. So every day you bring up the system and energize all the roads: you are testing the **plumbing**, not the correctness of execution — "flushing water down the pipes and seeing what happens."

- **The payoff is an instant diff.** When something blows up the next day you ask "what has changed since yesterday?" instead of searching the combinatorial space. You know exactly what changed.

- **Verdict: smoke testing is "the single most important system-wide quality control activity you will ever make."**

- **Forced-choice thought experiment:** given the bizarre choice between (a) daily smoke test and no system testing at the end, or (b) no daily smoke test but system testing at the end — **hands down choose the daily smoke test without system testing at the end**. Rationale: with a well-designed, well-built system you have **every expectation that system testing will be flawless** — you still do it, but the expectation is success. Requirement defects surface later and are handled by composable design.

- **Airline analogy:** after building an airplane the company does not finish riveting the wings and hand it to the customer — they do **test flights**. The test pilot and organization have every expectation the plane will pass and fly in circles. It doesn't mean you skip testing, but the expectation is success. Counterpoint that anchors the whole lecture: "if I'm at the end of the project and I'm standing it up and the plumbing doesn't work, **all hope is lost**."

- **Microsoft, cited directly** (a page Juval highlights): **"After code reviews, smoke testing is the most cost-effective method of identifying and fixing defects in software."** His reaction: "What? The most effective? … And sadly you never heard about it."

- **Nuance:** code reviews are not really a *testing* activity — they are a **quality control** activity. Strip them out of the testing category and the conclusion is categorical: smoke testing is the single most important **system-level testing** activity you will ever do.

#### Test engineers, not test monkeys

- **STE = Software Test Engineer** — "full-fledged software engineers whose mission in life is to write code to break your code." "Probably the best ROI you can get in software development." **Your best developers should be your test engineers.** Mental model: "every time somebody moves one semicolon the wrong way, a mountain of vicious adversarial code jumps on it and tears it apart."

- **Microsoft had two engineer flavors: SDE** (Software Design Engineer) **and STE** (Software Test Engineer). Both wrote code all day; the STEs wrote code to break the SDEs' code. Microsoft's average ratio was **2 STE : 1 SDE** — "for one guy writing code, two guys were writing code to break the other guy's code."

- **The WCF team ran 4:1** in favor of STEs. Result: "WCF is a paragon of quality… one of the most challenging pieces of software mankind has ever created. I have 800 pages book across four editions that describe WCF and **the word bug is not mentioned there even once**."

- **WCF anecdote:** early on, only two people had visibility across the whole product line — the WCF architect and Juval. Weekly he got a DLL plus "a monster Excel spreadsheet with 220 columns" and hundreds of developer rows showing what changed. The WCF team was **twice as large as the .NET team**; if that took 2 years, **WCF took 5**.

- **The "think of the children" email.** Juval found the team doing the opposite of the elemental distributed-computing practice of **compensation**. He emailed the chief architect: "Since the dawn of time, we've known in distributed computing that you need to do it like that. I look at your code and you're doing exactly the opposite. Why? **Think of the children.** … I am splunking using Reflector into your code. It is so easy to fix. Don't do this, do that instead. **Have mercy.**" Reply, one line: "**Oh, it's a bug, we'll fix it.**" Days later: "Of course we fixed it, just like you said. **Except it takes 10 days to clear the testing pipeline.**"

- **What that pipeline looked like:** to test the TCP channel, STEs built a **fake TCP stack that replaced ws2_32.dll**, dropped packets, with a **trackball controlling the drop rate**, to see how WCF's reliability mechanisms handled it. "Now *that's* quality right there."

- **SQL Server story:** a "teddy bear" of a former lead developer of SQL Server (10+ years) left Microsoft for a Bellevue startup. "I knew it was bad out there. I had no idea how bad it is." **No test engineers at all.** His boss: "Get out of my office." He trained his top developer into a test engineer; "the project was a smashing success. Everybody came to me and said, how did you do it? **One test engineer. That's it.**"

- **At Microsoft, QA/QC on your CV used to be a badge of honor.** Microsoft for many years had the rule: **nobody is promoted unless they were a test engineer or managed test engineers.** "Every public figure you've seen from Microsoft was either a test engineer or managed test engineers."

- **Hiring lever:** ~100,000 engineers at Microsoft, ~70,000 historically STEs, **≥10% turnover** → 5–10k ex-Microsoft test engineers per year for decades. "Put an ad in the paper: we're looking for an ex-Microsoft test engineer. Compensation? We don't care, we'll weigh you and give you weight in gold."

- **Same for medical:** GE Medical Systems, Philips Medical, etc. have armies of test engineers, because "**the most important bug in the history of software development was in a radiology machine**" — a machine that made patients "extra crisp," because instead of a tiny dose it "basically put them in the microwave for a few minutes," and every fix made it worse.

- **The reason you have no test engineers is brutally simple: "You didn't ask for them."** "The only reason you don't have test engineers is you. It's your fault." Repeated refrain: **"Are you making excuses again?"**

- **The overcapacity diagnosis:** "You already have crazy levels of overcapacity. Why? Because you practice a **voodoo religion you call Agile**." In one recovery engagement he measured **24–39 developers** where project design said **4** → **600%–1,000% overcapacity**. "I have seen a thousand percent overcapacity. Five hundred is absolutely not unheard of."

- **IBM story:** a company acquired a garage startup, scaled an army of devs, failed; hired **IBM**, "an army of developers for three years. **Not a single line of working code left the building.**" Root cause: **knowledge transfer** — IBM devs couldn't grasp the domain.

- **The prescription: "Fire the bottom third. Keep the middle third as developers. Take the top third and make them test engineers. You'll be better for it."** Second lever: "Go to Amazon, type **software test engineering**, take the top five titles, give it to the top third of developers and say, read this. I just solved it for you."

- **Life advice wrapped around the scolding:** "Every time your brain starts making excuses, cross it out and say, I'm now going to force myself to make a list of all the ways I'm going to make something good happen." "You're your own worst enemies. Stop doing that." "You are the people you've been waiting for. Nobody else is going to do it for you."

- **Thames Valley story (London):** a five-floor IT building with **nine systems, all nine "smoldering craters."** A young first-job-out-of-university engineer, **Andrew**, asks on a walk whether he should pivot. Juval: "You're a smart kid. Most people don't even notice." Trains him as the project's test engineer — he became "probably the best developer on the team."

- **Most companies only have testers:** "Press the button, press the button, take a banana. This is why I call these people **test monkeys**. It's literally monkey see, monkey do." He knows "monkey" is insulting — "It's done on purpose. If your job is click the button, click the button, take a banana, you're a monkey. You're not a test engineer."

- **Ratios.** Good: **2 testers : 1 developer**. Not a hard rule — where you can do damage (life-saving mechanical equipment) **2:1 is a must**; social media where a bug makes someone lose their tweet, **1:1 is good enough**. **No team should fall below 1:1.** Industry reality: **1:10**.

- **Consequence 1 — the tester cannot scale with the team.** Go from 3 devs to 6 to 9 and the tester would need 2×, 3× the output; nobody can. So testers get relegated to "recurring work which is invariant to team size" — another way of saying **low added value**.

- **Consequence 2 — developers end up doing the testing.** Measure the real testing:development ratio and it's probably 2:1 or 3:1 *in favor of testing*; it just isn't the testers doing it. "The more developers spend time testing, the less time they spend writing features and adding value to customers."

- **Aggressive schedule? "Should we add developers?" — No. Add testers.**

- **"In software development, quality leads to productivity. If you have high quality code, you don't spend time chasing ghosts, and you spend more time adding value."** "The reason I'm so fanatic on quality is because I'm really fanatic about productivity… **The only way out is through.**" Quality is also **"the ultimate project management technique"**: once you infect developers with the obsession for quality, you let them drive, you trust them, they won't cut corners, and you don't have to do much as a manager.

- **The 19th-century analogy:** infant mortality was two thirds; everyone from pauper to king had lice and fleas and you could smell them entering the room; "**every one of you has a higher standard of living than the king in the 19th century**." It took "a little bit of salt, a little bit of water, a little bit of nothing." "You cannot imagine [a clean environment] from the context of your smoldering crater."

#### Windows 10 as the proof case

- "Windows 11 is just Windows 10 with a different skin." Up to Windows 10, "Windows" was a marketing name for ~10 different OSes (Azure, laptop, server, tablet, Surface, HoloLens) — "that's where the similarities end."

- **Windows 10 = "one ring to rule them all,"** a genuine single code base: **no `#define`, no conditional compilation, no if/else** — achieved via **composable design** (componentize the OS; HoloLens doesn't need a keyboard, so no keyboard component).

- **Fermi estimate:** ~**20 million lines of code**, **2 years** (gap between Windows 8 and 10), **~200 developers** → **100,000 lines of super-complex, first-of-a-kind OS code per developer**. "Could any developer own 100,000 lines? Hell no. And yet it did happen. **The numbers don't lie.**" "You keep extrapolating from your miserable existence to what is possible. Microsoft didn't do it the way you're doing it."

- **The mechanism: pipelines / assembly lines.** Code → unit testing → integration testing → regression testing → system testing → … Nominal ~10 pipelines, **actual number was 7**. "While on the calendar two years have passed, **on the Microsoft clock 20 years have passed.**" Caveat: "It takes years to build the capacity to work this way, and **Microsoft has spent 40 years honing itself**." Key enabler: **a high ratio of testers to developers.**

#### What QC does in a service architecture

- **"We build teams with the people we have, not the people we wish we would have had."** What the under-strength testers *can* do: write the **system-level test plan based on use cases** and run it as a **black box** ("I don't care what's happening inside") — highly repetitive — plus **daily build and daily smoke test**. Automate that to offload the test monkey ASAP.

- **Structure:** every **service** has its own test environment ("fundamentally a construction facility"), every **integration point** on the integration tree has its own test environment, and there is a system-level one.

- **The most annoying email in engineering: "Yesterday at 4 p.m. it didn't work."** Nothing else. It drags 7 people into a 2-hour war-room meeting = **14 hours, two days, blown on a silly meeting**.

- **Fix:** print the integration chart on the plotter, cover the wall of the tester's office, and teach them to run the tests at the integration points: "if this passed and this failed, the problem must be in this subtree." You are now doing **binary search for the defect** — **trinary search** with three services, "it converges much faster."

- **New email:** "Yesterday at 4 p.m. it didn't work. **Culprit component: the queue manager. Owner: Dave.**" Enabled by the **1:1 mapping of services to developers** — "we know exactly who to blame. There's no 'this' anymore." Second email, from Dave: "Yeah, I should have tested this before I checked it in. So I came to work today at 6:30 and I fixed it, I tested the whole thing, it's working, we're good to go." — **"A self-healing team."**

#### Zero tolerance for defects

- **"By far, by far, by far the most important practice in quality control is adopting zero tolerance for defects."** If anybody has a bug in a service, **nobody goes home, nobody goes for lunch, nobody does anything until you fix it** — short of a family emergency.

- **"The zero is not on the defects. The zero is on the tolerance."** His rhetorical counter: "How much tolerance does the organization have for sexual harassment — is it 0.37 or is it exactly zero? How much for financial misconduct? **Why is this any different?**" He routinely had developers bring **sleeping bags and cots** to the office and put them in the corner. "Not that I ever had to use it. But it would send a message."

- **Why zero:** "The inherent complexity of a modular system is so high that if the services themselves are flaky, **all hope is lost.**" The only fighting chance is that individual services are **completely and utterly rock solid**.

- **The proof by induction.** Hour zero, first second, first line of code — how many defects? Zero. Put a button next to that line, step over it, examine every variable; any defect, fix it. Zero. Add line i+1, same. **By induction, you can always, always, always have zero defects at the service level.** "What I describe is not difficult, it's easy. It only gets difficult if you don't do this — if you normalize your deviation."

- System level is not guaranteed zero, but: **defects in the plumbing → daily smoke test; defects in the requirements → composable design.** "It doesn't guarantee it, but it enables it." He keeps a plastic bug trophy on his shelf from PMs who couldn't believe a release had no defects.

- Two techniques to achieve it: methodological line-by-line testing, and **"putting the fear of God in your developers."** But you need an environment conducive to quality work.

#### Testers as the anti-team

- **"We treat the testers as being part of the team. The testers are not part of the team. The testers are the enemy of the team."** Developers are paid to *ship*; testers must be paid to *fail shipping*. "How could people with diametrically opposed objectives share the same team?"

- This ignores the "ancestral relationship" between PM and lead tester — "scratch my back, I scratch yours, you sign off on the release, we both get a little bonus."

- **Provocation: pay testers on commission** — you only get paid when you find bugs. "Salespeople work on commission." "Am I paying you for effort or for results?" Escalation: a **pot of gold** (multiples of annual salary) for developers who ship, and a pot of gold for testers who *fail the release*. **"Let the Hunger Games begin. For them it's a zero-sum game; for me it's win-win. Whichever team wins, I win."** Where does the gold come from? **The losing team's salary, plus a bonus.**

- **"If you pay people for effort, they will do more effort. If you pay people for results, you're going to get results. That's how the world really works."**

- **"Often QA is part of the problem."** QC should **not report to project managers** — they should report **directly to top engineering management**. "They don't care if the project passes. In fact, they get compensated if the project fails."

- **Story:** newly appointed division manager, first team meeting; the **QC lead** asks verbatim, "At what level of defects would you consider the system ready for release?" He bangs the table — "We're not going to have any defects" — **and fires him. Rotten apple.** Then promotes a young tester found hiding under a table in the QC den, on the deal "I'll teach you how to do your job; you do it exactly like I tell you." "Ten years later that kid was **director of quality control for the entire corporation**. Do you think it's an accident? I caught him early enough."

- **"Defects should not be a way of life. It's unacceptable to have defects."**

#### The quarterly quality-review tribunal

- As a young division manager, second release, composable design, zero defects — summoned to the quarterly quality review, must bring **transparencies** with quality metrics including **release volatility**: **defects you were supposed to fix ÷ defects you did fix, over time.** "Now that's a nasty one." Fix 2 but were supposed to fix 10 → what happened to the other 8? Fix 6 when supposed to fix 2 → where did the other 4 come from?

- His problem: **"I don't have any defects. What is zero divided by zero? Nobody knows."** The GM's advice: "Just bring empty transparencies."

- The room is arranged like a **military tribunal**: CEO center, VP Software left, QA person right (the one he later shared an office wall with), all software managers in a big C "with the look of the condemned near the gallows." Each manager gets ~10 minutes of "What's going on? I look at the bug count and it goes pop, and the customer is on the phone."

- **His insight: "What are the units of suffering? … The units of suffering is time."** Less exposure = less suffering, regardless of intensity.

- **His move:** one empty transparency, "no defects," pick it up and walk out. The CEO calls him back: "We gave everybody 10 minutes, we'll give you 10 minutes" — and makes every manager **stare at an empty transparency for 10 minutes**. "Rubbing their noses in it. *What's your excuse? This young kid is doing it.*" "There was nothing in that more than what I've discussed with you right here. **These simple ideas. We do it completely wrong today.**"

#### The andon cord — the thing Agile forgot

- Everything in Agile comes from building cars, specifically **Toyota in the 1950s** and the first **just-in-time** implementation. (He prefers houses as a model; "I don't think a skateboard is a car.")

- In the Toyota Museum photo: the **andon cord** runs the entire length of the assembly line. Pull it and **the line stops**. **Anyone** can pull it, **any time they see any defect**, however minor.

- Stopping the line is **incredibly expensive**: JIT means no inventory — inventory is on trucks en route, the ship to Long Beach sails with or without your cars. The chain of reasoning it triggers: the defect exists in cars *upstream* too, so you flush them. Why the missing hole? A **drill bit** broke. Why did it break? Rated for 6,000 holes, only did 2,000. Why that vendor? Chose price over quality. → **Full-blown root cause analysis, everything stops until it's done — possibly for months.**

- **The worker: do we punish them? No — we give them a bonus.** Second pull: **an even larger bonus.** Third pull: **promote to management.** "Keen eye for detail, understanding of the entire assembly line, relentless commitment to quality — that's the kind of person you want in management."

- **The charge against Agile: "The Agileists went back in time to Toyota's '50s and picked all the process attributes and rituals — the Kanban board, the burndown rate, the stand-up meeting, all the rituals you keep doing — but they've conveniently left out the andon cord. The single most important artifact they forgot. It wasn't an afterthought. This was deliberate."** Reason: if you had an andon cord, "nothing will move, the line will never start."

- And it wasn't even a Japanese idea originally: **W. Edwards Deming**, 1947, two years after WWII, moved to Japan to teach throughput and impeccable quality — **Total Quality Management**. "The guy that invented this whole thing said it: zero defects, zero tolerance."

- Counter-response framing: "Isn't slow, expensive and full of defects the exact opposite of agility? You say slow and expensive, I imagine an elephant. You say agile, I imagine a bunny. **Zing zing zing.** Nobody looks at the elephant and says, oh, that elephant's so agile." Reference to **Isaiah 5:20** ("your world is upside down — black is white, white is black, bitter is sweet, sweet is bitter").

#### The O-ring theory of production

- **Challenger** took off and 30 seconds later became a $4 billion fireball. The chief engineer said don't launch; the NASA administrator overrode him. Congress appointed Nobel laureate physicist **Richard Feynman** to lead the investigation. The O-ring itself wasn't faulty — it **failed**. Rubber is **vulcanized** with sulfur; below freezing it goes brittle. There was frost that day, even in Florida. Feynman's demonstration: a **Styrofoam cup** of water and ice (≈0°C / 32°F), dunk the O-ring, snap it.

- The disparity that interested Congress: **a 30-cent part vs. a $4 billion fireball** — where a house in Palo Alto cost $40,000.

- **The formal model:** a system completes a task as the product of *n* subtasks, and failure of any subtask fails the whole. Normalize quality *qᵢ* to 0–1 (the range choice is arbitrary — "you can use 3 to 7 if you like"); 0 = always fails, 1 = always works. **What 0.9 *means* is up to you** — works 90% of the time, or 90% of inputs, or 90% of customer machines; you can even mix ("works perfectly half the time, 80% the other half" still averages 0.9).

- If each activity contributes one unit of value: **y = n × q₁ × q₂ × … × qₙ** — multiplicative, not additive.

- Ten activities at 1.0 → perfect. Ten at **99%** → ~10% of value lost. Ten at **95%** → roughly a third lost. **Non-linear degradation:** a 4% quality drop costs 33% of value; a 9% drop costs 61%. "Arguably, the more complex the system, the worse the effect."

- Three worked systems at 0.9 per component: **5 services → ~40% of value lost; 10 services → ~65%; 40 services → "completely and utterly dead."** And "five services is not a very complex system."

- **Punchlines: "Two bad services do not make one good service. Two faulty O-rings do not make one good O-ring. Two bad developers do not make one good developer."** "You can't replace quantity for quality."

- **"For Want of a Nail"** — 13th-century German folk poem: for want of a nail the shoe was lost … for want of a battle the kingdom was lost. "There you go — **the O-ring theory of production.** … A medieval peasant knows more about engineering than you do. **You're missing all the nails in all the services.**"

- **"You accepted defects at the service level. That's what I'm here to shake you out of. This is common sense. This is intuitively correct."**

#### What a bug is, and defensive programming

- **"A bug is always and everywhere a violation of an assumption."** You thought it wasn't null, it was null. You thought the list was zero-based, it was one-based. You thought it was initialized, it wasn't.

- Debugging is hard because **the violation and the symptom are usually in different places, days apart** — and that gap is incredibly hard to bridge. Defensive programming exists to **narrow the gap**.

- **"At least half your code has to be defensive programming. More is better."**

- **The assertion measurement:** assertions to regular lines of code ≈ **5:1** (roughly every sixth line). Measured on a code base that shipped **on schedule, on budget, with zero defects** — and he stresses the triad: **"You can never have one or two out of three"**; they feed on each other. The measurement was **fractal/uniform**: *any* slice he looked at showed 5:1 — not a few files with thousands of asserts and others with none. Can't prove it, but "it passes a smell test": high-quality code has short methods (~10 lines), so one assumption on input + one on output gets you there.

- **Assertions do three jobs:** (1) **instantly jump you to where the violation happened**, not where the symptoms show up two days later — "practically the best way of capturing programming mistakes"; (2) **document your assumptions** — "the fundamental reason developers introduce defects is because they don't understand the assumptions"; (3) **a message in a bottle** sent to yourself across the ocean, years into the future.

- **Message-in-a-bottle 1 (WCF / SecurityBehavior):** WCF is "a marvel of engineering — you put an attribute, you move mountains," *except* security, which required 80 lines of chicken-scratch XML config and weird certificate management — "that was done by design, that's what the lawyers at Microsoft wanted." In **2006** he wrote **ServiceModelEx**, introducing a declarative security attribute: `securityBehavior` with an enum selecting one of **five scenarios** (internet, intranet, anonymous, business-to-business, …) and a switch statement inside. In **2010**, extending it to the **service bus**, he added the enum value and the case — and hit F5 to find **an exception he had put in the code four years earlier** blowing up: "Did you remember that there's this and that also in the binding?" "Duh. Of course I didn't remember it." Worked two minutes later.

- **Message-in-a-bottle 2 (his energy farm):** "The first energy-net node in the world was actually my farm." A library that sends TCP packets **over plain vanilla power lines in the walls**, serializing to XML with timestamps. Parsing the payload in **2011** he asserted day ∈ [1,31] and time bounds. In **2018, seven years later, one assertion blew up** — some update made months come through as 4,000. "Of course you can assert that the month is between 1 and 12. **You can't trust anybody. You assert everything. Nobody said this number is going to be more than 12 forever.**"

- **Fractal view of code:** open any constructor or method and you see the same pattern — lots of asserts, then a little business logic at the bottom. In a constructor screenshot, **only the yellow lines are real work**; everything leading to them is defensive programming validating context, environment, variables. Result: "anything goes wrong, bam — you know exactly what went wrong, you know where, you don't have any ripple effects everywhere in your system."

- **Standalone services:** part of zero tolerance is that every service must be pluggable and testable **in complete isolation** — "view them as worlds in their own right, as if the service is its own separate system."

- **Extensive logging everywhere:** with 10/20/30/40 services "running doing wicked things everywhere, who can figure out what went wrong?" Log extensively and **interleave the entries** to build a picture of what actually took place. For the mechanics — activity IDs, exception promotion, inline vs async vs queued — see **Logging and the Flight Recorder** below.

- Even with all of it you will still have defects — but **"the average lifespan of a bug is going to be a few minutes. As soon as a bug does happen, you smite it and you fix it. Nobody needs to use the sleeping bags and everybody goes home happy."**

- **Closing loop:** service-level defects → methodological testing + assertions + standalone services + logging. **System-level plumbing defects → daily smoke test. Requirements defects → composable design.**

### Design for Performance

- [Transcript](../99-Resources/Transcripts/Design%20for%20Performance.md)

- A highly modular system of **10, 20, 30, 40 services** means each service carries its own "dashboard" of roughly **20 aspects** — security/no security, database/no database, hosted here vs. there, in-process vs. process boundary, transaction/no transaction, logging/no logging, and so on.

- Each of those ~20 items is **not a boolean flag**: there are many ways to do security, many ways to do logging — so the configuration space is a **"combinatorial spectrum of unimaginable scale, absolutely astronomical,"** and every one of those choices affects performance.

- **Most teams do performance testing at the end of the project,** which makes it a **boolean outcome**: pass → ship; fail → ship anyway, "apologizing of course to the customers, promising a service pack soon." Juval's challenge: **"what's the point of doing an activity as a Boolean outcome that regardless of the outcome we do exactly the same thing?"**

- Worse: **there may be no solution** to a performance problem. "It could be that your system is designed to have poor performance. So no amount of coding can change that."

- **It is not just the *value* of an aspect, it is the rate of change** that affects behavior. "Your system behaves very differently if it has **one client making five thousand calls** or **five thousand clients making one call**."

- **Why analytic modeling fails.** Model this and you get a **partial differential equation**, with the aspect settings serving as its **boundary conditions**. And per advanced calculus: do all PDEs have a solution? **"Hell no, absolutely not."** Many don't — meaning there may be no secret combination of dials and knobs that yields the desired performance.

- **The remedy: constantly benchmark the evolving system** throughout the project, not at the end.

- **"Benchmark" here does *not* mean an industry-wide benchmark.** It means a **micro benchmark on your own machine, in debug mode, with Visual Studio** ("and Outlook"). You are only after **order of magnitude**: one call per second? a hundred calls per second?

- **Cadence: benchmark every time you change an *aspect*,** not every time you change a line of code. Examples of aspect changes: interception with/without, database with/without, creating the setting with/re-creating it. Practical rhythm: **every day you do a build and run**, and you run the benchmark whenever an aspect changes.

- **"Horse trading."** If you change an aspect and performance stays adequate — nothing to worry about. If it becomes inadequate, **you know exactly what you changed**, so you can revert the aspect, or keep it and undo/compensate something over there that buys back the lost performance. The payoff is epistemic, not just numeric: **"at least you're not going to be groping in the dark. Now you start making educated choices."**

- **Track it in a project log:** columns for the various aspects, the perf result before/after the change, and **the date** — one row per aspect change. Real-project metrics include **P95** (95% of calls are at least at that level) plus **before phase 1 / after phase 1** columns and what changed / what did not.

- **Best practice: record your prediction of the numbers *in advance* of the benchmark.** Juval's predictions held up well ("I'm not doing too shabby") because he knows the **relative cost of an aspect** — given a baseline he can say "it should probably cost you this much." He used to teach a more technical version spending **half a day** explaining how to weigh aspects, with a table of "if you do this, it costs you this percentage" — but the table doesn't matter; the practice of recording and predicting does.

- **The horror story.** A project manager at one of the largest accounting firms in the world — a system **100,000 accountants** must use several times a day — rewrote a mainframe solution in .NET so roaming accountants could use mobile devices / a web service. Operations that took **sub-milliseconds on the mainframe now took 20 minutes** in .NET.

- **The decisive question Juval asks** (after the usual suspects): **"Did you maintain the track record of the various aspects and the micro benchmark every time you made a change?"** — No.

- **He charges a deliberately exorbitant fee** for exceedingly stupid customers: "I'm doing this for you because I want this to hurt… if you think that you can paper over with money for this kind of malpractice, I want you to remember not to do it." He also bills **even if he cannot solve the problem**, because there may not be one — and the client must accept that.

- **Escalation plan:** assemble a **dream team of experts** by domain — a system/distributed-computing expert (Juval himself), a database-design authority (e.g. someone who spent ten years as the **lead performance engineer on the SQL Server team**), and an Active Directory / credential-management expert (relevant with 100,000 accounts). Get everybody in one room, show the problem, hope something rings a bell; Juval moderates.

- **Scheduling comedy:** he works a **week-on-the-road / week-home** cadence and refuses three consecutive travel weeks ("I don't eat on the road, I get sick"). Proposed date: **"2037."** The client's counter-pressure: go-live at month's end, the CIO is on his back, and if the system fails, 100,000 accountants are unemployed — or, literally, **in jail**, because they must use it several times a day. "Think of the children." It became a **wife-level decision**; the wife said "go to Chicago." Experts have **"Swiss cheese calendars,"** so target the week after next when all can attend.

- **Reduction.** First meeting in Chicago (27 floors up): the demo shows the button returning after 20 minutes; the fresh-faced architect deflects ("it's not me, it's not Nat… it's not this, it's not that"). After three days Juval sends everyone home: **"You're never gonna figure it out like this… It's too complex. You need to do a reduction."** **Reduction** = come up with the smallest set of components — **smallest number of services, machines, web pages, clients, lines of code** — that **still manifests the problem**. Then, maybe, you'll see what it is. It took **three months** of reduction; reconvening the following May, he found the problem **in the middle of the second day**.

- **Moral: "They got lucky… You don't want to be in their shoes."** They also did something Juval explicitly says *not* to do in one of his books, and he gave them hell about it.

- **Objection and rebuttal: "My system only needs two calls a minute; my cell phone can do it — I don't need any of that."** Yes you do, because of **low-probability defects**. A defect that manifests once every **3,000 years** of continuous use can **sell through your entire testing cycle** and end up on customer machines. Scale it: **times × number of deployments × number of users × number of sessions × number of clicks** — "it blows up."

- **The support loop that follows:** customer calls, support says "we're looking into it," a **test monkey** presses the button — not reproducible — back to the customer, "poof," it blows up there again. "Sound familiar?"

- **Therefore: all systems must go through rigorous stress testing**, all the time, even if you do not care about performance numbers at all. Under stress, a problem that occurs **once a year in normal use** occurs **every 30 minutes or every three days** — and is therefore **reproducible**.

- **Tooling helps, but there are no shortcuts:** use tools like **Grafana** to visualize; on the current project they **instrument all the code** and measure everything.

### Services Simulation and Emulation

- [Transcript](../99-Resources/Transcripts/Simulation.md)

> [!note] Naming — the "energy project" is **Resilient Energy**
> Six mentions across this note say only "the energy project" or "the energy net." It now has a name: **Resilient Energy**, his current consulting engagement, described in full in [[Modules/Service Contract Design and Factoring#Sample Project II — The Real System (Resilient Energy)]] and [[99-Resources/Transcripts/Sample Project — Resilient Energy|its transcript]]. He introduces that lecture with *"this is the energy project I keep referring to you here. It's what I'm leading now on the side."*
>
> **Keep the nuance:** *"energy net"* looks like the **technology** term, not the company. Elsewhere he says *"the first energy-net node in the world was actually my farm"* — his own farm is an early instance of the technology, not the company. So "energy net" (technology) and "Resilient Energy" (company) refer to related but distinct things.

- **Every service has three modes and you need all three:** the **real/operational service**, the **emulator**, and the **simulator**.

- **An emulator is a do-nothing version of the service** — every call just returns "hello", "true", "okay", "zero", "three", whatever. Building one is "a hair's breadth from right-click → Implement Interface → OK" plus removing the exceptions. Rule of thumb: **if you spend more than a few minutes on an emulator, you're doing it wrong.**

- **A simulator is as real as the real service — indistinguishable.** It manages state and lets you inject errors; "sometimes it's as demanding as the service itself."

- **Working example (energy project):** there is no physical meter, so they simulate the meter *and everything that contributes to it*. Configure a node of the energy net — how many light bulbs, air conditioners — and it builds a **load curve**; it also computes **how much power you need to buy** from your trading policy. Add **solar** and it shows up as *negative* power; add a **battery** and you watch it discharge once the solar sets down. Two screens: a **design view** and a **live view** of what the meter reading would be, every point one minute apart.

- **Simulated clock:** every service runs against it, so you can pause, decelerate, or accelerate time. Accelerated ×200 you watch the sun rise at 8 a.m., solar production peak, and the net curve decrease.

- **"That's a lot of work." — No, it's not: developers do all three anyway.** They scaffold the interface (that's the emulator), write the implementation (the service), then comment things out and inject errors and weird cases (the simulator), then clean it all up. The prescription is to **structure that effort** — all emulator code here, all simulator code there, the actual service over there. "And you're not doing any more work."

- **Reason #1 — development overlap.** If A needs B you must normally wait for B, but much of A can be built against an *emulator* of B; only final testing needs the real B. With a long chain (A → B → C → … → XYZ), A would land as **the very last thing in the project**. Instead write a **simulator for B as the very first thing**, then move A's development to the beginning. You **change the topology of the critical path and start compressing the project**.

- **Reason #2 — debugging** that requires jumping through machines, clusters, and hardware (the "debug session from hell"): just simulate those things.

- **Reason #3 — demos on the marketing laptop.** Screenshots and demoware are bad, "because customers are onto us. They know that demoware doesn't mean anything." **"Nothing sells code like code. You sell code with code."** Install the whole thing on the laptop; the marketing person says with a straight face, "this is the actual code you're going to get." Only hardware and database are simulated — no rabbit in the hat. Customer effect: "there's no reason these guys are going to be late or promise me things that don't exist. This is it."

- **Reason #4 — running without the database or expensive hardware.** Example: a San Jose company selling a video compressor that streams 800 4K channels on a PC card, in a device with the form factor of **R2D2** (blinking lights, fiber optics) — capital equipment costing millions, sold in tiny volumes (a few per big city). Juval, in a hive where every cubicle had its own R2D2: "You don't have a simulator for this? This is expensive… Simulator, I'll do it on commission for you."

- **Reason #5 — daily/smoke tests that need a human assist** (click a message box, turn something on the hardware) break automation; it gets old very quickly. Emulate or simulate the part requiring the assist.

- **Reason #6 — stress testing and natural bottlenecks.** A remote database limited to 200 calls/sec, while low-probability defects lurking in the shadows only manifest at 10,000 calls/sec. The defect **sails through your entire test cycle** because of the natural bottleneck. Fix: after automating testing, **analyze the natural bottlenecks and eliminate them with simulators**, then "crank the testing up to 11 and see what breaks."

- **Reason #7 — business workflows with nebulous requirements.** Don't deploy to customer machines, have them complain, and rewrite. Simulate the customer environment and tune the workflow to perfection *before* you ever deploy.

- **Who tests the simulator?** Like any code it must be tested — but if **every service has a simulator, the simulator of the client becomes the test client of your simulator of the service**. "You basically pit the simulators against each other. So you don't actually do more work."

- **The simulators' duel.** Juval led a team that had to interface with another team he was certain "could not find their way out of a wet paper bag." Every commitment was untrustworthy, yet the dependency (protocol, messages) was strong, and he was accountable for delivery. So the first thing in the project: instruct his lead developer to write a **full-blown simulator for the other team's part**. Unbeknownst to him, they thought exactly the same thing about *his* team — "arguably **the only self-assumption you have to make about any team you have to interface with**" — and wrote a simulator for his stuff. Neither side knew, "because we never talked to those losers." Discovered months later, casually, in the cafeteria. He immediately called for **the simulators' duel**: hook the two up and spend months trying to tear each other apart. "It was beautiful — tears to my eye to this day."

- **Requirement: you must be able to switch modes (simulation / emulation) programmatically.** Reason: **production-time debugging.** It works for you but not at the customer's, because something in their environment differs — and it may have nothing to do with you. Remedy: bring up a **management console** that opens all running services and start **"looking for a line in the desert"** — bisect: "simulate me these, emulate me these, go." Whatever doesn't have the problem was in the half you simulated, so you localize the fault very quickly. **This tool will be an absolute must** — every deployment is different, every customer is different, and every customer has their own peculiar version of the system.

### Peer Reviews

- [Transcript](../99-Resources/Transcripts/Code%20Reviews.md)

- **"You have to review everything."** Reviews cover code *and* design artifacts — anything owned by a developer. Most teams believe they run reviews; they actually run **code walkthroughs** (projector or Zoom, author scrolls the code, group comments live). Better than nothing, "nowhere near as efficient" as a formal review.

- **A good review is a formal review** — defined by **designated roles**, not by a meeting. Juval's jab at teams that confuse the two: *"You also call slow and expensive full of defects agile. So perhaps words don't mean exactly what you think they mean."*

- **Roles.** **Moderator/mediator** — typically the architect, or somebody else you trust; assigns reviewers. **Developer** — the owner of the artifact. **Reviewers**. **Scribe** — records decisions (may be the artifact owner or somebody else).

- **Being assigned as a reviewer overrides everything else you do.** Rationale: the prime directive of teamwork is *never prevent others from doing their work*. You cannot hold anybody back.

- **Only the owning developer can declare "I'm ready for review."** It cannot be forced on them — they know when it is ready. Flow: developer sends the moderator the list of files/branch → moderator distributes it → reviewers review **offline**.

- **Reviewing happens on the job, not at home over the weekend.** Reviewers record comments **in the artifact**: low-tech convention is `//` + initials (`// JL`) plus why you're doing this and not that; modern tooling attaches the comment inline.

- **In the meeting you review the comments, never the artifact.** *"It's a review of the review."* Result: "you just bam, bam, bam, bam, bam go to the comments," so you cover much more in far less time.

- **Comment discipline.** A *repeated* comment (e.g. code style) is made at the **first place you see it**, since it applies everywhere. A **copy-paste bug** must be commented **every time** you see it.

- **Every comment is arbitrated by the moderator**, who asks the developer "what do you think about that?" If it must be fixed, the **scribe** records "line so-and-so, fix this and that" — which becomes an instruction for *all* developers. The ruling is not optional: *"It's not their code, it's the company's code. The company says you have to fix it, you have to fix it. Doesn't matter what you think."*

- **Statistics form** per review: service, moderator, scribe, owner, then **time spent per reviewer** and **comments per reviewer**, plus **major** and **minor** defects found separately. Purpose: **healthy peer pressure** — 3 hours vs 4 hours vs 20 minutes, or 27 vs 60 vs 3 comments, gets you called on it.

- **Any comment made in anybody's code is immediately and wholeheartedly applicable to everybody else's code.** It is a big no-no to find the same finding again, again, again in someone else's code. Even if you were not a reviewer or were **on vacation**, you must read the report and scrub your own code.

- **Two health trends:** the number of comments must fall **non-linearly as a function of time** (rising numbers are a bad sign), and the same finding must stop recurring across codebases.

- **Anecdote (energy project):** the first code review took **three meetings of three hours** and still produced **3 major and 132 minor defects** — on code that was "the best code I've ever seen in the wild." Today the same review cranks through in **about two hours** and mostly surfaces compliance items. *"That's the way it should be. People should write good code in the first place."*

- **The home-inspector analogy (the thesis).** If you design a single-family home and arrive for the first inspection to find a **30-floor skyscraper**, no inspection can fix it — they are building a different system. The useful case is a supporting wall moved by accident, or a deliberate deviation the architect must either reject or accept by crossing out the old wall, drawing the new one, initialling and signing: *"On this day, I approve moving this wall."* Conclusion: **"The purpose of reviews is to catch the occasional unintended misstep from your grand design. If the developers are hell-bent on butchering everything that you do, no amount of reviews can fix it."**

- **Walkthroughs keep a niche:** esoteric environments — a weird MVVM setup, a Kubernetes installation script — where walking the architect through what it is supposed to do yields valuable feedback even when nobody there knows the technology. For everything else, formal review.

- **Code reviews are the most efficient quality control mechanism** — "way more important than testing or anything else."

- **Body programming (his name for pairing).** The XP crowd got something **very right and very wrong**. Right: two pairs of eyes beat one, which cures **code blind** ("they're looking at the screen and they don't see it"). Wrong: **two bad developers don't make one good developer**, and most organizations chronically lack good developers, so doubling up good developers makes no sense.

- **Every developer has a body/buddy** (commutative, or a more complex mapping). Problems go to the **buddy first**, not the architect; only if the buddy cannot help do **both** go see the architect. Payoff: the buddy becomes intimately familiar with A's code, the architect's second pair of eyes arrives **judiciously, just when needed**, and the buddy can cover the mythological "hit by a bus" scenario.

- **Precondition.** Because reviews catch only *occasional missteps*, **everybody has to be on board in the first place** — coding standard, how you write code, the design. "Without all the up-front work, all the onboarding, and all the SDD, you're never gonna get quality reviews."

- **Managerial visibility.** Reporting "today the team spent three hours on the ABC component, we found 11 major defects and three minor defects" flips the manager into *"I see value here. I'm gonna allow this to continue."* Managers respond to visible defect-per-hour evidence, not claims.

- **The developer fallacy.** "I'm so good, look how amazing my code is" — it **doesn't matter**, because *in conjunction with somebody else's code that sucks, your code is going to suck too*. The only way your code can be amazing is if the other guy's code is amazing. *"High-quality software is a team sport. Doesn't matter how good you are — the team has to be good as well."*

- **Culture builds fast:** **success is addictive**, and high-quality people like producing quality work. On the energy project the developers eventually became sticklers, insisted on correctness, and cared about each other's code.

- **Strict coding standards are required** — *"One guy's code must look like the other guy's handwriting."* Two reasons. (1) *Less important:* indentation and formatting exist so your brain can wrap itself around the code. Humans don't review like a compiler (no symbol tree, no symbol table); we look for **patterns** — indentation, line, message, tick tick tick. Misaligned code disables the analysis, and opening A's code that doesn't look like yours has you moving things around — "oh my god, stop doing that." (2) *The real value:* when the standard **enforces the practices**, the machine-checkable work is already handled, so human reviewers spend their time on exactly what the standards make hard to enforce — the value of a human looking at code rather than a machine.

### Development and Design Standards

- [Transcript](../99-Resources/Transcripts/Coding%20Standards.md)

- **Legacy standards were "laborious, indigestible monsters"** — 225 pages of 1.2.3.4.5.6.7, impossible to digest, internalize, and comply. Hand a new developer **"the tomb"** and you get "oh yes, yes, standard" → 1.2, 1.5, 6.7… *"anybody saw me snoozing?"* → retention: **zero**.

- Worse, classic standards covered only *code* and ignored **project settings, structure, and framework guidelines**, which matter just as much.

- This frustration drove Juval to publish the **C# Coding Standard in 2003**, now the **industry de facto standard for C#** — any standard you use is probably that document or a derived work.

- **A good standard is thin on the *why*, rich on the *what*.** Two reasons: (1) which matters more, valuing the standard or complying with it? **Compliance comes first** — "the mommy says to the toddler: *Johnny, don't touch the stove*", she doesn't explain thermodynamics. (2) Full understanding of every programming decision **may take books and years of experience**, and you cannot afford to wait. Hence the register: **Do / Don't / Avoid / Never**. *"Why? Read one of my books."*

- **Purpose of a standard: prevent problems from happening.** It sits squarely in the *preventative* domain — a first comprehensive coding standard is a first-class preventive measure against known and recurring problems.

- **"Our monkey brain cannot handle the complexity of modern software development."** The standard is the *only fighting chance* you have.

- **The Boeing B-17 origin story (1934).** No USAF yet — the **Army Air Corps** kept crashing and dying. Boeing: "It flies fine on our machines." You cannot fly the B-17 as four single-engine airplanes — **emergent behavior** that doesn't exist in a single-engine plane. Four monster radial engines suck in so much fuel they **shift the center of gravity in flight**: all fuel on the left wing + left turn = spin; drop bombs and the CG moves again. Boeing developed **the checklist** (take off, land, turn — turns require coordinating with the flight engineer to shuffle fuel and adjust mixture). Planes stopped crashing; now every plane has one. **"If you have an airplane checklist, does it make you a pilot? No."** But it is a concise do/do/don't list you later *ascribe meaning to* so you don't forget it.

- **Juval's rule: every developer learns the standard by heart and passes a test — if they don't pass flawlessly, they don't write code.** The professional gauntlet:
  - Doctors pass a **by-heart test on Gray's Anatomy Atlas**. *"Nurse, is the spleen before or after the liver?" "Behind the liver." "I knew it, I was just asking."*
  - The anesthesiologist operates a machine with a hundred dozen levers that will kill you and bring you back, from an enormous manual. *"I wonder what this button does… Control-Z? There's no Control-Z."*
  - Every time a pilot is certified on a new airframe the **FAA** requires a checklist test — the checklist is **so big it would fill a suitcase**; the FAA designates **"memory items"** and allows **one mistake**.
  - Lawyers pass a **closed-book** local bar exam on equally thick material.
  - Electricians certified in **Santa Clara County** must pass the Santa Clara electrical code exam, by heart.

- **"Our basic expectation of professionals is that they know their trade by heart."** The "with my monkeys" excuse means *I find you guilty of not perceiving yourself as professionals* → you don't perceive software engineering as a profession → **anything goes and nothing matters**.

- **Adoption technique.** Step one: download the IDesign coding standard (or design standard / WCF standards), **read it yourself**, and make sure you can support any directive — if you don't like it, **change it, it's your project**. Step two: send the email titled **"Standard Adoption Meeting"** — not *review*, not *consideration*. The subject line already declares the outcome.

- **What actually happens in the room.** They grip and litigate individual rules because they cannot say the real thing: *"We don't need those stinking standards. It was so much better to be a lawless filthy monkey smearing code around however I want."* So they fight **attrition**. Crucially, **they don't resent the elements of the standard — they resent being corralled into a structure.** *"Do wild animals like to be corralled into a structure?"*

- **The sign sheet.** "Me, Joe Developer, for now I want to comply with the standard. Signature." And they sign — because **not signing the company's coding standard is a for-cause violation**: instant termination regardless of labor laws or tenure, like sexual harassment or financial misconduct. Worse, for-cause violations go on the **permanent record** and appear in every background check. Next review: *"What's going on? You didn't play, you said you would."* Within no time they forget they ever griped and are **much happier for it**.

- **Public vs internal standards.** The public IDesign C# standard is deliberately **bare-bones**: "if I published a standard that truly demanded how you write code, you wouldn't be able to do it." Internal team standards are **everything in the public standard plus this, this, and this** — *much* tighter.

- **Violation ladder (energy project):** 1st = teaching opportunity; 2nd = not so good; 3rd = suspension; 4th = you're out. **Nobody wants to walk** — nobody tolerates repeat offenders.

- **You must write clean code to begin with;** otherwise nothing survives review. **Code review catches the occasional slip, it does not rehabilitate.** Juval's bar to his developers: *"When you're sitting on the toilet thinking about code, your code in your head is compliant with the standard."*

- **"That's how we do things here."** Pilots don't fly the next airline the way they flew the last; hospitals each have their own procedures. If you think your developer is at liberty to make it up as they go — God help you.

- **Practical tricks if "my developers won't":** don't staple it to their forehead — **tape it to the monitor, print it, flip through it**; after a while it becomes second nature.

- **The blunt truth:** *"You, everybody on this call, do not know how to write code — except if you're already working on one of my teams. You think you do; you don't."* Every practice, from declaring variables to exception handling to asynchronous calls, is done **the worst possible way**, no matter the years of experience. Testimony (Remco): before joining he considered himself a good developer — "I'm a badass now" — and in hindsight did he actually know how to code? **"No."** Then their eyes open: "I'm so embarrassed by my old self," and they become **the standard cops**.

- **Two accelerators: tools and the hundred monkey experiment.** Absorbing a "lawless monkey" from another team is far easier **into a team that already practices a standard**.

- **The enforcer.** The energy project built a massive coding standard **enforcer**: **project settings + .editorconfig + Roslyn analyzer work** enforcing the *team* standard (stricter than the public one). It was built because imported framework code carried **thousands of violations**; it highlighted them and they were fixed slowly. Now it finds nothing — its value is **remediating existing code**; new code you simply write clean. A Roslyn version on the IDesign website enforces the public standard, runs **as part of compilation**, and is **extensible** (skip rules, change severity, add your own).

- **AI and standards: garbage in, garbage out.** Most coding AIs were trained on a vast amount of *subpar* code; forcing your code to look like that produces bad things. Countermeasure: use **good references** and techniques that **augment the AI with what you consider good code**. The next-generation enforcer will enforce **qualitative** rules such as "write readable code." *"Don't have the AI review your code and give you feedback without actually knowing what good even looks like."*

- **You also need a comprehensive design standard.** *"Up to a second ago it never crossed your mind that you should standardize design. Of course you should."* A standard **does not replace the need to know** — you still need the context, like an airline checklist that just makes sure you did this, this, and this.

- **The design standard: nine pages, five useful.** Cover page, table of contents, preface, resources — leaving **five pages** that are "all my knowledge of design," covering both **system design and project design**. *"Think about it — five pages. That's all it takes. Not a big deal at all."*

- **DIRECTIVES** — rules you should *never* violate; violate them and **your project is dead**. **GUIDELINES** — never violate unless you have an extraordinary reason; **"spoiler alert, you don't."** One or two guideline violations won't kill the project, several definitely will.

- **Prime directive: "Never decide against the requirements."** Comply with this one alone and **everything else falls out of it**.

- **The anti-popularity heuristic.** Nobody explains the prime directive because everybody is already doing the opposite. Whenever you identify something **everybody is doing uniformly**, it is not just wrong — it is *the worst* way of doing it; **flip it and you will find the best way.** ("Everybody's buying, prices through the roof — what do you do with your house? Blood flowing in the streets, brokers jumping out windows — what do you do?")

- **Sample directives from the design standard:** provide **composable design**; **design iteratively, build incrementally**; **design the project to build the system**; build along the **critical path**; capture **required behavior, not required functionality**; describe required behavior as **use cases**; document use cases containing nested conditions with **activity diagrams**; **avoid multiple architects**; have a **core team at the beginning**; ask only for the **lowest level of staffing** to progress unimpeded along the critical path; always **assign resources based on float**.

### Metrics Collection

- [Transcript](../99-Resources/Transcripts/Quality%20Assurance.md) — *Preventive action section*

- **Very easy to measure software** (complexity and many others). But metrics are almost never useful **in isolation** — a doctor measuring temperature finds a fever but doesn't know what's wrong; measure temperature + blood pressure + sugar + hormones + kidney function and **identify patterns** and you get clues. So collecting alone does nothing; you must **analyze**.

- Many organizations have SOPs that say "collect the metrics" — they collect so they can check the checkbox for the regulator, and nobody analyzes.

- **Don't look only at the here and now.** Metrics may still be **green** but show a worrying **trend**. "You don't wait for it to become not good — based on the trend you act now." Analyze historical trends and **project** the metrics. Examples: tracking effort and progress; tracking **float of near-critical changes** to see which areas of the project will start leaking effort into other parts, so you can be proactive.

- **Many collect and analyze but fail to act** — usually not from laziness, but because the required action is so overwhelming and staggering that it **paralyzes** them. "It's pointless to collect metrics and analyze them if you don't act on them." Sometimes it's decisive action on multiple fronts; QA must enforce. "It's a hell of a lot easier to fix the problem when it's small than when it's big."

- **Release volatility** (from the [Quality Control lecture](../99-Resources/Transcripts/Quality%20Control.md)) — **defects you were supposed to fix ÷ defects you did fix, over time.** "Now that's a nasty one." Fix 2 but were supposed to fix 10 → what happened to the other 8? Fix 6 when supposed to fix 2 → where did the other 4 come from? Juval's own problem at his second release: **"I don't have any defects. What is zero divided by zero? Nobody knows."**

- **The units of suffering are time.** Less exposure = less suffering, regardless of intensity — the insight that let him walk out of the quarterly quality-review tribunal with a single empty transparency.

### Metrics — the full lecture

- [Transcript](../99-Resources/Transcripts/Metrics.md)

- Everything above is the *philosophy* of metrics. This lecture is the *metric*: **complexity** — what to measure, the thresholds, the tooling, and what to do when the number is bad.

- **One addition to the doctor analogy:** the correlation runs both ways and is not one-to-one. "It could be that the patient has a fever, doesn't have a fever, and the patient is still sick."

#### Size is a dead metric

- The classic metric was **lines of code**, and Juval rejects absolute LOC: *"we all know we can have really simple lines of code that are so diabolically complex nobody can understand, but we can have easy-to-digest code that everybody can maintain."* So **measure proportions, not quantities**.

- **Exhibit:** a project from his pastor, shipped on schedule, on budget, with zero defects. In the treemap **blue = services code** — and **roughly half the project was not services code at all**: installation scripts, test environment, test code. *"And I think that's probably a good ratio."* Inside the blue block there is a second similar proportion between *actor service code* and another kind of code, which he defers to the next lecture.

- **Why function points failed:** people tried **function points** (thread = 10 points, user dialog = 5, database access = 3, summed). Two fatal problems: it is **incredibly labor-intensive**, and it is **subjective** — *"how many points is launching an asynchronous call? I don't know. Depends who's doing it."*

- **Why counting screens failed:** "look at Google. There's a very simple user input. Is that all of Google?"

- **Cyclomatic complexity wins** because it is a *formula*, and where there is a formula you can write tools. It measures **how convoluted** the code is — *"how like a ball of mud, like a hairball the cat dragged under the bed is your code."* **The best predictor of code quality and project status is complexity**: "if the code is very complex, the chance of you having any shadow of quality or meeting the schedule and the cost is about zero."

- **Tooling:** Visual Studio's **Code Metrics window** reports cyclomatic complexity per **method**, per **type**, per **package/assembly**. Juval insists on a **graphical** view — *"if I'm looking at all the numbers, my brain cannot wrap itself around it"* — in the treemap **big and dark is complex**.

#### Non-linearity: area vs volume

- The treemap encodes complexity as **surface area** (side squared); an alternative tool encodes it as **volume** (spheres, r cubed). Which is right? **It depends on the developer.** **Junior developers cannot handle high levels of complexity — even when they instigated it; senior developers typically can.** So: *square for a senior developer, cube for a junior developer.*

- **Live demo:** a small sphere inside a large one — how many times does it fit? Order of magnitude 1, 10, 100, 1,000, 10,000, 100,000? **Answer: a million.** *"This is an example of how incapable your brain is of doing nonlinear math. You would say maybe a thousand. No — it's a million. It's a thousand times worse."* His proof: **the Sun vs the Earth** — the Earth is iron, the Sun is hydrogen; how much heavier? "I don't know, a million times. Why? Because that's how aggressive the cube is."

#### The defect tracking system is a pack of lies

- If your mission is to fix a poor-quality code base, **the last thing you should do is open the defect tracking system**. Four reasons: (1) not all defects are in it — only the ones you *know about* or *had time to record*; (2) not everything in it is a defect — some are **feature requests**, some are **symptoms** of the real problem, i.e. you recorded the symptom, not the underlying problem; (3) **severity is nonsense** — there is no "itsy-bitsy little bug," **every single defect is a monster-killer defect that can take down the entire system**; (4) therefore you cannot triage from it.

- **What to do instead:** defects are **not uniformly spread** — roughly **80% of defects in 20% of the types** (a **Pareto distribution**), and **the more complex types have more than their fair share of defects**.

- **The algorithm:** measure **all** the types, calculate cyclomatic complexity, and **identify the most complex component and clean that one up first** — *"I bet that if you clean that one up, it will do more for quality than anything else in the system."* Then the runner-up. Keep going.

#### Thresholds and the gatekeeper rule

- **"Nobody should check in really complex code. Nobody."** Working numbers: **no more than 100–150** cyclomatic points per type; *"between you and me, **75 is probably the upper limit of complexity we'll ever find**."*

- **Derivation of 75:** in **ServiceModelEx** he has one type that is *"a fundamental breakthrough in modern software engineering"* — doing something considered completely impossible, including inventing a new type of something that did not exist before. That type measures **75**. *"Where are you gonna get 75 in your code? You're writing simple business code. Are you doing fundamental breakthroughs in modern software engineering left and right? Probably not."* He **doubled his own most complex type** → **100** is the standard.

- **Derivation of 10:** a well-written method has complexity **1**; allow an order of magnitude worse → **10**; times ten for the type → **100**.

- **Make it a tool rule, not a policy memo:** install a **gatekeeper rule** in the development tool — you are not allowed to check in a type above ~100 (or a method above ~10). Whatever number you pick.

- **Applies to internal and external code alike.** A vendor swears it passes all testing and complies with all requirements — if it is hideously complex, **do not accept it**. Tell them **in advance**: "we require at most this level of complexity, and we are going to measure it — and you're not getting paid if it's complex." (They'll try to game the measurement; the answer is *"we're gonna weigh the whole thing and count it."*)

- **Meta-caveat on every number here:** *"every guideline I give you, every number is mushy. It's a low bar… All my guidelines are low bars. Just meet your commitments. I'm not raising the bar."* And even 100 or 75 is **ridiculously complex** — methods should be short, concise, easy to understand.

#### Refactoring is evil

- Definition he grants: *"refactoring is the act of arranging the furniture in the code differently without affecting the semantics of the code."*

- **You can never be sure you didn't change the semantics.** Even after full-blown system and stress testing the best you can say is *"we didn't change the semantics."* And **all the testing done on the code so far goes null and void** — *"you actually deduct value from the project."*

- **The box argument:** he draws an activity inside a box, doesn't say what's inside, and specifies its properties — **by its very definition it is precluded from adding value; it is expensive; it is risky because it breaks things; and it deducts value from work already done.** *"Would the word good be the first word that comes to mind to describe this obscenity?"*

- **Murphy's corner:** a developer feels pain in one area, refactors, makes *that* part easier — and makes **something else hideously more challenging**.

- **The competence argument:** *"in life we treat previous performance as a strong indication of future results."* Would you let a convicted pedophile babysit your kids? A doctor who butchers every patient? No. So **why do the same clueless monkeys who could not write the code well the first place get trusted to write it well the second time?** *"What has changed? Did they grow an extra brain, or perhaps a conscience?"*

- **Therefore: "every time they ask you to refactor the code, you should fire them."** And developers don't refactor once — they *con-con-constantly* refactor. **"Isn't perpetual refactoring an indication of perpetual inability of ever getting it right? In which case, why engage in it in the first place?"**

- **The book asymmetry:** how many books on how to refactor code? ~a hundred. How many books on **how to write code so you never have to refactor it**? **One** — and it requires investing in **proactive thinking**, whereas "what are human beings more — proactive or reactive?" *(The transcript renders the title as "writing software"; given the vault's references to* Righting Software*, confirm before quoting the title.)*

- **Etymology as argument:** *refactoring* comes from the Latin **facere — "to make"** (cf. *factory*). So "refactoring" = **"I need to remake the code."** Say it to your boss: *"Boss, I know you already paid us to do this code, but we have to remake it — because we messed it up. And we still want to get paid."* A boss with any sense says: *"Thank you for letting me know you messed it up. I require you to remake it **on your own dime**."*

- **The operational check-in rule (the hardest, most quotable part):**
  1. Measure the **entire code base**, write the complexity number down.
  2. Engage in your "fetish obsession with refactoring".
  3. Measure again. **You are not allowed to make it worse.**
  4. Improvement is not enough: **1000 → 900 is not acceptable.** *"There is no material difference between 900 and a thousand — both are hideously complex."* And you still owe me all the re-testing.
  5. **Requirement: a square-root reduction in complexity.** From 1000: 900 — no. 800 — no. 500 — *"I like where this is going,"* still complex. 100 — *"borderline."* **30 — "okay, I'm listening."** (√1000 ≈ 31.6 — the endpoint of the ladder is exactly the square root.)
  6. *"By the time you get it from a thousand to thirty, you probably shouldn't keep refactoring it."*

- **Ongoing goals, and the entry rule for inherited code: "Do no harm."** From now on we do not make it worse — *every line of code, every comma we put somewhere must not increase complexity. Not even by one point.*

- **Expected shape: a very aggressive L-curve reduction.** Down, down, then it **levels off** at a **fundamental level of complexity you probably cannot shake away**. Hopefully that floor is manageable — but now you know where the project is going. **If complexity keeps going up, bad things are happening. "Stop flying blind."**

#### Framework complexity, and two analyzer penalties

- **A good framework is characterized by a decreasing level of complexity bottom-up.** WCF's programming model on top is *"deceptively simple — it's just a few attributes and you move mountains"*, with insane complexity underneath. **The public types should be the least complex of your framework.**

- **Penalty 1 — advanced features raise measured complexity disproportionately.** C# **iterators, anonymous methods, LINQ**: write a simple anonymous method and *"the compiler is spewing a mountain of nested classes with backpointers… It makes a copy of the local variables into member variables of the nested hidden class and wires it all together. You want a cyclomatic complexity analyzer on it — complexity explodes."* **Discounting rule:** if your developers don't know what LINQ or anonymous methods are, **include** the generated complexity — *"for them it's just unbelievably weird and complex."* If they are comfortable with those features, **measure with and without** and compare.

- **Concrete case — the `Collection` class in ServiceModelEx.** Two complaints about LINQ: (a) **missing queries** — `Distinct`, `Unique`, `Complement`; (b) **LINQ doesn't respect you** — it takes an `IEnumerable` and returns an `IEnumerable`, so `array → LINQ → IEnumerable`, *butchering your design intent*. Fix using **overloading by type parameter arity**: array-in returns array-out for **every** LINQ query. Result: **one file with 1200 `yield return` statements**. *"You want the cyclomatic complexity analyzer on it, it explodes. But each one of those augmentations is very simple."*

- **Penalty 2 — compensating for an oversight in the framework you use.** Going *against the grain* drastically increases complexity — **and that is what the two monster boxes are.**

- **The Code Access Security / WCF war story** behind the treemap monsters:
  - **.NET 1.0 shipped with CAS.** Its idea: *it is wrong to look at what the **user** is allowed to do; we must look at what the **code** is allowed to do* — because **even if you're admin, you can still make mistakes. Click that link you shouldn't have.** Modern echo: Windows' "are you sure you want to install this?" prompt. About **24 permission types**, each with sub-scopes.
  - **The elegant part:** the code you are executing may have the permission, but the code that called it may not. So in .NET 1.0, **every call walked the entire call stack**, verifying every caller had permission.
  - **WCF v1:** the team reasoned that running services in **partial trust** would make the test matrix **80 factorial cells** — *"more than enough to uniquely name every quark in the universe several times."* So v1 **demanded full trust**. Consequence: **WCF could not run in a partial-trust environment such as a web server.**
  - **WCF v2** moved the `FullTrust` demand off the assembly onto **specific bindings**. Juval saw his chance and **completely redid both WCF and .NET to restore CAS into WCF — without changing the programming model of either.** *"This kind of code required black-belt WCF programming and black magic — occult, sacrifice chickens, moonlight programming in .NET."* He calls it **the single most complex thing he ever did**. Unusual inversion: *"typically you hack things to decrease security. I did the opposite."*
  - **The MSDN veto:** he submitted a white paper to MSDN; routed to the WCF team, who replied **"nobody should do what you did — we are vetoing the paper."** He emailed the .NET marketing manager: *"I'm the greatest advocate on the planet of WCF. Your team says no. Fine — I'll publish it on the IDesign website, and the preface will voice my opinion about why you vetoed it: **because you're jealous that I did something you said was impossible.**"* The marketing manager came down like a ton of bricks on the WCF team; the paper was published.
  - **How he beat 80!:** simple engineering reductions and down-to-earth assumptions reduced the test matrix to **2200 cells**. He tested **every cell** — half the time the result was a security exception, and half the time **he didn't know whether what he was attempting was impossible or just beyond him**.
  - **Epilogue:** the **next release of .NET cancelled Code Access Security completely and utterly** — *"which was never my intent."* To the point that **the giant box no longer even compiles**, because the namespaces are gone.
  - **Moral for metrics:** *"now I understand this big box and this big box. The rest is pretty easy."* — **anomalies in a complexity treemap are archaeology, not noise; go find the story behind the box.**

#### Code complexity ≠ design complexity

- They are **not the same derivative**. *"It is extremely unlikely you could have a simple implementation of a really complex design — that's probably never going to happen. But you can absolutely have a complex implementation of a simple design. So beware of that."*

- **Consequence:** low measured complexity is **not** evidence of good design, and high measured complexity is not automatically evidence of bad design — you still have to know whether you are reading the design or the implementation.

#### Complexity ↔ unpredictability (the CMM payoff)

- **Complexity correlates to unpredictability.** At **CMM Level 1** it is just the mob trying to write software and **all bets are off** as to how long anything will take.

- But unpredictability has a second dimension: **even if you are non-repeatable, how wide are the swings — what is the amplitude?** **Very complex code** that took a year last time → next time **five or seven years**. **Less complex code**, still non-repeatable → next time **about a year again, or two years**. **The more complex the code, the wider the amplitude** ⇒ the software environment is more out of control ⇒ business people get more aggravated.

- **Closing calibration:** *"I'm not saying go to CMM level five next Monday, but just fixing those levels of complexity will make everybody a hell of a lot happier."*

### Logging and the Flight Recorder

- [Transcript](../99-Resources/Transcripts/Logging.md)

- **The premise is mundane failure:** things break. The whole frame is that you cannot reason about a broken distributed system from memory or from a single component's view.

- **Every jumbo jet has a black box** — and Juval immediately deflates the name: "it's actually not black and it's not a box. It's actually orange and there's three of them. But conceptually it's a black box." It records **far more than cockpit conversation**: every instrument, everything on the displays, and **a bunch of sensors that are not even displayed**.

- **The aviation argument, stated as an absolute: "There has never been an accident in the history of aviation where they found the black box and did not figure out what went wrong."** That is the entire argument for comprehensive recording — and it works *on top of an unbelievable level of complexity*. Credibility anecdote: about fifteen years ago the **COO of IDesign's previous job was director of IT for the Boeing crash investigation team**.

- **Therefore: build a comprehensive flight recorder.** It records everything — every argument to every method, every call, "to every this, to every that."

- **Logging is also a development facility,** not just a post-mortem tool. Even while you develop, "complexity can run away from you and you won't be able to make sense of it," so you use logging to **see what your own system is doing**.

- **"The first task in every project needs to be a logbook. It is that important."** Build it before anything else so you can log from the very first line of code. Retrofitting is hard — "like doing it after the fact," you must add all the hooks, change base classes, "it's really difficult." If the logbook is already there, developers naturally treat logging as a **developer service** they always do.

- **"You cannot do too much logging."** His joke: two developers standing next to the smoldering remains of their system, signing to themselves *"we did too much logging."* — "Nobody's ever heard about those two developers."

- **Third-party components:** a "vendor" may just be **another team in the building**, and you never talk to them. Solution: **make the logbook yet another service in your system**, and hand that service to the other vendor so they log into it too.

- **Verbosity is a spectrum, not a switch** ("Logging is not a Boolean flag you do or you don't"). Range: lightweight (only the time of the call and which machine did something) → full-blown (every parameter, every value of every parameter, of every method, on every class, on every service). Verbosity must be **dynamically toggleable** — maybe the GUI sits at some trace level, but **as the system senses something is wrong it automatically raises the level of logging**. **"Pick the tool, the right tool for the job."**

- **Exception promotion.** In a long chain A → B → C → … where something detonates at the bottom, the exception climbs and **detonates other things at each hop**, each detonation leaving a trace and changing system behaviour. "You don't care about what the cloud of debris looked like. You care to see what was the original problem." By the time you read the log at the bottom it tells you nothing. The technique (chapter 6 of *Programming .NET Services*) is to take the **inner information and tunnel it all the way to the top** so it can be logged and displayed to the user.

- **Debug vs release:** in debug you can afford aggressive logging; in release, be less intrusive.

- **Faults vs exceptions.** Faults belong to *execution*: "I thought it's going to be this, it was actually that." Exceptions are **truly for the exceptional case** — out of memory, a crash. **"Most people commit a sin of even using exceptions as a way of controlling the flow of the system. No, no, no — exception is truly for the exceptional thing."**

- **Definitely avoid multiple uncorrelated log files.** With 10/20/30/40 services you would need 40 log files and 40 viewers, opening them all and piecing together in your mind what took place — "Nobody can do it. It's completely impossible."

- **Why timestamps fail.** Everyone logs by timestamp and then sorts. It fails for two reasons: (1) **clock skew** — you can never synchronize clocks down to the last nanosecond, so events can occur in one order and get logged in another; (2) **concurrency** — things happen on multiple threads, and **thread IDs mean nothing across a process or machine boundary**.

- **The replacement: activity ID propagation.** Someone — the root that started the whole thing — creates a unique ID (probably a GUID), embeds it in the outgoing message, **hidden somewhere in the headers**. Each downstream service logs that ID alongside its parameters and re-attaches it to its own outgoing calls. Now, despite 10–40 separate logbooks, you **query by activity ID** and build "a comprehensive picture of what actually took place."

- **Managing propagation is itself a design decision:** on a long call chain that has nothing to do with the actual problem, a subsystem near the bottom may **issue a new causality ID independent of the upstream one**, starting a fresh separate trace there instead of dragging in the whole irrelevant chain.

- **Pass-through services:** a service that legitimately says "I have nothing to do with this problem — the clients above me and the services below me, ignore what happens here, I'm perfectly fine." It still **propagates the ID** so logging works across it, but you ignore its internals.

- **Heisenberg, stated as a macro-scale law:** "whenever you observe something, you change it." For an electron you shoot a photon at it and drastically change it — but it's **also true at the macro level**: logging changes the system, and the more extensive and intrusive your logging, the more different your system gets. At the limit you can log something, "but it's not really your system anymore."

- **The signature formulation — quote it exactly: "You can get a very good picture of another system, or you can get an inaccurate picture of your system, but you can never get an accurate picture of your system. That is not going to happen."**

- **Mitigation depends on the nature of the problem:**
  - **Highly temporal problems**, timeline-sensitive, where you cannot tolerate "things happen like this but you log them like this" → **inline (synchronous) logging**: log everything in exactly the order it happens.
  - **Non-temporal problems** → **asynchronous logging**: log sometime later. Order may differ, "but it doesn't change as far as you're concerned what is going on."

- **Synchronous logging's failure mode:** massive load on the logbook, because everybody is logging synchronously and "bam, it crams it into there." Mitigation: **distribute the logging, consolidate the viewing.**

- **"An old observation in software engineering: anything you can do asynchronously, you must do queued."** So consider **queued logging**: push into a queue, and much later consolidate into a single logbook. "I don't care if it happens much later, I'm still okay with it."

- **No prescription:** "Which one is it? I don't know, elaborate and discuss, it's your system. It's just giving you ideas of how to do these things."

- **Recommended reading: *Programming WCF Services*.** "Not because WCF is relevant, but because that book is not about WCF. It's about how to design and build distributed systems. I'm only using WCF as a medium for expressing the design ideas." In the **800-page** book there is **less than 20 pages of actual WCF code — he counted it**. Everything else is design diagrams and concepts, including all the error-management material just discussed.

- **Concrete artifact:** WCF ships with an example logbook that lets you, **after the fact**, reconstruct the interaction between your various services, including interaction graphs. Many other tools do this kind of extensive logging and tracing.

### Management Visibility

- [Transcript](../99-Resources/Transcripts/Management Visibility.md)

> [!note] This section deliberately duplicates as little as possible
> The earned-value chart mechanics, integration-point reporting, "on time throughout", zero-defects induction, and documentation-as-trust-signal all already have canonical homes in this vault — see [[Modules/Project Planning#Project Tracking — Earned Value, Shallow S, and Living Plans]], [[Modules/Project Planning#Progress Reporting on Integration Points, Not Features]], [[Modules/Project Planning#Cost vs. Time Failure]], and [[#Zero tolerance for defects]]. What follows is the material unique to this lecture.

#### Management Is a Project Risk

- **Opening image:** *"Not a good idea to walk in the darkness without anybody knowing what you're doing."* Visibility is the whole subject — an unobserved project is a project **assumed guilty**.
- **Manage management like any other risk:** *"You are proactive about it. Don't be reactive."*
- **"Every manager out there is scheming to cancel your project."** Stated as provocation but delivered as fact — cancellation is a live, default option on every status-meeting agenda.
- **"Being canceled is a CLM"** — career-limiting move. This is the *manager's own* incentive, and it is what explains the hunting behaviour. (CLM defined in [[Modules/Project Planning#The Boss Argument: No Good Outcomes]].)
- **The shark analogy, new angle:** *"Managers are like sharks. How do they know a project is sick? It doesn't show progress."* Progress is the scent. **Silence reads as sickness.** Note this is a *different* figure from the sharks-in-the-water analogies in [[Modules/Project Planning#The Boss Argument: No Good Outcomes]], which are about throwing design attributes overboard.

#### Never Wait to Be Asked

> [!danger] The question you must never let be asked
> *"Because if a manager is asking you where are you, the manager is really asking, **should I cancel you?**"*
>
> By the time the question is asked, you have already lost the benefit of the doubt. The countermeasure is therefore **unsolicited, pushed status**: *"you have to push your status to them."*

- **The only acceptable answer to "where are you":** *"Your own schedule, on budget, with zero defects — that's where you are. There's no place else to be."* No third state, no hedging, **no "about 85%."**

#### The Four "Throughout the Project" Guarantees

Juval states one pattern four times over:

1. Zero defects **at the end** only if zero defects **throughout**.
2. On time **at the end** only if on time **throughout**.
3. On budget **at the end** only if on budget **throughout**.
4. Great documentation **at the end** only if great documentation **throughout**.

> [!quote] "This is life. This is how it works. There's no shortcuts."
> It rules out deferred heroics: *"I'm gonna allow this bug to swell, and then towards the end I'm gonna roll up my sleeves and smite all those evil defects. Impossible. It never works this way. It cannot happen this way."*

- **Dangling reference:** Juval calls this **"the securing pattern"** as though already named. It is **not defined anywhere in this vault** — treat it as a cross-reference to resolve when the missing session is recorded, and do not invent a definition.

#### The Chart as Signal, Not Report

- *"A great status report is the earned value chart"* — sent **every week**, schedule and budget. Explicitly **not features**: *"you cannot talk about features because the features come at the end, not throughout."*
- The chart's real function is psychological: **"The message is, I know what I'm doing. I'm in control. I'm trustworthy."** Mechanics live in [[Modules/Project Planning#Project Tracking — Earned Value, Shallow S, and Living Plans]]; here Juval adds none.
- **Constant stream of good news, measured in integration points:** *"Definitely use your service integration point as milestones."* Format — *"Today the project met milestone three, we integrated A with B, we want to integrate C with D."* The manager reads it in a minute and concludes *"milestone was made, progress was made, let me micromanage somebody else."* Cheap, legible, repeatable. Same mechanism, concretely, in [[#Peer Reviews]].

#### The Trust-Deficit Diagnosis

> [!quote] "You all suffer from chronic deficit in trust. Why? Because every commitment you ever set your name to was written on ice, your quality is nowhere to be seen. You're incredibly slow and expensive, full of defects, and then you had the audacity of calling yourself agile. What are you trying to gaslight the manager? You think they don't know this?"

Same sentiment, blunter, in [[#Architect and the Team]] ("every commitment was written on ice, promised agility and delivered mud").

#### Micromanagement Is a Trust Problem, Not a Time Problem

Juval removes the easy excuse first:

- Yes, you work harder than your parents — he names the **falling labor participation rate** (you must now earn enough to support lots of other people), offered as an aside he does not expand.
- But *"your manager is working hard too. **Everybody today that has a job is beaten to pulp.**"*

**Therefore micromanagement has exactly one cause: distrust.** *"Since we know your manager is also working very hard, and they still choose to micromanage you… Is it because they have the excess time? No, it's because they don't trust you."*

**Earn exemption by being visibly professional:** design reviews, an SDD with all the diagrams, *"there isn't a single typo in a document,"* a clean pushed status report → *"these guys clearly know what they're doing, clearly professionals. I'm gonna go and micromanage somebody else."*

> [!quote] "You get the manager off your back. That's it. That's all you need to do."

#### Demos — But Never of Features

- *"You cannot demonstrate any feature because features come at the end, once you have integrated the whole system."* Substitute the **service testing environment (STE)** or your **simulators**.
- **The sleeve-grab demo:** grab a manager — *"You gotta see this. Look, we are calling into this service, we're populating this, and here we're showing on this grid what's happening over there."* The manager concludes: **"Buttons were clicked, grids were filled, progress was made."** You gloss over the fact that no feature was demonstrated.
- **Cynical operational premise:** *"These people are simpletons, and you have to manage them as such."* The demo's value is psychological, not technical. Delivered deadpan, not as an apology.

#### The Goal State: the Closed-Door Test

> [!success] Success looks like avoidance
> *"When you're walking down the aisle and you see a manager, the manager immediately jumps to another room and closes the door because they fear being dragged by the sleeve and see another silly demo. That's an excellent place to be at."*

**The closer:** *"It should be no doubt in anybody's mind where you are: your own schedule, zero defects. **The last project I'm ever gonna cancel is your project.** That's a good place to be at."*

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

> [!question]- 61. Juval says that when a manager asks "where are you?", they are really asking something else. What — and what is the only correct answer?
>!
> [!summary]- Answer
> They are really asking **"should I cancel you?"** — asking is itself evidence that the project isn't radiating progress, which is the scent sharks follow ("how do they know a project is sick? It doesn't show progress"). The only acceptable answer is **"your own schedule, on budget, with zero defects — there's no place else to be."** Hence the rule: never wait to be asked; push your status proactively.

> [!question]- 62. Why can't a weekly status report or a demo be built on features, and what three things must you use instead?
>!
> [!summary]- Answer
> Because **features come at the end, not throughout** — you cannot demonstrate anything until the whole system is integrated, so feature-based reporting either goes dark or lies. Instead: (1) a **weekly earned value chart** showing your own schedule and budget; (2) **service integration points as milestones** ("we integrated A with B, we want to integrate C with D"); (3) demos of the **service testing environment or simulators** — "buttons were clicked, grids were filled, progress was made."

> [!question]- 63. Explain the argument that micromanagement is a trust problem rather than a time problem. What is the "closed door" test?
>!
> [!summary]- Answer
> He removes the obvious excuse first: you work harder than your parents, but so does your manager — *"everybody today that has a job is beaten to pulp."* So the manager is not micromanaging for spare capacity; they are doing it **because they don't trust you**. Fix it by being visibly professional — design reviews, a complete SDD, not a single typo, pushed status — so the manager decides *"these guys clearly know what they're doing, I'm gonna go micromanage somebody else."* Proof of success: you round a corner and the manager **jumps into another room and shuts the door** to avoid being dragged to another demo.

> [!question]- 64. State the four "throughout the project" guarantees and the excuse they rule out. What is the unresolved term Juval uses for this pattern?
>!
> [!summary]- Answer
> Zero defects, on time, on budget, and great documentation can each only be true **at the end** if they were true **throughout** the project. It rules out deferred heroics — letting defects accumulate and then rolling up your sleeves to "smite all those evil defects" at the end: *"impossible, it never works this way, it cannot happen this way."* Juval calls the pattern **"the securing pattern"**, which is **not defined anywhere in this vault** and is a dangling reference to a session not yet recorded.

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

> [!question]- 13. What is the prime directive of teamwork, and what single behavior does it forbid?
>!
> [!summary]- Answer
> *Never prevent others from doing their work.* It forbids pulling on the sleeve of another team member for help during onboarding — if that person is on the critical path, you just derailed the whole project. The corollary: never "help the new guy" by having them chase people for answers.

> [!question]- 14. Why is designating a "lightning rod" (one person everyone asks) not a real fix for onboarding?
>!
> [!summary]- Answer
> Because the lightning rod gets bombarded with the same questions over and over and eventually writes an FAQ/wiki to cope — which is just formalizing the same repeated, wasteful process. The organization still hasn't designed the onboarding.

> [!question]- 15. What are the rules for building onboarding categories — and what do you do with a category that has less than 3 or more than 10 elements?
>!
> [!summary]- Answer
> Categories cover domain, software design, system requirements, architecture, detail design, framework, technology, process/culture, standards, operations — ordered by logical dependency. Fewer than 3 elements → merge it into another category (1–2 items isn't a category); more than 10 → split into subcategories (too bloated).

> [!question]- 16. Juval gives two reasons to estimate and track how long each onboarding element takes. What are they?
>!
> [!summary]- Answer
> (1) Variance detection — planned 3 hours but spent 3 weeks means you're missing information; planned 3 days but done in 3 hours means they missed material. (2) You can pit people against each other — "everybody is at 60–70%, you're still at 15%" — to identify who is falling behind.

> [!question]- 17. Why are post-onboarding interviews done with both the architect AND the domain expert, in groups AND individually?
>!
> [!summary]- Answer
> The interviews' purpose is to improve the onboarding process itself — identify remaining gaps, see what the onboarding didn't cover, and constantly refine it. Soft, hard-to-document, folklore knowledge transfers best in person, and the domain expert and architect see different gaps.

> [!question]- 18. What are domain cutters, and what makes a *good* cutter question?
>!
> [!summary]- Answer
> Short weekly sessions where a domain expert poses a question that forces developers to do research. A good question is one you *can't* Google and be done with — it touches fundamental aspects of the domain knowledge and attacks the very added value of the system ("Why are we here? What's the market differentiator?").

> [!question]- 19. Why does Juval say "the onboarding must not be the sum of the learning"?
>!
> [!summary]- Answer
> Because onboarding is only a primer that kickstarts the learning effort — it's not the end of the journey. Developers must keep improving on an ongoing basis, and the domain never ends: "it's like an onion, there's more layers and more layers and more layers."

> [!question]- 20. What two things does tracking participation in the domain cutters reveal?
>!
> [!summary]- Answer
> (1) Drop-off: people participate initially, then busy life takes over and they taper off — not acceptable, so you either stop or change something. (2) Talent signal: developers who consistently participate and get answers right reveal themselves as your above-average developers to pay attention to.

> [!question]- 21. A team runs reviews by joining a Zoom call where the author scrolls the code and everyone comments live. Name the technique and explain precisely what separates a formal review from it — plus the one case where the walkthrough is the right tool.
>!
> [!summary]- Answer
> That is a **code walkthrough**, not a review. In a formal review the entire artifact examination happens **offline and before the meeting** — reviewers record comments in the artifact (`//` + initials + rationale, or inline tool comments) — and the meeting reviews *only the comments*, never the code: "it's a review of the review." A formal review also requires designated roles (moderator/architect, developer-owner, reviewers, scribe), the developer's own "I'm ready for review" declaration, moderator rulings recorded by the scribe as mandatory fixes, and post-review statistics. Walkthroughs remain correct for **esoteric environments** — a weird MVVM setup, a Kubernetes installation script — where walking the architect through what it is supposed to do yields valuable feedback even though nobody there knows the technology.

> [!question]- 22. Who declares that a review can begin, who arbitrates disputes over a comment, and what happens to a finding the developer disagrees with? Why is the last part non-negotiable?
>!
> [!summary]- Answer
> Only the **developer who owns the artifact** can say "I'm ready for review" — it cannot be forced on them, because they know when it is ready. The **moderator** (typically the architect) arbitrates, asking the developer "what do you think about that?" If it must be fixed, the **scribe** records it for all developers to apply. The developer's disagreement is irrelevant: **"It's not their code, it's the company's code. The company says you have to fix it, you have to fix it. Doesn't matter what you think."** Reviewer assignment is likewise mandatory and overrides other work — the prime directive of teamwork is never to prevent others from doing their work.

> [!question]- 23. What do the code review statistics track, and what two independent trends must they show for the program to be healthy?
>!
> [!summary]- Answer
> The form records service, moderator, scribe, owner, **time spent per reviewer**, **comments per reviewer**, and **major** vs **minor** defects. Time and comment counts create **healthy peer pressure**. The two health trends: (1) the number of comments must fall **non-linearly as a function of time** (rising numbers are a bad sign); (2) the same finding must stop recurring across codebases — any comment made in anybody's code is immediately applicable to everybody else's, including people who were not reviewers or were on vacation, who must read the report and scrub their own code. Corroboration: the energy project's first review — three three-hour meetings — still produced 3 major and 132 minor defects on the best code Juval had seen in the wild; today the same review runs in about two hours and mostly finds compliance issues.

> [!question]- 24. Use the home-inspector analogy to state the purpose of reviews, then explain why Juval rejects XP pair-programming and what his body system does instead.
>!
> [!summary]- Answer
> If you design a single-family home and arrive for the first inspection to find a **30-floor skyscraper**, no inspection can fix it — they are building a different system. Reviews cannot rescue a team hell-bent on butchering your design: **"the purpose of reviews is to catch the occasional unintended misstep from your grand design"** — the supporting wall moved by accident, or a deliberate deviation you either reject or accept by crossing out the wall, initialling and signing "on this day, I approve moving this wall." XP got two things right and wrong: right that two pairs of eyes beat one (curing **code blind**), wrong that pairing works when organizations chronically lack good developers — "two bad developers don't make one good developer." Instead **every developer has a body/buddy**: problems go to the buddy first, and only if the buddy cannot help do *both* go to the architect. The buddy grows intimately familiar with the developer's code, the architect's second pair of eyes arrives **judiciously, just when needed**, and the buddy can cover the "hit by a bus" scenario. Because reviews only catch occasional missteps, this only works if everyone is already on board via coding standards, onboarding, and SDD.

> [!question]- 25. Distinguish a *directive* from a *guideline* in the design standard, and name the prime directive plus the consequence of violating it.
>!
> [!summary]- Answer
> A **directive** is a rule you should *never* violate — violating it means **your project is dead**. A **guideline** should never be violated *unless you have an extraordinary reason* ("spoiler alert, you don't"); one or two violations won't kill the project, several will. The **prime directive** is **"Never decide against the requirements"** — comply with that one alone and everything else falls out of it.

> [!question]- 26. Why is the kickoff deliberately called a "standard *adoption*" meeting rather than a review or consideration meeting, and what mechanism ultimately gets developers to sign?
>!
> [!summary]- Answer
> The subject line pre-declares the outcome — the decision is already made, so the meeting is not a referendum on *whether*. Developers grip and litigate individual rules as **attrition**, because they cannot admit the real objection ("we don't need standards"); they resent being **corralled into a structure**, not the elements. The sign sheet works because **not signing is a for-cause violation** — instant termination regardless of tenure or labor law, recorded permanently and visible in background checks. So they sign, and at the next code review you hold them to it: "You didn't play, you said you would."

> [!question]- 27. What exactly is the coding standard "enforcer", what was it built for, and why is it mostly useful for existing rather than new code?
>!
> [!summary]- Answer
> The enforcer combines **project settings, .editorconfig, and Roslyn analyzer work** to mechanically enforce the standard (the team's stricter variant; the IDesign website version enforces the public C# standard). It runs **as part of compilation** and is **extensible** — disable rules, change severities, add rules. It was built because legacy/imported framework code carried **thousands of pre-existing violations**, which it highlighted for incremental fixing. Now it finds nothing, because **new code is written clean to begin with** — its job is remediation of inherited code, never a substitute for writing compliant code.

> [!question]- 28. Juval says a good standard is "thin on the why, rich on the what," yet also demands developers memorize it and pass a test. Reconcile the two using the B-17 checklist analogy.
>!
> [!summary]- Answer
> Compliance must precede understanding, because understanding every rationale "may take books and years of experience" and the project cannot wait — the standard's job is to **minimize harm** and **prevent problems**. Hence terse imperatives (Use/Avoid/Never/Do/Don't) with no rationale, so anyone can comply without appreciating why. The B-17 is the model: four radial engines create emergent behavior (fuel shifting the center of gravity, spins on left turns, bomb release shifting it again) that no pilot can intuit from single-engine experience, so Boeing shipped a **checklist** and planes stopped crashing. A checklist does not make you a pilot, but it gives you a concise do/don't list you later **ascribe meaning to**. Likewise, memorizing the standard (like the FAA's "memory items") is the professional baseline; appreciation arrives later, with experience.

> [!question]- 29. Distinguish emulator from simulator, and give Juval's effort rule-of-thumb for each.
>!
> [!summary]- Answer
> An **emulator** is a do-nothing version of the service: every call returns hello/true/okay/zero/three. Building one is "a hair's breadth from right-click → Implement Interface → OK" plus removing the exceptions — **if you spend more than a few minutes on an emulator, you're doing it wrong**. A **simulator** is as real as the real service and indistinguishable from it: it manages state and lets you inject errors, and is sometimes as demanding to build as the service itself.

> [!question]- 30. A project has a dependency chain A → B → C → … → XYZ, so A lands at the very end. What does Juval prescribe, and what is the project-level payoff?
>!
> [!summary]- Answer
> Write a **simulator for B as the very first thing in the project**, then move A's development to the *beginning*. A no longer has to wait on the real B, so you **change the topology of the critical path and compress the project**. Cheap emulators give the same overlap for shorter chains, but only final testing needs the real dependency.

> [!question]- 31. During stress testing your remote database caps you at 200 calls/sec while the defect you are hunting only appears at 10,000 calls/sec. What happens, and what is the fix?
>!
> [!summary]- Answer
> The natural bottleneck lets the low-probability defect **sail through your entire test cycle** — you can never reach the failure rate. After the test suite is automated, perform **analysis of the natural bottlenecks and eliminate them with simulators**, then crank the testing "up to 11" and see what breaks.

> [!question]- 32. Why must mode switching between simulation and emulation be programmatic rather than a rebuild? Name the diagnostic technique.
>!
> [!summary]- Answer
> For **production-time debugging**: the system works for you but fails at the customer's because something in their environment differs. You need a management console that opens all running services and flips each between simulate/emulate on the fly, then **bisects — "looking for a line in the desert"** ("simulate me these, emulate me these, go") — so the fault localizes to one half quickly. It becomes a must because every deployment and every customer is different, each with its own peculiar version of the system.

> [!question]- 33. What exactly is a "daily build," and why must the build machine be one that has never seen the code before?
>!
> [!summary]- Answer
> Every day, regardless of progress, you take all the code to a machine that has never seen the code or any development tool, install all the tools and libraries, do a full-blown build, then deploy to target machines and run the smoke test. A fresh machine guarantees the build is reproducible from scratch — it exposes missing dependencies, hidden local state, and silent breakage that "works on my machine" builds hide, which matters because modern service systems are large and not reference-based.

> [!question]- 34. Why does the number of "roads" make configuration bugs practically un-debuggable, and how does the daily smoke test defeat that?
>!
> [!summary]- Answer
> The roads — hosting, activation, instantiation, queuing, security, transactions, synchronization, discovery, timeouts — grow combinatorially ("the number of roads is n squared," ~100 roads for 10 services), each with dials and knobs that can be misconfigured. The spectrum of combinations is astronomical; there may be no working combination at all. Energizing all the plumbing daily turns an intractable search into an **instant diff**: "what has changed since yesterday?"

> [!question]- 35. In the forced choice between daily smoke testing with no end-of-project system testing, versus no daily smoke test but full system testing at the end, which wins and why?
>!
> [!summary]- Answer
> Daily smoke testing, hands down. With a well-designed, well-built system you should have every expectation that system testing will pass (like an airline's test flight — you expect the plane to fly, but you still do the test flight). But if you reach the end of the project and the plumbing does not work, "all hope is lost." Requirement-level defects surfacing later are handled by composable design, not by deferring plumbing verification.

> [!question]- 36. What does Microsoft's statement — "after code reviews, smoke testing is the most cost-effective method of identifying and fixing defects in software" — imply about how Juval classifies code reviews?
>!
> [!summary]- Answer
> Code reviews are not really a *testing* activity at all — they are a **quality control** activity. Strip them out of the testing category and the conclusion is categorical: smoke testing is the single most important system-level testing activity you will ever do, which is exactly what Juval had been arguing independently.

> [!question]- 37. Why does analytic modeling of performance yield a partial differential equation, and why does that matter for the "fix it later" approach?
>!
> [!summary]- Answer
> Because performance depends not only on the *value* of each of the ~20 aspects per service but on the **rate of change** of those aspects (one client making 5,000 calls behaves differently from 5,000 clients making one call). The aspect settings act as **boundary conditions** to a PDE — and **not all PDEs have solutions**. So there may be no combination of dials and knobs that produces the target performance, and if the system was *designed* for poor performance, "no amount of coding can change that." Hence benchmark continuously instead of testing at the end.

> [!question]- 38. What exactly should you benchmark, how often, and what kind of number are you looking for?
>!
> [!summary]- Answer
> A **micro benchmark on your own machine, in debug mode, with Visual Studio** — not an industry-wide benchmark. Run it **every time you change an aspect** (interception on/off, database on/off, etc.), not on every line of code, alongside the daily build-and-run. You are looking only for **order of magnitude** (1 call/sec vs. 100 calls/sec).

> [!question]- 39. Describe the "reduction" technique and the rule for what "small" means.
>!
> [!summary]- Answer
> When a performance problem is too complex to diagnose directly, reduce the system to the **smallest number of services, machines, web pages, clients, and lines of code that still manifests the problem**. In the Chicago case this took three months, after which the root cause surfaced on the second day of the next session. The team "got lucky" — you must do the reduction deliberately rather than hope.

> [!question]- 40. "My system only needs two calls a minute — why do I need stress testing?" Answer using the low-probability defect argument.
>!
> [!summary]- Answer
> Because a defect that appears once every **3,000 years** of single-user use can pass through the whole test cycle and reach customers: multiply by deployments × users × sessions × clicks and it becomes a realistic, frequent incident. Rigorous stress testing compresses it — a once-a-year fault happens **every 30 minutes or every three days** — so it is **reproducible** in-house instead of producing the "customer calls / test monkey presses the button / not reproducible / back to the customer" loop. This is required even if you do not care about performance numbers at all.

> [!question]- 41. Walk through Juval's root-cause chain starting from "the developer forgot the `i++`." Where does the chain end, and why is everything before that merely a symptom?
>!
> [!summary]- Answer
> Missing `i++` → developer didn't understand what the code should do → didn't understand the domain → didn't have enough time to understand the domain → no project design, so schedule/cost/resources were mis-accounted and the project became a pressure cooker → no point doing project design against a ball of mud, so no architecture → no architect → because the organization doesn't value software development as a profession. The root cause is **the rotten culture**; every earlier link is a symptom. This is the technique behind the **C** in CAPA: climb upward until you hit the root, then go hunt the other problems that same root could already have caused.

> [!question]- 42. Name the three members of the "three-headed monster" and say which of influence / power / authority each one owns. Why does proximity matter, and what does the "failed the release" interview question reveal?
>!
> [!summary]- Answer
> **Architect → influence. QA → power. Engineering management → authority.** One body with three heads, each owning a different part of the puzzle, so at enterprise scale co-location is essential — QA can't be on another continent and the architect "on the moon" (Juval shared an office wall with his QA person, VP of Software two doors down). Asking "how many times has QA failed the release?" tests whether QA has teeth: "never" means paper tigers, "all the time" means dysfunction, and "once or twice, and we didn't like it" is the good answer.

> [!question]- 43. Explain the Swiss cheese failure mode and connect it to the benchmark-optimization incident. What was the change that actually broke things?
>!
> [!summary]- Answer
> Each guardrail or best practice is a slice of cheese with holes — no single control is perfect. You can bypass one guardrail and the next should catch you; a defect only gets through when the holes **align across multiple slices**. In the incident the developer optimized a benchmark (an SOP explicitly forbids optimizing), tested only the passing path instead of all states, let the change propagate, skipped breaking it into small PRs, and tampered with the tooling — multiple guardrails violated at once. The change that actually broke things was a **domain change**, which should never have happened without consulting the domain expert.

> [!question]- 44. "Prevention is worth a pound of medicine," yet preventive work is much harder to drive than corrective work. Give the evolutionary argument and list the world-class *preventive* mechanisms.
>!
> [!summary]- Answer
> Evolutionarily we have roughly **100 million years** of primates and only an order-of-magnitude **~1,000 years** of civilization and complex situations — not enough for evolution to make us proactive. The opposable thumb made monkeys efficient (23½ hours a day arguing and throwing feces, 30 minutes feeding) versus the cow that must chew 23½ hours a day or die; after that much wasted time, reactivity is built in. Hence the **fire-brigade cycle**: budget grows only *after* the Great Fire, then decays until the next one. Reactive "amends" often make things worse — closing the barn door after the horse escapes, or putting a heart-attack patient on a treadmill. Preventive mechanisms named: a competent **architect** producing the most loosely coupled, least complex, minimal-cost design; **project design** that plans all quality-control activities (regression testing, regression test harness, test plan, test legs, simulators/emulators); **standards** followed even if you don't understand them; **customized/extensible tools** driven by you via hooks rather than driving you; and **metrics** collected, analyzed for pattern *and historical trend*, and acted on decisively before they leave the green.

> [!question]- 45. Juval says the only legitimate reason to change jobs is to "align your career phase with the environment." Map the two extreme environments an architect should sequence through, and explain why each is right for its phase.
>!
> [!summary]- Answer
> First: the most **pristine, immaculate** environment — no defects, real standards, structure, rigor — because that is where you learn how to work correctly. But in a place that is already perfect you cannot make much of a difference, so it is excellent for learning and poor for advancement. Second: the most **decrepit** environment — "sh*t hot bottom," a giant ball of mud on fire, code nobody can compile, developers jumping out of windows — because there even a little hygiene goes a long way, "even just a little bit of light in the darkness chases away the shadows," so ordinary common sense earns you enormous notoriety and feathers for your cap. Later phases: senior role in a clean environment, VP/director, possibly VC. The wrong reason to move is "it's bad here" — it's always going to be bad everywhere.

> [!question]- 46. You are interviewing architect candidates. Give the complete screening protocol Juval prescribes, and state which candidates you reject and which you hire.
>!
> [!summary]- Answer
> Attitude is the only thing that matters — integrity, accountability, responsibility, maturity, honesty — and competence is a distant second ("I can teach a monkey to design systems; it's very difficult to teach integrity"). **Initial filtering:** require reading chapters 2, 3, 4 and Appendix B of *Righting Software*; reject those who don't read it (and arguably those who read only the assigned chapters). Ask their opinion: disagree → reject. If they agree, ask *"Whose fault is it that in the current project and all the previous ones you didn't follow these ideas?"* — **hire only those who admit it was their fault.** Reject anyone who blames the scrum master, customer, manager, legacy, or culture: those are excuses ("imagine I traded shoes with you — would I have trouble working correctly? If no, then you're the problem"). Probe the recent project: was there a schedule, a budget, any notion of time and cost, and what did you do about defects? Grill them on agility — if they can't respond quickly to change, "why do you call it Agile?" — and reject anyone who can only recite rituals (cargo cult). Show the portfolio (project plan, tracking, earned-value, post-mortem, architecture, project design). **Avoid technical competence questions** — irrelevant and immaterial; only use them if you have surplus good-attitude supply, which you won't.

> [!question]- 47. Why must an architect be an extrovert when most developers are not, and what evidence does Juval cite? Name the three levers an architect can pull to get things done and identify the only one available to them.
>!
> [!summary]- Answer
> Developers are introverts roughly **2 out of 3** — supported by the Bell Labs 1980s study of best developers (affinity to music and languages, lower tolerance for BS but higher ethics, family over work) and by the Myers-Briggs study that seeded a Pascal program with 24 defects and found the top finders typed **INTJ**. The architect, however, is **a salesperson**: selling management who must trust them, selling a design to developers who must follow it without understanding every insight, and selling work to other architects for critique. Introverted delivery — slumped shoulders, mumbling — fails because management "cannot tell design from orange juice" and judges on confidence, body language, and inspiration. The three levers are **authority** ("I'm the boss"), **power** ("do this for me or I won't do that for you"), and **influence** ("do it because it's good — think of the children"). Architects are chronically short of power and authority; the only stick they have is **influence** — so stop yearning for the sticks you don't have.

> [!question]- 48. Describe the "master puppeteer" technique and the two tests that tell you it is safe to disengage from a project.
>!
> [!summary]- Answer
> When taking over a team in bad shape, you pull the strings of every puppet from the shadows so nobody sees you doing it. Privately, to each developer: "I don't care what happened before, it's blood under the bridge, but this cannot continue. I've spoken with everyone else on the team and they are all in favor of working correctly. I like you personally, but this isn't good. I'm going to help you, but you have to do it the way I'm telling you. Your suggestions, of course. On the way out, can you tell Bobby to come in?" Individually everyone sees only personal help; collectively the team experiences a **phase shift — yesterday despair, today delivery.** You can leave when (1) **the project stands on its own feet without you** — "if the project cannot survive without you, you've failed as architect" — and (2) **once you cut the strings off the puppet they keep doing things correctly.** Supporting practices: groom a junior architect as your replacement to fill the vacuum your departure creates, praise in public and criticize in private, and from day one tell the team "I'm going to leave the day you tell me you don't need me anymore" so the onus to improve is theirs.

> [!question]- 49. Juval distinguishes a *test engineer* from a *test monkey*, and gives specific ratios. What separates them, what ratio does he prescribe (and when does it change), and what are the two consequences of the industry-standard 1:10 ratio?
>!
> [!summary]- Answer
> A test engineer is a full-fledged software engineer whose "mission in life is to write code to break your code" — they write adversarial code (e.g. the STEs who replaced ws2_32.dll with a fake TCP stack and a trackball-controlled packet-drop rate). A test monkey just does repetitive, low-added-value work: "press the button, press the button, take a banana." Prescribed ratio: **2 testers : 1 developer**; **2:1 is a must** where you can do damage to people's lives, **1:1 is fine** for low-stakes software, and **no team may fall below 1:1**. Consequences of 1:10: (1) the tester **cannot scale with the team**, so they get relegated to recurring work invariant to team size — i.e. low value; (2) **developers end up doing the real testing**, so the effective testing:development ratio is still 2:1 or 3:1, but it eats feature-writing time. Hence: for an aggressive schedule, **add testers, not developers** — "quality leads to productivity."

> [!question]- 50. State the quality-chain formula and explain the non-linear degradation. Why does Juval say "two bad services do not make one good service," and how does the *For Want of a Nail* poem land the same point?
>!
> [!summary]- Answer
> With *n* subtasks, each contributing one unit of value and quality qᵢ normalized to 0–1: **y = n × q₁ × q₂ × … × qₙ**. The composition is **multiplicative**, so quality degrades **non-linearly**: 10 activities at 1.0 give perfection; at 99% you lose ~10%; a 4% quality drop costs 33% of value and a 9% drop costs 61%. At 0.9 per component, 5 services lose ~40% of value, 10 services ~65%, and 40 services are "completely and utterly dead" — while "five services is not a very complex system." Because failure of any subtask fails the whole, you cannot substitute quantity for quality — two bad services, two faulty O-rings, or two bad developers don't add up to one good one. The 13th-century poem is the same causal chain in narrative form: nail → shoe → horse → rider → message → battle → kingdom. "A medieval peasant knows more about engineering than you do. You're missing all the nails in all the services."

> [!question]- 51. What is the andon cord, why is pulling it "incredibly expensive," and what is Juval's charge against Agile? Who actually gets credit for the underlying idea?
>!
> [!summary]- Answer
> The andon cord runs the whole length of a Toyota JIT assembly line; **any worker, at any moment, upon seeing any defect however minor, may pull it and stop the line.** It's expensive because just-in-time means no inventory — trucks en route must turn around and the ship sails with or without your cars — and because detection at one station implies cars upstream are defective too, forcing a flush plus **full-blown root-cause analysis** (missing hole → broken drill bit → bit rated 2,000 not 6,000 holes → vendor chosen on price over quality), which can stop the line for months. The worker is **rewarded, not punished**: bonus for the first pull, a larger bonus for the second, **promotion to management** on the third. Juval's charge: Agile faithfully imported the Kanban board, the burndown rate and the stand-up, but **deliberately omitted the andon cord** — the single most important artifact — because with one, "nothing will move." The idea is not Japanese in origin: it is **W. Edwards Deming**, who went to Japan in 1947 and founded **Total Quality Management**.

> [!question]- 52. Give Juval's *induction proof* that zero defects at the service level is always achievable, explain why the "zero" is on the tolerance rather than the defects, and name the mechanisms that handle the defects zero tolerance cannot eliminate.
>!
> [!summary]- Answer
> Proof: at the first second of the project, with zero lines of code, you have zero defects. Write line 1; put a button beside it, step over it, examine every variable, and fix any defect immediately — still zero. Assume lines 1..i are defect-free; add line i+1 and do the same. By induction the whole service can be defect-free. "What I describe is not difficult, it's easy. It only gets difficult if you don't do this — if you normalize your deviation." The slogan is not a defect-count claim: **"The zero is not on the defects, the zero is on the tolerance"** — nobody goes home or to lunch until it's fixed, exactly as tolerance for harassment or financial misconduct is exactly zero. Service-level zero does **not** guarantee system-level zero, so other mechanisms carry the rest: **defects in the plumbing → the daily smoke test**; **defects in the requirements → composable design**; and residual escapes are handled by **assertions/defensive programming plus extensive interleaved logging**, which shrink the average bug's lifespan to "a few minutes."

> [!question]- 52. Give Juval's *induction proof* that zero defects at the service level is always achievable, explain why the "zero" is on the tolerance rather than the defects, and name the mechanisms that handle the defects zero tolerance cannot eliminate.
>!
> [!summary]- Answer
> Proof: at the first second of the project, with zero lines of code, you have zero defects. Write line 1; put a button beside it, step over it, examine every variable, and fix any defect immediately — still zero. Assume lines 1..i are defect-free; add line i+1 and do the same. By induction the whole service can be defect-free. "What I describe is not difficult, it's easy. It only gets difficult if you don't do this — if you normalize your deviation." The slogan is not a defect-count claim: **"The zero is not on the defects, the zero is on the tolerance"** — nobody goes home or to lunch until it's fixed, exactly as tolerance for harassment or financial misconduct is exactly zero. Service-level zero does **not** guarantee system-level zero, so other mechanisms carry the rest: **defects in the plumbing → the daily smoke test**; **defects in the requirements → composable design**; and residual escapes are handled by **assertions/defensive programming plus extensive interleaved logging**, which shrink the average bug's lifespan to "a few minutes."

> [!question]- 53. You inherit a 1000-point code base. The team refactors it down to 900 and asks to check it in. What is Juval's ruling, what quantitative bar must be met, and what is the endpoint of that bar?
>!
> [!summary]- Answer
> Reject it. *"There is no material difference between 900 and a thousand — both are hideously complex,"* and checking it in forces him to repeat every test ever run on the code. The bar is a **square-root reduction in complexity**: 900 no, 800 no, 500 "I like where this is going" but still complex, 100 "borderline," **30 — "okay, I'm listening"** (√1000 ≈ 31.6). He also adds: you are **never allowed to make it worse**, and by the time you get 1000 → 30 you probably shouldn't keep refactoring.

> [!question]- 54. Why should you never open the defect tracking system when your mission is to fix a poor-quality code base, and what should you do instead? Name the distributional assumption and the exact ordering rule.
>!
> [!summary]- Answer
> It is *"a pack of lies"*: (1) not all defects are recorded, only the ones known or with time to log; (2) not everything in it is a defect — some are feature requests, some are **symptoms** of the real problem; (3) severity ratings are nonsense — **every defect is a monster-killer defect** that can take down the whole system, so there is no "itsy-bitsy little bug" to deprioritize. Instead assume a **Pareto distribution — ~80% of defects in ~20% of the types** — and that **more complex types carry more than their fair share**. So: measure **all** types, compute **cyclomatic complexity**, and **clean up the single most complex type first**, then the runner-up, repeatedly. *"I bet that will do more for quality than anything else in the system."*

> [!question]- 55. Reconstruct the derivation of the 100 (type) / 10 (method) check-in thresholds. Where does 75 come from, and why does the rule also apply to vendor code?
>!
> [!summary]- Answer
> A well-written method has cyclomatic complexity **1**; allowing an order of magnitude worse gives **10** per method; ten times that gives **100** per type. The empirical anchor is **ServiceModelEx's single most complex type, which measures 75** — a type he calls a fundamental breakthrough requiring inventing something new. *"Where are you gonna get 75 in your code? You're writing simple business code. Are you doing fundamental breakthroughs left and right?"* He **doubled his own worst case** to set the standard. The rule must be enforced as a **gatekeeper rule inside the development tool**, not a memo — and it applies to external vendors: state the maximum complexity in the contract up front, measure the whole thing, and **they don't get paid if it's complex**. He stresses all these numbers are *"mushy… low bars"* whose only job is to make you meet your commitments.

> [!question]- 56. Two boxes dominate the ServiceModelEx complexity treemap. What is in them, and what general lessons about complexity measurement and frameworks do they teach?
>!
> [!summary]- Answer
> They are **not** bad code — they are the two places he went **against the grain of the framework**. One is his restoration of **Code Access Security into WCF and .NET without changing either programming model**, after the WCF team declared it impossible (their partial-trust test matrix would have been **80 factorial** cells; he reduced it to **2200** cells by engineering reductions and tested every one; MSDN's WCF team vetoed the paper and the .NET marketing manager overrode the veto; the next .NET release cancelled CAS entirely, so the code no longer even compiles). The other is the **`Collection` class**, where he augmented LINQ with missing queries (`Distinct`, `Unique`, `Complement`) and used **overloading by type parameter arity** so array-in returns array-out — producing **1200 `yield return` statements** in one file, which makes the analyzer explode even though each augmentation is simple. Lessons: (a) **advanced features designed to reduce complexity raise *measured* complexity disproportionately** — measure with and without them, and include the generated complexity if your developers aren't fluent in them; (b) **compensating for a framework's oversight spikes complexity**; (c) good frameworks show **decreasing complexity bottom-up**, with the public types least complex; (d) a treemap anomaly is archaeology — go find the story.

> [!question]- 57. Finish Juval's sentence: "You can get a very good picture of ______ system, or you can get an inaccurate picture of ______ system, but you can ______ picture of your system."
>!
> [!summary]- Answer
> "You can get a very good picture of **another** system, or you can get an inaccurate picture of **your** system, but you can **never** get an accurate picture of **your** system." It is the Heisenberg uncertainty principle applied at macro scale: observing changes what you observe, and the more intrusive the logging, the more the logged system diverges from the real one.

> [!question]- 58. Why does timestamp-based correlation fail across 10–40 services, and what replaces it? Describe the replacement precisely.
>!
> [!summary]- Answer
> Two reasons: **clock skew** — clocks can never be synchronized to the nanosecond, so events can be logged out of order; and **concurrency** — events happen on multiple threads, and thread IDs are meaningless across process or machine boundaries. The replacement is **activity ID propagation**: the root originator generates a unique ID (a GUID), hides it in the message **headers**, and every service logs it with its local parameters and re-attaches it to its own outgoing calls. You then query all the separate logbooks by activity ID to reconstruct one comprehensive picture.

> [!question]- 59. Compare inline, asynchronous, and queued logging: when does each win, and what breaks if you get it wrong?
>!
> [!summary]- Answer
> **Inline/synchronous** — log in the exact order it happens; required when the problem is **highly temporal** and timeline-sensitive. Its risk: everyone logging synchronously creates **massive load on the logbook** ("bam, it crams it into there"). **Asynchronous** — log sometime later; acceptable when ordering doesn't matter to the investigation. **Queued** — push to a queue and consolidate into a single logbook much later, following the maxim "anything you can do asynchronously, you must do **queued**"; also the answer to the load problem: **distribute the logging, consolidate the viewing**. Which one applies is system-specific — "elaborate and discuss, it's your system."

## Related

- [[MOC — Course Overview]]
- [[Modules/The Architect]]
- [[Modules/Introduction to Service-Orientation]]
- [[Modules/Design and Architecture]]