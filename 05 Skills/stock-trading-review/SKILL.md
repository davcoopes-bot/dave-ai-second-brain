---
name: stock-trading-review
description: >
  Run a structured trading review session — reviewing positions, tracking performance, and building out the trading framework. Use this skill whenever Dave says "let's review my trades", "check my portfolio", "trading update", "how's the stock going", or wants to document or improve his trading approach. Also use when Dave wants to research a specific stock or make a buy/sell decision.
---

# Skill: Stock Trading Review

Dave has $17k deployed in stocks with no documented framework in the vault. This skill exists to change that — and to make every future trading session systematic rather than ad hoc.

**Two modes:**
1. **Framework build** — first-time or periodic session to document and improve the trading system itself
2. **Position review** — session focused on specific holdings, performance, and upcoming decisions

---

## Before Starting

Run the portfolio snapshot script first to get live prices — saves Dave reading out numbers manually:

```bash
python3 "05 Skills/stock-trading-review/scripts/portfolio_snapshot.py"
```

Then read:
1. `CLAUDE.md` — overall goals, current financial position
2. `GOALS.md` — the $10k/month and $1M targets, income stream pipeline
3. `06 Wiki/wiki/finance/stock-trading-overview.md` — the trading framework page (may be incomplete — update it during this session if new information comes up)

When Dave's positions change, update `POSITIONS` dict in `scripts/portfolio_snapshot.py`.

---

## Mode 1: Framework Build

Use this when the trading wiki page is empty or incomplete, or when Dave wants to properly document his approach.

### Step 1 — Interview

Ask Dave directly:
- **What's your current strategy?** (e.g., growth stocks, dividend investing, swing trading, index funds, options — what are you actually doing?)
- **What's your entry process?** (How do you decide to buy something? What criteria does a stock need to meet?)
- **What's your exit process?** (When do you sell? Do you use stop-losses? Do you take profits at a target?)
- **What are you tracking?** (P&L, individual stock performance, benchmarks — what metrics matter?)
- **What's your position sizing rule?** (What % of capital per position? Max per sector?)
- **What's the goal for trading?** (Grow $17k to X by when? Beating index? Specific income target?)
- **What's your read on what's working vs. not working so far?**

Don't make assumptions. If Dave doesn't have answers, that's the finding — and the gap to fill.

### Step 2 — Build the Framework Page

After the interview, update `06 Wiki/wiki/finance/stock-trading-overview.md` with everything Dave provided.

- Mark confirmed information clearly
- Mark unknowns/undecided as `_[TBD — Dave to confirm]_`
- Never invent strategy details. Only write what Dave told you.

### Step 3 — Identify the Gaps

After documenting what exists, identify the highest-leverage gaps:
- No entry criteria = buying on gut = no edge
- No exit criteria = holding winners too long or selling too soon
- No position sizing = one bad bet can wreck the portfolio
- No tracking = can't improve what you don't measure

Tell Dave plainly which gaps are highest risk.

### Step 4 — Recommend the Next Build

Based on what's missing, recommend the single highest-leverage thing to build next:
- A simple entry checklist?
- A position sizing rule?
- A tracking spreadsheet?
- A watchlist system?

One thing. Not five.

---

## Mode 2: Position Review

Use this for a regular check-in on current holdings and upcoming decisions.

### Step 1 — Get the Current Picture

Ask Dave to share:
- Current holdings (stock, number of shares, entry price, current price)
- Any open orders or planned moves
- Anything that's up/down significantly since last review

If Dave has a brokerage app, he can read the numbers out or paste them in. Don't ask him to screen share — just describe.

### Step 2 — Run the Review

For each position:
- **P&L status:** Up or down? By how much?
- **Does the original thesis still hold?** Why did he buy this? Is that still true?
- **Is there a decision to make?** (Hold / add / trim / sell — be specific)

For the overall portfolio:
- **Concentration risk:** Is any single position too large?
- **Correlation risk:** Are all positions moving together? (Diversification check)
- **Cash position:** Is there dry powder for opportunities?

### Step 3 — State Decisions Clearly

For each position where a decision is needed:
- State the recommended action (hold / add / trim / exit)
- State the reasoning in one sentence
- State the trigger that would change the call

**⚠️ Important:** Claude is not a licensed financial advisor. All analysis here is for thinking purposes only — Dave makes all final decisions himself. Flag any high-conviction calls as opinions, not instructions.

### Step 4 — Update the Wiki

After the review, append a brief entry to `06 Wiki/wiki/finance/stock-trading-overview.md`:

```
## Review Log

| Date | Portfolio value | Key decisions made | Notes |
|------|----------------|-------------------|-------|
| [date] | $[value] | [decisions] | [notes] |
```

And log the review in `06 Wiki/system/log.md`:
```
## [YYYY-MM-DD] update | Trading review
- Pages updated: wiki/finance/stock-trading-overview.md
- Summary: [1–2 sentences on what was decided]
```

---

## Rules for This Skill

- **Never invent trading strategy.** Only document what Dave has confirmed.
- **Flag all placeholders clearly.** Anything unconfirmed gets `_[TBD]_`.
- **No specific investment recommendations beyond analysis.** Present the thinking, let Dave decide.
- **One decision at a time.** Don't overwhelm with 10 simultaneous calls.
- **Always update the wiki after a session.** Knowledge that doesn't get filed is lost.
