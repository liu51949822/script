#!/bin/bash
# SSL Certificate Check Script - 检查 SSL 证书到期时间
# Usage: ./ssl-check.sh domain.com [port]

set -euo pipefail

DOMAIN="${1:-}"
PORT="${2:-443}"

if [[ -z "$DOMAIN" ]]; then
    echo "Usage: $0 <domain> [port]"
    echo "Example: $0 example.com 443"
    exit 1
fi

echo "检查 SSL 证书: $DOMAIN:$PORT"

CERT_INFO=$(echo | openssl s_client -servername "$DOMAIN" -connect "${DOMAIN}:${PORT}" 2>/dev/null | openssl x509 -noout -dates -subject 2>/dev/null)

if [[ -z "$CERT_INFO" ]]; then
    echo "✗ 无法连接到 $DOMAIN:$PORT 或获取证书信息"
    exit 1
fi

echo "$CERT_INFO"

NOT_AFTER=$(echo "$CERT_INFO" | grep "notAfter" | cut -d= -f2)
EXPIRE_TS=$(date -j -f "%b %d %T %Y %Z" "$NOT_AFTER" +%s 2>/dev/null || date -d "$NOT_AFTER" +%s 2>/dev/null)
NOW_TS=$(date +%s)
DAYS_LEFT=$(( ($EXPIRE_TS - $NOW_TS) / 86400 ))

echo ""
echo "到期时间: $NOT_AFTER"
echo "剩余天数: $DAYS_LEFT 天"

if [[ $DAYS_LEFT -lt 7 ]]; then
    echo "⚠️  警告: 证书即将过期!"
elif [[ $DAYS_LEFT -lt 30 ]]; then
    echo "⚠️  注意: 证书将在一个月内过期"
else
    echo "✅ 证书状态正常"
fi
