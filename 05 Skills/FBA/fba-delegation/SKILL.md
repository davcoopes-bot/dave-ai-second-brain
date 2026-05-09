---
name: fba-delegation
description: >
  Trigger phrases: "plan our fba work", "what should we do today", "split the work",
  "delegation", "what's next for fba", "divide the tasks", "who does what",
  "fba task split", "coordinate with josh"
---

# Skill: FBA Delegation

> **Purpose:** Figure out where FBA is at right now, then split the work between Dave and Josh with zero overlap. Route to the right existing skill for execution.
>
> **What this skill does NOT do:** Run research itself. Handle the daily sync (that's `fba-daily-sync`). Write wiki pages (that's `wiki-ingest`). Score the session. Suggest system improvements. Those skills exist — this one routes to them.

---

## Step 1 — Read Current State

Before asking Dave anything, read these files:

1. `06 Wiki/system/index.md` — find the current FBA priority actions queue
2. `06 Wiki/wiki/fba/fba-research-overview.md` — current niche shortlist and stage context
3. `02 Chess Moves (Long-Term Planning)/(C) Chess Moves — Dave 2026.md` — settled decisions and next actions

Do not ask Dave to explain context that's already in the vault. Use what's there.

---

## Step 2 — Detect Current FBA Stage

Based on what you just read, determine which stage the FBA operation is in:

| Stage | Definition | Key indicator |
|-------|-----------|---------------|
| **Research** | Identifying and scoring niches | No niche finalised; H10 not yet run |
| **Validation** | Running real H10 data on shortlisted niche | H10 purchased; Xray exports being pulled |
| **Sourcing** | Finding suppliers, getting quotes, ordering samples | Niche locked; Alibaba outreach in progress |
| **Listing** | Building the Amazon listing | Samples approved; listing content being written |
| **Launch** | Product live; PPC campaign running | ASIN created; first orders expected |
| **Optimisation** | Reviewing PPC, reviews, ranking | Live with sales data; improving metrics |
| **Scaling** | Expanding SKUs, inventory, or niches | First product profitable; second product pipeline |

State the detected stage clearly. If it's ambiguous (between two stages), say so and explain why.

---

## Step 3 — Confirm With Dave (One Question Only)

Ask one question to confirm or correct the stage detection, and surface anything urgent:

> "Based on the vault, we're in **[Stage]** — [one-sentence justification]. Is that right, or has something changed since last session? Anything urgent that's moved?"

Wait for the answer before proceeding.

---

## Step 4 — Split the Work

Generate the task split for this stage. Format exactly as below:

---

### Current Stage: [Stage Name]

**Dave's priority task:**
> [Single most important task Dave should do next — one action, specific and concrete]

**Why Dave:** [One sentence — why this lands with Dave, not Josh]

---

**Josh's priority task:**
> [Single most important task Josh should do next — one action, specific and concrete]

**Why Josh:** [One sentence — why this lands with Josh, not Dave]

---

**⚠️ No-overlap check:**
- Dave doing: [task summary]
- Josh doing: [task summary]
- These are parallel / sequential? [state which]
- Risk of duplication: [None / Low / Flag — explain if flagged]

---

**Sync point:** [When should Dave and Josh compare outputs before proceeding? e.g. "Before ordering samples — Dave shares supplier shortlist with Josh first."]

---

## Step 5 — Route to the Right Skill

Tell Dave which existing skill to run next (do not re-execute that skill here):

| If the stage task involves... | Route to... |
|-------------------------------|-------------|
| Niche scoring or research analysis | `05 Skills/FBA/fba-product-research/SKILL.md` |
| Keyword research (H10 data) | `05 Skills/FBA/fba-keyword-research/SKILL.md` |
| Product review analysis | `05 Skills/review-analysis/SKILL.md` |
| End-of-day sync with Josh | `05 Skills/FBA/fba-daily-sync/SKILL.md` |
| Adding new research to the wiki | `05 Skills/wiki-ingest/SKILL.md` |
| Strategic decision (budget, niche commitment) | `05 Skills/chess-moves/SKILL.md` |

State: **"Next skill to run: [skill name] — [one sentence on why]"**

If no skill covers the next task (e.g. placing a supplier order, creating an Amazon account), flag it as a manual action.

---

## Completion Checklist

Before finishing the session, confirm:

- [ ] Stage detected and confirmed by Dave
- [ ] Dave has one clear, specific next action
- [ ] Josh has one clear, specific next action  
- [ ] No overlap between their tasks
- [ ] Sync point defined
- [ ] Correct skill identified for execution

Do not end the session without all five boxes checked.

---

## Reference — FBA Scoring Framework

The full scoring rubric lives at `06 Wiki/wiki/concepts/fba-scoring-framework.md`. Do not reproduce it here — read it from the wiki when needed.

Current niche shortlist summary (from index):
- Silicone splatter screen — 93/100 ✅ Green Light
- Cable management — 88/100 ✅ Green Light
- Padded lifting straps — 85/100 🟡 Investigate More

---

## Notes

- Dave and Josh are equal partners. Tasks should respect each person's strengths if known, otherwise split by availability and logical sequencing.
- The fba-daily-sync skill handles the end-of-day Claude-to-Claude knowledge transfer between Dave and Josh's sessions. Run it at the end of any research-heavy session.
- All FBA data is currently simulated. Do not recommend ordering samples or committing capital until real H10 Xray data has been validated.
