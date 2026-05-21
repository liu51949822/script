#!/bin/bash
# Disk Space Alert Script - 磁盘空间告警
# Usage: ./disk-alert.sh [threshold_percent]

set -euo pipefail

THRESHOLD="${1:-80}"

echo "=== 磁盘空间检查 ==="
echo "告警阈值: ${THRESHOLD}%"
echo "时间: $(date '+%Y-%m-%d %H:%M:%S')"

ALERT_COUNT=0

while IFS= read -r line; do
    filesystem=$(echo "$line" | awk '{print $1}')
    size=$(echo "$line" | awk '{print $2}')
    used=$(echo "$line" | awk '{print $3}')
    avail=$(echo "$line" | awk '{print $4}')
    use_percent=$(echo "$line" | awk '{print $5}' | sed 's/%//')
    mount=$(echo "$line" | awk '{print $6}')
    
    if [[ "$use_percent" =~ ^[0-9]+$ ]]; then
        if [[ $use_percent -ge $THRESHOLD ]]; then
            echo "  ⚠️  $mount - $used/$size (${use_percent}%) - 超出阈值!"
            ALERT_COUNT=$((ALERT_COUNT + 1))
        else
            echo "  ✅ $mount - $used/$size (${use_percent}%)"
        fi
    fi
done < <(df -h | tail -n +2)

echo ""
if [[ $ALERT_COUNT -gt 0 ]]; then
    echo "⚠️  $ALERT_COUNT 个分区磁盘使用率超过 ${THRESHOLD}%!"
    exit 1
else
    echo "✅ 所有分区磁盘使用率正常"
fi
