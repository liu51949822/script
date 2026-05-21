# metis — 计划咨询代理 (Pre-planning Consultant)

## 简介

任务前分析顾问，在开始实施前对需求进行深度分析，识别隐藏意图、歧义点和潜在失败风险。

## 使用场景

- 复杂/模糊需求的分析和澄清
- 识别用户未明确说出的意图
- 发现 AI 实施中的常见失败模式
- 评估任务范围和复杂度
- 在正式规划前做前置分析

## 用法

```text
task(subagent_type="metis", load_skills=[], run_in_background=false,
     prompt="[请求背景]: ... [我的计划]: ... [分析要求]: ...")
```

## 示例

```text
task(subagent_type="metis", load_skills=[], run_in_background=false,
     prompt="## 上下文：用户要求添加人脸识别功能
      ## 我的计划：使用 CompreFace 创建 Docker Compose 配置
      ## 分析：
      1. 用户的隐藏意图可能是什么？
      2. 这个方案有什么 AI 容易出错的地方？
      3. 我是否遗漏了关键考虑因素？")
```

## 参考

- 类型: subagent_type="metis"
- 来源: Metis - OhMyOpenCode
- 特点: 先分析后实施，降低返工风险
