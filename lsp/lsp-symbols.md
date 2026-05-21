# lsp_symbols — 符号搜索

## 简介

获取文件内或整个工作区的符号 (Symbol) 列表。支持按名称搜索、浏览大纲、查找特定函数/类/接口/变量。

## 使用场景

- 获取文件的组织结构 (大纲视图)
- 按名称搜索工作区中的函数/类/接口
- 快速定位某个符号的定义
- 了解大文件的模块结构

## 用法

### 文件内符号 (Document Symbols)

```text
lsp_symbols(filePath="文件路径", scope="document")
```

### 工作区符号搜索 (Workspace Symbols)

```text
lsp_symbols(filePath="文件路径", scope="workspace", query="搜索关键词")
```

| 参数 | 必填 | 说明 |
|------|------|------|
| `filePath` | ✅ | 任意文件的路径 (用于确定 LSP 上下文) |
| `scope` | ✅ | `"document"` 或 `"workspace"` |
| `query` | workspace 时必填 | 符号名搜索关键字 |
| `limit` | 可选 | 最大返回数 (默认 50) |

## 示例

```text
# 获取文件的完整符号列表 (大纲)
lsp_symbols(filePath="/project/src/main.ts", scope="document")

# 在工作区搜索所有包含 "auth" 的符号
lsp_symbols(filePath="/project/src/main.ts", scope="workspace",
            query="auth", limit=30)
```

## 符号类型

LSP 支持搜索的符号类型包括：

- 函数 (Function)
- 类 (Class)
- 接口 (Interface)
- 方法 (Method)
- 变量 (Variable)
- 常量 (Constant)
- 模块 (Module)
- 命名空间 (Namespace)
- 枚举 (Enum)
- 属性 (Property)

## 参考

- LSP 规范: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_documentSymbol
- Workspace 符号: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#workspace_symbol
