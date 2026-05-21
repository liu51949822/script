# /ai-slop-remover — AI 代码异味清除

## 简介

从代码中移除 AI 代码特有的 "异味" 和模式，同时保留功能完整性。

## 使用场景

- 去除过度注释和不必要的文档字符串
- 清理 AI 生成的冗余代码
- 规范化 AI 特有的命名模式
- 删除无用导入和空 catch 块
- 移除样板代码 (boilerplate)

## 用法

```text
# 对单个文件清理
task(category="unspecified-high", load_skills=["ai-slop-remover"],
     prompt="清理 docker/xxx/installcompose.file")
```

### 清除目标

| AI 异味类型 | 说明 |
|-------------|------|
| 过度注释 | 不需要的解释性注释 |
| 冗余导入 | 未使用的 import |
| 空的 catch/except | catch(e) {} |
| 模板代码 | 不必要的 boilerplate |
| AI 风格命名 | 过于抽象或冗长的命名 |
| 虚假乐观 | 过于乐观的错误处理注释 |

## 参考

- 命令: `name="ai-slop-remover"`
- 来源: OhMyOpenCode 内置技能
- 最佳实践: 每次提交前运行
