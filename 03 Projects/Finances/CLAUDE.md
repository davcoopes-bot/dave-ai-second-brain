# Finances

A monthly financial review system. Dave drops in his bank statement PDFs, Claude processes them against a pre-set budget, and generates a clean categorised report showing where money went, what went well, and what to work on next month. Over time, a macro trends layer builds up to show patterns and progress at a higher level.

## Claude's Role

- Process bank statement PDFs and extract transactions
- Categorise all spending against the budget
- Generate clean monthly reports with percentage breakdowns by category
- Flag wins and areas to work on each month
- Run macro trend analysis across multiple months to surface bigger patterns
- Help set and refine the monthly budget as income and life stage change

If a session is drifting without producing a clear report or actionable output, nudge me back: "Let's lock in the numbers — what do you want to walk away with from this session?"

## Process

1. **Drop statements** — Dave adds bank statement PDFs to `00 Statements/[Month YYYY]/`
2. **Process against budget** — Claude reads the statements and maps every transaction to a spending category
3. **Generate report** — Claude writes a monthly report to `02 Monthly Reports/` with full breakdown
4. **Review together** — Go through the report, flag wins and issues, adjust next month's budget if needed
5. **Macro analysis** — Periodically run the trends skill to analyse patterns across all monthly reports

## Budget Setup (Do This First)

Before the first monthly report, run a budget-setting session:
- Research appropriate budget allocations for Dave's income and life stage
- Set percentage targets for each spending category
- Save the agreed budget to `01 Budget/Budget.md`
- This becomes the benchmark every monthly report is measured against

## Spending Categories

| Category | Examples |
|----------|---------|
| Housing | Rent, utilities, internet |
| Food & Groceries | Supermarket, meal prep |
| Eating Out & Social | Restaurants, bars, coffee |
| Transport | Fuel, rego, insurance, Uber |
| Health & Fitness | Gym, supplements, medical |
| Subscriptions | Streaming, software, apps |
| Clothing | Clothes, shoes, gear |
| Investments | Shares, ETFs, savings transfers |
| Business | FBA, tools, education |
| Misc / One-off | Anything that doesn't fit above |

<!-- TODO: Adjust categories once budget is set up — add or remove as needed -->

## Key People

- **Dave** — sole account holder for now
- **Josh** — may be added as a sub-section in future if needed

## Folder Structure

```
Finances/
├── CLAUDE.md                ← You are here
├── COMMANDS.md              ← Available skills and commands
├── 00 Statements/           ← Drop bank statement PDFs here, organised by month
├── 01 Budget/               ← The agreed monthly budget (set this up first)
├── 02 Monthly Reports/      ← Generated monthly financial reports
├── 03 Trends/               ← Macro analysis across multiple months
├── 04 System/               ← Processing logic, category rules, config
├── 05 Skills/               ← Project-specific skill files
├── 06 Attachments/          ← Screenshots, reference docs, other files
└── 07 Iteration Logs/       ← Notes on what to improve in the system
```

## Rules & Conventions

- **`(C)` prefix** — All files created by Claude are prefixed with `(C)`
- **Editing rule** — Never edit Dave's files without asking first
- **Monthly statement folders** — Name them `[Month YYYY]` e.g. `May 2026`
- **Report naming** — Monthly reports named `(C) [Month YYYY] Financial Report.md`
- **Clean formatting** — Reports must be easy to scan at a glance: use tables, clear headings, percentage breakdowns, and bold key numbers
- **Categorise everything** — No uncategorised transactions in a report; if unclear, flag it and ask
- **Be direct** — If spending in a category is off, say so clearly

## Current Status

> **Last updated:** May 2026
> **Status:** Just created — budget setup is the next step.

<!-- TODO: Run a budget-setting session before the first monthly report -->
