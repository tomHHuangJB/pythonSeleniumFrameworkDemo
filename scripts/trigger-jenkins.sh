#!/bin/sh
# Trigger local Jenkins job manually.
JENKINS_URL="http://localhost:9082"  # Update if your Jenkins runs elsewhere.
JOB_NAME="python-selenium-ci"        # Update to your Jenkins job name.
USER="admin"                         # Update with your Jenkins username.
TOKEN="115edc29812e7737ebf08b81af67642808"  # Update with your Jenkins API token.

CRUMB_JSON=$(curl -sS -u "$USER:$TOKEN" "$JENKINS_URL/crumbIssuer/api/json" 2>/dev/null || true)
CRUMB=$(printf '%s' "$CRUMB_JSON" | sed -n 's/.*"crumb":"\([^"]*\)".*/\1/p')
CRUMB_FIELD=$(printf '%s' "$CRUMB_JSON" | sed -n 's/.*"crumbRequestField":"\([^"]*\)".*/\1/p')

RESP=$(mktemp)
DATA='json={}'
if [ -n "$CRUMB" ] && [ -n "$CRUMB_FIELD" ]; then
  STATUS=$(curl -sS -o "$RESP" -w "%{http_code}" -X POST \
    -u "$USER:$TOKEN" -H "$CRUMB_FIELD: $CRUMB" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    --data "$DATA" "$JENKINS_URL/job/$JOB_NAME/build" || true)
else
  STATUS=$(curl -sS -o "$RESP" -w "%{http_code}" -X POST \
    -u "$USER:$TOKEN" -H "Content-Type: application/x-www-form-urlencoded" \
    --data "$DATA" "$JENKINS_URL/job/$JOB_NAME/build" || true)
fi

if [ "$STATUS" -ge 200 ] && [ "$STATUS" -lt 400 ]; then
  echo "Triggered Jenkins job: $JOB_NAME (HTTP $STATUS)"
  rm -f "$RESP"
  exit 0
fi

echo "Failed to trigger Jenkins job: $JOB_NAME (HTTP $STATUS)" >&2
if [ -s "$RESP" ]; then
  echo "Response body:" >&2
  cat "$RESP" >&2
fi
rm -f "$RESP"
exit 1
