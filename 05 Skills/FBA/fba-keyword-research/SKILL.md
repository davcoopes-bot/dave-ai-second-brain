---
name: fba-keyword-research
description: >
  Run structured keyword research for any Amazon FBA product. Use this skill when Dave says
  "keyword research", "pull keywords for [product]", "what are people searching for for [product]",
  "H10 keyword research", "keyword deep dive", "what should I be ranking for", or when preparing
  to write or optimise an Amazon listing. Also use before evaluating whether a niche has accessible
  traffic. Produces a keyword master list with volume estimates, competition tier, and PPC priority
  ranking — ready for listing optimisation and campaign setup.
---

# Skill: FBA Keyword Research

Run a structured keyword research session for any Amazon FBA product. Produces a keyword master list with search volume estimates, competition tier, and PPC priority ranking — ready to use for listing optimisation and campaign setup.

---

## Phase 1: Clarify the Product

Before running research, confirm:
1. **Exact product** — e.g. "silicone splatter screen with hot handle"
2. **Target market** — AU, US, or both? (Default: US Amazon unless Dave specifies)
3. **Price point** — matters for CPC and margin assumptions

If unclear, ask one clarifying question. Don't ask three.

---

## Phase 2: Keyword Discovery

### Seed Keywords
Start with 3–5 seed keywords Dave provides or you infer from the product. Example for splatter screen:
- "splatter screen"
- "grease splatter guard"
- "silicone splatter screen"
- "frying pan cover"
- "splatter guard for frying"

### Expansion — Run via WebSearch
For each seed, search:
- `"[seed keyword]" amazon bestseller`
- `amazon "[seed keyword]" reviews`
- `"[seed keyword]" site:amazon.com`

Capture:
- **Related search terms** shown in autocomplete and "customers also searched"
- **Product titles** of the top 5–10 listings (titles reveal keyword priorities)
- **Review language** — exact words buyers use in 1-star and 5-star reviews

### Long-tail Generation
From the seed and expansion research, generate:
- 3–5 **high-volume head terms** (broad, competitive, expensive CPC)
- 5–10 **mid-tail keywords** (2–3 words, moderate competition)
- 10–20 **long-tail keywords** (3–5 words, lower volume, lower CPC, easier to rank)

---

## Phase 3: Competition & Volume Assessment

For the top 20–30 keywords identified, estimate:

| Signal | How to Assess |
|--------|--------------|
| Search volume tier | High (10k+/mo) / Medium (1k–10k) / Low (<1k) — use listing count as proxy |
| Competition | Count how many sponsored listings appear; note avg review count of top 10 |
| CPC estimate | Check if any PPC data surfaces in search; use category benchmarks if not |
| Buyability | Does the SERP show products clearly matching the keyword? (intent match) |

### Competition Tier Definitions
- **Tier 1 (Red):** Top 10 avg reviews >500. Avoid as primary keyword — use as secondary.
- **Tier 2 (Yellow):** Top 10 avg reviews 100–500. Winnable with good launch velocity.
- **Tier 3 (Green):** Top 10 avg reviews <100. Priority targets — early rank opportunity.

---

## Phase 4: Output — Keyword Master List

```
## Keyword Master List — [Product Name]
**Date:** [date]
**Market:** [US/AU]

### Tier 3 — Priority Targets (Green)
| Keyword | Volume Est. | Avg Reviews (Top 10) | CPC Est. | Notes |
|---------|------------|---------------------|----------|-------|

### Tier 2 — Secondary Targets (Yellow)
| Keyword | Volume Est. | Avg Reviews (Top 10) | CPC Est. | Notes |
|---------|------------|---------------------|----------|-------|

### Tier 1 — Brand Terms (Long-term Only)
| Keyword | Volume Est. | Avg Reviews (Top 10) | CPC Est. | Notes |
|---------|------------|---------------------|----------|-------|

### Recommended PPC Campaign Structure
- Auto campaign: [budget/day]
- Exact match (Tier 3 keywords): [list top 5]
- Broad match (Tier 2 keywords): [list top 5]
- Negative keywords: [list any obvious negatives]

### Listing Title Recommendation
[Draft title using primary keywords in correct order — most important first]

### Top 5 Backend Keywords
[Search terms not in title/bullets that should go in backend fields]
```

---

## Phase 5: Wiki Integration (Optional)

If Dave has a niche page for this product in `06 Wiki/wiki/fba/`, append the keyword findings:

1. Read the existing niche page
2. Add a `## Keyword Research ([date])` section with the master list
3. Update `06 Wiki/system/index.md` summary line to reflect that keyword data is now present
4. Append to `06 Wiki/system/log.md`:
   ```
   ## [date] update | Keyword Research — [product]
   - Niche page updated: wiki/fba/[niche-page].md
   - Keywords found: [X] total, [Y] Tier 3 targets
   ```

---

## Rules

- **Never hallucinate search volumes** — if you don't have real data, say "estimated" and explain the reasoning
- **Be specific** — give actual keyword strings, not categories
- **Flag the review ceiling** — if a keyword's top 10 avg reviews exceed 500, call it out clearly as a red flag
- **End with a clear next action** — what should Dave do first with these keywords?
