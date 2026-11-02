# Juval Lowy's Architect's Master Class — Study Notes

This Obsidian vault tracks study notes for **Juval Lowy's Architect's Master Class**, a comprehensive course on software architecture covering process, technology, service-orientation, and the IDesign method.

## Vault Structure

```
├── Vault Index.md              ← Master navigation
├── MOC — Course Overview.md    ← Course map + progress tracker
├── Modules/                    ← One folder per course module
│   ├── The Architect.md
│   ├── Microservices Development Process.md
│   ├── Introduction to Service-Orientation.md
│   ├── Service Contract Design and Factoring.md
│   ├── Design and Architecture.md
│   ├── Design Aspects.md
│   ├── Design Aspects/             ← subfolder for sub-notes
│   ├── Agile and Design.md
│   ├── Groupthink.md
│   ├── Architect in Age of AI.md
│   ├── Project Planning.md
│   └── What Comes Next.md
├── 00-Inbox/                   ← Quick capture, sort later
├── 01-Templates/               ← Note templates with frontmatter
└── 99-Resources/               ← Attachments, images, tag reference
    └── Transcripts/             ← Lecture transcripts with key excerpts
```

## Agent Skills

The `skills/` folder publishes three [skills.sh](https://skills.sh) agent skills distilled from the course. Each one has a stdlib-only Python script, so the numbers come from code instead of mental arithmetic:

| Skill | What it does |
|---|---|
| [`idesign-method`](skills/idesign-method/SKILL.md) | System design: volatility-based decomposition, the Clients/Managers/Engines/ResourceAccess/Utilities taxonomy, and closed-architecture rules. Validates an architecture JSON and draws Mermaid call chains |
| [`service-contract-design`](skills/service-contract-design/SKILL.md) | Contract design and factoring. Measures operations per contract, property-like operations, arguments per operation, contracts per service, and CRUD verbs on ResourceAccess, from JSON or C#/Java/TypeScript source |
| [`project-design`](skills/project-design/SKILL.md) | Project design: critical path, float, float-based staffing, cost curve, planned earned value (shallow S), Obsidian canvas of the network, and weekly tracking with symptom diagnosis |

### Installing the skills

**Requirements**
- [Node.js](https://nodejs.org) 22.20 or later, which runs the `npx skills` installer
- Python 3.8 or later, which runs the skills' scripts. They use only the standard library, so you don't need `pip install`
- A coding agent that supports skills, such as Claude Code, Codex, Cursor or OpenCode. See the [supported agents](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)

**1. See what's available**

```bash
npx skills add samon11/architect-masterclass --list
```

**2. Install**

Run the command from the project where you want to use the skills. By default, skills are installed into that project.

```bash
# Interactive: pick skills and agents from a menu
npx skills add samon11/architect-masterclass

# Every skill, for Claude Code
npx skills add samon11/architect-masterclass --skill '*' -a claude-code

# Just one or two skills
npx skills add samon11/architect-masterclass --skill project-design
npx skills add samon11/architect-masterclass --skill idesign-method --skill service-contract-design

# Install globally (every project), without prompts
npx skills add samon11/architect-masterclass --skill '*' -g -a claude-code -y
```

| Option | Effect |
|---|---|
| `-s, --skill <name>` | Install only the named skill(s). `'*'` means all of them |
| `-a, --agent <agent>` | Target specific agents (`claude-code`, `codex`, `cursor`, ...). `'*'` means all detected agents |
| `-g, --global` | Install to your user directory instead of the current project |
| `--copy` | Copy files instead of symlinking them into the agent's directory |
| `-y, --yes` | Skip confirmation prompts |

**3. Use them**

Your agent loads a skill automatically when your request matches it. Try:
- *"Design the architecture for a clinic scheduling system using the IDesign Method."*
- *"Review the contracts in `src/Contracts` against Juval's contract metrics."*
- *"Here's my architecture. How long will it take, what will it cost, and what does the earned-value curve look like with 4 developers?"*

In Claude Code you can also call a skill directly, for example `/project-design`.

**Manage installed skills**

```bash
npx skills list                     # show installed skills
npx skills check                    # check for updates
npx skills update                   # pull the latest versions
npx skills remove project-design    # uninstall a skill
```

**Without the installer**

Each skill is a self-contained folder. To install one by hand, copy `skills/<name>/` into your agent's skills directory, e.g. `.claude/skills/<name>/` in a project or `~/.claude/skills/<name>/` for Claude Code globally.

**Run the scripts directly**

You can run the calculators without an agent. Each skill ships with an example:

```bash
python3 skills/idesign-method/scripts/validate_architecture.py skills/idesign-method/examples/architecture.json --out out/architecture
python3 skills/service-contract-design/scripts/contract_metrics.py --source path/to/src --out out/contracts
python3 skills/project-design/scripts/plan_project.py plan skills/project-design/examples/network.json --out out/plan
python3 skills/project-design/scripts/plan_project.py track skills/project-design/examples/network.json skills/project-design/examples/status.json --out out/tracking
```

## Key Links

- [Juval Lowy / IDesign](https://www.idesign.net)
- [Righting Software (book)](https://www.idesign.net/Books)
- [Deep NETernals podcast](https://www.idesign.net/Programming/p/Deep_NETernals.html)

## Study Workflow

> [!tip] How to study
> 1. Start with [[MOC — Course Overview]] to see your progress
> 2. Work through modules in order
> 3. Use callouts and wikilinks to connect concepts
> 4. Take the quiz at the end of each module note to test retention

## Building This Vault

This vault was built using the [Pi coding agent](https://github.com/earendil-works/pi) with the [Obsidian plugin](https://obsidian.md/plugins).

## License

All content is for personal study purposes. Course material is © Juval Lowy / IDesign.
