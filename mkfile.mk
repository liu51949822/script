# 自用脚本集合

## 目录结构

| 目录 | 说明 | 数量 |
|------|------|------|
| `docker/` | Docker Compose 服务配置 | 92 个服务 |
| `base/` | Shell 运维脚本 | 10 个脚本 |
| `python/` | Python 工具脚本 | 10 个脚本 |
| `gitaction/` | GitHub Actions 工作流 | 1 个 |

## 快速使用

```bash
# 启动服务
cd docker/<service> && docker compose -f installcompose.file up -d

# 批量管理
bash base/compose-up.sh --all

# 健康检查
bash base/health-check.sh

# 生成 README
python3 python/index-generator.py
```
