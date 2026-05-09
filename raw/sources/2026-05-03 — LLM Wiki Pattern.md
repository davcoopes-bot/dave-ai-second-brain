# LLM Wiki Pattern
> **Source type:** Idea file / article
> **Date saved:** 2026-05-03
> **Author:** Unknown (shared by Dave)
> **Status:** Ingested 2026-05-03

---

> [Original content pasted by Dave — stored here as immutable source record]

The core idea: instead of RAG (retrieve at query time), the LLM incrementally builds and maintains a persistent wiki — a structured, interlinked collection of markdown files. When a new source is added, the LLM reads it, extracts key information, and integrates it into the existing wiki: updating entity pages, revising topic summaries, noting contradictions. Knowledge compounds with every source and every question.

**Architecture:** Three layers — raw sources (immutable), the wiki (LLM-maintained), and the schema (operating rules in CLAUDE.md or AGENTS.md).

**Operations:** Ingest, Query, Lint.

**Indexing:** index.md (content-oriented catalog) + log.md (chronological append-only record).

**Optional tooling:** qmd (local markdown search engine, BM25/vector hybrid), Obsidian Web Clipper, Marp (slide decks from markdown), Dataview (YAML frontmatter queries).

**Why it works:** The tedious part of a knowledge base is bookkeeping. Humans abandon wikis because maintenance cost grows faster than value. LLMs don't get bored, don't forget cross-references, can touch 15 files in one pass. The wiki stays maintained because maintenance cost is near zero.

**Inspiration:** Vannevar Bush's Memex (1945) — private, actively curated, associative trails between documents. The part Bush couldn't solve was who does the maintenance. The LLM handles that.
