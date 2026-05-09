---
name: aios-audit
description: >
  Score Dave's AI vault system against the Four C's framework to surface gaps and prioritise
  improvements. Use this skill when Dave says "audit the vault", "how good is my AI setup",
  "what's missing from my system", "run the four C's audit", "what should I improve in the vault",
  or at the start of a monthly review. Produces a score out of 100 and a ranked list of gaps to fix.
---

# Skill: AIOS Audit (Four C's)

Objectively score the vault system across all four pillars — Context, Connections, Capabilities, Cadence — and find the highest-leverage gap to fix next.

---

## Before Starting

Read these files to understand the current state of the vault:
1. `CLAUDE.md` — current context and project status
2. `06 Wiki/system/index.md` — what's been built in the wiki
3. `05 Skills/` folder listing — what skills exist

---

## Pillar 1 — Context (0–25 pts)

Claude's knowledge of Dave's world.

| Question | Points |
|----------|--------|
| Does Claude know who Dave is, what he's building, and why? | 0–8 |
| Does Claude know current priorities, active projects, and goals? | 0–8 |
| Does Claude know Dave's communication style, decision-making patterns, and known blind spots? | 0–9 |

**Deduct 3 pts** for each major active project with no context in `CLAUDE.md` or the wiki.

---

## Pillar 2 — Connections (0–25 pts)

Claude's ability to reach relevant data and tools.

The 7 tier-1 domains for Dave's setup:
1. FBA research tools (Helium 10, supplier data)
2. Stock/trading data
3. Financial tracking (bank statements, budget)
4. Calendar/scheduling
5. Communication (notes, journals)
6. Web research (WebSearch, WebFetch)
7. Vault file system (read/write to all folders)

| Score | Condition |
|-------|-----------|
| 25 pts | All 7 connected and tested |
| Pro-rated | (connected domains / 7) × 25 |
| Deduct 3 pts | Per connected domain that's untested or broken |

---

## Pillar 3 — Capabilities (0–25 pts)

Reusable skills that exist and work.

| Question | Points |
|----------|--------|
| 5+ working skills exist in `05 Skills/` | 0–15 |
| Skills can run multi-step workflows without Dave re-explaining context | 0–5 |
| Skills get updated when they produce wrong output (not just used once and forgotten) | 0–5 |

---

## Pillar 4 — Cadence (0–25 pts)

Things running on a schedule without manual triggering.

| Question | Points |
|----------|--------|
| Any tasks running automatically without Dave having to initiate? | 0–15 |
| Automated triggers exist (e.g. scheduled reviews, recurring syncs)? | 0–10 |

---

## Score Interpretation

| Score | Status | Priority |
|-------|--------|----------|
| 75–100 | Strong system | Add cadence and advanced skills |
| 50–74 | Working but gaps | Add connections + fill skill gaps |
| 25–49 | Early stage | Fix context first, then one connection |
| 0–24 | Just starting | Rebuild CLAUDE.md context before anything else |

---

## Output Format

Give Dave:

1. **Score** — X/100 with breakdown by pillar
2. **Top 3 gaps** — ranked by leverage (what fixing it would unlock)
3. **Recommended next action** — one specific thing to do this week to improve the score
4. **What's working well** — don't just focus on gaps; name what's solid

---

## Log It

Append to `06 Wiki/system/log.md`:

```
## [YYYY-MM-DD] | AIOS Audit
- Score: [X]/100
- Context: [X]/25 | Connections: [X]/25 | Capabilities: [X]/25 | Cadence: [X]/25
- Top gap: [name it]
- Next action: [what Dave is doing about it]
```

---

## Rules

- Be honest about the score — don't round up to make it look better
- Gaps in Cadence are expected at this stage; don't penalise too harshly for what's genuinely hard to set up
- The recommended next action must be specific and doable in one session — not "improve connections" but "add WebSearch testing to the wiki-ingest skill"
