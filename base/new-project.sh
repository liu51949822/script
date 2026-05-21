#!/bin/bash
# 项目脚手架 — 快速初始化不同技术栈的新项目
# 用法: ./new-project.sh <项目名> [类型]
# 类型: python, node, go, docker, basic (默认 basic)
# 示例: ./new-project.sh my-api python
# 自动创建目录结构、基础配置文件和 .gitignore

set -euo pipefail

PROJECT_NAME="${1:-}"
if [[ -z "$PROJECT_NAME" ]]; then
    echo "用法: ./new-project.sh <项目名> [类型]"
    echo "类型: python, node, go, docker, basic (默认 basic)"
    exit 1
fi

TYPE="${2:-basic}"
PROJECT_DIR="./$PROJECT_NAME"

if [[ -d "$PROJECT_DIR" ]]; then
    echo "❌ 目录 $PROJECT_DIR 已存在"
    exit 1
fi

echo "创建项目: $PROJECT_NAME (类型: $TYPE)"
mkdir -p "$PROJECT_DIR"

case $TYPE in
    python)
        mkdir -p "$PROJECT_DIR"/{src,tests}
        cat > "$PROJECT_DIR/requirements.txt" << 'PYEOF'
# Python 依赖
pyyaml>=6.0
requests>=2.31
PYEOF
        cat > "$PROJECT_DIR/src/main.py" << 'PYEOF'
#!/usr/bin/env python3
def main():
    print("Hello from $PROJECT_NAME")

if __name__ == '__main__':
    main()
PYEOF
        ;;
    node)
        mkdir -p "$PROJECT_DIR"/src
        cat > "$PROJECT_DIR/package.json" << NODEEOF
{
  "name": "$PROJECT_NAME",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "start": "node src/index.js",
    "test": "echo ok"
  }
}
NODEEOF
        echo "console.log('Hello from $PROJECT_NAME');" > "$PROJECT_DIR/src/index.js"
        ;;
    go)
        mkdir -p "$PROJECT_DIR"/cmd
        cat > "$PROJECT_DIR/go.mod" << GOEOF
module github.com/user/$PROJECT_NAME

go 1.22
GOEOF
        cat > "$PROJECT_DIR/main.go" << 'GOEOF'
package main

import "fmt"

func main() {
    fmt.Println("Hello!")
}
GOEOF
        ;;
    docker)
        cat > "$PROJECT_DIR/docker-compose.yml" << DCEOF
version: '3.8'
services:
  app:
    image: alpine:latest
    container_name: $PROJECT_NAME
    restart: always
    command: echo "Hello from $PROJECT_NAME"
DCEOF
        ;;
    *)
        cat > "$PROJECT_DIR/README.md" << MDEOF
# $PROJECT_NAME

## 说明

项目说明文档。
MDEOF
        ;;
esac

cat > "$PROJECT_DIR/README.md" << MDEOF
# $PROJECT_NAME

> 由 new-project.sh 生成 ($TYPE 类型)
MDEOF

cat > "$PROJECT_DIR/.gitignore" << GITEOF
__pycache__/
*.pyc
node_modules/
.env
.DS_Store
GITEOF

echo ""
echo "✅ 项目已创建: $PROJECT_DIR"
echo ""
echo "快速开始:"
echo "  cd $PROJECT_NAME"
[[ "$TYPE" == "python" ]] && echo "  python3 src/main.py"
[[ "$TYPE" == "node" ]]   && echo "  npm install && npm start"
[[ "$TYPE" == "go" ]]     && echo "  go run main.go"
