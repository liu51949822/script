# lsp_diagnostics — 代码诊断

## 简介

获取文件的错误、警告、提示信息。每次代码修改后必须运行的检查工具，用于确保代码质量。

## 使用场景

- 每次保存/修改文件后检查语法错误
- 提交代码前确保零错误
- 发现潜在的类型错误和逻辑问题
- 代码审查时检查改动区域的健康状况

## 用法

```text
lsp_diagnostics(filePath="文件或目录路径", severity="级别")
```

| 参数 | 必填 | 说明 |
|------|------|------|
| `filePath` | ✅ | 文件或目录的绝对路径 |
| `severity` | 可选 | 过滤级别: error, warning, information, hint, all |

## 示例

```text
# 检查单个文件的所有诊断
lsp_diagnostics(filePath="/project/src/main.ts")

# 只看错误 (忽略警告)
lsp_diagnostics(filePath="/project/src/main.ts", severity="error")

# 检查整个目录
lsp_diagnostics(filePath="/project/src/")
```

## 严重级别

| 级别 | 含义 | 处理策略 |
|------|------|----------|
| `error` | 编译错误/类型错误 | 必须修复 |
| `warning` | 潜在问题 | 建议修复 |
| `information` | 提示信息 | 按需处理 |
| `hint` | 优化建议 | 可选 |

## 工作流程

```
修改代码 → lsp_diagnostics → 有错误？
  ├─ 否 → 提交
  └─ 是 → 修 → 再次 lsp_diagnostics → 全部清除 → 提交
```

## 禁止

- ⛔ 不修复诊断就声明 "完成"
- ⛔ 通过 `@ts-ignore` / `as any` 等绕过检查
- ⛔ 只检查部分文件就发布

## 参考

- LSP 规范: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_publishDiagnostics
- 协议: Language Server Protocol 3.17
