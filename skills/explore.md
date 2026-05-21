# explore — 代码库探索代理

## 简介

代码库上下文搜索代理，用于在代码库中查找模式、实现、结构和约定。
相当于结合了 grep + AST 搜索 + 文件模式匹配的智能搜索工具。

## 使用场景

- 查找特定功能在代码库中的实现位置
- 发现项目中的代码模式和约定
- 搜索配置文件、API 路由、数据库模型等
- 跨文件追踪调用链和依赖关系
- 了解代码库结构和组织方式

## 用法

加载多个 explore 代理并行搜索，每个负责不同的搜索角度：

```text
task(subagent_type="explore", load_skills=[], prompt="[CONTEXT]: ... [GOAL]: ... [REQUEST]: 具体搜索指令",
     run_in_background=true, description="搜索描述")
```

### prompt 结构

- `[CONTEXT]`: 当前任务上下文，涉及哪些文件和模块
- `[GOAL]`: 搜索结果将用来做什么决策
- `[REQUEST]`: 具体的搜索指令 — 找什么、返回什么格式、跳过什么

## 示例

```text
# 并行搜索模式
task(subagent_type="explore", load_skills=[], run_in_background=true,
     prompt="[CONTEXT]: 实现 JWT 认证中间件
      [GOAL]: 了解现有认证模式和中间件结构
      [REQUEST]: 查找 auth 中间件、login/signup 处理、token 生成方式。跳过 test 目录。返回文件路径和模式描述。")

task(subagent_type="explore", load_skills=[], run_in_background=true,
     prompt="[CONTEXT]: 添加错误处理
      [GOAL]: 遵循现有错误处理模式
      [REQUEST]: 查找 Error 子类、错误响应格式、全局错误中间件。返回错误类层次结构和响应格式。")
```

## 参考

- 类型: subagent_type="explore"
- 特点: 只读、免费、轻量、适合并行搜索
- Aliases: Contextual Grep
