---
name: h10-export-guide
description: >
  Generates the exact Helium 10 Xray search terms, column checklist, and export
  instructions for the next niche in the research queue. Use this skill whenever
  Dave is about to open H10 and wants to know exactly what to search and export.
  Triggers on phrases like "what do I search in H10", "H10 guide", "what to Xray",
  "what should I export", "next niche", "H10 export", or "what keywords for H10".
---

# Skill: H10 Export Guide

You are generating a precise H10 Xray briefing for Dave's next research session.
The goal is zero ambiguity — Dave opens H10, follows this brief, exports the
right data, and drops it in `raw/`. Done.

---

## Step 1 — Read the Queue

Read these two files:
- `06 Wiki/system/index.md` — check Priority Actions section
- `06 Wiki/wiki/fba/fba-research-overview.md` — check the master rankings table

Identify:
1. Which niches are flagged as next in the queue (status: "Samples needed", "H10 validation needed", "Investigate More")
2. Which niches have already been validated with real H10 data
3. What data gaps exist (missing review counts, missing keywords, etc.)

---

## Step 2 — Generate the Brief

For each niche that needs H10 validation (up to 3), output a clean brief in this
exact format:

---

### 🎯 [Niche Name] — H10 Xray Brief

**Why this one:** [One sentence on what we need to confirm]

**Search these keywords in H10 Xray (one at a time):**
| Priority | Keyword | Why |
|----------|---------|-----|
| 1 | `[exact keyword]` | [what this tells us] |
| 2 | `[exact keyword]` | [what this tells us] |
| 3 | `[exact keyword]` | [what this tells us] |

**Before exporting — make sure these columns are visible in Xray:**
- ✅ Product Title
- ✅ ASIN
- ✅ Brand
- ✅ Price
- ✅ Monthly Revenue
- ✅ Monthly Sales (units)
- ✅ **Reviews** ← most critical — confirm this is showing
- ✅ Rating
- ✅ BSR
- ✅ FBA / FBM
- ✅ Date First Available

**How to add missing columns:** Click the column selector icon (grid/table icon,
top right of Xray panel) → toggle on any missing columns.

**Export instructions:**
1. Click **Export** (top right of Xray) → downloads as CSV
2. Save with this exact filename: `H10-[keyword-slug].csv`
   - e.g. `H10-cable-management-box.csv`
3. Drop in: `raw/sources/`
4. Repeat for each keyword above

**What to do when you drop the files:**

Option A — Instant verdict (no wait):
```bash
python3 "05 Skills/FBA/niche-decision/scripts/h10_quick_stats.py" raw/sources/H10-[keyword].csv
```
Runs in 5 seconds. Shows total revenue, review moat, top 10 table, and quick verdict. Then trigger the niche-decision skill for full scoring.

Option B — Let the overnight agent process it:
The FBA research agent will auto-detect the new CSV on next run, ingest it, and write a full niche wiki page. No action needed — just drop the file and wait for the morning pull.

---

## Step 3 — Flag Any Gaps

If a niche already has some H10 data but is missing specific columns (e.g.
review counts weren't exported), call this out specifically:

> ⚠️ **[Niche] — Partial data only.** We have revenue but not review counts.
> Re-run Xray for `[keyword]` with the Reviews column visible and re-export.

---

## Step 4 — Priority Order

End with a clear priority order:

> **Do this one first:** [Niche] — [one sentence why it's priority]
> **Then:** [Niche 2]
> **Then:** [Niche 3]

Don't tell Dave to do everything at once. One keyword at a time.
