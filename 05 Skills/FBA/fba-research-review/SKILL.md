---
name: fba-research-review
description: >
  Reviews what the automated FBA research agent has produced, surfaces what needs
  Dave's action, and updates priorities. Use this skill when Dave comes back after
  the agent has run and says "what did the agent find", "review what's new",
  "what came in overnight", "what's the agent done", "show me the research",
  "morning review", or "FBA update". Always pull from GitHub first to ensure
  the latest agent output is loaded.
---

# Skill: FBA Research Review

You are reviewing what the overnight FBA research agent has produced and telling
Dave what matters, what needs his action, and what can wait.

Be a filter, not a reporter. Dave doesn't need a summary of everything the agent
wrote — he needs to know where to spend his next 30 minutes.

---

## Step 1 — Pull Latest from GitHub

Before reading anything, make sure the vault is up to date:

```bash
cd "/Users/dave/Desktop/Dave's AI Brain"
git pull origin main
```

If there are merge conflicts, surface them immediately — don't silently resolve them.

---

## Step 2 — What Has Changed Since Last Review

Check git log to see what the agent committed:

```bash
git log --oneline --since="7 days ago"
```

For each agent commit found, note:
- Date and time
- What the commit message says was done
- Which files were changed (`git show --name-only [commit-hash]`)

If no new commits from the agent, tell Dave immediately:
> "The agent hasn't committed any new research since [last run date]. Check
> https://claude.ai/code/routines/trig_016gto8no4HwX9Va1UjUdJwu to see if
> there's an issue with the scheduled run."

---

## Step 3 — Read New Research

For each new or updated file the agent wrote, read it and extract:
- What niche was researched
- What score it received
- What verdict was reached
- What the key finding was (the one number or fact that drives the verdict)
- What data gaps remain (still needs H10 validation?)

---

## Step 4 — The Briefing

Output a clean, scannable briefing. No padding.

---

### 📋 FBA Research Briefing — [Date]

**Agent ran:** [X] times since last review | **New pages:** [X] | **Updated pages:** [X]

---

#### 🔴 Needs Your Action Now

[List niches where a decision or physical action is required from Dave]

For each:
> **[Niche]** — [Score]/100 [Verdict emoji]
> **Finding:** [One sentence — the key number or fact]
> **Your action:** [Exactly what Dave needs to do — e.g. "Run H10 Xray on 'cable
> management box' — export with Reviews column — drop in raw/sources/"]

---

#### 🟡 Promising — Worth Reading

[List niches that scored 60+ and are worth Dave's attention, but don't need
immediate action]

For each:
> **[Niche]** — [Score]/100 [Verdict emoji]
> **Why it's interesting:** [One sentence]
> **Status:** [What's needed next before a decision]

---

#### ❌ Passed / Eliminated

[List niches the agent researched and passed — brief reason only]

- **[Niche]** — [Why it failed the pre-filter or scored too low]

---

#### ⚠️ Data Gaps — H10 Still Needed

[List niches that have simulated data or missing review counts and can't be
decided yet]

For each:
> **[Niche]** — Run H10 Xray on: `[exact keywords]`
> **What's missing:** [Reviews / Revenue / Both]

---

### Priority Queue — Updated

Based on this review, here is the updated action queue:

1. **[Highest priority action]** — [Why it's first]
2. **[Second]**
3. **[Third]**

---

## Step 5 — Update Priority Actions

After the briefing, update `06 Wiki/system/index.md` Priority Actions section
with the current queue from Step 4.

Also update `06 Wiki/wiki/fba/fba-research-overview.md` priority action queue.

Append to `06 Wiki/system/log.md`:
```
- YYYY-MM-DD: FBA research review completed. X new niches. Priority: [top action].
```

---

## Step 6 — Commit the Updates

```bash
cd "/Users/dave/Desktop/Dave's AI Brain"
git add -A
git commit -m "FBA review YYYY-MM-DD — priority queue updated"
git push origin main
```

---

## Rules

- Always pull first — never review stale data
- One action per niche maximum — don't give Dave a list of five things for each product
- Be blunt about passes — don't soften them
- If the agent hasn't run or failed, say so immediately and give Dave the routines link
- Never re-summarise things Dave already knows — reference what changed, not the full history
