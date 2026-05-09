---
name: wiki-ingest
description: >
  Ingest a new source into the 06 Wiki/ knowledge base. Use this skill whenever Dave drops a file into raw/, pastes content directly, or says "ingest this", "add this to the wiki", "file this", or "save this to the wiki". Follows the full ingest workflow from WIKI-SCHEMA.md: read, discuss, source summary, concept/entity pages, index update, log entry.
---

# Skill: Wiki Ingest

Ingest a new source into Dave's persistent wiki. One disciplined ingest = compounding knowledge. Sloppy ingest = noise.

Follow the WIKI-SCHEMA.md workflow exactly. Do not skip steps.

---

## Before Starting

Read these three files to get context:
1. `06 Wiki/system/WIKI-SCHEMA.md` — the ingest rules and conventions
2. `06 Wiki/system/index.md` — existing pages (so you know what already exists and what needs updating vs. creating)
3. The source file itself

---

## Step 1 — Read the Source

Read the full source file. If Dave pasted content directly into the conversation, treat that as the source.

Identify:
- What domain does this touch? (FBA / finance / trading / personal / research / concepts)
- What existing wiki pages are relevant?
- What's new vs. what reinforces existing knowledge?
- Are there any contradictions with existing wiki content?

---

## Step 2 — Discuss Key Takeaways

Surface 3–5 key takeaways from the source. Ask Dave:
- "What angle matters most to you from this?"
- "Is there anything in here you want filed differently or skipped?"

Don't start writing pages until this is clear.

---

## Step 3 — Create the Source Summary Page

**File location:** `06 Wiki/wiki/sources/`
**Filename:** `src — [Title].md`

Template:
```markdown
# src — [Source Title]

> **Category:** sources
> **Last updated:** YYYY-MM-DD
> **Source type:** [Article / FBA research / Video / Book / Conversation / Official doc / Other]
> **Source URL (if applicable):** [URL or "N/A"]

## Summary
[1–2 paragraph overview of what this source is and why it matters]

## Key Takeaways
- Takeaway one
- Takeaway two
- Takeaway three

## Concepts Introduced or Reinforced
- [[concept-page]] — [one line on how this source relates]

## Contradictions with Existing Wiki
- [None / List any contradictions found]

## Open Questions
- [Questions this source raises but doesn't answer]

## Related Wiki Pages
- [[related-page]]
```

---

## Step 4 — Update or Create Concept / Entity Pages

For each major concept, framework, or niche the source touches:

**If the page already exists:** read it, then add new information. Note the change in the Revision History section at the bottom.

**If the page doesn't exist yet:** create it using the standard page template from WIKI-SCHEMA.md. File it under the correct `06 Wiki/wiki/[category]/` subfolder.

**⚠️ Always write to `06 Wiki/wiki/[category]/` — never to the root `wiki/` folder.**

---

## Step 5 — Update index.md

Add all new pages to `06 Wiki/system/index.md`:
- Under the correct category section
- One-line summary and link for each new page
- Update the total page count at the top

If updating an existing page significantly, update its summary line too.

---

## Step 6 — Append to log.md

Append to `06 Wiki/system/log.md`:

```
## [YYYY-MM-DD] ingest | [Source Title]

- Raw source: [file path or "pasted directly"]
- Source URL: [URL or "N/A"]
- Summary page created: wiki/sources/src — [Title].md
- Pages created: [list or "none"]
- Pages updated: [list or "none"]
- Contradictions: [list or "none"]
- Open questions: [list or "none"]
```

---

## Step 7 — Close the Session

Tell Dave:
1. What was created / updated
2. Any contradictions or open questions to resolve
3. Recommended next ingest or follow-up action

---

## Common Mistakes to Avoid

- Writing to root `wiki/` instead of `06 Wiki/wiki/` — always check the path
- Skipping the log entry — every ingest must be logged
- Creating a new concept page when one already exists — check index.md first
- Updating index.md total page count incorrectly — count before and after
