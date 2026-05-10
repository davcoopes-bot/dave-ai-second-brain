#!/usr/bin/env python3
"""
Portfolio Snapshot — Dave's AI Brain
Fetches live prices and calculates P&L for all holdings.

Usage:
    python3 portfolio_snapshot.py           # Full snapshot
    python3 portfolio_snapshot.py --watch   # Refresh every 60s (Ctrl+C to stop)
    python3 portfolio_snapshot.py --help

Update your positions below in POSITIONS when trades change.
"""

import argparse
import time
import sys
from datetime import datetime
from typing import Optional

try:
    import yfinance as yf
except ImportError:
    print("ERROR: yfinance not installed. Run: pip3 install yfinance")
    sys.exit(1)

# =============================================================================
# DAVE'S POSITIONS — UPDATE THESE WHEN YOU TRADE
# Format: "TICKER": {"units": X, "avg_buy": X.XX, "currency": "AUD"/"USD", "action": "...", "note": "..."}
# =============================================================================

POSITIONS = {
    # --- ASX ETFs ---
    "VTS.AX":  {"units": 8,       "avg_buy": 332.65, "currency": "AUD", "action": "Hold + add",  "note": "Broad US market anchor"},
    "AINF.AX": {"units": 210,     "avg_buy": 18.03,  "currency": "AUD", "action": "Hold",         "note": "AI infrastructure ETF"},
    "SEMI.AX": {"units": 52,      "avg_buy": 33.67,  "currency": "AUD", "action": "Hold + add",  "note": "Semiconductor ETF"},
    "NDQ.AX":  {"units": 30,      "avg_buy": 51.38,  "currency": "AUD", "action": "Hold + add",  "note": "Nasdaq 100 ETF"},
    "FANG.AX": {"units": 46,      "avg_buy": 33.53,  "currency": "AUD", "action": "Hold",         "note": "FANG+ ETF"},
    "VVLU.AX": {"units": 9,       "avg_buy": 62.20,  "currency": "AUD", "action": "Hold",         "note": "Global Value ETF"},

    # --- ASX Individual Stocks ---
    "EXR.AX":  {"units": 20_000,  "avg_buy": 0.201,  "currency": "AUD", "action": "⏳ HOLD — await Diona-1 flow test", "note": "Binary catalyst: positive=hold, disappointing=SELL"},
    "ERA.AX":  {"units": 1_600,   "avg_buy": 0.297,  "currency": "AUD", "action": "❌ SELL",      "note": "Thesis gone. -98.82%. Execute sell."},
    "FTI.AX":  {"units": 47,      "avg_buy": None,   "currency": "AUD", "action": "Hold / ignore","note": "Free allocation from listing change"},
    "RIL.AX":  {"units": 103_500, "avg_buy": None,   "currency": "AUD", "action": "Hold / ignore","note": "Free allocation from listing change"},

    # --- US Stocks (via Revolut) — values in USD, converted to AUD ---
    "NBIS":    {"units": None,    "avg_buy": None,   "currency": "USD", "action": "Active trade",  "note": "~$1,200 AUD. Buy/sell at 15-20% gains. No set unit count."},
    "CEG":     {"units": None,    "avg_buy": None,   "currency": "USD", "action": "Long-term hold","note": "~$1,000 AUD. Nuclear/AI power infrastructure."},
}

# Action priorities — show these at top of output
HIGH_PRIORITY = ["EXR.AX", "NBIS", "ERA.AX"]


def get_aud_usd_rate() -> float:
    """Fetch current AUD/USD exchange rate."""
    try:
        rate_data = yf.Ticker("AUDUSD=X").fast_info
        rate = getattr(rate_data, 'last_price', None)
        if rate and rate > 0:
            return rate
    except Exception:
        pass
    # Fallback to approximate
    print("⚠️  Could not fetch AUD/USD rate — using 0.64 as fallback")
    return 0.64


def get_price(ticker: str) -> Optional[float]:
    """Get current price for a ticker."""
    try:
        t = yf.Ticker(ticker)
        info = t.fast_info
        price = getattr(info, 'last_price', None)
        if price and price > 0:
            return float(price)
    except Exception:
        pass
    return None


def colour(text: str, colour_code: str) -> str:
    """Add terminal colour codes."""
    codes = {"green": "\033[92m", "red": "\033[91m", "yellow": "\033[93m",
             "blue": "\033[94m", "bold": "\033[1m", "dim": "\033[2m", "reset": "\033[0m"}
    return f"{codes.get(colour_code, '')}{text}{codes['reset']}"


def pnl_str(pnl: float, pnl_pct: float) -> str:
    """Format P&L with colour."""
    sign = "+" if pnl >= 0 else ""
    pnl_text = f"{sign}${pnl:,.0f} ({sign}{pnl_pct:.1f}%)"
    return colour(pnl_text, "green" if pnl >= 0 else "red")


def format_price(price: float, currency: str = "AUD") -> str:
    if price >= 100:
        return f"${price:,.2f}"
    elif price >= 1:
        return f"${price:.3f}"
    else:
        return f"${price:.4f}"


def snapshot():
    """Run a full portfolio snapshot."""
    print(colour(f"\n{'='*60}", "blue"))
    print(colour(f"  DAVE'S PORTFOLIO SNAPSHOT — {datetime.now().strftime('%d %b %Y, %H:%M AWST')}", "bold"))
    print(colour(f"{'='*60}", "blue"))

    # Fetch AUD/USD rate
    aud_usd = get_aud_usd_rate()
    usd_aud = 1 / aud_usd if aud_usd else 1.5625  # fallback
    print(f"\n  AUD/USD: {aud_usd:.4f}  (1 USD = {usd_aud:.4f} AUD)\n")

    # Fetch all prices
    print("  Fetching prices...", end="", flush=True)
    prices = {}
    for ticker in POSITIONS:
        price = get_price(ticker)
        prices[ticker] = price
    print(" done\n")

    total_aud = 0.0
    total_cost_aud = 0.0
    results = []

    for ticker, pos in POSITIONS.items():
        price = prices.get(ticker)
        units = pos.get("units")
        avg_buy = pos.get("avg_buy")
        currency = pos.get("currency", "AUD")
        action = pos.get("action", "—")
        note = pos.get("note", "")

        # Current value in AUD
        if price and units:
            value_local = price * units
            value_aud = value_local * usd_aud if currency == "USD" else value_local
        elif price:
            value_aud = None  # US stock with unknown units
        else:
            value_aud = None

        # P&L
        pnl = None
        pnl_pct = None
        if price and units and avg_buy:
            cost_local = avg_buy * units
            cost_aud = cost_local * usd_aud if currency == "USD" else cost_local
            pnl_aud = value_aud - cost_aud
            pnl_pct = ((price - avg_buy) / avg_buy) * 100
            total_aud += value_aud
            total_cost_aud += cost_aud
        elif value_aud:
            total_aud += value_aud

        results.append({
            "ticker": ticker,
            "price": price,
            "units": units,
            "avg_buy": avg_buy,
            "value_aud": value_aud,
            "pnl_pct": pnl_pct,
            "pnl_aud": pnl_aud if (pnl_pct is not None) else None,
            "action": action,
            "note": note,
            "currency": currency,
        })

    # --- High Priority positions first ---
    print(colour("  ⚠️  HIGH PRIORITY POSITIONS", "bold"))
    print("  " + "-" * 56)
    for r in results:
        if r["ticker"] not in HIGH_PRIORITY:
            continue
        _print_position(r, usd_aud)

    # --- ASX ETFs ---
    print(colour("\n  📊 ASX ETFs", "bold"))
    print("  " + "-" * 56)
    asx_etf_tickers = ["VTS.AX", "AINF.AX", "SEMI.AX", "NDQ.AX", "FANG.AX", "VVLU.AX"]
    for r in results:
        if r["ticker"] in asx_etf_tickers:
            _print_position(r, usd_aud)

    # --- Other ASX ---
    other_asx = [t for t in POSITIONS if t.endswith(".AX") and t not in asx_etf_tickers and t not in HIGH_PRIORITY]
    if other_asx:
        print(colour("\n  📋 ASX — Other", "bold"))
        print("  " + "-" * 56)
        for r in results:
            if r["ticker"] in other_asx:
                _print_position(r, usd_aud)

    # --- US Stocks ---
    us_non_priority = [t for t in POSITIONS if not t.endswith(".AX") and t not in HIGH_PRIORITY]
    if us_non_priority:
        print(colour("\n  🇺🇸 US Stocks", "bold"))
        print("  " + "-" * 56)
        for r in results:
            if r["ticker"] in us_non_priority:
                _print_position(r, usd_aud)

    # --- Portfolio Total ---
    if total_aud > 0:
        total_pnl = total_aud - total_cost_aud if total_cost_aud > 0 else None
        total_pnl_pct = ((total_aud - total_cost_aud) / total_cost_aud * 100) if total_cost_aud > 0 else None

        print(colour(f"\n  {'='*56}", "blue"))
        print(colour(f"  PORTFOLIO TOTAL (tracked positions): ${total_aud:,.0f} AUD", "bold"))
        if total_pnl is not None:
            print(f"  P&L vs cost:  {pnl_str(total_pnl, total_pnl_pct)}")
        print(colour(f"  {'='*56}", "blue"))

    print()


def _print_position(r: dict, usd_aud: float):
    """Print a single position row."""
    ticker = r["ticker"].replace(".AX", "")
    price = r["price"]
    units = r["units"]
    value_aud = r["value_aud"]
    pnl_pct = r["pnl_pct"]
    pnl_aud = r["pnl_aud"]
    action = r["action"]
    note = r["note"]
    currency = r["currency"]

    price_str = format_price(price, currency) if price else colour("N/A", "dim")
    value_str = f"${value_aud:,.0f} AUD" if value_aud else colour("unknown", "dim")
    units_str = f"{units:,}" if units else "unknown"
    currency_tag = f" ({currency})" if currency == "USD" else ""

    print(f"\n  {colour(ticker, 'bold')}{currency_tag}")
    print(f"    Price: {price_str}  |  Units: {units_str}  |  Value: {value_str}")

    if pnl_pct is not None and pnl_aud is not None:
        print(f"    P&L:   {pnl_str(pnl_aud, pnl_pct)}")

    if action:
        action_colour = "yellow" if "HOLD" in action or "Hold" in action else (
            "red" if "SELL" in action else "green"
        )
        print(f"    → {colour(action, action_colour)}")

    if note:
        print(f"    {colour(note, 'dim')}")


def main():
    parser = argparse.ArgumentParser(
        description="Live portfolio snapshot for Dave's AI Brain.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Update POSITIONS dict in this file when you make trades.
Prices are pulled live from Yahoo Finance — may be delayed 15 mins for ASX.
        """
    )
    parser.add_argument("--watch", action="store_true",
                        help="Refresh every 60 seconds (Ctrl+C to stop)")
    args = parser.parse_args()

    if args.watch:
        print("Watching portfolio — refresh every 60s. Ctrl+C to stop.")
        try:
            while True:
                snapshot()
                print(f"  Next refresh in 60s...")
                time.sleep(60)
        except KeyboardInterrupt:
            print("\nStopped.")
    else:
        snapshot()


if __name__ == "__main__":
    main()
