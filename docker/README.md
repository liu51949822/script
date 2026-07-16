# Docker Compose 脚本集合

> 共 95 个服务配置 | 每个目录包含 `installcompose.file`

## 分类索引

| 分类 | 服务 |
|------|------|
| 🗄 数据库 | pgsql, mysql, mariadb, mongodb, neo4j, cassandra, redis, dragonfly, couchdb, clickhouse, cockroachdb, arangodb |
| 📊 时序/搜索 | elasticsearch, influxdb, tdengine, questdb, meilisearch, typesense, pgvector, searxng |
| 💬 消息队列/协调 | rabbitmq, kafka, etcd, consul |
| 🌐 Web/代理 | nginx, caddy, traefik, nginx-proxy-manager, frp, pi-hole |
| 🔧 开发工具 | jenkins, gitea, sonarqube, n8n, hasura, wekan, plane |
| 🛠 管理工具 | portainer, dozzle, watchtower, pgadmin, redis-commander, mongo-express |
| 📊 监控/BI | prometheus-grafana, uptime-kuma, netdata, loki, kibana, graylog, vector, metabase, superset, airflow |
| 🔐 认证/安全 | keycloak, vault, vaultwarden, authelia, compreface |
| 💾 存储/云盘 | minio, nextcloud, paperless-ngx |
| 📝 CMS/博客 | wordpress, ghost, directus |
| 🎬 媒体/音乐 | jellyfin, photoprism, navidrome, calibre-web, kavita, immich |
| 🏠 智能家居/IoT | home-assistant, emqx, node-red, mosquitto |
| 📄 办公/工具 | onlyoffice, stirling-pdf, it-tools, privatebin |
| 🤖 AI/LLM | ollama, open-webui, dify, flowise |
| 📋 其他 | freshrss, linkding, shlink, homer, umami, matomo, wikijs, wireguard-easy |

## 使用方式

```bash
# 启动单个服务
cd docker/<service_name>
docker compose -f installcompose.file up -d

# 使用脚本批量管理
cd base
./compose-up.sh <service_name>  # 启动指定服务
./compose-up.sh --all           # 启动所有服务
./health-check.sh               # 检查服务状态
./backup-volumes.sh             # 备份数据卷
```

## 工具脚本

| 目录 | 说明 |
|------|------|
| `base/` | Shell 脚本: 系统信息、Docker 管理、备份、健康检查等 |
| `python/` | Python 工具: YAML 验证、端口检查、密码生成、证书检查等 |
| `gitaction/` | GitHub Actions 工作流 |

## 注意事项

- 每个 `installcompose.file` 中的密码占位符 (`your_*_password`) 使用前请修改
- 不同服务间的端口可能有冲突，请根据当前服务调整端口映射
- 生产环境建议使用 Docker Swarm 或 Kubernetes 代替单机 docker compose
