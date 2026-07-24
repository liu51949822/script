#!/bin/bash
# 磁盘清理 - 清理临时文件和缓存释放空间
# 生成日期: 2026-07-24

set -e

echo "=== 磁盘清理 ==="
echo "  清理 Docker 无用数据..."
docker system prune -af --volumes 2>/dev/null && echo "  done" || echo "  docker not available"
echo "  清理临时文件..."
rm -rf /tmp/* 2>/dev/null
rm -rf ~/.cache/* 2>/dev/null
echo "  磁盘使用:"
df -h / 2>/dev/null || true
echo "=== 完成 ==="
