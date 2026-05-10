#!/usr/bin/env python3
"""
Amazon Listing Scraper
Extracts title, bullets, price, reviews, images, and Q&A from Amazon product pages.

Usage:
    python3 scrape_listing.py --asins B0XXXXXX B0YYYYYY
    python3 scrape_listing.py --asins B0XXXXXX --marketplace com.au --output /tmp/out.json
    python3 scrape_listing.py --help
"""

import argparse
import json
import time
import sys
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
except ImportError:
    print("ERROR: Playwright not installed. Run: pip3 install playwright && python3 -m playwright install chromium")
    sys.exit(1)


def scrape_asin(page, asin: str, marketplace: str = "com.au") -> dict:
    """Scrape a single Amazon product listing."""
    url = f"https://www.amazon.{marketplace}/dp/{asin}"
    result = {
        "asin": asin,
        "url": url,
        "marketplace": marketplace,
        "error": None,
        "title": None,
        "price": None,
        "rating": None,
        "review_count": None,
        "bullets": [],
        "images": [],
        "has_a_plus": False,
        "qa_questions": [],
        "brand": None,
        "date_first_available": None,
    }

    try:
        print(f"  Fetching {url} ...", end="", flush=True)
        page.goto(url, wait_until="domcontentloaded", timeout=30000)
        page.wait_for_load_state("networkidle", timeout=15000)

        # Check for CAPTCHA / bot detection
        if "Type the characters" in page.content() or "Enter the characters" in page.content():
            result["error"] = "CAPTCHA detected — Amazon blocked scraping. Use manual fallback."
            print(" CAPTCHA")
            return result

        # Check for "page not found"
        if "unavailable" in page.title().lower() or "page not found" in page.content().lower():
            result["error"] = "Product page unavailable or ASIN not found"
            print(" not found")
            return result

        print(" loaded", flush=True)

        # --- Title ---
        title_el = page.query_selector("#productTitle")
        if title_el:
            result["title"] = title_el.inner_text().strip()

        # --- Price ---
        price_el = (
            page.query_selector(".a-price .a-offscreen") or
            page.query_selector("#priceblock_ourprice") or
            page.query_selector("#priceblock_dealprice") or
            page.query_selector(".priceToPay .a-offscreen")
        )
        if price_el:
            result["price"] = price_el.inner_text().strip()

        # --- Rating & Review Count ---
        rating_el = page.query_selector("#acrPopover")
        if rating_el:
            result["rating"] = rating_el.get_attribute("title")

        review_el = page.query_selector("#acrCustomerReviewText")
        if review_el:
            result["review_count"] = review_el.inner_text().strip()

        # --- Brand ---
        brand_el = (
            page.query_selector("#bylineInfo") or
            page.query_selector(".po-brand td:last-child") or
            page.query_selector("a#bylineInfo")
        )
        if brand_el:
            result["brand"] = brand_el.inner_text().strip().replace("Brand: ", "").replace("Visit the ", "").strip()

        # --- Bullet Points ---
        bullets_el = page.query_selector_all("#feature-bullets ul li span.a-list-item")
        result["bullets"] = [b.inner_text().strip() for b in bullets_el if b.inner_text().strip()]

        # --- Images (main image gallery) ---
        img_els = page.query_selector_all("#altImages img, #imageBlock img")
        seen_srcs = set()
        for img in img_els:
            src = img.get_attribute("src") or ""
            # Filter out tiny thumbnails and icon images
            if src and "sprite" not in src and src not in seen_srcs and len(src) > 20:
                # Convert thumbnail URLs to full-size
                full_src = src.replace("._SS40_", "._SL500_").replace("._AC_US40_", "._AC_SL500_")
                seen_srcs.add(src)
                result["images"].append(full_src)
        result["images"] = result["images"][:10]  # Cap at 10

        # --- A+ Content ---
        aplus_el = page.query_selector("#aplus, #aplus3p_feature_div, .aplus-module")
        result["has_a_plus"] = aplus_el is not None

        # --- Date First Available (from product details) ---
        details_rows = page.query_selector_all("table.a-keyvalue tr, #detailBullets_feature_div li")
        for row in details_rows:
            text = row.inner_text().strip()
            if "Date First Available" in text or "first available" in text.lower():
                parts = text.split(":")
                if len(parts) >= 2:
                    result["date_first_available"] = parts[-1].strip()
                break

        # --- Q&A (first 5 questions) ---
        try:
            qa_section = page.query_selector("#ask_feature_div, #askATFLink")
            if qa_section:
                qa_els = page.query_selector_all(".a-fixed-right-grid-inner .a-col-left span")
                result["qa_questions"] = [q.inner_text().strip() for q in qa_els[:5] if q.inner_text().strip()]
        except Exception:
            pass  # Q&A is optional

        # Small delay between requests to be polite
        time.sleep(2)

    except PlaywrightTimeout:
        result["error"] = "Timeout loading page — Amazon may be slow or blocking"
    except Exception as e:
        result["error"] = f"Unexpected error: {str(e)}"

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Scrape Amazon product listings for FBA competitive analysis.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 scrape_listing.py --asins B0XXXXXX B0YYYYYY
  python3 scrape_listing.py --asins B0XXXXXX --marketplace com
  python3 scrape_listing.py --asins B0XXXXXX --output /tmp/listing.json

Notes:
  - Amazon actively blocks scraping. If you see CAPTCHA errors, use manual fallback.
  - Runs on amazon.com.au by default. Use --marketplace com for US Amazon.
  - Output is JSON — paste into analysis session or save to raw/sources/.
        """
    )
    parser.add_argument("--asins", nargs="+", required=True, help="One or more ASINs to scrape (e.g. B0XXXXXX)")
    parser.add_argument("--marketplace", default="com.au", help="Amazon marketplace TLD (default: com.au, alternatives: com, co.uk, de)")
    parser.add_argument("--output", default=None, help="Output JSON file path (default: print to stdout)")
    parser.add_argument("--headed", action="store_true", help="Run browser in headed mode (helps avoid bot detection)")
    args = parser.parse_args()

    print(f"Amazon Listing Scraper — {len(args.asins)} ASIN(s) on amazon.{args.marketplace}")
    print(f"Mode: {'headed' if args.headed else 'headless'}")
    print("-" * 50)

    results = []

    with sync_playwright() as p:
        # Use headed mode if requested (better for avoiding bot detection)
        browser = p.chromium.launch(headless=not args.headed)

        # Set a realistic user agent
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800},
            locale="en-AU",
        )
        page = context.new_page()

        for i, asin in enumerate(args.asins):
            print(f"\n[{i+1}/{len(args.asins)}] ASIN: {asin}")
            result = scrape_asin(page, asin.strip(), args.marketplace)
            results.append(result)

            if result.get("error") and "CAPTCHA" in result["error"]:
                print("\n⚠️  CAPTCHA detected. Amazon is blocking scraping.")
                print("   Fallback: open each listing manually and paste the text into Claude.")
                print("   Use URL:", f"https://www.amazon.{args.marketplace}/dp/{asin}")
                # Still try remaining ASINs in case it was a one-off
                time.sleep(5)

        browser.close()

    # Format output
    print("\n" + "=" * 50)
    print("RESULTS SUMMARY")
    print("=" * 50)
    for r in results:
        status = "✅" if not r.get("error") else "❌"
        title_preview = (r["title"] or "")[:70] + "..." if (r["title"] or "") and len(r["title"]) > 70 else (r["title"] or "—")
        print(f"\n{status} {r['asin']}")
        print(f"   Title: {title_preview}")
        print(f"   Price: {r['price'] or '—'} | Rating: {r['rating'] or '—'} | Reviews: {r['review_count'] or '—'}")
        print(f"   Bullets: {len(r['bullets'])} | Images: {len(r['images'])} | A+: {'Yes' if r['has_a_plus'] else 'No'}")
        if r.get("error"):
            print(f"   Error: {r['error']}")

    # Save or print JSON
    output_json = json.dumps(results, indent=2, ensure_ascii=False)
    if args.output:
        Path(args.output).write_text(output_json)
        print(f"\n📄 Full JSON saved to: {args.output}")
    else:
        print("\n--- FULL JSON ---")
        print(output_json)


if __name__ == "__main__":
    main()
