---
name: vault-weekly-digest
description: Generates a plain English weekly digest of everything the autonomous agents and Claude have done in the vault over the past 7 days. Reads git history and the wiki activity log to surface what ran, what was found, and what changed. Use when Dave asks "what happened this week", "what did the agents do", "weekly digest", "catch me up", "weekly summary", "what's the agent been doing", or "what came in while I was away".
---

# Vault Weekly Digest

To generate a plain English summary of the past week's autonomous activity — what the agents ran, what they found, and what changed. Designed for Dave to open on a Monday morning or after time away and immediately know the state of the system in 2 minutes.

---

## Step 1 — Pull Latest

Always pull first — never run a digest on stale data:

```bash
cd "/Users/dave/Desktop/Dave's AI Brain"
git pull origin main
```

---

## Step 2 — Collect Raw Activity

Run these in parallel to gather everything from the past 7 days:

```bash
# All commits in the last 7 days with dates
git log --oneline --since="7 days ago" --format="%ad | %s" --date=short

# Files changed by agents (not just Claude interactive sessions)
git log --since="7 days ago" --name-only --format="%s" | grep -v "^$"
```

Also read: `06 Wiki/system/log.md` — pull all entries from the past 7 days.

---

## Step 3 — Categorise the Activity

Sort all commits and log entries into buckets:

| Bucket | What it includes |
|--------|-----------------|
| **FBA Research** | Agent research runs, niche pages created/updated, H10 data ingested |
| **Stock Monitoring** | Stock agent runs, alerts created, wiki updates |
| **Wiki Updates** | New pages, updated pages, log entries from Claude sessions |
| **System & Automation** | Plist changes, skill updates, agent prompt changes, GitHub actions |
| **Vault Maintenance** | Cleanup, reorganisation, CLAUDE.md updates |

For each bucket, count:
- How many agent runs (look for automated commit messages)
- How many human-assisted sessions (look for session-close commits)
- What was the net output (new pages, updated scores, alerts fired)

---

## Step 4 — The Digest

Output in this exact format. Be brief — this is a scan, not a report. No padding.

---

### 🧠 Vault Weekly Digest — [Date Range]

**[X] agent runs · [X] Claude sessions · [X] wiki pages touched**

---

#### 🤖 Autonomous Agents

**FBA Research Agent** — ran [X] times
- [Brief bullet on what it produced — niches researched, scores updated, any PASS/GO verdicts]
- [Data quality note if relevant — simulated vs real H10]

**Stock Monitoring Agent** — ran [X] times
- [Brief bullet — what positions were flagged, any alerts created]
- [EXR status if anything notable happened]

**Auto-Pull** — ran [X] times · [X] new commits pulled

---

#### 📊 FBA Research Progress

[Only include if there was FBA activity]

Niches researched this week:
- **[Niche]** — [Score]/100 [verdict emoji] — [one sentence key finding]
- **[Niche]** — [Score]/100 [verdict emoji] — [one sentence key finding]

Priority queue as of today:
1. [Top action]
2. [Second action]

---

#### 📈 Stock Monitoring

[Only include if there was stock activity or alerts]

- **EXR**: [Status — any Diona-1 news? Flow test results?]
- **NBIS**: [Any significant moves?]
- **Alerts created**: [X] — [brief description if any]

---

#### 📚 Wiki & System

- New wiki pages: [X]
- Updated pages: [X]
- Skills updated: [list any]
- System changes: [list any plist/agent/automation changes]

---

#### 📣 Signal Check

**Is the system working?** [Yes / Partially / No — one sentence on health of automation]

**Momentum:** [One sentence — is the work moving forward, stuck, or drifting?]

**One thing that needs Dave's attention:** [Specific action or decision — not a list]

---

## Step 5 — Append to Log

```
- YYYY-MM-DD: Weekly digest generated. [X] agent runs. Top signal: [one sentence].
```

Append to `06 Wiki/system/log.md`.

---

## Rules

- Start with the count summary — always lead with numbers
- Agent health first — if automation is broken, say so in the first line
- No duplicate information — if something is in the digest, don't repeat it in the log entry
- If agents haven't run, say that bluntly and give Dave the routines link:
  `https://claude.ai/code/routines`
- End with exactly ONE thing for Dave to do next — not a list
