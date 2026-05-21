# MCP 协议概述

## 什么是 MCP？

MCP (Model Context Protocol) 是一个开放协议，定义了 AI 代理与外部工具、数据源、服务之间通信的标准方式。类似于 USB-C 为外设提供的标准化连接，MCP 为 AI 应用提供了标准化的工具集成接口。

## 核心概念

### MCP 服务器 (Server)

提供特定功能的服务端，每个服务器暴露三类操作：

```
MCP Server
├── Tools       → 可执行的操作 (函数)
├── Resources   → 可读取的数据 (文件/API)
└── Prompts     → 可复用的提示模板
```

### MCP 客户端 (Client)

AI 代理通过客户端连接 MCP 服务器，调用其操作获取数据或执行动作。

### 三方关系

```
AI 代理 (Client) ← → MCP 协议 ← → MCP 服务器 (Server) → 外部系统/数据
```

## 在本环境中的使用

通过 `skill` 命令加载 MCP 技能，通过 `skill_mcp` 工具调用具体操作：

```text
# 1. 加载 MCP 技能
skill(name="playwright")

# 2. 调用 MCP 工具
skill_mcp(mcp_name="playwright",
          tool_name="browser_navigate",
          arguments='{"url": "https://example.com"}')
```

## MCP 优势

| 特性 | 说明 |
|------|------|
| 标准化 | 统一的接口规范，所有 MCP 服务器使用相同协议 |
| 可插拔 | 按需加载/卸载 MCP 服务器 |
| 安全 | 服务器在隔离环境中运行，客户端控制访问范围 |
| 可组合 | 多个 MCP 服务器协同工作 |
| 实时 | 工具调用结果实时返回给 AI 代理 |

## 常见 MCP 服务器

| 服务器 | 能力 | 地址 |
|--------|------|------|
| Playwright | 浏览器自动化 | https://github.com/microsoft/playwright-mcp |
| Filesystem | 文件系统操作 | https://github.com/modelcontextprotocol/servers |
| GitHub | GitHub API 操作 | https://github.com/modelcontextprotocol/servers |
| PostgreSQL | 数据库查询 | https://github.com/modelcontextprotocol/servers |
| SQLite | SQLite 操作 | https://github.com/modelcontextprotocol/servers |
| Fetch | HTTP 请求 | https://github.com/modelcontextprotocol/servers |

## 参考

- 官方文档: https://modelcontextprotocol.io/
- 规范: https://spec.modelcontextprotocol.io/
- GitHub 仓库: https://github.com/modelcontextprotocol/servers
- Python SDK: https://github.com/modelcontextprotocol/python-sdk
- TypeScript SDK: https://github.com/modelcontextprotocol/typescript-sdk
