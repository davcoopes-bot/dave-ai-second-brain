---
name: h10-scraper
description: >
  Automated Helium 10 data collection. Reads keywords from raw/h10-queue.txt,
  searches Amazon for each keyword, enriches results via H10's direct API
  (sales, BSR, reviews), and saves CSVs to raw/sources/ for the niche-decision
  skill. Use when Dave adds keywords to the queue and wants H10 data without
  manual CSV exports. Triggers on "run H10 scraper", "scrape H10",
  "process the queue", or "get H10 data for [keyword]".
---

# Skill: H10 Scraper

Automates the H10 Xray data step end-to-end — no browser required, no manual exports, no column configuration.

**How it works:**
1. Searches Amazon.com for the keyword using your live Chrome session
2. Calls H10's product APIs (sales-chart, bsr-chart, review-chart) per ASIN
3. Saves a CSV to `raw/sources/` ready for `h10_quick_stats.py`

---

## Setup (One-Time)

Capture your H10 + Amazon sessions from Chrome:
```bash
python3 "05 Skills/FBA/h10-scraper/scripts/h10_scraper.py" --login
```

Requires:
- Chrome open and logged into `members.helium10.com`
- `pycookiecheat` installed: `pip3 install pycookiecheat`
- `playwright` installed: `pip3 install playwright && playwright install chromium`
- `requests` installed: `pip3 install requests`

Session saved to `~/.h10-session.json`. Redo `--login` if H10 session expires (weeks).
Amazon cookies are pulled fresh from Chrome on every run — no action needed.

---

## Normal Usage

### Step 1 — Add keywords to the queue

Edit `raw/h10-queue.txt`:
```
padded lifting straps
figure 8 lifting straps
cable management box
```

Or ask Claude to add them. One keyword per line.

### Step 2 — Run the scraper

```bash
python3 "05 Skills/FBA/h10-scraper/scripts/h10_scraper.py"
```

Outputs:
- `raw/sources/H10-padded-lifting-straps.csv`
- `raw/sources/H10-figure-8-lifting-straps.csv`
- `raw/sources/H10-cable-management-box.csv`

After each keyword:
- Processed keyword is removed from the queue
- FAIL keywords are filed under `# FAILED PRODUCTS` in `raw/h10-queue.txt`
- **`03 Projects/FBA Research/(C) Niche Research Tracker.md` is auto-updated** — summary table, detailed section, and Research Log all written automatically

### Step 3 — Get instant stats

```bash
python3 "05 Skills/FBA/niche-decision/scripts/h10_quick_stats.py" raw/sources/H10-*.csv
```

---

## Single Keyword (Skip Queue)

```bash
python3 "05 Skills/FBA/h10-scraper/scripts/h10_scraper.py" --keyword "padded lifting straps"
```

---

## Check Session

```bash
python3 "05 Skills/FBA/h10-scraper/scripts/h10_scraper.py" --check-session
```

If expired: re-run `--login`.

---

## How It Works

1. Pulls Amazon.com cookies fresh from your Chrome browser (via `pycookiecheat`)
2. Launches headless Playwright browser → searches Amazon for the keyword
3. Extracts top organic ASINs, titles, prices from search results
4. For each ASIN, calls H10's authenticated product APIs:
   - `members.helium10.com/api/v1/product/sales-chart` → sums last 30 days → Monthly Revenue
   - `members.helium10.com/api/v1/product/bsr-chart` → most recent value → BSR
   - `members.helium10.com/api/v1/product/review-chart` → most recent count → Reviews
5. Saves formatted CSV to `raw/sources/` with standard naming (`H10-{slug}.csv`)
6. Marks keyword as done in queue file

Auth: H10 Bearer token from `~/.h10-session.json` localStorage. Valid for weeks.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `Session invalid` or H10 API 401 | Run `--login` again |
| Amazon bot check triggered | Chrome must be running with active Amazon session |
| `pycookiecheat` error | Chrome must be open; `pip3 install pycookiecheat` |
| Revenue shows N/A | H10 may have no data for that ASIN — check manually |
| Playwright not installed | `pip3 install playwright && playwright install chromium` |

---

## Files

| File | Purpose |
|------|---------|
| `scripts/h10_scraper.py` | Main scraper script |
| `raw/h10-queue.txt` | Keyword queue — edit to add/remove |
| `~/.h10-session.json` | Saved H10 session (auto-managed) |
| `raw/sources/H10-*.csv` | Output CSVs — picked up by niche-decision skill |
