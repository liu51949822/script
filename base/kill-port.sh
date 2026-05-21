#!/bin/bash
# 端口释放脚本 — 查找占用指定端口的进程并安全终止
# 用法: ./kill-port.sh <端口号>
# 示例: ./kill-port.sh 8080
# 不带参数时列出当前所有监听端口

set -euo pipefail

PORT="${1:-}"

if [[ -z "$PORT" ]]; then
    echo "用法: ./kill-port.sh <端口号>"
    echo "示例: ./kill-port.sh 8080"
    echo ""
    echo "当前监听的端口:"
    lsof -iTCP -sTCP:LISTEN -P -n 2>/dev/null | awk 'NR>1{print $1, $9}' | sed 's/.*://' | sort -n | uniq | head -20
    exit 1
fi

echo "查找端口 $PORT 的进程..."

if command -v lsof &>/dev/null; then
    PIDS=$(lsof -tiTCP:"$PORT" -sTCP:LISTEN 2>/dev/null)
elif command -v ss &>/dev/null; then
    PIDS=$(ss -tlnp 2>/dev/null | grep ":$PORT " | grep -oP 'pid=\K\d+')
else
    echo "❌ 需要 lsof 或 ss 命令"
    exit 1
fi

if [[ -z "$PIDS" ]]; then
    echo "✅ 端口 $PORT 没有被占用"
    exit 0
fi

echo "发现以下进程:"
for pid in $PIDS; do
    PROC=$(ps -p "$pid" -o comm= 2>/dev/null || echo "unknown")
    echo "  PID: $pid  ($PROC)"
done

echo ""
read -p "确认杀掉这些进程? [y/N] " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    for pid in $PIDS; do
        kill -9 "$pid" 2>/dev/null && echo "  ✅ PID $pid 已终止" || echo "  ❌ PID $pid 终止失败"
    done
    echo "端口 $PORT 已释放"
else
    echo "已取消"
fi
