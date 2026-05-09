#!/bin/bash
# Research Workflow — Inbox Auto-Sort
# Runs every 30 seconds via launchd.
# Naming convention: "STOCK - ...", "CRYPTO - ...", "FBA - ..."

INBOX="/Users/dave/Desktop/Co-Work Homebase/02 Projects/Research Workflow/Inbox"
BASE="/Users/dave/Desktop/Co-Work Homebase/02 Projects/Research Workflow"

for f in "$INBOX"/*; do
  [ -f "$f" ] || continue
  name=$(basename "$f")
  upper=$(echo "$name" | tr '[:lower:]' '[:upper:]')
  if [[ "$upper" == STOCK* ]]; then
    dest="$BASE/Watchlist/Stocks"
  elif [[ "$upper" == CRYPTO* ]]; then
    dest="$BASE/Watchlist/Crypto"
  elif [[ "$upper" == FBA* ]]; then
    dest="$BASE/Watchlist/FBA"
  else
    continue
  fi
  mv "$f" "$dest/"
done
