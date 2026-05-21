# /git-master — Git 操作专家技能

## 简介

Git 版本控制专家，负责所有 Git 相关操作 — 提交、合并、rebase、历史搜索、分支管理等。

## 使用场景

- 创建规范的 Git 提交
- 查看提交历史和文件变更
- 搜索谁写了某段代码、何时添加
- 分支合并和冲突解决
- Rebase 和 squash 操作
- 创建 Pull Request

## 用法

配合 task 使用 git-master 技能：

```text
task(category="quick", load_skills=["git-master"],
     prompt="commit message: 添加用户注册功能\n需要添加的文件: src/auth/register.ts")
```

### 安全规则

- 不修改 git config
- 不执行破坏性操作 (force push 等)
- 不跳过 hooks
- 不在主分支上 force push

## 示例

```text
# 提交代码
task(category="quick", load_skills=["git-master"],
     prompt="提交所有 docker/ 目录的变更，commit message: 'Add nginx compose file'")

# 查看历史
task(category="quick", load_skills=["git-master"],
     prompt="查找 docker/ 目录最近10次提交记录")
```

## 参考

- 命令: `name="git-master"`
- 来源: OhMyOpenCode 内置技能
- 最佳实践: 原子提交、清晰的 commit message
