#!/bin/bash
# tavily_search.sh - AI-optimized search via Tavily API
# Usage: ./tavily_search.sh "your query" [max_results] [search_depth: basic|advanced]

QUERY="$1"
MAX="${2:-5}"
DEPTH="${3:-advanced}"

KEYS=(
  "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"
  "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"
  "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"
)

for KEY in "${KEYS[@]}"; do
  RESULT=$(curl -s -X POST "https://api.tavily.com/search" \
    -H "Content-Type: application/json" \
    -d "{\"api_key\":\"$KEY\",\"query\":\"$QUERY\",\"max_results\":$MAX,\"search_depth\":\"$DEPTH\",\"include_raw_content\":false}")
  
  if echo "$RESULT" | grep -q '"results"'; then
    echo "$RESULT"
    exit 0
  fi
done

echo '{"error": "All Tavily keys exhausted or failed"}'
exit 1
