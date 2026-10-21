# AGENTS.md

> Rules and instructions for AI agents working with this Obsidian vault.

## Purpose

This vault tracks study notes for **Juval Lowy's Architect's Master Class**, a comprehensive course on software architecture covering process, technology, service-orientation, and the IDesign method.

## Available Skills

| Skill | Description | When to Use |
|-------|-------------|-------------|
| `obsidian-markdown` | Create and edit Obsidian Flavored Markdown with wikilinks, callouts, properties, and embeds | Writing or editing any `.md` note in the vault |
| `obsidian-bases` | Create and edit Obsidian Bases (`.base` files) with views, filters, and formulas | Building database-like views or trackers for notes |
| `obsidian-cli` | Interact with Obsidian vaults via CLI (read, create, search, manage notes) | Programmatic vault operations, plugin dev |
| `json-canvas` | Create and edit JSON Canvas files (`.canvas`) with nodes, edges, and groups | Building visual canvases or mind maps |
| `defuddle` | Extract clean markdown from web pages | Reading external articles or documentation |

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
│   ├── Design Aspects/Fractal Architecture.md
│   ├── Agile and Design.md
│   ├── Groupthink.md
│   ├── Architect in Age of AI.md
│   └── What Comes Next.md
├── 00-Inbox/                   ← Quick capture, sort later
├── 01-Templates/               ← Note templates with frontmatter
└── 99-Resources/               ← Attachments, images, tag reference
    ├── Transcripts/             ← Lecture transcripts with key excerpts
    ├── Media/                   ← Raw lecture recordings (.webm), gitignored
    └── ...
```

## Conventions

- **Frontmatter** is required on every note (title, date, module, type, tags)
- **Wikilinks** (`[[Note Name]]`) for internal vault connections
- **Callouts** (`> [!type]`) for highlighted information blocks
- **Topic checkboxes** (`- [ ]`) on module pages to track progress
- **Tags**: `#course/notes`, `#module-N`, `#concept`, `#juval-lowy`, `#ai`, etc.
- **Raw recordings** live in `99-Resources/Media/`, which is gitignored. Never commit audio or video.

## Creating New Notes

1. Choose the right template from `01-Templates/`
2. Fill in frontmatter (title, date, module, type, tags)
3. Write content using Obsidian Flavored Markdown
4. Link related notes with `[[wikilinks]]`
5. Place notes in the appropriate folder:
   - **Module notes** → `Modules/<Module Name>/` (use the `.md` file for the main note)
   - **Transcripts** → `99-Resources/Transcripts/` (raw lecture transcripts with key excerpts)
   - **Concept notes** → `00-Inbox/` (quick capture, sort later)
   - **Sub-notes** → `Modules/<Module Name>/` (related notes that belong to a module)
   - **Raw recordings** → `99-Resources/Media/` (gitignored archive; see [Using `macparakeet-cli`](#using-macparakeet-cli))

## After Importing a Transcript

> [!note] Generating the raw transcript
> To produce the transcript text from a lecture recording (`.webm`, `.mp3`, `.m4a`, `.mp4`, …), use [`macparakeet-cli`](#using-macparakeet-cli) below, then paste or import the result into `99-Resources/Transcripts/<Lecture Name>.md`.

When a transcript and its key takeaways have been imported, follow this post-import workflow:

1. **Update the corresponding module note** — Extract the key insights, definitions, and takeaways from the transcript and append or integrate them into the relevant `Modules/<Module Name>.md` note using `obsidian-markdown`. Link related concepts with wikilinks.
2. **Add a quiz** — Append a quiz section (`## Quiz`) to the corresponding module note with 5–10 questions covering the key material from the transcript. Use a mix of question types (e.g., fill-in-the-blank, short answer, scenario-based). Format questions as collapsible callouts so the user can attempt answers before revealing them, e.g.:
   ```
   > [!question]- 1. What is service orientation?
   >!
   > [!summary]- Answer
   > Service orientation is...
   ```
3. **Quiz the user** — After updating the note and adding the quiz, actively quiz the user by presenting the questions one at a time (or a small batch). Wait for their answers before revealing them.
4. **Challenge them to teach** — After quizzing, challenge the user to explain the material back to you in their own words, as if teaching it. Pretend to be a student sitting in on their lecture — ask deeper follow-up questions, play devil's advocate, and probe edge cases. Identify any gaps in their understanding and keep pushing until they can articulate the concept thoroughly. This active recall and teach-back solidifies retention.

## Working with Skills

### Using `obsidian-markdown`

For all note creation and editing. Ensures proper frontmatter, wikilinks, callouts, and embeds.

### Using `obsidian-bases`

To create `.base` files for views like:
- Course progress tracker (filtered by module, status)
- Concept index (grouped by module, sorted by date)
- Study timeline (daily notes with word estimates)

### Using `obsidian-cli`

For programmatic operations:
```bash
obsidian read file="Modules/The Architect"
obsidian search query="volatility" limit=20
obsidian append file="Modules/Design and Architecture" content="## Notes\n\n### The IDesign Method\n- New content here"
```

### Using `json-canvas`

To create visual maps of:
- Course module relationships
- Fractal architecture diagrams
- Design principle hierarchies

### Using `macparakeet-cli`

Local speech-to-text on Apple Silicon (Parakeet TDT). Use this to turn lecture recordings into transcript text.

> [!important] Archive the recording first
> Before transcribing, copy the source recording into `99-Resources/Media/` (gitignored) so the vault owns the original even if `~/Downloads/` is cleared:
> ```bash
> cp -n ~/Downloads/quality_assurance.webm "99-Resources/Media/"
> ```
> Then transcribe from the archived copy. Never commit files under `99-Resources/Media/`.

For a single recording, the transcript goes to **stdout** and progress to **stderr**, so redirection works:
```bash
macparakeet-cli transcribe "99-Resources/Media/composable design.webm" \
  -f transcript --mode clean --speaker-detection off \
  > "99-Resources/Transcripts/composable design.txt"
```

To have the CLI write the file itself (named after the input), use `--output-dir`:
```bash
macparakeet-cli transcribe "99-Resources/Media/quality_assurance.webm" \
  -f transcript --mode clean --speaker-detection off \
  --output-dir "99-Resources/Transcripts"
```

Batch a whole folder in one pass:
```bash
macparakeet-cli transcribe "99-Resources/Media"/*.webm -f transcript --output-dir "99-Resources/Transcripts"
```

Key options:

| Flag | Notes |
|------|-------|
| `-f transcript` | **Prose only** — use this for notes. Default `-f text` adds a `File:`/`Duration:`/`Speakers:` header block plus a word-timestamp dump |
| `--mode clean` | Strips filler words. Default `raw` keeps everything |
| `--speaker-detection off` | Drops `Speaker 1:` labels; leave on for multi-speaker panels |
| `--engine <name>` | `parakeet` (default, local), `nemotron`, `whisper`, `cohere` |
| `--language <code>` | Language hint for `whisper`/`nemotron`/`cohere` (ignored by Parakeet) |
| `--no-history` | Skip saving the result to the MacParakeet history database |

Re-export an already-transcribed recording without re-running STT:
```bash
macparakeet-cli history transcriptions          # list records + IDs
macparakeet-cli export <id> -f txt -o lecture.txt
macparakeet-cli export <id> -f markdown -o lecture.md
```

- Video containers (`.webm`, `.mp4`) need no conversion — the CLI extracts the audio track
- Move or rename the resulting `.txt` into `99-Resources/Transcripts/` if it was written elsewhere

### Using `defuddle`

To extract content from external sources:
```bash
defuddle parse <url> --md
```

## Important Links

- [Juval Lowy / IDesign](https://www.idesign.net)
- [Righting Software (book)](https://www.idesign.net/Books)
- [Deep NETernals podcast](https://www.idesign.net/Programming/p/Deep_NETernals.html)
- [Obsidian Help](https://help.obsidian.md)