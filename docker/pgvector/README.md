# pgvector - PostgreSQL 向量数据库

使用 [pgvector](https://github.com/pgvector/pgvector) 扩展为 PostgreSQL 添加向量相似度搜索能力，支持：

- **精确最近邻搜索** (KNN)
- **近似最近邻搜索** (ANN) — 使用 IVFFlat 或 HNSW 索引
- **多种距离度量**: L2 (欧氏距离)、IP (内积)、Cosine (余弦相似度)
- **兼容 OpenAI / Cohere / HuggingFace 等 Embedding 输出**

适用于 AI 应用：RAG（检索增强生成）、语义搜索、推荐系统等。

---

## 快速开始

### 启动服务

```bash
docker compose -f installcompose.file up -d
```

### 验证安装

```bash
docker exec -it pgvector-server psql -U vector_admin -d vectordb -c "SELECT extversion FROM pg_extension WHERE extname = 'vector';"
```

输出应显示 pgvector 的版本号，例如 `0.7.0`。

---

## 基础使用

### 1. 连接数据库

```bash
docker exec -it pgvector-server psql -U vector_admin -d vectordb
```

### 2. 启用向量扩展

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

### 3. 创建向量表

```sql
CREATE TABLE documents (
    id BIGSERIAL PRIMARY KEY,
    content TEXT,
    metadata JSONB,
    embedding vector(1536)   -- 1536 = OpenAI text-embedding-3-small 的维度
);
```

### 4. 插入向量数据

```sql
INSERT INTO documents (content, metadata, embedding)
VALUES
('PostgreSQL is a powerful RDBMS', '{"source": "wiki"}', '[0.001, 0.002, ...]'::vector),
('pgvector enables vector search', '{"source": "github"}', '[0.003, 0.004, ...]'::vector);
```

### 5. 向量相似度搜索

```sql
-- 余弦相似度（最常用）
SELECT id, content, 1 - (embedding <=> '[0.001, 0.002, ...]'::vector) AS similarity
FROM documents
ORDER BY embedding <=> '[0.001, 0.002, ...]'::vector
LIMIT 10;

-- L2 欧氏距离
SELECT id, content, embedding <-> '[0.001, 0.002, ...]'::vector AS distance
FROM documents
ORDER BY embedding <-> '[0.001, 0.002, ...]'::vector
LIMIT 10;

-- IP 内积
SELECT id, content, embedding <#> '[0.001, 0.002, ...]'::vector AS dot_product
FROM documents
ORDER BY embedding <#> '[0.001, 0.002, ...]'::vector
LIMIT 10;
```

---

## 索引优化

当数据量较大（>1000 条）时，建议创建索引以加速查询。

### IVFFlat 索引（快速构建）

```sql
-- ivfflat 索引需要先聚类，索引创建完成后建议调高 probes
CREATE INDEX ON documents USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);

-- 查询时设置 probes 数量（默认 1，越大越精确但越慢）
SET ivfflat.probes = 10;
```

### HNSW 索引（更高精度、更慢构建）

```sql
-- HNSW 索引无需聚类，精度优于 IVFFlat（从 pgvector 0.5.0 起支持）
CREATE INDEX ON documents USING hnsw (embedding vector_cosine_ops) WITH (m = 16, ef_construction = 200);
```

### 距离算子与索引类型对照

| 距离类型 | 算子 | ivfflat ops | hnsw ops |
|---------|------|-------------|----------|
| L2 欧氏距离 | `<->` | `vector_l2_ops` | `vector_l2_ops` |
| IP 内积 | `<#>` | `vector_ip_ops` | `vector_ip_ops` |
| Cosine 余弦 | `<=>` | `vector_cosine_ops` | `vector_cosine_ops` |

---

## 常用 Embedding 模型维度参考

| 模型 | 维度 |
|------|------|
| OpenAI text-embedding-3-small | 1536 |
| OpenAI text-embedding-3-large | 3072 |
| Cohere embed-english-v3.0 | 1024 |
| BAAI/bge-large-zh-v1.5 | 1024 |
| sentence-transformers/all-MiniLM-L6-v2 | 384 |

---

## 配合 Python 使用

```python
import psycopg2
import numpy as np

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="vectordb",
    user="vector_admin",
    password="your_secure_password"
)

# 假设你已经有了 embedding
query_vector = np.random.rand(1536).tolist()

with conn.cursor() as cur:
    cur.execute("""
        SELECT id, content, 1 - (embedding <=> %s::vector) AS similarity
        FROM documents
        ORDER BY embedding <=> %s::vector
        LIMIT 10
    """, (query_vector, query_vector))
    results = cur.fetchall()
    for row in results:
        print(f"ID: {row[0]}, Content: {row[1][:50]}..., Similarity: {row[2]:.4f}")
```

---

## 数据持久化

- 向量数据保存在 `./pgvector-data/` 目录
- 初始化 SQL 脚本放在 `./init-sql/`（启动时自动执行）
- PostgreSQL 配置文件：`./pgvector-conf/postgresql.conf`

### 数据备份

```bash
docker exec pgvector-server pg_dump -U vector_admin -d vectordb > vectordb_backup.sql
```

### 数据恢复

```bash
cat vectordb_backup.sql | docker exec -i pgvector-server psql -U vector_admin -d vectordb
```

---

## 参考链接

- [pgvector GitHub](https://github.com/pgvector/pgvector)
- [pgvector Docker Hub](https://hub.docker.com/r/pgvector/pgvector)
- [PostgreSQL 官方文档](https://www.postgresql.org/docs/current/)
