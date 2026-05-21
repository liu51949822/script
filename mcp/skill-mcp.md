# skill_mcp — MCP 调用工具

## 简介

`skill_mcp` 是调用 MCP (Model Context Protocol) 服务器操作的统一接口。通过指定 MCP 服务器名称和操作类型，可以访问各种外部工具和数据源。

## 基本语法

```text
skill_mcp(
    mcp_name="服务器名称",      # 必填: MCP 服务器标识
    tool_name="工具名",          # 调用工具 (三选一)
    resource_name="资源URI",     # 读取资源 (三选一)
    prompt_name="提示模板名",    # 获取提示模板 (三选一)
    arguments='{"key":"val"}',  # 可选: 参数 (JSON)
    grep="正则"                 # 可选: 输出过滤
)
```

### 参数说明

| 参数 | 必填 | 说明 |
|------|------|------|
| `mcp_name` | ✅ | MCP 服务器名 (如 playwright) |
| `tool_name` | 三选一 | 执行工具操作 |
| `resource_name` | 三选一 | 读取资源内容 |
| `prompt_name` | 三选一 | 获取提示模板 |
| `arguments` | 可选 | 传递给工具/资源/提示的参数 |
| `grep` | 可选 | 用正则过滤输出行 |

## 使用模式

### 调用工具

```text
skill_mcp(mcp_name="playwright",
          tool_name="browser_screenshot",
          arguments='{"name": "shot.png"}')
```

### 读取资源

```text
skill_mcp(mcp_name="filesystem",
          resource_name="file:///path/to/file")
```

### 获取提示模板

```text
skill_mcp(mcp_name="some-server",
          prompt_name="greeting",
          arguments='{"name": "World"}')
```

## 输出过滤

使用 `grep` 参数只保留匹配的行：

```text
skill_mcp(mcp_name="playwright",
          tool_name="browser_get_content",
          grep="error|warning")
```

## 参考

- MCP 规范: https://modelcontextprotocol.io/
- skill_mcp 工具: 本环境内置
