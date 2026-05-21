#!/bin/bash
# Backup Docker Volumes Script - 备份 Docker 数据卷
# Usage: ./backup-volumes.sh [volume_name] [backup_dir]

set -euo pipefail

BACKUP_DIR="${2:-./docker-backups}"
TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
mkdir -p "$BACKUP_DIR"

backup_volume() {
    local vol=$1
    echo "备份卷: $vol"
    docker run --rm \
        -v "${vol}:/source:ro" \
        -v "$(pwd)/$BACKUP_DIR:/backup" \
        alpine:latest \
        tar czf "/backup/${vol}_${TIMESTAMP}.tar.gz" -C /source . \
        2>/dev/null && echo "  ✓ ${vol}_${TIMESTAMP}.tar.gz" || echo "  ✗ 备份失败: $vol"
}

if [[ "${1:-}" != "" ]]; then
    backup_volume "$1"
else
    echo "=== Backup All Docker Volumes ==="
    volumes=$(docker volume ls -q 2>/dev/null)
    if [[ -z "$volumes" ]]; then
        echo "没有找到 Docker 卷"
        exit 0
    fi
    for vol in $volumes; do
        backup_volume "$vol"
    done
fi

echo ""
echo "备份目录: $BACKUP_DIR"
echo "=== 备份完成 ==="
