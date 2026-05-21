#!/bin/bash
# 代码统计脚本 — 按编程语言统计文件数和代码行数
# 用法: ./code-stats.sh [目录]
# 统计类型: .sh .py .js .ts .yml .json .md .html .css .sql
# 附带 Git 提交统计 (提交数、贡献者排行)

set -euo pipefail

DIR="${1:-.}"
echo "=== 代码统计: $DIR ==="

TOTAL_FILES=$(find "$DIR" -type f \
    \( -name "*.sh" -o -name "*.py" -o -name "*.js" -o -name "*.ts" \
    -o -name "*.yml" -o -name "*.yaml" -o -name "*.json" -o -name "*.md" \
    -o -name "*.html" -o -name "*.css" -o -name "*.sql" \) 2>/dev/null | wc -l | tr -d ' ')
echo "代码文件数: $TOTAL_FILES"

echo ""
printf "%-8s %8s %10s\n" "类型" "文件数" "行数"
echo "--------------------------------"

for ext in sh py js ts yml yaml json md html css sql; do
    count=$(find "$DIR" -type f -name "*.$ext" 2>/dev/null | wc -l | tr -d ' ')
    if [[ "$count" -gt 0 ]]; then
        lines=$(find "$DIR" -type f -name "*.$ext" -exec cat {} \; 2>/dev/null | wc -l | tr -d ' ')
        printf "%-8s %8s %10s\n" ".$ext" "$count" "$lines"
    fi
done

echo "---"
echo "Git 统计:"
git log --oneline 2>/dev/null | wc -l | tr -d ' ' | xargs echo "  提交数:"
git shortlog -sn 2>/dev/null | head -5 || echo "  (非 git 仓库)"
