#!/usr/bin/env bash
set -euo pipefail

TARGET_URL="${1:-https://outputmarketing.lovable.app}"
BASE_DIR="${2:-.}"
TS="$(date +"%Y%m%d-%H%M%S")"
OUT_DIR="$BASE_DIR/outputmarketing-scrape-$TS"
mkdir -p "$OUT_DIR"

echo "Scraping $TARGET_URL into $OUT_DIR"

if command -v wget >/dev/null 2>&1; then
  wget \
    --mirror \
    --convert-links \
    --adjust-extension \
    --page-requisites \
    --no-parent \
    --directory-prefix="$OUT_DIR" \
    "$TARGET_URL" \
    | tee "$OUT_DIR/wget.log"
else
  # Fallback: at minimum capture the entry HTML
  curl -L --fail --show-error "$TARGET_URL" -o "$OUT_DIR/index.html"
fi

find "$OUT_DIR" -type f | wc -l | awk '{print "Downloaded files: " $1}'
echo "Done."
