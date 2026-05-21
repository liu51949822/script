#!/bin/bash
# Git 一键同步脚本 — 拉取远端、同步当前分支、清理已合并分支
# 用法: ./git-sync.sh
# 功能: fetch 远程更新 → pull 当前分支 → 删除本地已合并分支 → 显示仓库状态

set -euo pipefail

echo "=== Git Sync ==="
echo "时间: $(date '+%H:%M:%S')"

BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "")

if [[ -z "$BRANCH" ]]; then
    echo "❌ 不在 Git 仓库中"
    exit 1
fi

echo "当前分支: $BRANCH"

echo "[1/4] 拉取远程更新..."
git fetch --all --prune 2>/dev/null && echo "  ✅ 远程更新已拉取" || echo "  ⚠️ 拉取失败"

echo "[2/4] 当前分支同步..."
git pull origin "$BRANCH" 2>/dev/null && echo "  ✅ $BRANCH 已同步" || echo "  ⚠️ 同步失败（可能有冲突需手动解决）"

echo "[3/4] 清理已合并的分支..."
MERGED=$(git branch --merged "$BRANCH" | grep -v "^\*\|main\|master\|develop\|$BRANCH" | sed 's/^[ *]*//')
if [[ -n "$MERGED" ]]; then
    echo "$MERGED" | while read b; do
        git branch -d "$b" 2>/dev/null && echo "  🗑️ $b (已删除)" || echo "  ⚠️ $b (删除失败)"
    done
else
    echo "  ✅ 没有需要清理的分支"
fi

echo "[4/4] 仓库状态..."
git status --short 2>/dev/null || echo "  (无变更)"

echo "=== 同步完成 ==="
