#!/bin/bash
# Docker Cleanup Script - 清理未使用的 Docker 资源
# Usage: ./docker-cleanup.sh [--all]

set -euo pipefail

echo "=== Docker Cleanup ==="
echo "清理日期: $(date '+%Y-%m-%d %H:%M:%S')"

# 基础清理
echo "[1/5] 清理已停止的容器..."
docker container prune -f 2>/dev/null && echo "  ✓ 已停止容器清理完成" || echo "  (无容器需要清理)"

echo "[2/5] 清理悬空镜像 (dangling)..."
docker image prune -f 2>/dev/null && echo "  ✓ 悬空镜像清理完成" || echo "  (无镜像需要清理)"

echo "[3/5] 清理未使用的网络..."
docker network prune -f 2>/dev/null && echo "  ✓ 未使用网络清理完成" || echo "  (无网络需要清理)"

echo "[4/5] 清理构建缓存..."
docker builder prune -f 2>/dev/null && echo "  ✓ 构建缓存清理完成" || echo "  (无缓存需要清理)"

if [[ "${1:-}" == "--all" ]]; then
    echo "[5/5] 深度清理所有未使用镜像..."
    docker image prune -a -f 2>/dev/null && echo "  ✓ 所有未使用镜像清理完成"
fi

echo ""
echo "=== 清理后磁盘使用 ==="
docker system df 2>/dev/null

echo ""
echo "=== 清理完成 ==="
