---
name: fba-product-research
description: >
  Full FBA product research workflow for Amazon sellers. Use this skill whenever
  Dave (or anyone) wants to find Amazon FBA product opportunities, research niches,
  validate product ideas, or get a go/no-go decision on a product. Triggers on
  phrases like "find FBA products", "research a niche", "product research",
  "validate this product idea", "is this a good FBA product", "find me something
  to sell on Amazon", or anything about Amazon selling opportunities. Run this
  skill proactively any time product research is mentioned — don't just answer
  conversationally, run the full workflow.
---

# FBA Product Research Skill

You are running a systematic FBA product research session. Your job is to help
find, validate, and score Amazon product opportunities so Dave and Josh can make
fast, data-backed decisions on what to sell.

This skill runs as a guided workflow. You drive the process — Dave provides
context and any real data he has, you do the analysis and thinking.

**Data mode:** By default, simulate realistic Helium 10 data so the full
analysis can run immediately without interruption. Always label simulated data
clearly. If Dave pastes in real Helium 10 data at any point, switch to using
that instead — real data takes priority and should be noted as such in the
final report.

---

## The Core Framework

Good FBA products share a profile: simple physical goods, $20–70 price point,
lightweight, not dominated by major brands, with enough search demand to be
worth entering but not so saturated that new entrants get crushed. The goal is
to find niches where the top sellers are leaving money on the table — poor
listings, weak branding, unaddressed complaints in reviews.

The workflow has six phases. Move through them in order.

---

## Phase 1: Niche Ideation

Always run this phase. If Dave has given a specific product, run the pre-filter
on it and note whether it passes — then move on. If he hasn't given a product,
generate ideas from scratch using the angles below.

**Angles to explore (for open-ended sessions):**
1. **Everyday annoyances** — things people complain about around the house, in
   the kitchen, travelling, working from home. Problems that have a simple
   physical solution.
2. **Hobby/passion niches** — people spend freely on things they love. Think
   fishing, hiking, gaming, gym, cooking, gardening, pets.
3. **Life stage triggers** — new parents, new homeowners, university students,
   new gym-goers all have sudden buying needs.
4. **Upgrade markets** — products where the standard version is cheap and
   unsatisfying, and there's appetite for a better one.
5. **Underserved audiences** — a product that exists for one demographic but
   isn't marketed to another (e.g., left-handers, plus size, seniors).

For each angle, generate 3–4 specific product ideas. Then apply the quick
pre-filter and cut down to the 3–5 strongest candidates.

**Quick pre-filter (cut anything that fails more than one):**
- Price can credibly land between $20–70 ✓/✗
- Not electronics, fragile, or liquid ✓/✗
- Not a category dominated by Nike, Rubbermaid, Hasbro-type brands ✓/✗
- Under ~2 lbs (keeps FBA fees manageable) ✓/✗
- Not a legal/safety minefield (medical devices, kids toys with strict regs) ✓/✗

---

## Phase 2: Helium 10 Research Parameters

For each shortlisted product, state the exact Helium 10 parameters Dave would
use if running this for real. Then simulate realistic data using these
parameters as the basis.

### Step A — Black Box (Product Database Search)

```
Category:        [most relevant category for the product]
Monthly Revenue: Min $5,000
Review Count:    Max 300
Price:           Min $18, Max $75
Star Rating:     Max 4.3
```

Simulate a table of 10 realistic results (product name, price, monthly revenue,
reviews, star rating, BSR). Label clearly as **SIMULATED DATA**.

### Step B — Magnet (Keyword Research)

```
Search term:          [main product keyword]
Search Volume:        Min 3,000
Competing Products:   Max 500
```

Simulate the top 8–10 keywords by search volume with monthly search volumes and
competing product counts. Note whether the trend looks stable/growing/declining.

### Step C — Xray (Competitor Deep Dive)

Simulate an Xray table for the top 10 results on page 1: product name, monthly
revenue, review count, star rating, price, BSR. This is the data that feeds
directly into Phase 3 analysis.

---

## Phase 3: Market Analysis

Interpret the data — don't just restate numbers. Cover all five of these:

**Revenue distribution:**
Is monthly revenue spread across multiple sellers, or does one or two products
take almost everything? Concentrated = harder to break in. Distributed = room
for a new entrant.

**Review ceiling:**
Average review count for the top 10. Under 150 is very good. Over 400 is a
red flag that you'll need heavy review-building investment before you're
visible.

**Price consistency:**
Are most products priced similarly? Consistency = stable market. Wide variance
can mean immature niche (opportunity) or race to the bottom (avoid).

**Review quality gap:**
What are the common complaints in reviews? If the top products sit at 4.1–4.3
stars with consistent themes (sizing, material, missing features), that's your
differentiation brief. If everything is 4.7+ with glowing reviews, hard to
compete.

**Keyword demand reality check:**
Does search volume align with revenue? High volume + low revenue = poor
conversion or weak buying intent. High volume + healthy revenue = what you want.

**Competitive density:**
Three things to assess here — together they tell you how hard it actually is
to get a foothold:

1. **Total competing ASINs** (from Magnet "Competing Products" count on the
   main keyword). Under 200 = relatively open. 200–500 = competitive but
   manageable. 500+ = crowded, need a long-tail entry strategy.

2. **Brand concentration on page 1** — are the top 10 Xray listings spread
   across 8–10 different sellers, or are 3–4 listings from the same brand/
   seller account? If one seller holds multiple top spots, they're likely
   running a brand dominance strategy and will be hard to displace. Distributed
   sellers = healthier entry conditions.

3. **New seller viability** — look at the BSR range and monthly revenue of
   positions 6–10 in the Xray results. If the tail-end listings (positions
   7–10) are still doing $5k+/month with under 200 reviews, that's a green
   signal — new entrants can get traction without needing to be #1 on page 1.
   If only positions 1–3 make real money, the niche has a winner-takes-most
   dynamic and is much harder to crack.

**Seasonal flag:**
Is this product likely to have seasonal demand spikes? Flag clearly:
- 🟢 Year-round: consistent demand, lower risk
- 🟡 Mildly seasonal: small peak (e.g. back-to-school, summer), manageable
- 🔴 Highly seasonal: Christmas gifts, pool toys, etc. — cash flow risk, only
  proceed if you understand the seasonality and can plan inventory accordingly

---

## Phase 4: Alibaba Cost Estimate

Before scoring on business viability, do a quick sourcing sanity check.
Estimate the likely Alibaba landed cost based on the product type:

**Rough COGS benchmarks (landed, inclusive of shipping to FBA warehouse):**
- Simple soft goods (straps, bands, wraps): $2–5
- Small hard goods under 0.5 lb (clips, hooks, organisers): $3–7
- Medium hard goods 0.5–1.5 lb (kitchen tools, accessories): $5–12
- Larger/complex items 1.5–3 lb (bags, frames, multi-part kits): $10–20

State the estimated landed COGS range for this product and use the midpoint
for margin calculations.

**Margin formula:**
```
Net Margin % = (Selling Price - COGS - FBA Fees - PPC) / Selling Price

FBA fees (standard size):
  Under 1 lb:    ~$3.50–5.00
  1–2 lb:        ~$5.00–7.50
  2–3 lb:        ~$7.50–9.50

PPC estimate (early months):  15–20% of revenue
```

Show the working. Be honest about margin — don't fudge it to make a borderline
product look viable.

---

## Phase 5: Competitor Listing Audit

Look at what the top 3 competitors are likely doing wrong in their Amazon
listings. This is where differentiation turns from a product angle into a
launch strategy. Assess:

**Title & keywords:**
Are titles keyword-stuffed and unreadable, or well-written and benefit-led?
A clean, conversion-focused title is a competitive advantage.

**Main image:**
Is the hero image on a white background only, or does it show the product in
use? Lifestyle images in the main slot drive significantly higher CTR.

**Bullet points:**
Do they lead with features or benefits? Do they address the known review
complaints? Weak bullets = opportunity to out-convert on the same traffic.

**Review complaint themes:**
Summarise the 2–3 most common complaints across the top sellers. These become
your product brief and your listing's implicit promise — "we fixed what
everyone hates."

**Brand presence:**
Do the top sellers look like real brands (logo, A+ content, branded storefront)
or generic Chinese private labels? Weak brand presence = easier to displace
with even basic branding.

Rate the overall listing quality as: **Strong** / **Average** / **Weak**

---

## Phase 6: Scoring — Go / No-Go Decision

Score each product out of 100. Be honest — don't round up to make a mediocre
product look better than it is.

### ⚠️ Single Source of Truth — Read the Wiki Framework First

Before scoring, read the full rubric from the wiki:

**`06 Wiki/wiki/concepts/fba-scoring-framework.md`**

That page is the single source of truth for the scoring system. It contains the full 5-category rubric, all point breakpoints, the pre-filter gate, the Helium 10 research sequence, and the verdict thresholds. Do not use any other version of the rubric — if this skill and the wiki ever disagree, the wiki wins and this skill is outdated.

### Score Interpretation (quick reference — full rubric is in the wiki)

| Score | Call | What it means |
|-------|------|---------------|
| 75–100 | ✅ Green light | Strong opportunity. Move to sourcing. |
| 55–74 | 🟡 Investigate more | Promising but has a meaningful risk. Identify the weak point. |
| 35–54 | 🔶 Caution | Real problems. Only continue if there's a specific angle that fixes the weakness. |
| Under 35 | ❌ Pass | Numbers don't stack up. Move on. |

---

## Phase 7: Research Report + Save to File

After scoring, produce the research report AND save it as a file.

**Save location:** `/Users/dave/Desktop/Dave's AI Brain/03 Projects/FBA Research/`
**Filename format:** `(C) [Product Name] Research — [YYYY-MM-DD].md`

Create the FBA Research directory if it doesn't exist.

Report format (use exactly):

---

## FBA Research Report — [Product Name]

**Date:** [today's date]
**Researched by:** Claude + Dave
**Data:** Simulated / Real (note which)

### Product Overview
[2–3 sentences: what the product is, target customer, why it exists]

### Market Snapshot
| Metric | Value |
|--------|-------|
| Main keyword search volume | |
| Total competing ASINs (main keyword) | |
| Avg monthly revenue (top 10) | |
| Avg review count (top 10) | |
| Price range (top 10) | |
| Brand concentration (page 1) | Distributed / Moderate / Concentrated |
| Tail-end viability (pos 7–10 revenue) | |
| Seasonal profile | 🟢 Year-round / 🟡 Mild / 🔴 Seasonal |
| Est. landed COGS (Alibaba) | |
| Est. FBA fees | |
| Est. net margin | |
| Competitor listing quality | Strong / Average / Weak |

### Scores
| Category | Score | /Max | Notes |
|----------|-------|------|-------|
| Revenue Potential | | /25 | |
| Competition Gap | | /25 | |
| Search Demand | | /20 | |
| Differentiation | | /15 | |
| Business Viability | | /15 | |
| **TOTAL** | | /100 | |

### Verdict
**[Green Light / Investigate More / Caution / Pass]**

[2–4 sentences: the real reason for this verdict. What's strong, what's the
risk, what would need to be true for this to work.]

### The Opportunity
[What makes this product beatable. Review complaints. The differentiation play.
Listing weaknesses you can exploit.]

### Next Steps
1. [Specific action]
2. [Specific action]
3. [Specific action]

---

If multiple products were researched, add a **Final Rankings** section after
all individual reports:

## Final Rankings

| Rank | Product | Score | Verdict | Why |
|------|---------|-------|---------|-----|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

**Recommendation:** [1–2 sentences on which to pursue first and why]

---

## Quick Reference: FBA Sweet Spot

- Price: $25–65
- Weight: under 1.5 lbs
- Monthly revenue (top 10 avg): $8k–25k
- Review count (top 10 avg): under 200
- Main keyword volume: 8k–50k/month
- No brand dominance
- Clear quality/branding gap vs existing sellers
- Margin after all costs: 35%+
- Competitor listings: Average or Weak
- Seasonal profile: Year-round or Mild preferred
