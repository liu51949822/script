# Playwright MCP — 浏览器自动化

## 简介

基于 Playwright 的浏览器 MCP 服务器。实现 Web 浏览器全自动化 — 导航、点击、输入、截图、内容提取。

## 使用场景

- 网页截图和渲染检查
- 自动化 Web 表单填写和提交
- 网页信息采集和内容提取
- Web UI 功能验证
- 网站监控和巡检

## 前置条件

```text
# 加载 Playwright 技能
skill(name="playwright")
```

## 可用工具

### browser_navigate — 页面导航

```text
skill_mcp(mcp_name="playwright", tool_name="browser_navigate",
          arguments='{"url": "https://example.com"}')
```

### browser_screenshot — 截图

```text
skill_mcp(mcp_name="playwright", tool_name="browser_screenshot",
          arguments='{"name": "page.png", "width": 1280, "height": 720}')
```

### browser_click — 页面点击

```text
skill_mcp(mcp_name="playwright", tool_name="browser_click",
          arguments='{"selector": "#submit-btn"}')
```

### browser_fill — 填写输入框

```text
skill_mcp(mcp_name="playwright", tool_name="browser_fill",
          arguments='{"selector": "#username", "value": "admin"}')
```

### browser_evaluate — 执行 JavaScript

```text
skill_mcp(mcp_name="playwright", tool_name="browser_evaluate",
          arguments='{"script": "document.title"}')
```

### browser_get_content — 获取页面内容

```text
skill_mcp(mcp_name="playwright", tool_name="browser_get_content")
```

### browser_get_cookies — 获取 Cookie

```text
skill_mcp(mcp_name="playwright", tool_name="browser_get_cookies")
```

## 完整示例

```text
skill(name="playwright")

# 1. 导航到目标页面
skill_mcp(mcp_name="playwright", tool_name="browser_navigate",
          arguments='{"url": "http://localhost:3000"}')

# 2. 截图
skill_mcp(mcp_name="playwright", tool_name="browser_screenshot",
          arguments='{"name": "homepage.png"}')

# 3. 获取页面内容
skill_mcp(mcp_name="playwright", tool_name="browser_get_content")
```

## 参考

- Playwright: https://playwright.dev/
- MCP Playwright: https://github.com/microsoft/playwright-mcp
- OhMyOpenCode 集成: 通过 skill_mcp 调用
