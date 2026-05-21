# deep — 自主研究执行代理

## 简介

目标导向的自主问题求解器。用于需要深度研究并端到端实现的任务。
每个调用专注一个目标、交付一个成果。

## 使用场景

- 需要研究的端到端实现
- 独立的功能模块开发
- 跨多个文件/模块的完整功能
- 需要探索性编码的任务
- 单次可独立验证的交付物

## 用法

```text
task(category="deep", load_skills=["skill1", "skill2"],
     run_in_background=true,
     prompt="[GOAL]: 明确的目标和成功标准
      [DELIVERABLE]: 具体的产出物
      [CONSTRAINTS]: 约束条件和边界")
```

### 原则

- 一个调用 = 一个目标 = 一个交付物
- 多目标必须拆分为多个并行的 `deep` 调用
- 必须给出明确成功标准
- 允许自主探索和决策

## 示例

```text
# 正确：单一目标
task(category="deep", load_skills=[], run_in_background=true,
     prompt="GOAL: 创建一个 pgvector Docker Compose 配置
      DELIVERABLE: docker/pgvector/installcompose.file + README.md
      要求: PostgreSQL 16 + pgvector 0.7, 带健康检查")

# 错误：多个目标塞在一起
task(category="deep", load_skills=[], run_in_background=true,
     prompt="GOAL: 创建 pgvector + mysql + nginx 配置")  # ❌
```

## 参考

- 分类: category="deep"
- 适用: 需要研究 + 实现的任务
- 特点: 自主决策、端到端交付
