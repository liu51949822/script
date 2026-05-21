# lsp_goto_definition — 跳转到符号定义

## 简介

跳转到光标所在符号的定义位置。类似于 IDE 中的 "Go to Definition" (Cmd+Click / F12)。

## 使用场景

- 查看函数/类/变量的定义
- 了解某个 API 的源代码实现
- 导航到导入模块的声明处
- 检查类型定义的详细信息

## 用法

```text
lsp_goto_definition(filePath="文件路径", line=行号, character=列号)
```

| 参数 | 必填 | 说明 |
|------|------|------|
| `filePath` | ✅ | 文件的绝对路径 |
| `line` | ✅ | 行号 (从 1 开始) |
| `character` | ✅ | 列号 (从 0 开始) |

## 示例

```text
# 查看 src/main.ts 第 10 行第 5 列位置的符号定义
lsp_goto_definition(filePath="/project/src/main.ts",
                    line=10, character=5)
```

## 使用场景示例

### 查看函数定义

当看到一个函数调用但不确定其实现时：

```text
lsp_goto_definition(filePath="/project/src/api/handler.ts",
                    line=42, character=8)
```

### 查看类型定义

当需要了解某个类型的具体定义时：

```text
lsp_goto_definition(filePath="/project/src/types/user.ts",
                    line=15, character=12)
```

## 参考

- LSP 规范: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_definition
- 协议: Language Server Protocol 3.17
