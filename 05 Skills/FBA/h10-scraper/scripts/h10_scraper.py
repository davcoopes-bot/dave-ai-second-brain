#!/usr/bin/env python3
"""
H10 Scraper — Automated Helium 10 data collection via direct API.

Flow:
  1. Read keywords from raw/h10-queue.txt
  2. Search Amazon.com for each keyword → extract top ASINs + product metadata
  3. Call H10 API for each ASIN → sales revenue, BSR, review data
  4. Save CSV to raw/sources/H10-{slug}.csv

Usage:
    python3 h10_scraper.py                         # Process all queue keywords
    python3 h10_scraper.py --keyword "cable box"   # Single keyword, skip queue
    python3 h10_scraper.py --login                 # Re-capture H10 session from Chrome
    python3 h10_scraper.py --check-session         # Verify session is valid
    python3 h10_scraper.py --top 20                # Pull top N results (default: 10)
    python3 h10_scraper.py --no-clear              # Don't mark keywords done in queue

Session: ~/.h10-session.json (extracted from Chrome via --login)
Queue:    raw/h10-queue.txt
Output:   raw/sources/H10-{keyword-slug}.csv
"""

import argparse
import csv
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Tuple

try:
    from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout
except ImportError:
    print("ERROR: Playwright not installed. Run: pip3 install playwright && playwright install chromium")
    sys.exit(1)

try:
    import requests
except ImportError:
    print("ERROR: requests not installed. Run: pip3 install requests")
    sys.exit(1)

# ─── CONFIG ───────────────────────────────────────────────────────────────────

VAULT_ROOT   = Path(__file__).parent.parent.parent.parent.parent  # Dave's AI Brain/
QUEUE_FILE   = VAULT_ROOT / "raw" / "h10-queue.txt"
OUTPUT_DIR   = VAULT_ROOT / "raw" / "sources"
SESSION_FILE  = Path.home() / ".h10-session.json"
TRACKER_FILE  = VAULT_ROOT / "03 Projects" / "FBA Research" / "(C) Niche Research Tracker.md"

H10_MEMBERS  = "https://members.helium10.com"
H10_RESEARCH = "https://research-tools.helium10.com"
MARKETPLACE  = "ATVPDKIKX0DER"   # Amazon US

# How many seconds to wait between ASIN API calls (be respectful)
API_DELAY = 0.4

# ─── SESSION MANAGEMENT ────────────────────────────────────────────────────────

def load_session() -> dict:
    """Load the saved H10 session from disk."""
    if not SESSION_FILE.exists():
        print(f"ERROR: No session file at {SESSION_FILE}")
        print("Run with --login to capture your H10 session from Chrome.")
        sys.exit(1)
    with open(SESSION_FILE) as f:
        return json.load(f)


def get_bearer_token(session: dict) -> Tuple[str, str]:
    """Extract bearer token and account ID from session's localStorage."""
    for origin in session.get("origins", []):
        if "helium10" in origin.get("origin", ""):
            for item in origin.get("localStorage", []):
                if item["name"] == "CORE_BEARER_TOKEN":
                    token_data = json.loads(item["value"])
                    account_id = list(token_data.keys())[0]
                    bearer = list(token_data.values())[0]
                    return bearer, account_id
    print("ERROR: CORE_BEARER_TOKEN not found in session. Re-run --login.")
    sys.exit(1)


def get_h10_cookies(session: dict) -> dict:
    """Extract Helium10 cookies from session."""
    return {
        c["name"]: c["value"]
        for c in session.get("cookies", [])
        if "helium10" in c.get("domain", "")
    }


def check_session() -> bool:
    """Verify the saved H10 session is still valid."""
    session = load_session()
    bearer, account_id = get_bearer_token(session)
    h10_cookies = get_h10_cookies(session)

    headers = {
        "Authorization": f"Bearer {bearer}",
        "Accept": "application/json",
    }
    try:
        r = requests.get(
            f"{H10_MEMBERS}/api/v1/customers/me",
            headers=headers,
            cookies=h10_cookies,
            timeout=10,
            params={"accountId": account_id},
        )
        if r.status_code == 200:
            data = r.json()
            email = data.get("data", {}).get("email", "unknown")
            print(f"✅ Session valid — logged in as: {email}")
            return True
        else:
            print(f"❌ Session invalid (HTTP {r.status_code}). Re-run --login.")
            return False
    except Exception as e:
        print(f"❌ Session check failed: {e}")
        return False


def do_login():
    """Capture H10 session from the user's existing Chrome browser using pycookiecheat."""
    try:
        import pycookiecheat
    except ImportError:
        print("ERROR: pycookiecheat not installed. Run: pip3 install pycookiecheat")
        sys.exit(1)

    print("Extracting H10 session from your Chrome browser...")
    print("(Chrome must be running and you must be logged into members.helium10.com)")
    print()

    # Get cookies from Chrome
    h10_cookies_raw = pycookiecheat.chrome_cookies("https://members.helium10.com")
    amazon_cookies_raw = pycookiecheat.chrome_cookies("https://www.amazon.com")

    if not h10_cookies_raw:
        print("ERROR: No H10 cookies found. Make sure you're logged into members.helium10.com in Chrome.")
        sys.exit(1)

    print(f"Found {len(h10_cookies_raw)} H10 cookies, {len(amazon_cookies_raw)} Amazon cookies")

    # Use Playwright to navigate to H10 and capture full session state (localStorage too)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()

        # Inject H10 cookies
        cookie_list = [
            {
                "name": name,
                "value": str(value),
                "domain": ".helium10.com",
                "path": "/",
                "httpOnly": False,
                "secure": False,
                "sameSite": "Lax",
            }
            for name, value in h10_cookies_raw.items()
        ]
        context.add_cookies(cookie_list)

        page = context.new_page()
        page.goto(f"{H10_MEMBERS}/dashboard", timeout=30000, wait_until="domcontentloaded")
        time.sleep(4)

        # Check if we landed on dashboard (logged in)
        url = page.url
        title = page.title()
        print(f"Landed on: {title} ({url})")

        if "signin" in url or "login" in url:
            print("ERROR: Redirected to login page. Chrome cookies may be expired.")
            browser.close()
            sys.exit(1)

        # Save full storage state (includes localStorage with CORE_BEARER_TOKEN)
        storage_state = context.storage_state()
        browser.close()

    # Inject Amazon cookies into the storage state
    amazon_cookie_list = [
        {
            "name": name,
            "value": str(value),
            "domain": ".amazon.com",
            "path": "/",
            "httpOnly": False,
            "secure": False,
            "sameSite": "Lax",
        }
        for name, value in amazon_cookies_raw.items()
    ]
    storage_state.setdefault("cookies", []).extend(amazon_cookie_list)

    # Save to session file
    with open(SESSION_FILE, "w") as f:
        json.dump(storage_state, f)

    print(f"\n✅ Session saved to {SESSION_FILE}")
    print("Verifying session...")
    check_session()


# ─── AMAZON SEARCH ─────────────────────────────────────────────────────────────

def search_amazon(keyword: str, session: dict, top_n: int = 10) -> list[dict]:
    """
    Search Amazon.com for keyword, return list of top product dicts.
    Each dict: {asin, title, price, rating, reviews, rank}
    """
    # Pull Amazon cookies fresh from Chrome each run (avoids stale session issues)
    amazon_cookies = {}
    try:
        import pycookiecheat
        amazon_cookies = pycookiecheat.chrome_cookies("https://www.amazon.com")
    except Exception:
        pass

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            extra_http_headers={"Accept-Language": "en-US,en;q=0.9"},
        )

        # Inject Amazon cookies
        if amazon_cookies:
            cookie_list = [
                {
                    "name": name,
                    "value": str(value),
                    "domain": ".amazon.com",
                    "path": "/",
                    "httpOnly": False,
                    "secure": False,
                    "sameSite": "Lax",
                }
                for name, value in amazon_cookies.items()
            ]
            context.add_cookies(cookie_list)

        page = context.new_page()
        search_url = f"https://www.amazon.com/s?k={keyword.replace(' ', '+')}&language=en_US"
        print(f"  Searching Amazon: {search_url}")

        try:
            page.goto(search_url, timeout=30000, wait_until="domcontentloaded")
            time.sleep(3)
        except PWTimeout:
            print("  WARNING: Amazon page load timed out, trying with what loaded...")

        # Check for CAPTCHA / error
        title = page.title()
        if "robot" in title.lower() or "captcha" in title.lower() or "something went wrong" in title.lower():
            print(f"  WARNING: Amazon bot check triggered (title: {title})")
            page.screenshot(path=str(OUTPUT_DIR / f"debug-amazon-{slug(keyword)}.png"))
            browser.close()
            return []

        # Extract product data from search results
        products = page.evaluate(f"""
            () => {{
                const results = [];
                const seen = new Set();
                const maxResults = {top_n * 3};  // Grab extra in case some are ads/sponsored

                // Get all search result items
                const items = document.querySelectorAll('[data-asin][data-component-type="s-search-result"]');

                for (const item of items) {{
                    if (results.length >= maxResults) break;

                    const asin = item.getAttribute('data-asin');
                    if (!asin || !/^[A-Z0-9]{{10}}$/.test(asin) || seen.has(asin)) continue;
                    seen.add(asin);

                    // Title
                    const titleEl = item.querySelector('h2 a span, h2 span, .a-text-normal');
                    const title = titleEl ? titleEl.textContent.trim() : '';

                    // Price
                    let price = null;
                    const priceEl = item.querySelector('.a-price .a-offscreen');
                    if (priceEl) {{
                        const priceStr = priceEl.textContent.replace(/[^0-9.]/g, '');
                        price = parseFloat(priceStr) || null;
                    }}

                    // Rating
                    let rating = null;
                    const ratingEl = item.querySelector('.a-icon-star-small .a-icon-alt, .a-icon-star .a-icon-alt, [aria-label*="out of 5 stars"]');
                    if (ratingEl) {{
                        const rText = (ratingEl.getAttribute('aria-label') || ratingEl.textContent || '');
                        const rMatch = rText.match(/(\\d+\\.?\\d*)/);
                        rating = rMatch ? parseFloat(rMatch[1]) : null;
                    }}

                    // Review count
                    let reviewCount = null;
                    const reviewEl = item.querySelector('[aria-label*="stars"] + span, .a-size-base.s-underline-text');
                    if (reviewEl) {{
                        const rText = reviewEl.textContent.replace(/,/g, '');
                        const rMatch = rText.match(/(\\d+)/);
                        reviewCount = rMatch ? parseInt(rMatch[1]) : null;
                    }}

                    // Sponsored check
                    const isSponsored = !!item.querySelector('.s-label-popover-default, [data-component-type="sp-sponsored-result"]');

                    results.push({{
                        asin,
                        title,
                        price,
                        rating,
                        reviews: reviewCount,
                        sponsored: isSponsored,
                        rank: results.length + 1,
                    }});
                }}
                return results;
            }}
        """)

        page.screenshot(path=str(OUTPUT_DIR / f"debug-amazon-{slug(keyword)}.png"))
        browser.close()

    if not products:
        print(f"  WARNING: No products found on Amazon for '{keyword}'")
        return []

    # Filter out sponsored, take top_n organic results
    organic = [p for p in products if not p.get("sponsored")]
    if len(organic) < 5:
        # If very few organic, include sponsored too
        organic = products

    top = organic[:top_n]
    print(f"  Found {len(products)} products on Amazon, using top {len(top)} organic")
    return top


# ─── H10 API ───────────────────────────────────────────────────────────────────

def h10_api_headers(bearer: str) -> dict:
    return {
        "Authorization": f"Bearer {bearer}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }


def get_monthly_revenue(asin: str, bearer: str, cookies: dict, account_id: str) -> Optional[float]:
    """Return estimated monthly revenue for an ASIN using H10's sales-chart API."""
    try:
        r = requests.get(
            f"{H10_MEMBERS}/api/v1/product/sales-chart",
            headers=h10_api_headers(bearer),
            cookies=cookies,
            params={
                "asin": asin,
                "marketplace": MARKETPLACE,
                "accountId": account_id,
            },
            timeout=10,
        )
        if r.status_code != 200:
            return None

        sales = r.json().get("results", {}).get("sales", [])
        if not sales:
            return None

        # Sum last 30 data points (daily revenue estimates)
        last_30 = sorted(sales, key=lambda x: x["x"], reverse=True)[:30]
        return round(sum(d["y"] for d in last_30), 2)

    except Exception:
        return None


def get_current_bsr(asin: str, bearer: str, cookies: dict, account_id: str) -> Optional[int]:
    """Return current BSR for an ASIN using H10's bsr-chart API."""
    try:
        r = requests.get(
            f"{H10_MEMBERS}/api/v1/product/bsr-chart",
            headers=h10_api_headers(bearer),
            cookies=cookies,
            params={
                "asin": asin,
                "marketplace": MARKETPLACE,
                "accountId": account_id,
            },
            timeout=10,
        )
        if r.status_code != 200:
            return None

        bsr_history = r.json().get("results", {}).get("bsrHistory", [])
        if not bsr_history:
            return None

        # Most recent BSR value
        latest = max(bsr_history, key=lambda x: x.get("end", x.get("start", 0)))
        return latest.get("value")

    except Exception:
        return None


def get_review_count(asin: str, bearer: str, cookies: dict, account_id: str) -> Tuple[Optional[int], Optional[float]]:
    """Return (review_count, rating) for an ASIN using H10's review-chart API."""
    try:
        r = requests.get(
            f"{H10_MEMBERS}/api/v1/product/review-chart",
            headers=h10_api_headers(bearer),
            cookies=cookies,
            params={
                "asin": asin,
                "marketplace": MARKETPLACE,
                "accountId": account_id,
            },
            timeout=10,
        )
        if r.status_code != 200:
            return None, None

        reviews = r.json().get("results", {}).get("reviews", [])
        if not reviews:
            return None, None

        # Most recent data point
        latest = max(reviews, key=lambda x: x.get("timestamp", 0))
        count = latest.get("count")
        rating = latest.get("rating")  # May or may not be present
        return count, rating

    except Exception:
        return None, None


def enrich_with_h10(products: list[dict], bearer: str, cookies: dict, account_id: str) -> list[dict]:
    """Add H10 revenue, BSR, and review data to each product dict."""
    enriched = []
    total = len(products)

    for i, product in enumerate(products, 1):
        asin = product["asin"]
        print(f"  [{i}/{total}] {asin} — {product.get('title', '')[:50]}")

        # Revenue
        revenue = get_monthly_revenue(asin, bearer, cookies, account_id)
        print(f"         Revenue: ${revenue:,.0f}/mo" if revenue else "         Revenue: N/A")
        time.sleep(API_DELAY)

        # BSR
        bsr = get_current_bsr(asin, bearer, cookies, account_id)
        print(f"         BSR: #{bsr:,}" if bsr else "         BSR: N/A")
        time.sleep(API_DELAY)

        # Reviews (use H10 count if Amazon scrape missed it)
        h10_reviews, h10_rating = get_review_count(asin, bearer, cookies, account_id)
        reviews = product.get("reviews") or h10_reviews
        rating  = product.get("rating")  or h10_rating
        print(f"         Reviews: {reviews:,}" if reviews else "         Reviews: N/A")
        time.sleep(API_DELAY)

        enriched.append({
            **product,
            "monthly_revenue": revenue,
            "bsr": bsr,
            "reviews": reviews,
            "rating": rating,
        })

    return enriched


# ─── CSV OUTPUT ────────────────────────────────────────────────────────────────

def save_csv(products: list[dict], keyword: str) -> Path:
    """Save enriched product list as CSV in the format expected by h10_quick_stats.py."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    filename = f"H10-{slug(keyword)}.csv"
    filepath = OUTPUT_DIR / filename

    fieldnames = [
        "ASIN", "Title", "Price", "Monthly Revenue",
        "BSR", "Reviews", "Rating", "FBA", "Rank", "Sponsored"
    ]

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for p in products:
            writer.writerow({
                "ASIN":            p.get("asin", ""),
                "Title":           p.get("title", ""),
                "Price":           f"${p['price']:.2f}" if p.get("price") else "",
                "Monthly Revenue": f"${p['monthly_revenue']:,.0f}" if p.get("monthly_revenue") else "",
                "BSR":             p.get("bsr", ""),
                "Reviews":         p.get("reviews", ""),
                "Rating":          p.get("rating", ""),
                "FBA":             "FBA",          # Default — most Amazon listings are FBA
                "Rank":            p.get("rank", ""),
                "Sponsored":       "Yes" if p.get("sponsored") else "No",
            })

    return filepath


# ─── PASS / FAIL ASSESSMENT ───────────────────────────────────────────────────

REVENUE_FLOOR   = 200_000  # Minimum total page 1 revenue/month (LegacyX H10 criteria)
REVIEW_CEILING  = 500      # Maximum avg reviews before market is "closed" (LegacyX H10 criteria)

def assess_keyword(products: list[dict]) -> Tuple[str, str]:
    """
    Quick pass/fail check against the FBA scoring framework thresholds.
    Returns (verdict, reason) where verdict is 'PASS', 'POTENTIAL', or 'FAIL'.

    POTENTIAL criteria (near-miss — added to 🟡 Potential Niches section):
      - Revenue >= $40k AND avg reviews <= 1,500
      - OR revenue >= $50k AND avg reviews <= 2,000
    """
    with_revenue = [p for p in products if p.get("monthly_revenue")]
    with_reviews = [p for p in products if p.get("reviews")]

    total_revenue = sum(p["monthly_revenue"] for p in with_revenue)
    avg_reviews   = sum(p["reviews"] for p in with_reviews) / len(with_reviews) if with_reviews else 0
    prices        = [p["price"] for p in products if p.get("price")]
    avg_price     = sum(prices) / len(prices) if prices else 0

    reasons = []

    if total_revenue < REVENUE_FLOOR:
        reasons.append(f"Revenue too small (${total_revenue:,.0f}/mo < ${REVENUE_FLOOR:,} floor)")

    if avg_reviews > REVIEW_CEILING:
        reasons.append(f"Closed market ({avg_reviews:,.0f} avg reviews > {REVIEW_CEILING:,} ceiling)")

    if avg_price > 0 and not (20 <= avg_price <= 60):
        reasons.append(f"Price outside sweet spot (avg ${avg_price:.0f})")

    if not reasons:
        return "PASS", f"${total_revenue:,.0f}/mo revenue, {avg_reviews:,.0f} avg reviews, avg ${avg_price:.0f}"

    # Check for POTENTIAL (near-miss) — close on both dimensions
    is_potential = (
        (total_revenue >= 150_000 and avg_reviews <= 750) or
        (total_revenue >= 200_000 and avg_reviews <= 1_000)
    )
    if is_potential:
        rev_pct  = total_revenue / REVENUE_FLOOR * 100
        rev_pct_ceil = avg_reviews / REVIEW_CEILING * 100
        return "POTENTIAL", f"Near-miss — ${total_revenue:,.0f}/mo ({rev_pct:.0f}% of floor), {avg_reviews:,.0f} avg reviews ({rev_pct_ceil:.0f}% of ceiling)"

    return "FAIL", " | ".join(reasons)


# ─── QUEUE MANAGEMENT ──────────────────────────────────────────────────────────

def read_queue() -> list[str]:
    """Read pending keywords from queue file."""
    if not QUEUE_FILE.exists():
        return []
    keywords = []
    with open(QUEUE_FILE) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                keywords.append(line)
    return keywords


def update_queue_with_result(keyword: str, products: list[dict], verdict: str, reason: str):
    """
    Remove keyword from the active QUEUE section and either:
      - FAIL → append to the FAILED PRODUCTS section with stats
      - PASS → remove cleanly (Green Light — Dave will handle next steps)
    """
    if not QUEUE_FILE.exists():
        return

    lines = QUEUE_FILE.read_text().splitlines()

    # Remove the keyword line from the queue
    new_lines = [line for line in lines if line.strip() != keyword]

    if verdict in ("FAIL", "POTENTIAL"):
        with_revenue = [p for p in products if p.get("monthly_revenue")]
        with_reviews = [p for p in products if p.get("reviews")]
        total_rev   = sum(p["monthly_revenue"] for p in with_revenue)
        avg_rev_str = f"${total_rev:,.0f}/mo"
        avg_reviews = (sum(p["reviews"] for p in with_reviews) / len(with_reviews)) if with_reviews else 0
        rev_str     = f"{avg_reviews:,.0f} avg reviews" if avg_reviews else "— avg reviews"
        prefix      = "# POTENTIAL" if verdict == "POTENTIAL" else "# FAIL"
        fail_line   = f"{prefix} | {keyword:<28} | {avg_rev_str:>12} | {rev_str:<22} | {reason.split(' | ')[0]}"

        # Find insertion point after FAILED PRODUCTS header
        insert_at = len(new_lines)
        for i, line in enumerate(new_lines):
            if "─── FAILED PRODUCTS" in line or line.startswith("# FAIL |") or line.startswith("# POTENTIAL |") or line.startswith("# Auto-populated"):
                insert_at = i + 1

        new_lines.insert(insert_at, fail_line)
        QUEUE_FILE.write_text("\n".join(new_lines) + "\n")
        tag = "🟡 POTENTIAL" if verdict == "POTENTIAL" else "FAILED PRODUCTS"
        print(f"  → Moved to {tag}: {fail_line.strip()}")

    else:
        # Green Light — just remove from queue, don't add to failed
        QUEUE_FILE.write_text("\n".join(new_lines) + "\n")
        print(f"  → ✅ GREEN LIGHT: {keyword} — removed from queue")


# ─── OBSIDIAN TRACKER ──────────────────────────────────────────────────────────

def update_obsidian_tracker(keyword: str, products: list[dict], verdict: str, reason: str):
    """
    Auto-update the Obsidian Niche Research Tracker note after each scrape.

    Updates three sections:
      1. Summary table          — adds a new row with key stats + verdict
      2. ✅ Green Lights / ❌ Failed Niches — adds a full detail block
      3. Research Log           — appends to today's row or creates a new one
    """
    if not TRACKER_FILE.exists():
        print(f"  WARNING: Tracker file not found at {TRACKER_FILE} — skipping vault update.")
        return

    # ── Compute stats ──────────────────────────────────────────────────────────
    with_revenue = [p for p in products if p.get("monthly_revenue")]
    with_reviews = [p for p in products if p.get("reviews")]
    prices       = [p["price"] for p in products if p.get("price")]

    total_rev   = sum(p["monthly_revenue"] for p in with_revenue)
    avg_reviews = int(sum(p["reviews"] for p in with_reviews) / len(with_reviews)) if with_reviews else 0
    avg_price   = sum(prices) / len(prices) if prices else 0
    today       = datetime.now().strftime("%Y-%m-%d")
    csv_name    = f"H10-{slug(keyword)}.csv"

    rev_str       = f"${total_rev:,.0f}" if with_revenue else "—"
    rev_mo_str    = f"${total_rev:,.0f}/mo" if with_revenue else "—"
    avg_rev_str   = f"{avg_reviews:,}" if with_reviews else "—"
    avg_price_str = f"${avg_price:.2f}" if prices else "—"
    short_reason  = reason.split(" | ")[0]  # First failure reason only

    verdict_cell  = "✅ PASS" if verdict == "PASS" else ("🟡 POTENTIAL" if verdict == "POTENTIAL" else "❌ FAIL")
    verdict_emoji = "✅" if verdict == "PASS" else ("🟡" if verdict == "POTENTIAL" else "❌")

    rev_flag     = ("✅ passes revenue floor" if total_rev >= REVENUE_FLOOR
                    else "❌ below $50k floor")
    reviews_flag = (f"❌ closed market (>{REVIEW_CEILING:,} ceiling)"
                    if avg_reviews > REVIEW_CEILING
                    else f"✅ under {REVIEW_CEILING:,} ceiling")
    price_flag   = ("✅ in sweet spot" if prices and 20 <= avg_price <= 60
                    else ("❌ outside $20–$60 sweet spot" if prices else "—"))

    # ── Content blocks ─────────────────────────────────────────────────────────
    summary_row = (
        f"| {keyword} | {today} | {rev_str} | {avg_rev_str} "
        f"| {avg_price_str} | {verdict_cell} | {short_reason} |"
    )

    detail_lines = [
        "",
        f"### {keyword}",
        f"- **Date:** {today}",
        f"- **Revenue:** {rev_mo_str} total page 1 {rev_flag}",
        f"- **Avg reviews:** {avg_rev_str} {reviews_flag}",
        f"- **Avg price:** {avg_price_str} {price_flag}",
        f"- **Verdict:** {'PASS' if verdict == 'PASS' else 'FAIL'} — {reason}",
        f"- **CSV:** `raw/sources/{csv_name}`",
        "",
    ]

    log_row = f"| {today} | {keyword} | {verdict_emoji} {verdict} — {short_reason} |"

    # ── Read ───────────────────────────────────────────────────────────────────
    lines = TRACKER_FILE.read_text().splitlines()

    # Pass 0 — update frontmatter date
    lines = [f"updated: {today}" if l.startswith("updated:") else l for l in lines]

    # Pass 1 — append to Summary table (after last data row)
    new_lines  = []
    in_summary = False
    done       = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if "## Summary" in line:
            in_summary = True
        if in_summary and not done:
            is_data_row = line.startswith("|") and not line.startswith("|---")
            next_is_row = (i + 1 < len(lines)) and lines[i + 1].startswith("|")
            if is_data_row and not next_is_row:
                new_lines.append(line)
                new_lines.append(summary_row)
                done = True
                i += 1
                continue
        new_lines.append(line)
        i += 1
    lines = new_lines

    # Pass 2 — insert detail block into the correct section
    if verdict == "PASS":
        # Replace *None yet* placeholder if present
        new_lines = []
        replaced  = False
        for line in lines:
            if not replaced and "*None yet" in line:
                new_lines.extend(detail_lines)
                replaced = True
            else:
                new_lines.append(line)
        if not replaced:
            # Placeholder gone — append at end of Green Lights section (before ---)
            new_lines  = []
            in_gl      = False
            inserted   = False
            for line in lines:
                if "## ✅ Green Lights" in line:
                    in_gl = True
                if in_gl and not inserted and (line.strip() == "---" or
                        (line.startswith("## ") and "Green Lights" not in line)):
                    new_lines.extend(detail_lines)
                    inserted = True
                new_lines.append(line)
        lines = new_lines
    elif verdict == "POTENTIAL":
        # Append a row to the 🟡 Potential Niches table
        rev_pct     = total_rev / REVENUE_FLOOR * 100
        rev_pct_ceil = avg_reviews / REVIEW_CEILING * 100
        potential_row = (
            f"| 🔥 {keyword} | ${total_rev:,.0f} | {int(avg_reviews):,} "
            f"| {rev_pct:.1f}% | {rev_pct_ceil:.1f}% | Near-miss — investigate sub-niches |"
        )
        new_lines  = []
        in_pot     = False
        inserted   = False
        i = 0
        while i < len(lines):
            line = lines[i]
            if "## 🟡 Potential Niches" in line:
                in_pot = True
            if in_pot and not inserted:
                is_data_row  = line.startswith("|") and not line.startswith("|---")
                next_is_row  = (i + 1 < len(lines)) and lines[i + 1].startswith("|")
                if is_data_row and not next_is_row:
                    new_lines.append(line)
                    new_lines.append(potential_row)
                    inserted = True
                    i += 1
                    continue
            new_lines.append(line)
            i += 1
        lines = new_lines
    else:
        # Append to Failed Niches section — right before ## Research Log
        new_lines  = []
        in_failed  = False
        inserted   = False
        i = 0
        while i < len(lines):
            line = lines[i]
            if "## ❌ Failed Niches" in line:
                in_failed = True
            if in_failed and not inserted and "## Research Log" in line:
                new_lines.extend(detail_lines)
                new_lines.append("---")
                new_lines.append("")
                inserted = True
            new_lines.append(line)
            i += 1
        if in_failed and not inserted:
            new_lines.extend(detail_lines)
        lines = new_lines

    # Pass 3 — update Research Log (append to today's row or add new row)
    new_lines   = []
    in_log      = False
    log_updated = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if "## Research Log" in line:
            in_log = True
        if in_log and not log_updated:
            # Append to existing row for today
            if f"| {today} |" in line and not line.startswith("|---"):
                segs = line.split("|")           # ['', ' date ', ' kws ', ' results ', '']
                if len(segs) >= 5:
                    segs[2] = f" {segs[2].strip()}, {keyword} "
                    segs[3] = f" {segs[3].strip()}, {verdict_emoji} {verdict} "
                    new_lines.append("|".join(segs))
                    log_updated = True
                    i += 1
                    continue
            # Append new row after last table row
            is_data_row = line.startswith("|") and not line.startswith("|---")
            next_is_row = (i + 1 < len(lines)) and lines[i + 1].startswith("|")
            if is_data_row and not next_is_row:
                new_lines.append(line)
                new_lines.append(log_row)
                log_updated = True
                i += 1
                continue
        new_lines.append(line)
        i += 1
    if not log_updated:
        new_lines.append(log_row)
    lines = new_lines

    # ── Write back ─────────────────────────────────────────────────────────────
    TRACKER_FILE.write_text("\n".join(lines) + "\n")
    print(f"  → Obsidian tracker updated: {TRACKER_FILE.name}")


# ─── HELPERS ───────────────────────────────────────────────────────────────────

def slug(keyword: str) -> str:
    """Convert keyword to URL-safe filename slug."""
    return re.sub(r"[^a-z0-9]+", "-", keyword.lower()).strip("-")


def print_summary(products: list[dict], keyword: str, filepath: Path):
    """Print a quick summary table of results."""
    print(f"\n{'─'*60}")
    print(f"  {keyword.upper()}")
    print(f"{'─'*60}")
    print(f"  {'#':<3} {'Revenue':>12} {'BSR':>8} {'Reviews':>10}  Title")
    print(f"  {'─'*56}")

    total_revenue = 0
    for i, p in enumerate(products, 1):
        rev = p.get("monthly_revenue")
        bsr = p.get("bsr")
        reviews = p.get("reviews")
        title = (p.get("title") or p.get("asin", ""))[:45]

        rev_str  = f"${rev:,.0f}" if rev else "N/A"
        bsr_str  = f"#{bsr:,}" if bsr else "N/A"
        rev_str_r= f"{rev_str:>12}"
        bsr_str_r= f"{bsr_str:>8}"
        rev_num = f"{reviews:,}" if reviews else "N/A"
        print(f"  {i:<3} {rev_str_r} {bsr_str_r} {rev_num:>10}  {title}")
        if rev:
            total_revenue += rev

    print(f"{'─'*60}")
    print(f"  Total estimated monthly revenue: ${total_revenue:,.0f}")
    print(f"  Saved: {filepath}")
    print()


# ─── MAIN ──────────────────────────────────────────────────────────────────────

def scrape_keyword(keyword: str, session: dict, top_n: int = 10, auto_update_queue: bool = True) -> Optional[Path]:
    """Full pipeline: Amazon search → H10 enrichment → CSV save → pass/fail assessment."""
    print(f"\n{'='*60}")
    print(f"  Scraping: {keyword}")
    print(f"{'='*60}")

    bearer, account_id = get_bearer_token(session)
    h10_cookies = get_h10_cookies(session)

    # 1. Amazon search → ASINs + basic product data
    products = search_amazon(keyword, session, top_n=top_n)
    if not products:
        print(f"  ❌ No products found for '{keyword}' — skipping")
        return None

    # 2. H10 API enrichment → revenue, BSR, reviews
    print(f"\n  Enriching {len(products)} products with H10 data...")
    enriched = enrich_with_h10(products, bearer, h10_cookies, account_id)

    # 3. Save CSV
    filepath = save_csv(enriched, keyword)

    # 4. Print summary
    print_summary(enriched, keyword, filepath)

    # 5. Pass/fail assessment → auto-update queue file
    verdict, reason = assess_keyword(enriched)
    if verdict == "FAIL":
        print(f"  ❌ VERDICT: FAIL — {reason}")
    elif verdict == "POTENTIAL":
        print(f"  🟡 VERDICT: POTENTIAL — {reason}")
    else:
        print(f"  ✅ VERDICT: PASS — {reason}")

    if auto_update_queue:
        update_queue_with_result(keyword, enriched, verdict, reason)
        update_obsidian_tracker(keyword, enriched, verdict, reason)

    return filepath


def main():
    parser = argparse.ArgumentParser(
        description="H10 Scraper — Automated Helium 10 data collection",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--login",         action="store_true", help="Re-capture H10 session from Chrome")
    parser.add_argument("--check-session", action="store_true", help="Verify saved session is valid")
    parser.add_argument("--keyword",       type=str,            help="Scrape a single keyword (skip queue)")
    parser.add_argument("--top",           type=int, default=10, help="Number of top products (default: 10)")
    parser.add_argument("--no-clear",      action="store_true", help="Don't update queue file after scraping")
    args = parser.parse_args()

    if args.login:
        do_login()
        return

    if args.check_session:
        valid = check_session()
        sys.exit(0 if valid else 1)

    # Load session (required for all other operations)
    session = load_session()

    # Verify session quickly
    bearer, account_id = get_bearer_token(session)
    print(f"Session loaded — account ID: {account_id}")

    auto_update = not args.no_clear

    if args.keyword:
        # Single keyword mode — queue update only applies if keyword is actually in queue
        filepath = scrape_keyword(args.keyword, session, top_n=args.top, auto_update_queue=auto_update)
        if not filepath:
            sys.exit(1)
        return

    # Queue mode
    keywords = read_queue()
    if not keywords:
        print("Queue is empty. Add keywords to raw/h10-queue.txt and try again.")
        return

    print(f"Queue: {len(keywords)} keyword(s) to process")

    scraped_ok = []
    scrape_failed = []

    for keyword in keywords:
        filepath = scrape_keyword(keyword, session, top_n=args.top, auto_update_queue=auto_update)
        if filepath:
            scraped_ok.append(keyword)
        else:
            scrape_failed.append(keyword)

    print(f"\n{'='*60}")
    print(f"  Done — {len(scraped_ok)} scraped, {len(scrape_failed)} errored")
    if scraped_ok:
        print(f"  ✅ {', '.join(scraped_ok)}")
    if scrape_failed:
        print(f"  ❌ Scrape error (no data): {', '.join(scrape_failed)}")
    print()


if __name__ == "__main__":
    main()
