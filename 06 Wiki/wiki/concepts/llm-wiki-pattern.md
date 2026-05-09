# LLM Wiki Pattern

> **Category:** concepts
> **Last updated:** 2026-05-03
> **Sources:** [[wiki/sources/src — LLM Wiki Pattern.md]]

---

## Summary

A pattern for building a personal knowledge base where an LLM incrementally maintains a persistent, interlinked wiki — rather than re-deriving knowledge from raw documents on every query (RAG). The key property: knowledge compounds. The more sources you add and the more questions you ask, the richer and more interconnected the wiki becomes, without requiring manual maintenance.

---

## The Core Distinction

| Standard RAG | LLM Wiki |
|---|---|
| Retrieves from raw docs at query time | Maintains a synthesised wiki continuously |
| Re-derives knowledge on every query | Synthesis is pre-built and current |
| Cross-references found at query time | Cross-references already exist in the wiki |
| No accumulation | Knowledge compounds |
| Scales with retrieval quality | Scales with maintenance discipline |

---

## Architecture

**Layer 1 — Raw Sources (immutable)**
Your curated collection of source documents. Articles, papers, PDFs, clipped web pages, images. The LLM reads from these but never modifies them. Source of truth.

**Layer 2 — The Wiki (LLM-maintained)**
A directory of markdown files. Summaries, entity pages, concept pages, comparisons, an overview. The LLM owns this entirely — creates pages, updates them on new ingests, maintains cross-references, flags contradictions.

**Layer 3 — The Schema**
A document (CLAUDE.md, AGENTS.md, or WIKI-SCHEMA.md) that tells the LLM how the wiki is structured, what conventions to follow, and what workflows to use. The LLM becomes a disciplined wiki maintainer, not a generic chatbot.

---

## Core Operations

**Ingest**
Drop a source → LLM reads it → discusses key takeaways → writes source summary page → updates concept/entity pages → updates index → logs the ingest. One source might touch 10–15 pages.

**Query**
Ask a question → LLM reads index → reads relevant pages → synthesises answer with citations. Good answers get filed back as new wiki pages.

**Lint**
Periodic health-check: orphan pages, missing cross-references, stale claims, concepts that need their own page, suggested new sources to fill data gaps.

---

## Indexing Approach

Two special files:
- **index.md** — Content-oriented catalog. Every page listed with a one-line summary and link. LLM reads this first on every query to find relevant pages. Sufficient for ~hundreds of pages without vector embeddings.
- **log.md** — Chronological append-only record. Every ingest, query, lint pass logged with consistent prefix format for grep-ability.

---

## Why It Works

The tedious part of a knowledge base is not the reading or thinking — it's the bookkeeping: updating cross-references, keeping summaries current, noting contradictions, maintaining consistency across dozens of pages. Humans abandon wikis because maintenance burden grows faster than value. LLMs do this cheaply, reliably, and at scale.

---

## Optional Tooling

- **Obsidian Web Clipper** — Browser extension, converts articles to markdown for raw/sources/
- **qmd** — Local markdown search engine (BM25/vector hybrid + LLM reranking). Useful when wiki exceeds ~100 pages and index.md becomes slow.
- **Marp** — Markdown-based slide deck format. Generate presentations directly from wiki content.
- **Dataview** — Obsidian plugin for querying YAML frontmatter across pages. Useful for dynamic tables.

---

## Historical Inspiration

Vannevar Bush's **Memex** (1945) — a proposed personal, curated knowledge store with associative trails between documents. The part Bush couldn't solve was maintenance. The LLM handles that.

---

## Application to Dave's Brain

This wiki is built on this pattern. `06 Wiki/` is the implementation:
- `raw/sources/` = immutable source layer
- `wiki/` = LLM-maintained knowledge layer
- `system/WIKI-SCHEMA.md` = the schema / constitution
- `system/index.md` = navigation map
- `system/log.md` = activity timeline

---

## Related Pages

- [[wiki/sources/src — LLM Wiki Pattern.md]]

---

## Open Questions

- At what page count does index.md alone become insufficient? Estimate: 200–300 pages.
- Is qmd worth installing now or only when the wiki grows?

---

## Revision History

- 2026-05-03: Created. Source: LLM Wiki Pattern idea file (pasted by Dave).
