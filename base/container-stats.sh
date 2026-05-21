#!/bin/bash
# Docker Stats Monitor - 实时显示容器资源使用
# Usage: ./container-stats.sh [container_name]

set -euo pipefail

if [[ "${1:-}" != "" ]]; then
    docker stats "$1" --no-stream 2>/dev/null || echo "容器 $1 不存在或未运行"
else
    echo "=== Container Resource Usage ==="
    echo "时间: $(date '+%Y-%m-%d %H:%M:%S')"
    echo ""
    docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}\t{{.BlockIO}}" 2>/dev/null || echo "没有运行中的容器"
fi
