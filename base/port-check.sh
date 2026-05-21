#!/bin/bash
# Port Checker Script - 检查端口占用情况
# Usage: ./port-check.sh [port]

set -euo pipefail

check_port() {
    local port=$1
    echo "检查端口: $port"
    
    # Linux: ss, macOS: lsof
    if command -v ss &>/dev/null; then
        ss -tlnp 2>/dev/null | grep ":$port " && echo "  端口 $port 已被占用" || echo "  ✅ 端口 $port 可用"
    elif command -v lsof &>/dev/null; then
        lsof -iTCP:"$port" -sTCP:LISTEN -P 2>/dev/null && echo "  端口 $port 已被占用" || echo "  ✅ 端口 $port 可用"
    else
        echo "  无法检查 (需要 ss 或 lsof 命令)"
    fi
}

if [[ "${1:-}" != "" ]]; then
    check_port "$1"
else
    echo "=== 常用端口检查 ==="
    PORTS=(80 443 3306 5432 6379 27017 8080 9090 3000)
    for port in "${PORTS[@]}"; do
        check_port "$port"
    done
fi
