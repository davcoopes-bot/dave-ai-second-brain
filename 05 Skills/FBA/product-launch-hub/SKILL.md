---
name: product-launch-hub
description: >
  Trigger phrases: "set up a launch hub", "product agreed", "we're going with this product",
  "create the launch folder", "build the launch hub", "product is confirmed",
  "launch hub", "set up the product folder", "let's launch this product"
---

# Skill: Product Launch Hub

> **Purpose:** When a product gets the green light, generate the full launch infrastructure in one automated run. One designated folder per product, fully organised, with everything needed from supplier contact to live listing.
>
> **Output:** `03 Projects/FBA Launches/[Product Name]/` containing 7 structured files covering every phase from sourcing to optimisation.
>
> **Rule:** This skill only runs AFTER a product has been validated with real H10 data and agreed by Dave and Josh. Do not run on simulated data alone.

---

## Step 1 — Read Everything First

Before asking Dave anything, read:

1. The relevant niche page — e.g. `06 Wiki/wiki/fba/niche-silicone-splatter-screen.md`
2. `06 Wiki/wiki/concepts/fba-scoring-framework.md` — scoring rubric and thresholds
3. `06 Wiki/wiki/fba/fba-listing-optimisation.md` — listing build rules
4. `06 Wiki/wiki/fba/fba-ranking-factors.md` — A10 ranking signals
5. `06 Wiki/wiki/fba/fba-image-requirements.md` — image compliance rules
6. `06 Wiki/wiki/fba/fba-compliance-suppression.md` — suppression risks
7. `03 Projects/FBA Research/(C) Alibaba Supplier Shortlist — [niche].md` — if it exists

Extract from the niche page:
- Product name and score
- Market snapshot (revenue, reviews, price range)
- The two or three core problems to solve (differentiation brief)
- Product specification non-negotiables
- Keyword strategy
- Competitor landscape
- Target sell price and COGS range

---

## Step 2 — Ask Five Questions

Ask Dave all five in one message:

1. **Product name for the folder** — What do you want to call this product internally? (e.g. "Silicone Splatter Screen" or a code name if preferred)

2. **Launch budget confirmed** — What's the total budget allocated? (Initial order + photography + PPC month 1)

3. **Supplier status** — Has a supplier been selected, or is outreach still in progress? If selected, what's their name?

4. **Target launch date** — Rough timeline: when do you want to be live on Amazon? (Working backwards sets the milestones)

5. **H10 data status** — Has real H10 Xray been run and confirmed for this product? (If not, flag and pause — this hub should only be built on validated data)

---

## Step 3 — Generate the Folder and 7 Files

Create the folder: `03 Projects/FBA Launches/[Product Name]/`

Generate each file below. Use `(C)` prefix on all files.

---

### File 1: `(C) 00 — Overview.md`

The master snapshot. Everything important on one page. Quick links to all other files.

Contents:
- Product name, niche score, data status (simulated vs. validated)
- **Financial Model** — sell price, COGS, FBA fees, PPC %, net margin, break-even units/month
- **Key differentiators** — the 2–3 problems being solved (from niche page)
- **Current phase** — [Sourcing / Pre-Launch / Launch / Optimisation]
- **Budget** — total allocated, spent to date, remaining
- **Quick links** to all 6 other files in the folder

---

### File 2: `(C) 01 — Supplier Tracker.md`

All supplier activity in one place. Never lose a contact or email thread.

Contents:
- **Supplier shortlist table** — populated from the Alibaba shortlist file if it exists:

| # | Supplier | Platform | Contact | MOQ | Unit price | Trade Assurance | OEM | Certs | Sample status | Notes |
|---|---------|----------|---------|-----|-----------|-----------------|-----|-------|--------------|-------|

- **Selected supplier** — [TBD until confirmed]
- **Email log** — chronological record of all outreach:

| Date | Supplier | Type | Summary | Response? |
|------|---------|------|---------|-----------|

- **Sample tracker** — date ordered, cost, arrival date, test results (pass/fail per non-negotiable)
- **Final order details** — MOQ, unit price, total COGS, lead time, shipping terms

---

### File 3: `(C) 02 — Launch Timeline.md`

Phase-by-phase timeline with milestones. Update the status column as each item is completed.

Contents:

**Phase 1 — Sourcing (Target: Weeks 1–4)**

| Milestone | Owner | Target date | Status |
|-----------|-------|------------|--------|
| Supplier outreach sent (3–5 suppliers) | Dave + Josh | | ⬜ |
| Supplier quotes received | Dave | | ⬜ |
| Samples ordered (top 2–3 suppliers) | Dave | | ⬜ |
| Samples arrived and tested | Dave + Josh | | ⬜ |
| Supplier selected | Dave + Josh | | ⬜ |
| Production order placed | Dave | | ⬜ |

**Phase 2 — Pre-Launch Prep (Target: Weeks 4–8)**

| Milestone | Owner | Target date | Status |
|-----------|-------|------------|--------|
| GS1 barcode purchased | Dave | | ⬜ |
| Amazon Seller Central account active | Dave | | ⬜ |
| ASIN created (draft listing) | Dave | | ⬜ |
| Product photography brief sent | Dave | | ⬜ |
| Photography completed and approved | Dave + Josh | | ⬜ |
| Listing copy written (title, 5 bullets, description) | Dave | | ⬜ |
| Backend keywords loaded | Dave | | ⬜ |
| A+ Content designed and uploaded | Josh | | ⬜ |
| PPC campaign built (not yet live) | Dave | | ⬜ |

**Phase 3 — Launch (Target: Weeks 8–12)**

| Milestone | Owner | Target date | Status |
|-----------|-------|------------|--------|
| Inventory shipped to FBA warehouse | Dave | | ⬜ |
| Inventory confirmed received by Amazon | Dave | | ⬜ |
| Listing goes live | Dave | | ⬜ |
| PPC campaigns activated | Dave | | ⬜ |
| First sale | — | | ⬜ |
| First 10 reviews | — | | ⬜ |

**Phase 4 — Optimisation (Month 3–6)**

| Milestone | Owner | Target date | Status |
|-----------|-------|------------|--------|
| PPC ACOS under 30% | Dave | | ⬜ |
| 25+ reviews | — | | ⬜ |
| Ranking on page 1 for launch keyword | — | | ⬜ |
| First profitable month | — | | ⬜ |
| Reorder placed before stockout | Dave | | ⬜ |

---

### File 4: `(C) 03 — Listing Build.md`

Everything needed to build the Amazon listing. Partially populated from niche page research. Backend keywords left for after H10.

Contents:

**Title**
Direction from niche page (lead with the product improvement, not the product type).
> Draft: [pulled from niche page listing brief]
> Hard cap: 200 characters. Mobile truncates at ~80 — the first 80 chars must carry the message.

**5 Bullets**
One bullet per solved complaint. Pulled from the niche page differentiation brief.
> Bullet 1: [Complaint #1 — solve it directly]
> Bullet 2: [Complaint #2 — solve it directly]
> Bullet 3: [Complaint #3]
> Bullet 4: [Complaint #4]
> Bullet 5: [Brand/quality/guarantee angle]

**Backend Keywords**
> ⚠️ POPULATE AFTER H10 — pull the full keyword list from Magnet and Cerebro. Load all relevant terms not already in the title or bullets.

**Image Sequence (7 images + 1 video)**
> Image 1 (Main): Pure white background, product at 85% of frame. No text, no graphics. Amazon compliance required.
> Image 2: Lifestyle — product in use, solving complaint #1 visually
> Image 3: Problem/solution — before and after (old product vs. yours)
> Image 4: Feature callout — close-up of the key differentiator (e.g. silicone handle)
> Image 5: Size/fit — showing compatibility with standard product (e.g. fits 12" pan)
> Image 6: Infographic — key specs and benefits with icons
> Image 7: Social proof or bundle shot (if applicable)
> Video: 30–60 second product demo — show it solving the problem in real use

**A+ Content Brief**
> Module 1: Hero banner — brand story or product mission (1 sentence)
> Module 2: Feature comparison table — your product vs. standard version
> Module 3: Lifestyle imagery — product in context
> Module 4: FAQ — address top 3 pre-purchase questions from competitor reviews

---

### File 5: `(C) 04 — PPC Strategy.md`

⚠️ **FRAMEWORK ONLY — populate fully after H10 keyword data is available.**

Contents:

**Launch Phase Strategy (Days 1–30)**
Goal: buy rank and velocity, not profit. Ignore ACOS for the first 30 days.

| Campaign type | Match type | Keywords | Starting bid | Notes |
|--------------|-----------|---------|-------------|-------|
| Exact match | Exact | [Top 5–10 primary keywords — from H10 Magnet] | 1.5–2× suggested bid | |
| Phrase match | Phrase | [20–30 secondary keywords] | Suggested bid | |
| Auto campaign | Auto | — | $0.75–$1.00 | Harvesting new keywords |

**ACOS Targets by Phase**
| Phase | ACOS target | Why |
|-------|------------|-----|
| Days 1–30 | Ignore — buy velocity | Rank and reviews matter more than profit at launch |
| Days 31–60 | Under 40% | Optimising — cut losers, scale winners |
| Days 61–90 | Under 30% | Building toward sustainable ACOS |
| Month 4+ | 20–25% | Mature campaign — profitable |

**Keyword Targeting Sequence**
> Enter on low-competition sub-keywords first. Build reviews. Then push toward head terms.
> [Sequence from niche page keyword strategy — TBD after H10]

**Budget Allocation**
> ⚠️ Fill in after H10 and budget is confirmed.
> Rule: PPC budget = 17–20% of projected monthly revenue for manageable markets.

---

### File 6: `(C) 05 — Marketing Strategy.md`

⚠️ **FRAMEWORK ONLY — populate fully after H10 keyword data is available.**

Contents:

**Amazon-Native Strategy**
- PPC: see `(C) 04 — PPC Strategy.md`
- Review strategy: Use Amazon's "Request a Review" button on every order (day 4–5 post-delivery). Target 25 reviews in first 60 days to unlock category visibility.
- Ranking: velocity in first 30 days is critical — every sale signals demand to A10. Don't go out of stock in month 1 under any circumstances.
- Listing optimisation: A/B test title variations at 30 days using Manage Experiments (requires Brand Registry).

**External Traffic (Framework — Assess After Launch)**
> ⚠️ Do not invest in external traffic until Amazon-native PPC is profitable and product has 25+ reviews. External traffic before that point burns budget without conversion.
> Options to assess at month 3: TikTok organic, Instagram organic, Meta ads (retargeting), influencer seeding.

**Brand Building (Framework)**
> Brand name: [TBD]
> Brand positioning: [TBD — define before photography brief]
> Visual identity: [TBD — logo, colour palette, packaging brief]

---

### File 7: `(C) 06 — Job Delegation.md`

Dave and Josh task split for the current phase. Update at the start of each new phase.

Contents:

**Current Phase: [Phase name]**

| Task | Owner | Due | Status | Notes |
|------|-------|-----|--------|-------|
| [Task 1] | Dave | | ⬜ | |
| [Task 2] | Josh | | ⬜ | |

> Populate using `05 Skills/FBA/fba-delegation/SKILL.md` at the start of each phase. The delegation skill reads the current state and produces the task split — use it here, don't duplicate manually.

**Sync cadence:**
- Daily sync: use `05 Skills/FBA/fba-daily-sync/SKILL.md` at end of any research or decision session
- Phase gate review: before moving to the next phase, both Dave and Josh confirm all milestones in `02 — Launch Timeline.md` are checked off

**Communication log:**
| Date | Topic | Dave's view | Josh's view | Decision |
|------|-------|------------|------------|---------|

---

## Step 4 — Update the Wiki and Log

After generating all 7 files:

1. Add the product to `06 Wiki/system/index.md` under a new **FBA Launches** section:
   ```
   | [Product Name] | Active launch — [current phase] | `03 Projects/FBA Launches/[Product Name]/` |
   ```

2. Append to `06 Wiki/system/log.md`:
   ```
   ## [DATE] update | Launch hub created — [Product Name]
   - Folder created: 03 Projects/FBA Launches/[Product Name]/
   - Files generated: 7 (Overview, Supplier Tracker, Timeline, Listing Build, PPC Strategy, Marketing Strategy, Job Delegation)
   - Current phase: Sourcing
   - Budget: [confirmed budget]
   - Supplier status: [selected / outreach in progress]
   ```

---

## Step 5 — Close Out

Output a clean summary to Dave:

> **Launch hub created: [Product Name]**
>
> Folder: `03 Projects/FBA Launches/[Product Name]/`
>
> | File | Status |
> |------|--------|
> | 00 — Overview | ✅ Populated |
> | 01 — Supplier Tracker | ✅ Populated from shortlist / ⚠️ Blank — no shortlist found |
> | 02 — Launch Timeline | ✅ Phases and milestones set |
> | 03 — Listing Build | ✅ Title + bullets drafted, keywords pending H10 |
> | 04 — PPC Strategy | ⚠️ Framework only — populate after H10 |
> | 05 — Marketing Strategy | ⚠️ Framework only — populate after H10 |
> | 06 — Job Delegation | ⚠️ Run fba-delegation to populate |
>
> **Next action:** [Clearest single next step — e.g. "Run supplier-outreach skill to send first contact emails" or "Run fba-delegation to split the Phase 1 tasks between Dave and Josh"]

---

## Rules

- **Never run on unvalidated data** — if H10 hasn't confirmed the niche, stop at Step 2 and tell Dave why.
- **One folder per product** — don't merge two products into one hub.
- **Pull from the wiki first** — every piece of research that exists in the niche pages should be pulled into the hub automatically. Don't ask Dave to re-explain what's already filed.
- **Leave frameworks clearly marked** — any section that needs H10 data must be labelled `⚠️ FRAMEWORK ONLY — populate after H10`. Never leave a blank section without explanation.
- **The hub is the single source of truth** — once created, all supplier contacts, email logs, and task tracking happen here. Not in chat, not in separate notes.
