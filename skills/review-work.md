# /review-work — 实现审查工作流

## 简介

实现后的全面审查器，并行启动 5 个子代理从不同维度审查实现质量和完整性。

## 使用场景

- 完成功能实现后的质量把关
- 合并 PR 前的最终检查
- 检查实现是否满足原始需求
- 安全漏洞扫描
- QA 自动化测试执行

## 审查流程

当调用后，自动并行启动 5 个审查代理：

```text
1. Oracle — 检查实现是否满足原始需求和约束
2. Oracle — 代码质量审查
3. Oracle — 安全审查
4. unspecified-high — 手动 QA 执行测试
5. unspecified-high — 上下文挖掘 (GitHub/git/Slack/Notion)
```

## 用法

```text
task(category="unspecified-high", load_skills=["review-work"],
     prompt="审查我的实现...")
```

### 通过条件

所有 5 个审查代理必须全部通过：

| 代理 | 审查重点 |
|------|----------|
| Oracle 1 | 功能完整性和需求符合度 |
| Oracle 2 | 代码质量、可维护性 |
| Oracle 3 | 安全漏洞、密钥泄露 |
| QA | 功能测试执行 |
| Context | 上下文一致性和完整性 |

## 参考

- 命令: `name="review-work"`
- 场景: 合并 PR 前、发布前
- 来源: OhMyOpenCode 内置技能
