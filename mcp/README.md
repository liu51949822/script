# MCP (Model Context Protocol) 工具集

> Model Context Protocol — AI 代理与外部工具/数据源交互的标准协议

## 目录

| 文档 | 说明 |
|------|------|
| [playwright](./playwright.md) | 浏览器自动化 MCP |
| [skill-mcp](./skill-mcp.md) | skill_mcp 工具使用说明 |
| [mcp-overview](./mcp-overview.md) | MCP 协议概述与最佳实践 |

## MCP 在本环境中的使用

通过 `skill_mcp` 工具调用各种 MCP 服务器：

```text
skill_mcp(mcp_name="服务器名", tool_name="工具名", arguments='{"key":"value"}')
```

## 可用 MCP 服务器

| MCP 服务器 | 工具/资源 | 用途 |
|------------|-----------|------|
| playwright | browser_navigate, browser_screenshot, browser_click | Web 浏览器自动化 |
| (可扩展) | 按需添加 | 数据库、文件系统、API 等 |

## 参考

- MCP 规范: https://modelcontextprotocol.io/
- GitHub: https://github.com/modelcontextprotocol/servers
