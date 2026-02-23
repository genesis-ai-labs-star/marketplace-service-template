#!/bin/bash
# serper_search.sh - Google Search via Serper API
# Usage: ./serper_search.sh "your query" [num_results]

QUERY="$1"
NUM="${2:-5}"

KEYS=(
  "2a5caa37b2d9c04c05fa778e7596fa000d88ba68"
  "7484cfb6b9c7e41ffa379dcb5e895184203987f6"
)

for KEY in "${KEYS[@]}"; do
  RESULT=$(curl -s -X POST "https://google.serper.dev/search" \
    -H "X-API-KEY: $KEY" \
    -H "Content-Type: application/json" \
    -d "{\"q\":\"$QUERY\",\"num\":$NUM}")
  
  # Check if successful (no error message)
  if echo "$RESULT" | grep -q '"organic"'; then
    echo "$RESULT"
    exit 0
  fi
done

echo '{"error": "All keys exhausted or failed"}'
exit 1
