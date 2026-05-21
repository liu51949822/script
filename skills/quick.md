# quick — 快速修复分类

## 简介

用于简单、快速、单文件的修改。适合代码清理、格式化、小 bug 修复等简单任务。

## 使用场景

- 单文件 typo 修复
- 简单配置修改
- 变量重命名
- 添加注释
- 小幅度代码调整
- 重复性简单修改

## 用法

```text
task(category="quick", load_skills=["git-master"],
     prompt="修复 docker/nginx/installcompose.file 中的端口号，将 8080 改为 8081")
```

### 适用判断

| 如果任务... | 分类 |
|-------------|------|
| 影响 1 个文件，改动 < 5 行 | quick |
| 影响 2-3 个文件，改动简单 | quick |
| 需要新建文件 | 非 quick |
| 需要跨多个模块 | 非 quick |
| 涉及逻辑判断 | 非 quick |

## 参考

- 分类: category="quick"
- 适用: 微小的、确定性的修改
- 特点: 快速、低成本、低风险
