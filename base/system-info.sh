#!/bin/bash
# System Info Script - 系统信息收集
# Usage: ./system-info.sh

set -euo pipefail

echo "=============================="
echo "     System Information"
echo "=============================="
echo "收集时间: $(date '+%Y-%m-%d %H:%M:%S')"

echo ""
echo "--- OS Info ---"
uname -a 2>/dev/null || echo "N/A"
cat /etc/os-release 2>/dev/null | head -5 || echo "N/A"

echo ""
echo "--- CPU ---"
echo "CPU Cores: $(nproc 2>/dev/null || sysctl -n hw.ncpu 2>/dev/null || echo 'N/A')"
echo "Load Average: $(uptime 2>/dev/null | awk -F'load average:' '{print $2}' || echo 'N/A')"

echo ""
echo "--- Memory ---"
free -h 2>/dev/null || vm_stat 2>/dev/null | head -10 || echo "N/A"

echo ""
echo "--- Disk ---"
df -h / 2>/dev/null || echo "N/A"

echo ""
echo "--- Network ---"
echo "Hostname: $(hostname 2>/dev/null || echo 'N/A')"
echo "Private IP: $(hostname -I 2>/dev/null | awk '{print $1}' || ipconfig getifaddr en0 2>/dev/null || echo 'N/A')"

echo ""
echo "--- Docker Info ---"
docker info --format '{{.ServerVersion}}' 2>/dev/null && echo "Docker 版本: $(docker --version)" || echo "Docker not found"

echo ""
echo "--- Running Containers ---"
docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}' 2>/dev/null || echo "No containers running"
