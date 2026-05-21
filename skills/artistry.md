# artistry — 非常规问题求解

## 简介

不受常规模式约束的创新求解器。当标准方法无效时，使用创造性方法解决复杂问题。

## 使用场景

- 标准方案无法解决的问题
- 需要跳出框架的创新方案
- 非技术限制下的创造性工程
- 混合多个领域的跨界方案
- 约束条件异常苛刻的问题

## 用法

```text
task(category="artistry", load_skills=[...],
     run_in_background=true,
     prompt="[问题描述 + 尝试过的标准方案 + 为何行不通 + 约束条件]")
```

### 适用判断

```
标准方案有效？ → 用 ultrabrain 或指定分类
标准方案无效？ → 考虑 artistry
需要创新？     → 考虑 artistry
约束太特殊？   → 考虑 artistry
```

## 示例

```text
task(category="artistry", load_skills=[],
     prompt="需要在单片机上运行 ML 推理，但内存只有 256KB。
     标准深度学习框架都不可行。
     约束：不能添加外部硬件，必须实时 (<50ms)。
     请设计一个可行方案。")
```

## 参考

- 分类: category="artistry"
- 适用: 标准路径走不通时
- 特点: 创造力驱动，不受常规限制
