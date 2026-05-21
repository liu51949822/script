# GitHub Actions 工作流集合

> 共 10 个工作流 | 放到 `.github/workflows/` 目录下使用

## 工作流列表

| 工作流 | 文件 | 触发方式 | 说明 |
|--------|------|----------|------|
| 🐳 Docker 构建推送 | `docker-build-push.yml` | push / 手动 | 检测变更的 docker 目录，构建并推送镜像 |
| 🔍 Compose 验证 | `docker-compose-validate.yml` | PR / push / 手动 | 验证 YAML 语法、检查必需字段、检测端口冲突 |
| 📝 README 同步 | `repo-readme-sync.yml` | push / 手动 | compose 文件变更时自动更新 README |
| 🚀 自动发布 | `auto-release.yml` | tag push | 推送 v* tag 时自动创建 Release |
| 📤 SSH 部署 | `deploy-ssh.yml` | push / 手动 | 同步文件到远程服务器并重启服务 |
| 🕐 Issue 清理 | `stale-issues.yml` | 定时 / 手动 | 自动关闭 60 天无活动的 Issue |
| 🔄 镜像同步 | `sync-mirror.yml` | push / 定时 / 手动 | 同步到 Gitee 等镜像仓库 |
| 📦 定时备份 | `backup-schedule.yml` | 定时 / 手动 | 每周备份到 Release，保留最近 5 个 |
| 🔒 安全审计 | `security-audit.yml` | push / PR / 定时 | Gitleaks + CodeQL + 密码检查 |
| 🏷️ 自动标签 | `auto-labeler.yml` | PR | 根据 PR 内容自动添加标签 |

## 使用方式

### 1. 复制到仓库

```bash
# 将所有工作流复制到你的仓库
cp gitaction/*.yml /path/to/your-repo/.github/workflows/
```

### 2. 配置 Secrets

在仓库 Settings > Secrets and variables > Actions 中添加：

| Secret | 用于 | 说明 |
|--------|------|------|
| `DOCKERHUB_USERNAME` | docker-build-push | Docker Hub 用户名 |
| `DOCKERHUB_TOKEN` | docker-build-push | Docker Hub 访问令牌 |
| `HOST` | deploy-ssh | 远程服务器 IP/域名 |
| `USERNAME` | deploy-ssh | SSH 用户名 |
| `KEY` | deploy-ssh | SSH 私钥 |
| `PORT` | deploy-ssh | SSH 端口 (默认 22) |
| `GITEE_MIRROR_URL` | sync-mirror | Gitee 镜像仓库 URL |
| `VERCEL_TOKEN` | 可选 | Vercel 部署令牌 |

### 3. 手动触发

大部分工作流支持 `workflow_dispatch`，可在 Actions 页面手动触发。

### 4. 测试 YAML 语法

```bash
# 安装 actionlint 验证
brew install actionlint
actionlint gitaction/*.yml

# 或用 python 快速验证
python3 -c "import yaml; [yaml.safe_load(open(f'gitaction/{f}')) for f in __import__('os').listdir('gitaction') if f.endswith('.yml')]"
```

## 自定义

- `docker-build-push.yml` 中的 `matrix.service` 根据你的服务列表修改
- `deploy-ssh.yml` 中的部署路径 `/opt/scripts` 根据实际修改
- `stale-issues.yml` 中的天数阈值按需调整
- `backup-schedule.yml` 中的 cron 表达式可根据需要修改
