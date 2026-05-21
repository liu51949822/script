# lsp_rename — 符号重命名

## 简介

对工作区内的符号进行批量重命名。自动更新所有引用位置，确保命名变更后一致性。类似 IDE 中的 "Rename Symbol" (F2)。

## 使用场景

- 重命名函数名使其更清晰
- 修改变量名以符合命名规范
- 重构时统一命名
- 从糟糕的命名改为业务术语

## 用法

### 第一步：检查是否可以重命名

```text
lsp_prepare_rename(filePath="文件路径", line=行号, character=列号)
```

### 第二步：执行重命名

```text
lsp_rename(filePath="文件路径", line=行号, character=列号, newName="新名称")
```

| 参数 | 必填 | 说明 |
|------|------|------|
| `filePath` | ✅ | 文件的绝对路径 |
| `line` | ✅ | 行号 (从 1 开始) |
| `character` | ✅ | 列号 (从 0 开始) |
| `newName` | ✅ (rename) | 新的符号名称 |

## 示例

```text
# 检查是否可重命名
lsp_prepare_rename(filePath="/project/src/auth/login.ts",
                   line=5, character=12)

# 执行重命名: loginUser → authenticateUser
lsp_rename(filePath="/project/src/auth/login.ts",
           line=5, character=12,
           newName="authenticateUser")
```

## 安全规则

| 操作 | 是否允许 |
|------|----------|
| 重命名局部变量 | ✅ |
| 重命名函数 | ✅ |
| 重命名类/接口 | ✅ |
| 重命名导出符号 | ✅ |
| 重命名第三方库中的符号 | ❌ (无法解析) |
| 跨语言重命名 | ❌ (仅限同一语言) |

## 最佳实践

```text
# 1. 先检查所有引用
lsp_find_references(filePath="/project/src/auth/login.ts",
                    line=5, character=12)

# 2. 确认后执行重命名
lsp_rename(filePath="/project/src/auth/login.ts",
           line=5, character=12,
           newName="authenticateUser")

# 3. 验证无残留
lsp_diagnostics(filePath="/project/src/")
```

## 参考

- LSP 规范: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_rename
- 准备重命名: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_prepareRename
