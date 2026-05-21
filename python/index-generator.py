#!/usr/bin/env python3
"""Docker Compose Service Index Generator - 生成服务索引 README"""
import os, sys, yaml

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
DOCKER_DIR = os.path.join(os.path.dirname(SCRIPTS_DIR), 'docker')
OUTPUT = os.path.join(DOCKER_DIR, 'README.md')

CATEGORIES = {
    'databases': ('🗄 数据库', ['pgsql', 'mysql', 'mariadb', 'mongodb', 'neo4j', 'cassandra', 'redis', 'dragonfly', 'couchdb', 'clickhouse', 'cockroachdb', 'arangodb']),
    'timeseries_search': ('📊 时序/搜索', ['elasticsearch', 'influxdb', 'tdengine', 'questdb', 'meilisearch', 'typesense', 'pgvector', 'searxng']),
    'queue': ('💬 消息队列/协调', ['rabbitmq', 'kafka', 'etcd', 'consul']),
    'web': ('🌐 Web/代理', ['nginx', 'caddy', 'traefik', 'nginx-proxy-manager', 'frp', 'pi-hole']),
    'dev': ('🔧 开发工具', ['jenkins', 'gitea', 'sonarqube', 'n8n', 'hasura', 'wekan', 'plane']),
    'mgmt': ('🛠 管理工具', ['portainer', 'dozzle', 'watchtower', 'pgadmin', 'redis-commander', 'mongo-express']),
    'monitor': ('📊 监控/BI', ['prometheus-grafana', 'uptime-kuma', 'netdata', 'loki', 'kibana', 'graylog', 'vector', 'metabase', 'superset', 'airflow']),
    'auth': ('🔐 认证/安全', ['keycloak', 'vault', 'vaultwarden', 'authelia', 'compreface']),
    'storage': ('💾 存储/云盘', ['minio', 'nextcloud', 'paperless-ngx']),
    'cms': ('📝 CMS/博客', ['wordpress', 'ghost', 'directus']),
    'media': ('🎬 媒体/音乐', ['jellyfin', 'photoprism', 'navidrome', 'calibre-web', 'kavita', 'immich']),
    'smart': ('🏠 智能家居/IoT', ['home-assistant', 'emqx', 'node-red', 'mosquitto']),
    'office': ('📄 办公/工具', ['onlyoffice', 'stirling-pdf', 'it-tools', 'privatebin']),
    'ai': ('🤖 AI/LLM', ['ollama', 'open-webui', 'dify', 'flowise']),
    'other': ('📋 其他', ['freshrss', 'linkding', 'shlink', 'homer', 'umami', 'matomo', 'vpn', 'wikijs', 'wireguard-easy']),
}

def get_existing():
    if not os.path.isdir(DOCKER_DIR):
        return set()
    return {name for name in os.listdir(DOCKER_DIR)
            if os.path.isfile(os.path.join(DOCKER_DIR, name, 'installcompose.file'))}

def main():
    existing = get_existing()
    
    lines = [
        '# Docker Compose 脚本集合',
        '',
        f'> 共 {len(existing)} 个服务配置 | 每个目录包含 `installcompose.file`',
        '',
        '## 分类索引',
        '',
        '| 分类 | 服务 |',
        '|------|------|',
    ]
    
    for key, (emoji_name, services) in CATEGORIES.items():
        found = [s for s in services if s in existing]
        if found:
            lines.append(f'| {emoji_name} | {", ".join(found)} |')
    
    lines.extend([
        '',
        '## 使用方式',
        '',
        '```bash',
        '# 启动单个服务',
        'cd docker/<service_name>',
        'docker compose -f installcompose.file up -d',
        '',
        '# 使用脚本批量管理',
        'cd base',
        './compose-up.sh <service_name>  # 启动指定服务',
        './compose-up.sh --all           # 启动所有服务',
        './health-check.sh               # 检查服务状态',
        './backup-volumes.sh             # 备份数据卷',
        '```',
        '',
        '## 工具脚本',
        '',
        '| 目录 | 说明 |',
        '|------|------|',
        '| `base/` | Shell 脚本: 系统信息、Docker 管理、备份、健康检查等 |',
        '| `python/` | Python 工具: YAML 验证、端口检查、密码生成、证书检查等 |',
        '| `gitaction/` | GitHub Actions 工作流 |',
        '',
        '## 注意事项',
        '',
        '- 每个 `installcompose.file` 中的密码占位符 (`your_*_password`) 使用前请修改',
        '- 不同服务间的端口可能有冲突，请根据当前服务调整端口映射',
        '- 生产环境建议使用 Docker Swarm 或 Kubernetes 代替单机 docker compose',
    ])
    
    with open(OUTPUT, 'w') as f:
        f.write('\n'.join(lines) + '\n')
    
    print(f"已生成 {OUTPUT}")

if __name__ == '__main__':
    main()
