#!/bin/bash
# 开发环境检查脚本 — 检测常用开发工具是否已安装及版本
# 用法: ./env-check.sh
# 检查项: Git, Docker, Python3, Node.js, Go, pip3, npm, VS Code 等

set -euo pipefail

echo "=== 开发环境检查 ==="
echo "时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

check_cmd() {
    local cmd=$1 label=$2
    if command -v "$cmd" &>/dev/null; then
        local ver=$($cmd --version 2>&1 | head -1 | cut -c1-50)
        echo "  ✅ $label: $ver"
        return 0
    else
        echo "  ❌ $label: 未安装"
        return 1
    fi
}

MISSING=0

echo "--- 基础工具 ---"
check_cmd git "Git"          || ((MISSING++))
check_cmd curl "curl"        || ((MISSING++))
check_cmd wget "wget"        || ((MISSING++))

echo ""
echo "--- Docker ---"
check_cmd docker "Docker"    || ((MISSING++))

echo ""
echo "--- 编程语言 ---"
check_cmd python3 "Python3"  || ((MISSING++))
check_cmd node "Node.js"     || ((MISSING++))
check_cmd go "Go"            || ((MISSING++))
check_cmd java "Java"        || ((MISSING++))

echo ""
echo "--- 包管理 ---"
check_cmd pip3 "pip3"        || ((MISSING++))
check_cmd npm "npm"          || ((MISSING++))
check_cmd pnpm "pnpm"        || ((MISSING++))

echo ""
echo "--- 编辑器 ---"
check_cmd code "VS Code"     || ((MISSING++))
check_cmd vim "Vim"          || ((MISSING++))

echo ""
echo "--- 网络 ---"
check_cmd ssh "SSH"          || ((MISSING++))
check_cmd nc "netcat"        || ((MISSING++))

echo ""
echo "--- 结果 ---"
if [[ "$MISSING" -gt 0 ]]; then
    echo "⚠️  $MISSING 个工具未安装"
else
    echo "✅ 所有工具就绪"
fi
