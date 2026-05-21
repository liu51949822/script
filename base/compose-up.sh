#!/bin/bash
# Docker Compose Batch Start Script - 批量启动 docker 目录下的 compose 服务
# Usage: ./compose-up.sh [service_name | --all]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DOCKER_DIR="$(dirname "$SCRIPT_DIR")/docker"

if [[ ! -d "$DOCKER_DIR" ]]; then
    echo "✗ docker 目录不存在: $DOCKER_DIR"
    exit 1
fi

start_service() {
    local dir=$1
    local name=$(basename "$dir")
    local compose_file="$dir/installcompose.file"
    
    if [[ -f "$compose_file" ]]; then
        echo "启动: $name"
        cd "$dir" && docker compose -f installcompose.file up -d 2>/dev/null && echo "  ✓ $name 已启动" || echo "  ✗ $name 启动失败"
    fi
}

if [[ "${1:-}" == "--all" ]]; then
    echo "=== 启动所有服务 ==="
    for dir in "$DOCKER_DIR"/*/; do
        start_service "$dir"
    done
elif [[ "${1:-}" != "" ]]; then
    if [[ -d "$DOCKER_DIR/$1" ]]; then
        start_service "$DOCKER_DIR/$1"
    else
        echo "✗ 服务不存在: $1"
        echo "可用服务:"
        ls "$DOCKER_DIR"
        exit 1
    fi
else
    echo "Usage: $0 <service_name> | --all"
    echo ""
    echo "可用服务:"
    ls "$DOCKER_DIR"
fi
