# src — LLM Wiki Pattern

> **Category:** sources
> **Last updated:** 2026-05-03
> **Raw file:** [[2026-05-03 — LLM Wiki Pattern]]
> **Source type:** Idea file / article

---

## Summary

An idea file describing a pattern for building personal knowledge bases using LLMs. The core insight: instead of re-deriving knowledge from raw documents at query time (RAG), the LLM incrementally builds and maintains a persistent, interlinked wiki. Knowledge compounds with every source and every question — the synthesis is already done, not re-done on every query.

---

## Key Takeaways

- **RAG vs Wiki:** RAG retrieves from raw docs at query time — no accumulation. The wiki compiles knowledge once and keeps it current, so cross-references and synthesis are always pre-built.
- **Three-layer architecture:** raw sources (immutable), the wiki (LLM-maintained markdown), and the schema (operating rules document).
- **Operations:** Ingest (add source → update wiki), Query (search index → synthesise answer → optionally file result), Lint (health-check for orphans, stale claims, gaps).
- **Indexing without RAG infrastructure:** At moderate scale (~100 sources), an `index.md` file is sufficient — LLM reads it first, then drills into relevant pages. No vector embeddings needed.
- **Maintenance is the key insight:** Humans abandon wikis because the bookkeeping burden grows faster than the value. LLMs do the maintenance cheaply and reliably — they don't get bored or forget cross-references.
- **Queries can file back as pages:** Good answers to questions become new wiki pages, so exploration compounds in the knowledge base just like ingested sources do.
- **Historical parallel:** Vannevar Bush's Memex (1945) — the LLM solves the maintenance problem Bush couldn't.

---

## Concepts Introduced

- [[wiki/concepts/llm-wiki-pattern.md]] — The pattern itself
- RAG (Retrieval-Augmented Generation) — contrasted with the wiki approach
- Memex — historical inspiration

---

## Contradictions With Existing Wiki

None (first ingest).

---

## Open Questions

- At what scale does `index.md` break down and require a proper search engine like qmd?
- Which Obsidian plugins are most valuable to install first? (Dataview and Marp mentioned)
- How granular should wiki pages be — one page per concept or grouped by topic?
- What's Dave's first domain to deeply populate: FBA, finance, or trading strategy?

---

## Related Pages

- [[wiki/concepts/llm-wiki-pattern.md]]

---

## Revision History

- 2026-05-03: Created. Source: LLM Wiki Pattern idea file (pasted by Dave).
