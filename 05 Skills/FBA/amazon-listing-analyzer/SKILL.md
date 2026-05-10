---
name: amazon-listing-analyzer
description: Analyzes Amazon product listings for a given niche to identify competitor patterns, successful listing formulas, differentiation opportunities, and pricing strategies. Works with H10 Xray CSV exports and product ASINs. Use when Dave asks "how are competitors listed", "what keywords do top sellers use", "analyze competitor listings", "listing analysis for [niche]", "how should we differentiate our listing", or "what's working on Amazon for [product]".
---

# Amazon Listing Analyzer

To analyze how top competitors in a niche present their products on Amazon — extracting keywords, positioning angles, differentiation patterns, and listing quality signals. This is a pre-launch intelligence step that runs after a niche gets a GREEN LIGHT or INVESTIGATE MORE verdict and before finalizing product design or listing copy.

---

## When to Use

- After a niche passes the H10 scoring threshold (60+/100) and needs deeper competitive intelligence
- When deciding how to differentiate the product before ordering samples
- When drafting a listing and need to know what keywords and angles top sellers use
- When comparing 5–10 ASINs to find gaps in the market

---

## Input Required

Either (a) an H10 Xray CSV export for the niche (already in `raw/sources/`), or (b) a list of ASINs, or (c) a direct ask like "analyze cable management box competitors".

---

## Step 1 — Load H10 Data

If an H10 CSV exists in `raw/sources/` for this niche:
- Load all rows
- Sort by Monthly Revenue descending
- Take the top 10 by revenue as the "competitor set"
- For each: note ASIN, Price, Revenue, Reviews, Brand, Date First Available

If no H10 data, ask Dave to run an H10 Xray first and drop the CSV in `raw/sources/`.

---

## Step 2 — Deep Listing Analysis

For the top 5–10 competitors, use the Playwright script at `scripts/scrape_listing.py` to pull live listing data from each ASIN's Amazon page.

```bash
python3 "05 Skills/FBA/amazon-listing-analyzer/scripts/scrape_listing.py" --asins B0XXXXXX B0YYYYYY --output /tmp/listing-analysis.json
```

If scraping is blocked (Amazon bot detection), fall back to manual analysis:
- Open each ASIN at `https://www.amazon.com.au/dp/[ASIN]`
- Paste the listing HTML/text and analyse manually

For each listing, extract:

| Field | What to note |
|-------|-------------|
| **Title** | Keywords in first 80 chars, key differentiators called out |
| **Bullet points** | What problems/benefits they lead with, order of priority |
| **Price positioning** | Where they sit in the range — premium, mid, budget |
| **Images** | How many, lifestyle vs white background, infographics used |
| **Review count + rating** | Age of reviews, rating distribution |
| **A+ content** | Yes/No — brand story, comparison table, rich media |
| **Q&A** | What questions buyers ask — signals unmet needs |
| **Listing age** | Date First Available — how established is this seller |

---

## Step 3 — Pattern Extraction

After reading all listings, identify:

### Keyword Patterns
- What words appear in EVERY top 10 title → must-have keywords
- What words appear in 5+ titles → strong signals
- What words only appear in 1–2 titles → differentiation opportunities

### Positioning Angles
What problem or benefit does each competitor lead with?
- Functional: "holds 200 cables", "fits under desk"
- Aesthetic: "minimalist design", "cable-free look"
- Convenience: "easy setup", "no tools required"
- Quality: "heavy duty", "durable ABS plastic"

Which angle is underserved? That's the gap.

### Price Clustering
Where does the market cluster?
- Budget tier (< $X)
- Mid tier ($X–$Y)
- Premium tier (> $Y)

Where is the revenue concentrated? Where are the reviews concentrated?

### Listing Quality Distribution
- How many have A+ content (brand registered)?
- How many have 7+ images?
- How many have a comparison table?
- Is there a quality gap (top sellers have great content, lower sellers are weak)?

---

## Step 4 — Differentiation Map

Output a table showing where each competitor plays and where the gaps are:

| Angle | Covered by | Strength |
|-------|------------|---------|
| [Angle 1] | [Brand A, Brand B] | Strong — well served |
| [Angle 2] | [Brand C] | Weak — only one player |
| [Angle 3] | Nobody | Gap — unserved |

Recommend 1–2 positioning angles to target based on:
1. Underserved in current listings
2. Supported by Q&A (buyers are asking about this)
3. Differentiable in the product design/sourcing

---

## Step 5 — Listing Blueprint

Based on the analysis, output a draft listing framework:

```
TITLE FORMULA:
[Main keyword] + [Key differentiator] + [Secondary keyword] + [Size/quantity if relevant]

BULLET 1 (lead with the gap/angle):
[Problem → Solution → Outcome]

BULLET 2:
[Second strongest benefit]

BULLET 3:
[Quality/material/durability signal]

BULLET 4:
[Compatibility/size/specs — practical]

BULLET 5:
[Trust/guarantee/brand story]

MUST-HAVE KEYWORDS (title + bullets):
[list]

RECOMMENDED PRICE POINT:
$[X] — [reason: sits above budget cluster, below premium, room for PPC margin]

IMAGE STRATEGY:
1. Hero: white background, product prominent
2. Lifestyle: [scenario that hits the gap angle]
3. Infographic: [key specs/dimensions]
4. Comparison: us vs competitors
5-7. Detail shots + in-use
```

---

## Step 6 — Update Wiki

Add a `## Listing Intelligence` section to the niche wiki page (`06 Wiki/wiki/fba/niche-[slug].md`):

- Date of analysis
- Competitor set analysed (ASINs)
- Key patterns found
- Recommended positioning angle
- Draft listing framework

Append to `06 Wiki/system/log.md`:
```
- YYYY-MM-DD: Listing analysis complete for [niche]. Recommended angle: [X]. Blueprint saved.
```

---

## Rules

- Never recommend an angle that every top seller already uses well — that's a commodity war
- If Q&A reveals a strong unmet need, weight that heavily — it's real buyer signal
- The listing blueprint is a starting point, not a final copy — always test
- If Amazon blocks scraping, use the manual fallback — don't skip the analysis
- Check `.com.au` (Australian marketplace) AND `.com` (US) — top sellers may differ
