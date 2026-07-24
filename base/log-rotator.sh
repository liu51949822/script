#!/bin/bash
# 日志轮转 - 自动切割和压缩日志文件
# 生成日期: 2026-07-23

set -e

echo "=== 日志轮转 ==="
LOG_DIR="${1:-/var/log}"
DAYS="${2:-7}"
find "$LOG_DIR" -name "*.log" -type f -mtime +$DAYS -exec gzip {} \;
find "$LOG_DIR" -name "*.gz" -type f -mtime +30 -delete
echo "  Log rotation completed for $LOG_DIR"
echo "=== 完成 ==="
