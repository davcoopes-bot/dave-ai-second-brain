# WIKI-SCHEMA.md — LLM Wiki Constitution
> This is the operating manual for the LLM Wiki layer inside Dave's AI Brain.
> It runs *alongside* the existing second brain — it never overwrites, deletes, or renames anything outside `06 Wiki/`.

---

## 1. What This Wiki Is

A persistent, compounding knowledge base maintained entirely by Claude. You source and direct. Claude does the filing, cross-referencing, and bookkeeping.

Every time a new source is ingested, Claude doesn't just file it — it integrates it: updating concept pages, flagging contradictions, strengthening the synthesis. Knowledge compounds instead of sitting in a pile.

**The three files that matter most:**
- `system/index.md` — Navigation map. Read this first on every session.
- `system/log.md` — Append-only timeline. Every action gets logged here.
- `system/WIKI-SCHEMA.md` — This file. The constitution. Read it when uncertain.

---

## 2. Folder Layout

```
Dave's AI Brain/          ← Vault root
├── raw/                  ← SOURCE INBOX (vault root level — this is where raw files go)
│   └── sources/          ← Dated source files dropped here before ingest. IMMUTABLE.
└── 06 Wiki/              ← Wiki system
    ├── wiki/
    │   ├── business/     ← Income streams, strategy, business models, plans
    │   ├── fba/          ← FBA niches, product research, suppliers, competitors
    │   ├── finance/      ← Stock trading, budgeting, investing, net worth tracking
    │   ├── fitness/      ← Training, health, performance, recovery
    │   ├── cars/         ← Car knowledge, purchases, maintenance
    │   ├── personal/     ← Self-improvement, psychology, identity, relationships
    │   ├── research/     ← Deep research topics that span multiple categories
    │   ├── people/       ← Key people: Josh, mentors, authors, competitors
    │   ├── concepts/     ← Mental models, frameworks, principles, vocabulary
    │   └── sources/      ← One summary page per ingested source
    └── system/
        ├── WIKI-SCHEMA.md  ← This file
        ├── index.md        ← Content map
        └── log.md          ← Append-only timeline
```

**Hard rules on folders:**
- Raw source files live in the **vault root `raw/`** folder — NOT inside `06 Wiki/`. This is the established pattern for this vault.
- `raw/` is read-only for Claude. Never edit, rename, or delete raw source files once placed.
- Wiki pages live under `06 Wiki/wiki/[category]/` — never in the root `wiki/` folder or any other location.
- Everything outside `06 Wiki/` (except reading `raw/`) is Dave's domain. Claude does not touch it without explicit approval.
- When adding a new category, propose it first, then create after confirmation.

**⚠️ Common mistake to avoid:** There is a root-level `wiki/` folder that is NOT the wiki. The real wiki is at `06 Wiki/wiki/`. Always write new wiki pages to `06 Wiki/wiki/[category]/`, never to the root `wiki/` folder.

---

## 3. Naming Conventions

| Item | Convention | Example |
|---|---|---|
| Source files (raw) | `YYYY-MM-DD — Title.md` | `2026-05-03 — LLM Wiki Pattern.md` |
| Wiki pages | `kebab-case.md` | `llm-wiki-pattern.md` |
| Source summary pages | `src — Title.md` | `src — LLM Wiki Pattern.md` |
| Claude-created files | `(C)` prefix | `(C) fba-niche-comparison.md` |
| Log entries | `## [YYYY-MM-DD] action | Title` | `## [2026-05-03] ingest | LLM Wiki Pattern` |

---

## 4. Ingest Workflow

When Dave drops a source into `raw/` or `raw/sources/` (vault root level) and says "ingest this":

**Step 1 — Read.** Claude reads the source fully.

**Step 2 — Discuss.** Claude surfaces 3–5 key takeaways and asks Dave what angle matters most.

**Step 3 — Source summary.** Create `wiki/sources/src — [Title].md` with:
- One-paragraph summary
- Key takeaways (3–7 bullets)
- Concepts introduced or reinforced
- Contradictions with existing wiki pages (if any)
- Open questions raised
- Links to related wiki pages

**Step 4 — Update concept/entity pages.** For each major concept or entity mentioned, update or create its wiki page. Add the source as a citation.

**Step 5 — Update index.md.** Add new pages with one-line summaries and links.

**Step 6 — Log it.** Append to `system/log.md`:
```
## [YYYY-MM-DD] ingest | [Source Title]
- Summary page: wiki/sources/src — [Title].md
- Pages created: [list]
- Pages updated: [list]
- Contradictions: [list or "none"]
- Open questions: [list or "none"]
```

---

## 5. Query Workflow

When Dave asks a question:

1. Read `system/index.md` to identify relevant pages.
2. Read those pages in full.
3. Synthesise an answer with citations (`[[page-name]]` links).
4. If the answer is substantial and reusable, offer to file it as a new wiki page.
5. Log the query:
```
## [YYYY-MM-DD] query | [Question summary]
- Pages consulted: [list]
- Answer filed: [page path or "no"]
```

---

## 6. Update Workflow

When new information changes something already in the wiki:

1. Read the existing page.
2. Make the minimum edit that incorporates the new information.
3. Note the change at the bottom of the page in a `## Revision History` section:
```
- [YYYY-MM-DD] Updated [section] based on [source].
```
4. Log it:
```
## [YYYY-MM-DD] update | [Page name]
- What changed: [brief description]
- Source: [source title or "conversation"]
```

---

## 7. Contradiction Handling

When a new source contradicts an existing wiki claim:

1. Do not silently overwrite. Surface the contradiction to Dave.
2. Present both positions clearly.
3. Ask Dave which to trust, or whether both should coexist with a note.
4. Update the page with a `> ⚠️ Contradiction noted:` callout block.
5. Log the contradiction.

---

## 8. Lint Workflow

When Dave says "lint the wiki" or periodically on request:

Check for:
- Pages mentioned in other pages but not in `index.md` (orphans)
- Concepts mentioned in multiple pages that should have their own page
- Stale claims that newer sources may have superseded
- Missing cross-references between related pages
- Data gaps worth investigating (suggest new sources to find)

Report findings as a list. Don't auto-fix without confirmation.

Log:
```
## [YYYY-MM-DD] lint | Health check
- Orphans: [list]
- Missing pages: [list]
- Stale claims: [list]
- Suggested sources: [list]
```

---

## 9. Inviolable Rules

1. **Never touch anything outside `06 Wiki/`** without Dave's explicit approval.
2. **Never edit raw source files.** They are the ground truth.
3. **Never delete wiki pages.** Archive them to `wiki/archive/` if needed.
4. **Always log every action** in `system/log.md`.
5. **Always update `system/index.md`** after creating or significantly updating a page.
6. **Ask before restructuring.** Small edits: proceed. New categories or renamed folders: propose first.
7. **Call out contradictions** — do not silently reconcile them.
8. **End every session with a clear next action** — what should Dave do or ingest next?

---

## 10. Page Template

```markdown
# [Page Title]

> **Category:** [business / fba / finance / fitness / cars / personal / research / people / concepts / sources]
> **Last updated:** YYYY-MM-DD
> **Sources:** [[src — Title]], [[src — Title2]]

## Summary
[2–4 sentence overview]

## Key Points
- Point one
- Point two

## Related Pages
- [[related-page-1]]
- [[related-page-2]]

## Open Questions
- Question one

## Revision History
- [YYYY-MM-DD] Created. Source: [title]
```

---

*This schema is a living document. Propose changes to Dave; update after approval.*
