#!/bin/bash
# 网络基准测试工具
# 用法: ./network-bench.sh [目标主机] [次数]
# 示例: ./network-bench.sh google.com 5

TARGET="${1:-google.com}"
COUNT="${2:-5}"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "=========================================="
echo "  网络基准测试"
echo "  目标: $TARGET"
echo "  时间: $DATE"
echo "=========================================="

# 1. ping 延迟测试
echo ""
echo "--- Ping 延迟 ($COUNT 次) ---"
ping -c "$COUNT" "$TARGET" 2>/dev/null | tail -1 || echo "  ping 失败"

# 2. DNS 解析时间
echo ""
echo "--- DNS 解析 ---"
if command -v dig &>/dev/null; then
    dig "$TARGET" +stats 2>/dev/null | grep "Query time" || echo "  dig 失败"
elif command -v nslookup &>/dev/null; then
    time nslookup "$TARGET" 2>/dev/null | grep -E "Address|Name" || echo "  nslookup 失败"
fi

# 3. HTTP 响应时间
echo ""
echo "--- HTTP 响应 ---"
if command -v curl &>/dev/null; then
    curl -s -o /dev/null -w "  HTTP 状态码: %{http_code}\n  DNS 时间: %{time_namelookup}s\n  连接时间: %{time_connect}s\n  TLS 时间: %{time_appconnect}s\n  首字节: %{time_starttransfer}s\n  总时间: %{time_total}s\n 下载速度: %{speed_download} bytes/s\n" "https://$TARGET" 2>/dev/null || echo "  curl 失败"
fi

# 4. 路由追踪
echo ""
echo "--- 路由追踪 (前 10 跳) ---"
if command -v traceroute &>/dev/null; then
    traceroute -m 10 "$TARGET" 2>/dev/null || echo "  traceroute 失败"
elif command -v tracert &>/dev/null; then
    tracert -h 10 "$TARGET" 2>/dev/null | head -15 || echo "  tracert 失败"
fi

echo ""
echo "=========================================="
echo "  测试完成"
echo "=========================================="
