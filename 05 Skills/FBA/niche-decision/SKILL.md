---
name: niche-decision
description: >
  Takes real H10 Xray data and produces an instant go/no-go verdict using the
  FBA scoring framework. Use this skill whenever Dave has dropped H10 CSV files
  into raw/ and wants a decision, or says "make a call", "go or no-go",
  "is this worth it", "H10 data is in", "score this", "validate this niche",
  or "should I pursue this". Always reads real data from raw/ — never simulates.
---

# Skill: Niche Decision

You are making a go/no-go call on a niche using real Helium 10 data.
This is a decision skill, not a research skill. The data is already in —
your job is to interpret it fast and give Dave a clear verdict.

Be blunt. A bad product that looks good on paper is worse than a pass.

---

## Step 1 — Read Context

Read these files first:
- `06 Wiki/wiki/concepts/fba-scoring-framework.md` — the scoring rubric (single source of truth)
- `06 Wiki/wiki/fba/fba-research-overview.md` — current niche standings
- The niche page if it exists: `06 Wiki/wiki/fba/niche-[slug].md`

---

## Step 2 — Load the H10 Data

Scan `raw/` and `raw/sources/` for CSV files starting with "H10" that relate
to this niche.

For each CSV:
- Parse all columns: Product, ASIN, Organic Rank, Price, Revenue, Reviews,
  Rating, FBA/FBM, BSR, Date First Available
- Calculate:
  - **Total page revenue** (sum of all Revenue values)
  - **Top 10 average revenue** (avg of top 10 by revenue)
  - **Top 10 average review count** (avg of top 10 by revenue)
  - **Price range** (min–max of top 10)
  - **Revenue distribution** (what % does #1 hold? Is it spread or concentrated?)
  - **FBA penetration** (what % of top 10 are FBA?)
  - **Review moat assessment** (see benchmarks below)

**Review moat benchmarks:**
- < 200 avg (top 10): ✅ Easy entry
- 200–500 avg: 🟡 Manageable — 6–9 months of review building
- 500–1,000 avg: 🔶 Hard — long-tail strategy required
- 1,000+ avg: ❌ Closed

**Flag any missing data explicitly** — if Reviews column is empty, say so and
note it affects the Competition Gap score.

---

## Step 3 — Score the Niche

Apply the full rubric from `06 Wiki/wiki/concepts/fba-scoring-framework.md`.
Score each category honestly:

| Category | Score | /Max | Key data points used | Confidence |
|----------|-------|------|---------------------|------------|
| Revenue Potential | | /25 | | High/Medium/Low |
| Competition Gap | | /25 | | High/Medium/Low |
| Search Demand | | /20 | | High/Medium/Low |
| Differentiation | | /15 | | High/Medium/Low |
| Business Viability | | /15 | | High/Medium/Low |
| **TOTAL** | | /100 | | |

**Confidence column:** If a score relies on estimated or missing data, mark it
Low confidence. A Low confidence score in Competition Gap (missing reviews)
means the verdict should be conditional.

---

## Step 4 — The Verdict

State the verdict clearly at the top:

### ✅ GREEN LIGHT / 🟡 INVESTIGATE MORE / 🔶 CAUTION / ❌ PASS

**Score: [X]/100**

**The single most important finding:**
[One sentence. The number or fact that drives the verdict more than anything else.]

**What's working:**
- [Bullet]
- [Bullet]

**What's not working / risks:**
- [Bullet]
- [Bullet]

**The verdict in plain English:**
[2–4 sentences. No jargon. What does this actually mean for Dave and Josh?
Should they order samples? Move on? What would change this verdict?]

---

## Step 5 — Conditional Verdicts

If data gaps exist (missing reviews, missing sales units), issue a conditional
verdict:

> **Conditional verdict:** 🟡 Investigate More — pending review count data.
> If avg reviews on top 10 come back under 200, this upgrades to Green Light.
> If 400+, this is a Pass. Re-run Xray with Reviews column visible.

Never issue a Green Light on incomplete data.

---

## Step 6 — Update the Wiki

After the verdict:

1. Update `06 Wiki/wiki/fba/niche-[slug].md`:
   - Update frontmatter score and verdict
   - Update Market Snapshot table with real numbers
   - Update Competitor Landscape with real product data
   - Update Revision History
   - Change data status from SIMULATED to REAL H10

2. Update `06 Wiki/wiki/fba/fba-research-overview.md`:
   - Update the niche row with new score, verdict, and status

3. Update `06 Wiki/system/index.md`:
   - Update the niche summary line

4. Append to `06 Wiki/system/log.md`

---

## Step 7 — Next Action

End with one clear next action:

> **Next:** [Specific action — e.g. "Order 3 samples from Alibaba for cable
> management box — search 'cable organizer box with lid' and filter for
> suppliers with 3+ years and Trade Assurance"]

One action. Not a list of five things. What is the single highest-leverage move
right now?
