#!/bin/bash
# Docker Health Check Script - 检查所有容器健康状态
# Usage: ./health-check.sh

set -euo pipefail

echo "=== Docker Container Health Check ==="
echo "检查时间: $(date '+%Y-%m-%d %H:%M:%S')"

HEALTHY=0
UNHEALTHY=0
NO_CHECK=0

containers=$(docker ps -q 2>/dev/null)

if [[ -z "$containers" ]]; then
    echo "没有运行中的容器"
    exit 0
fi

for cid in $containers; do
    name=$(docker inspect --format '{{.Name}}' "$cid" 2>/dev/null | sed 's/\///')
    status=$(docker inspect --format '{{.State.Status}}' "$cid" 2>/dev/null)
    
    health=$(docker inspect --format '{{if .State.Health}}{{.State.Health.Status}}{{else}}none{{end}}' "$cid" 2>/dev/null)
    
    case "$health" in
        healthy) 
            echo "  ✅ $name ($status) - 健康"
            HEALTHY=$((HEALTHY + 1))
            ;;
        unhealthy)
            echo "  ❌ $name ($status) - 不健康!"
            UNHEALTHY=$((UNHEALTHY + 1))
            ;;
        starting)
            echo "  ⏳ $name ($status) - 启动中..."
            HEALTHY=$((HEALTHY + 1))
            ;;
        none)
            echo "  ⬜ $name ($status) - 无健康检查"
            NO_CHECK=$((NO_CHECK + 1))
            ;;
    esac
done

echo ""
echo "--- 汇总 ---"
echo "健康容器: $HEALTHY"
echo "不健康容器: $UNHEALTHY"
echo "无健康检查: $NO_CHECK"

if [[ $UNHEALTHY -gt 0 ]]; then
    echo "⚠️  有不健康的容器! 请检查日志"
    exit 1
else
    echo "✅ 所有容器状态正常"
fi
