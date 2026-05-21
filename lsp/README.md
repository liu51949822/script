# LSP (Language Server Protocol) 工具集

> Language Server Protocol — 代码智能分析的标准协议接口

## 目录

| 文档 | 说明 |
|------|------|
| [lsp-goto-definition](./lsp-goto-definition.md) | 跳转到符号定义 |
| [lsp-find-references](./lsp-find-references.md) | 查找所有符号引用 |
| [lsp-symbols](./lsp-symbols.md) | 文件/工作区符号搜索 |
| [lsp-diagnostics](./lsp-diagnostics.md) | 代码错误和警告诊断 |
| [lsp-rename](./lsp-rename.md) | 符号重命名 (重构) |

## LSP 在这里的作用

本环境内置了完整的 LSP 工具链，支持 TypeScript、JavaScript、Python、Go、Rust、Java 等多种语言的代码分析。

## 快速参考

| 工具 | 用途 | 使用频率 |
|------|------|----------|
| lsp_diagnostics | 检查代码错误 | ⭐⭐⭐⭐⭐ 每次修改后必用 |
| lsp_find_references | 查找用法 | ⭐⭐⭐⭐⭐ 重构前必用 |
| lsp_goto_definition | 查看定义 | ⭐⭐⭐⭐ 了解代码时用 |
| lsp_symbols | 搜索符号 | ⭐⭐⭐⭐ 大型项目搜索 |
| lsp_rename | 批量重命名 | ⭐⭐⭐ 安全重构用 |
