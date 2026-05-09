---
name: session-close
description: >
  Trigger phrases: "close the session", "end of session", "wrap up", "session close",
  "before we finish", "anything to update", "save what we learned", "wrap this up"
---

# Skill: Session Close

> **Purpose:** Capture what was learned or decided before the session ends. Two minutes now compounds into a significantly smarter vault over time. Every insight that doesn't get filed is lost permanently.
>
> **When to run:** At the end of any session where something useful happened — a decision was made, new information came up, a contradiction was found, or context shifted.
>
> **What this is NOT:** A full wiki ingest (that's `wiki-ingest`). A weekly status update (that's `weekly-update`). This is a quick capture layer — lightweight, fast, every session.

---

## Step 1 — Scan the Session

Before asking Dave anything, review what happened in this conversation:

- What decisions were made?
- What new information came up that isn't in the wiki yet?
- Did anything contradict an existing wiki page?
- Did any wiki page get used and turn out to be wrong, incomplete, or stale?
- Did Dave mention anything about Josh, FBA, trading, finance, or goals that isn't already captured?

Do this silently. Don't output the scan — just use it to inform the questions in Step 2.

---

## Step 2 — The Five Questions

Ask Dave all five in one message. Keep it tight — this should take under 2 minutes.

---

**Session close — quick capture before we finish:**

1. **Decisions:** Did we settle anything today that should be recorded? *(New positions, changed plans, confirmed or ruled out options)*

2. **New info:** Did anything come up — a number, a fact, an insight — that isn't in the wiki yet and should be?

3. **Contradictions:** Did anything we discussed clash with something already in the vault? *(I'll flag what I spotted, but you may have noticed something too)*

4. **Stale pages:** Did we pull up any wiki pages that felt out of date or incomplete?

5. **Next session:** What's the first thing you want to pick up next time?

---

## Step 3 — Process the Answers

Based on Dave's answers and your own scan from Step 1, do the following:

### A — Immediate wiki updates (do these now)

For any contradiction or clear error in an existing page: fix it directly using Edit. Note the change in the page's revision history.

For any decision that updates a settled position in Chess Moves: update `02 Chess Moves (Long-Term Planning)/(C) Chess Moves — Dave 2026.md`.

For any trading decision: update the review log in `06 Wiki/wiki/finance/stock-trading-overview.md`.

### B — Queue items for full ingest (flag, don't build now)

If new information is substantial enough to warrant a full wiki page (new source, new niche, new research), don't build it now. Add it to the Suggested Next Ingests section of `06 Wiki/system/index.md` with a one-line description.

### C — CLAUDE.md updates

If Dave's weekly context shifted — what's working, what's not, what he's sitting on — update the Weekly Update section of `CLAUDE.md`. Only update if something actually changed; don't rewrite just to rewrite.

---

## Step 4 — Log the Session

Append a brief entry to `06 Wiki/system/log.md`:

```
## [YYYY-MM-DD] session-close | [one-line session description]

- Decisions captured: [list or "none"]
- Wiki pages updated: [list or "none"]
- Queued for ingest: [list or "none"]
- Contradictions fixed: [list or "none"]
- Next session: [what Dave said]
```

---

## Step 5 — Close Out

End with a single clean message:

> **Session closed.** Here's what was filed:
> - [Bullet list of anything actually updated or queued]
>
> Next session starts on: **[what Dave flagged as the first thing to pick up]**

If nothing needed filing, say so plainly:
> **Session closed.** Nothing new to file — vault is current. Next session: [what Dave flagged].

---

## Rules

- **Fast over perfect.** A quick capture is infinitely better than a perfect capture that never happens. Don't over-engineer this.
- **Don't ingest during session close.** If something needs a full ingest, queue it. Do it properly next session.
- **Only update what changed.** Don't rewrite pages just to refresh them. Noise in the wiki is as bad as missing information.
- **Flag but don't fix big contradictions here.** If a contradiction requires significant rework of a page, flag it in the log and queue a dedicated session. Only fix clear, small errors in session close.
- **The log entry is mandatory.** Even if nothing was updated, the log entry still gets written. The pattern of sessions is itself useful information.
