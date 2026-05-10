#!/usr/bin/env python3
"""
H10 Quick Stats — Instant market summary from a Helium 10 Xray CSV export.

Parses an H10 Xray CSV and outputs the key numbers for the FBA scoring framework:
- Total page 1 revenue
- Top 10 avg revenue, price, reviews, rating
- Revenue distribution (concentration / spread)
- Review moat classification
- FBA penetration
- Pass/investigate flags

Usage:
    python3 h10_quick_stats.py raw/sources/H10-cable-management-box.csv
    python3 h10_quick_stats.py raw/sources/H10-cable-management-box.csv --top 15
    python3 h10_quick_stats.py raw/sources/H10-*.csv  (multiple files)
    python3 h10_quick_stats.py --help
"""

import argparse
import csv
import sys
import os
from pathlib import Path
from typing import List, Optional
import statistics


def colour(text: str, code: str) -> str:
    codes = {
        "green": "\033[92m", "red": "\033[91m", "yellow": "\033[93m",
        "blue": "\033[94m", "bold": "\033[1m", "dim": "\033[2m", "reset": "\033[0m"
    }
    return f"{codes.get(code, '')}{text}{codes['reset']}"


def find_column(headers: List[str], candidates: List[str]) -> Optional[int]:
    """Find a column index by trying multiple possible header names."""
    headers_lower = [h.lower().strip() for h in headers]
    for candidate in candidates:
        c = candidate.lower().strip()
        if c in headers_lower:
            return headers_lower.index(c)
        # Partial match
        for i, h in enumerate(headers_lower):
            if c in h or h in c:
                return i
    return None


def parse_number(val: str) -> Optional[float]:
    """Parse a number string, handling $, commas, K, M suffixes."""
    if not val or val.strip() in ("", "-", "N/A", "n/a", "—"):
        return None
    v = val.strip().replace(",", "").replace("$", "").replace("%", "")
    multiplier = 1.0
    if v.endswith("K") or v.endswith("k"):
        multiplier = 1_000
        v = v[:-1]
    elif v.endswith("M") or v.endswith("m"):
        multiplier = 1_000_000
        v = v[:-1]
    try:
        return float(v) * multiplier
    except ValueError:
        return None


def review_moat_label(avg_reviews: float) -> str:
    if avg_reviews < 200:
        return colour("✅ Easy entry (<200 avg)", "green")
    elif avg_reviews < 500:
        return colour("🟡 Manageable (200–500 avg)", "yellow")
    elif avg_reviews < 1000:
        return colour("🔶 Hard (500–1000 avg)", "yellow")
    else:
        return colour("❌ Closed (1000+ avg)", "red")


def analyse_csv(filepath: str, top_n: int = 10, verbose: bool = False) -> None:
    path = Path(filepath)
    if not path.exists():
        print(colour(f"ERROR: File not found: {filepath}", "red"))
        return

    print(colour(f"\n{'='*60}", "blue"))
    print(colour(f"  H10 QUICK STATS — {path.name}", "bold"))
    print(colour(f"{'='*60}", "blue"))

    rows = []
    headers = []

    with open(filepath, newline="", encoding="utf-8-sig") as f:
        # Try to detect delimiter
        sample = f.read(2048)
        f.seek(0)
        delimiter = "," if sample.count(",") > sample.count("\t") else "\t"

        reader = csv.reader(f, delimiter=delimiter)
        headers = next(reader, [])

        if not headers:
            print(colour("ERROR: Empty or unreadable CSV", "red"))
            return

        for row in reader:
            if row:
                rows.append(row)

    if not rows:
        print(colour("ERROR: No data rows found", "red"))
        return

    print(f"\n  Total products found: {len(rows)}")
    print(f"  Columns: {', '.join(headers[:8])}{'...' if len(headers) > 8 else ''}\n")

    # Find key columns
    rev_col = find_column(headers, ["monthly revenue", "revenue", "est. revenue", "estimated revenue", "rev"])
    price_col = find_column(headers, ["price", "avg price", "current price"])
    review_col = find_column(headers, ["reviews", "review count", "num reviews", "number of reviews", "rating count"])
    rating_col = find_column(headers, ["rating", "avg rating", "star rating", "stars"])
    fba_col = find_column(headers, ["fba", "fulfillment", "fulfil", "fba/fbm"])
    title_col = find_column(headers, ["title", "product", "product name", "name", "item"])
    asin_col = find_column(headers, ["asin", "asin/isbn"])
    bsr_col = find_column(headers, ["bsr", "best seller rank", "rank"])

    # Parse all products
    products = []
    for row in rows:
        def get(col):
            if col is not None and col < len(row):
                return row[col].strip()
            return ""

        revenue = parse_number(get(rev_col))
        price = parse_number(get(price_col))
        reviews = parse_number(get(review_col))
        rating = parse_number(get(rating_col))

        products.append({
            "title": get(title_col)[:60] + "..." if len(get(title_col)) > 60 else get(title_col),
            "asin": get(asin_col),
            "revenue": revenue,
            "price": price,
            "reviews": reviews,
            "rating": rating,
            "fba": get(fba_col),
            "bsr": parse_number(get(bsr_col)),
        })

    # Sort by revenue descending (products without revenue go last)
    products.sort(key=lambda p: p["revenue"] or 0, reverse=True)

    top = products[:top_n]
    all_with_revenue = [p for p in products if p["revenue"] is not None]
    top_with_revenue = [p for p in top if p["revenue"] is not None]

    # --- TOTAL PAGE REVENUE ---
    total_revenue = sum(p["revenue"] for p in all_with_revenue)
    top_revenue = sum(p["revenue"] for p in top_with_revenue)

    print(colour("  REVENUE", "bold"))
    print(f"  Total page 1 revenue:     ${total_revenue:>10,.0f} /mo")
    print(f"  Top {top_n} revenue:            ${top_revenue:>10,.0f} /mo")

    # Revenue concentration: what % does #1 hold?
    if top_with_revenue:
        top1_rev = top_with_revenue[0]["revenue"]
        concentration = top1_rev / top_revenue * 100 if top_revenue > 0 else 0
        concentration_str = f"  #{1} player holds {concentration:.0f}% of top {top_n} revenue"
        if concentration > 50:
            print(colour(f"  ⚠️ {concentration_str} (concentrated)", "yellow"))
        else:
            print(colour(f"  ✅ {concentration_str} (spread)", "green"))

    # Pre-filter: $50k minimum
    if total_revenue < 50_000:
        print(colour(f"\n  ❌ FAILS PRE-FILTER: Total page 1 revenue ${total_revenue:,.0f} < $50,000/mo minimum", "red"))
    else:
        print(colour(f"\n  ✅ Passes revenue pre-filter (>${50_000:,}/mo)", "green"))

    # --- AVG REVENUE TOP N ---
    revenues = [p["revenue"] for p in top_with_revenue]
    if revenues:
        avg_revenue = statistics.mean(revenues)
        median_revenue = statistics.median(revenues)
        print(f"\n  Avg revenue (top {len(revenues)}):    ${avg_revenue:>10,.0f} /mo")
        print(f"  Median revenue (top {len(revenues)}):  ${median_revenue:>10,.0f} /mo")

    # --- PRICE ---
    prices = [p["price"] for p in top if p["price"] is not None]
    if prices:
        print(colour("\n  PRICING", "bold"))
        print(f"  Price range (top {top_n}):    ${min(prices):.2f} – ${max(prices):.2f}")
        print(f"  Avg price:                 ${statistics.mean(prices):.2f}")
        # Check $20-60 sweet spot
        in_range = [p for p in prices if 20 <= p <= 60]
        if len(in_range) >= len(prices) * 0.7:
            print(colour("  ✅ Market clusters in $20–$60 sweet spot", "green"))
        else:
            low = len([p for p in prices if p < 20])
            high = len([p for p in prices if p > 60])
            if high > len(prices) * 0.3:
                print(colour("  ⚠️  Many products >$60 — premium market, harder to enter cheap", "yellow"))
            if low > len(prices) * 0.3:
                print(colour("  ⚠️  Many products <$20 — thin margin territory", "yellow"))

    # --- REVIEWS (the critical one) ---
    reviews_data = [p["reviews"] for p in top if p["reviews"] is not None]
    if not reviews_data:
        print(colour("\n  ⚠️  REVIEWS: No review data found in CSV!", "yellow"))
        print("  Re-export from H10 with the Reviews column visible.")
        print("  This is the most critical column for the Competition Gap score.")
    else:
        avg_reviews = statistics.mean(reviews_data)
        median_reviews = statistics.median(reviews_data)
        print(colour("\n  COMPETITION (REVIEWS)", "bold"))
        print(f"  Avg reviews (top {len(reviews_data)}):    {avg_reviews:>8,.0f}")
        print(f"  Median reviews:            {median_reviews:>8,.0f}")
        print(f"  Range:                     {min(reviews_data):,.0f} – {max(reviews_data):,.0f}")
        print(f"  Review moat:               {review_moat_label(avg_reviews)}")

        # Count how many have <200 reviews (easy entry targets)
        easy = len([r for r in reviews_data if r < 200])
        if easy > 0:
            print(colour(f"  ✅ {easy}/{len(reviews_data)} top products have <200 reviews — beatable", "green"))

    # --- FBA PENETRATION ---
    fba_data = [p["fba"] for p in top if p["fba"]]
    if fba_data:
        fba_count = len([f for f in fba_data if "fba" in f.lower() and "fbm" not in f.lower()])
        fba_pct = fba_count / len(fba_data) * 100
        print(colour("\n  FBA PENETRATION", "bold"))
        print(f"  FBA: {fba_count}/{len(fba_data)} ({fba_pct:.0f}%)")
        if fba_pct >= 70:
            print(colour("  ✅ Market is FBA-dominant (good — level playing field)", "green"))
        else:
            print(colour("  ⚠️  Many FBM sellers — may have logistics advantages", "yellow"))

    # --- TOP 10 TABLE ---
    if verbose or True:
        print(colour(f"\n  TOP {min(top_n, len(top))} PRODUCTS", "bold"))
        print("  " + "-" * 56)
        header_row = f"  {'#':<3} {'Revenue':>10} {'Price':>7} {'Reviews':>8} {'Title'}"
        print(colour(header_row, "dim"))
        for i, p in enumerate(top[:top_n], 1):
            rev_str = f"${p['revenue']:,.0f}" if p['revenue'] else "N/A"
            price_str = f"${p['price']:.2f}" if p['price'] else "N/A"
            review_str = f"{p['reviews']:,.0f}" if p['reviews'] else colour("MISSING", "red")
            title = p['title'] or p['asin'] or "Unknown"
            row = f"  {i:<3} {rev_str:>10} {price_str:>7} {review_str:>8}  {title}"
            if p['reviews'] and p['reviews'] < 200:
                print(colour(row, "green"))
            elif p['reviews'] and p['reviews'] > 500:
                print(colour(row, "dim"))
            else:
                print(row)

    # --- QUICK VERDICT ---
    print(colour(f"\n  QUICK VERDICT", "bold"))
    flags = []
    green = []

    if total_revenue < 50_000:
        flags.append("❌ Revenue too low (<$50k/mo total page 1)")
    else:
        green.append(f"✅ Revenue: ${total_revenue:,.0f}/mo")

    if reviews_data:
        if avg_reviews > 1000:
            flags.append("❌ Review moat: 1000+ avg (closed market)")
        elif avg_reviews > 500:
            flags.append("🔶 Review moat: 500–1000 avg (very competitive)")
        elif avg_reviews > 200:
            flags.append("🟡 Review moat: 200–500 avg (manageable)")
        else:
            green.append(f"✅ Review moat: <200 avg (easy entry)")
    else:
        flags.append("⚠️  Missing review data — cannot score Competition Gap")

    if prices and not (20 <= statistics.mean(prices) <= 60):
        flags.append("⚠️  Price point outside $20–$60 sweet spot")
    elif prices:
        green.append(f"✅ Price: avg ${statistics.mean(prices):.2f}")

    for g in green:
        print(f"  {g}")
    for f in flags:
        print(f"  {f}")

    if not flags or (len(flags) == 1 and "review data" in flags[0]):
        print(colour("\n  → Worth running through full niche-decision scoring", "green"))
    elif any("❌" in f for f in flags):
        print(colour("\n  → Likely a PASS. Confirm with full scoring framework.", "red"))
    else:
        print(colour("\n  → Needs investigation. Check missing data and run full scoring.", "yellow"))

    print()


def main():
    parser = argparse.ArgumentParser(
        description="Quick H10 Xray CSV stats for FBA niche pre-screening.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 h10_quick_stats.py raw/sources/H10-cable-management-box.csv
  python3 h10_quick_stats.py raw/sources/H10-*.csv
  python3 h10_quick_stats.py raw/sources/H10-cable-management-box.csv --top 15

Drop H10 Xray CSVs in raw/sources/ with filename format: H10-[keyword-slug].csv
Make sure the Reviews column is visible in H10 Xray before exporting.
        """
    )
    parser.add_argument("files", nargs="+", help="One or more H10 Xray CSV files to analyse")
    parser.add_argument("--top", type=int, default=10, help="Number of top products to analyse (default: 10)")
    args = parser.parse_args()

    for filepath in args.files:
        analyse_csv(filepath, top_n=args.top)


if __name__ == "__main__":
    main()
