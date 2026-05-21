# /playwright — 浏览器自动化技能

## 简介

基于 Playwright 的浏览器自动化技能。用于信息采集、网页截图、UI 测试、页面交互等所有浏览器相关操作。

## 使用场景

- 网页信息采集和内容提取
- 自动截图和页面渲染检查
- Web UI 功能验证
- 表单自动填写和提交
- 网站可用性监控

## 用法

通过 skill_mcp 调用 Playwright MCP 工具：

```text
# 加载技能
skill(name="playwright")
```

### 可用操作

- 导航到 URL
- 点击、输入、选择等页面交互
- 截图
- 获取页面内容
- Cookie 和 Session 管理
- 网络请求拦截

## 示例

```text
# 加载技能
skill(name="playwright")

# 导航和截图
skill_mcp(mcp_name="playwright", tool_name="browser_navigate",
          arguments='{"url": "https://example.com"}')
skill_mcp(mcp_name="playwright", tool_name="browser_screenshot")
```

## 参考

- 命令: `name="playwright"`
- 来源: OhMyOpenCode 内置技能
- 协议: MCP (Model Context Protocol)
