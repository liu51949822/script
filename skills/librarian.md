# librarian — 参考文档检索代理

## 简介

外部参考搜索代理，用于检索开源代码、官方文档、实现示例和技术资料。
相当于内置了 GitHub 代码搜索 + 文档查询 + 网页搜索的综合信息检索工具。

## 使用场景

- 查找第三方库的官方 API 文档
- 搜索开源项目中的实现示例
- 了解库/框架的最佳实践
- 调试第三方库的奇怪行为
- 查找配置参考和 migration 指南

## 用法

```text
task(subagent_type="librarian", load_skills=[], run_in_background=true,
     prompt="[CONTEXT]: ... [GOAL]: ... [REQUEST]: 具体搜索指令")
```

### 典型搜索

```text
# 搜索官方文档
task(subagent_type="librarian", load_skills=[], run_in_background=true,
     prompt="[CONTEXT]: 实现 JWT 认证
      [GOAL]: 获取当前安全最佳实践
      [REQUEST]: 查找 OWASP JWT 指南、推荐 token 过期策略、refresh token 轮换。不要基础教程。")

# 搜索开源实现
task(subagent_type="librarian", load_skills=[], run_in_background=true,
     prompt="[CONTEXT]: 构建 Express 中间件
      [GOAL]: 参考知名项目的中间件模式
      [REQUEST]: 查找 star >1000 的 Express 项目的中间件顺序、错误处理、权限控制模式。")
```

## 参考

- 类型: subagent_type="librarian"
- 特点: 只读、适合查阅外部资源
- 数据源: GitHub 开源代码 + Context7 文档 + 网页搜索
