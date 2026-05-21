#!/bin/bash
# Docker Logs Viewer - 查看 Docker 容器日志
# Usage: ./docker-logs.sh <container_name> [tail_lines]

set -euo pipefail

CONTAINER="${1:-}"
LINES="${2:-100}"

if [[ -z "$CONTAINER" ]]; then
    echo "Usage: $0 <container_name> [tail_lines]"
    echo ""
    echo "运行中的容器:"
    docker ps --format '  {{.Names}}' 2>/dev/null || echo "  没有运行中的容器"
    exit 1
fi

echo "=== 容器日志: $CONTAINER (最近 $LINES 行) ==="
echo "时间: $(date '+%Y-%m-%d %H:%M:%S')"

docker logs --tail "$LINES" "$CONTAINER" 2>&1 || echo "✗ 无法获取日志 (容器 $CONTAINER 不存在或未运行)"
