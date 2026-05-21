# lsp_find_references — 查找所有符号引用

## 简介

查找整个工作区中某个符号的所有引用位置。类似于 IDE 中的 "Find All References" (Shift+F12)。用于重构前了解所有使用位置。

## 使用场景

- 重命名/删除符号前确认所有引用位置
- 了解一个函数/类/变量在哪些地方被使用
- 检查 API 的使用范围
- 评估修改某个符号的影响范围
- 发现死代码 (未被引用的导出)

## 用法

```text
lsp_find_references(filePath="文件路径", line=行号, character=列号,
                    includeDeclaration=true/false)
```

| 参数 | 必填 | 说明 |
|------|------|------|
| `filePath` | ✅ | 文件的绝对路径 |
| `line` | ✅ | 行号 (从 1 开始) |
| `character` | ✅ | 列号 (从 0 开始) |
| `includeDeclaration` | 可选 | 是否包含声明本身 (默认不包含) |

## 示例

```text
# 查找 authHelper 的所有引用 (不含声明)
lsp_find_references(filePath="/project/src/auth/helper.ts",
                    line=1, character=0)

# 查找所有引用 (含声明行)
lsp_find_references(filePath="/project/src/auth/helper.ts",
                    line=1, character=0,
                    includeDeclaration=true)
```

## 实际场景

### 重构前检查

```text
# 在替换某个函数签名前，先查看所有调用处
lsp_find_references(filePath="/project/src/utils/format.ts",
                    line=22, character=14)
```

### 分析依赖范围

```text
# 查看某个工具函数是否还被使用
lsp_find_references(filePath="/project/src/utils/legacy.ts",
                    line=3, character=5)
```

## 参考

- LSP 规范: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_references
- 协议: Language Server Protocol 3.17
