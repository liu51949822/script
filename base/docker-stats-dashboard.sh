#!/bin/bash
# Docker 统计面板 - Web 可视化 Docker 容器状态
# 生成日期: 2026-07-24

set -e

echo "=== Docker 统计面板 ==="
echo "<html><body><h1>Docker Stats</h1><pre>$(docker stats --no-stream 2>&1)</pre></body></html>" > /tmp/docker-stats.html
echo "  Dashboard: file:///tmp/docker-stats.html"
echo "=== 完成 ==="
