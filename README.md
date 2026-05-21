# 自用脚本集合

> 个人运维开发工具箱 — Docker Compose 服务配置、运维脚本、Python 工具、CI/CD 工作流

---

## 📦 目录结构

| 目录 | 说明 | 数量 |
|------|------|------|
| [`docker/`](./docker/README.md) | Docker Compose 服务配置 | 92 个服务 |
| [`base/`](./base/) | Shell 运维脚本 | 15 个脚本 |
| [`python/`](./python/) | Python 工具脚本 | 16 个脚本 + 依赖 |
| [`gitaction/`](./gitaction/README.md) | GitHub Actions 工作流 | 11 个工作流 + 文档 |
| [`skills/`](./skills/) | 代理技能参考文档 | 12 个技能文档 |

---

## 🚀 快速开始

### 克隆仓库

```bash
git clone https://github.com/liu51949822/script.git
cd script
```

### 使用 Docker 服务

```bash
# 查看所有可用服务
ls docker/

# 启动单个服务 (如 PostgreSQL)
cd docker/pgsql
docker compose -f installcompose.file up -d

# 修改密码后启动
sed -i '' 's/your_secure_password/my_new_password/' installcompose.file
docker compose -f installcompose.file up -d
```

### 使用运维脚本

```bash
# 一键启动所有 Docker 服务
bash base/compose-up.sh --all

# 检查容器健康状况
bash base/health-check.sh

# 查看系统信息
bash base/system-info.sh

# 清理 Docker 无用资源
bash base/docker-cleanup.sh

# 更多脚本
ls base/
```

### 使用 Python 工具

```bash
# 安装依赖
pip install -r python/requirements.txt

# 列出所有 docker 服务并验证 YAML
python3 python/compose-validator.py

# 生成安全密码
python3 python/password-generator.py -n 5 -l 24

# 检查 SSL 证书到期
python3 python/cert-expiry.py google.com

# 更多工具
python3 python/text-tools.py uuid
python3 python/json-yaml.py docker/nginx/installcompose.file
```

### 部署 GitHub Actions

```bash
# 所有工作流已部署到 .github/workflows/
# 使用时只需在仓库 Settings > Secrets 中配置对应密钥
```

---

## 📚 分类说明

### 🐳 Docker 服务 (92个)

覆盖常用中间件、数据库、监控、AI 等。详见 [docker/README.md](./docker/README.md)。

**数据库**: pgsql, mysql, mariadb, mongodb, neo4j, cassandra, redis, dragonfly, couchdb, cockroachdb, arangodb, clickhouse
**时序/搜索**: influxdb, tdengine, questdb, elasticsearch, meilisearch, typesense, pgvector
**消息/协调**: rabbitmq, kafka, etcd, consul
**Web/代理**: nginx, caddy, traefik, nginx-proxy-manager, frp, pi-hole
**监控/BI**: prometheus-grafana, uptime-kuma, netdata, loki, kibana, graylog, metabase, superset, airflow
**AI/LLM**: ollama, open-webui, dify, flowise
**认证/安全**: keycloak, vault, vaultwarden, authelia, compreface
**工具/管理**: portainer, dozzle, watchtower, pgadmin, redis-commander, mongo-express
**CMS/博客**: wordpress, ghost, directus
**媒体**: immich, photoprism, jellyfin, navidrome, calibre-web, kavita
**存储**: minio, nextcloud, paperless-ngx
**IoT**: home-assistant, emqx, node-red, mosquitto
**协作**: mattermost, wekan, plane, wikijs

### 🛠 Shell 脚本 (15个)

```bash
base/
├── system-info.sh       # 系统信息收集
├── docker-cleanup.sh    # Docker 资源清理
├── backup-volumes.sh    # Docker 卷备份
├── health-check.sh      # 容器健康检查
├── container-stats.sh   # 容器资源监控
├── compose-up.sh        # 批量启动服务
├── disk-alert.sh        # 磁盘告警
├── port-check.sh        # 端口检查
├── ssl-check.sh         # SSL 证书检查
├── docker-logs.sh       # 容器日志查看
├── git-sync.sh          # Git 一键同步
├── kill-port.sh         # 端口释放
├── code-stats.sh        # 代码统计
├── new-project.sh       # 项目脚手架
└── env-check.sh         # 环境检查
```

### 🐍 Python 工具 (16个)

```bash
python/
├── compose-validator.py   # 验证 Docker Compose YAML
├── password-generator.py  # 安全密码生成
├── cert-expiry.py         # SSL 证书到期检查
├── port-checker.py        # 端口扫描
├── docker-stats.py        # 容器资源分析
├── env-generator.py       # 环境变量提取
├── config-backup.py       # 配置文件备份
├── index-generator.py     # README 索引生成
├── json-yaml.py           # JSON/YAML 互转
├── quick-http.py          # HTTP 服务器
├── markdown-toc.py        # MD 目录生成
├── csv-tools.py           # CSV/JSON 互转
├── text-tools.py          # 文本工具集
├── cron-helper.py         # Cron 表达式
├── yaml-sorter.py         # YAML 排序
└── ip-info.py             # IP 信息
```

---

## ⚙️ 配置说明

### 首次使用

1. 所有 `installcompose.file` 中的占位密码 (`your_*_password`) 必须在部署前修改
2. 不同服务间的端口可能有冲突，请根据实际环境调整端口映射
3. Python 工具需要安装依赖: `pip install -r python/requirements.txt`

### 环境变量

参考 `docker/.env.example` 配置通用环境变量：

```bash
cp docker/.env.example docker/.env
# 编辑 docker/.env 修改密码
```

---

## 🔗 相关链接

- [GitHub 仓库](https://github.com/liu51949822/script)
- [Docker 官方文档](https://docs.docker.com/compose/)
- [GitHub Actions 文档](https://docs.github.com/actions)

---

## 📄 许可

个人自用脚本集合。
