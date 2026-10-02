# RIP, vector database

- **ID**: a4d5be1f
- **原文链接**: https://turbopuffer.com/blog/rip-vector-database
- **作者**: Dan Harrison (Engineer)
- **日期**: 2026-09-30
- **分类**: infra
- **来源类型**: article
- **标签**: vector-database、retrieval、storage、architecture
- **质量评分**: 4/5
- **抓取时间**: 2026-10-03 (content-fetcher, opencli web read)

---

## 中文导读

turbopuffer 宣布 v3 存储架构重写：ANN 向量索引从主索引降级为普通二级索引，换用新主索引，文本/正则/向量检索全面提速，并为把更多 SQL 查询（GROUP BY、聚合）搬到 turbopuffer 打基础。回顾演进：v1 以对象存储为真相源，SPANN 分层聚类索引起步后迁移到 SPFresh 支持增量索引，靠极致便宜+够快的向量检索赢得 Cursor、Notion 等早期客户；文档内容全部按 ANN 地址（ClusterId+LocalId）键控存储。v2 加入属性过滤（倒排索引映射到 ANN 地址）与 BM25 全文检索，随后聚合、正则、模糊匹配、稀疏向量等查询形态都长在同一套向量主键布局上。向量主键的代价在三点：存储放大（多向量文档如 late interaction 需为每个向量复制全部内容）、写放大（SPFresh rebalance 移动向量时级联搬运整个文档及其全部倒排索引，调优已边际收益递减）、向量化受限（每种查询计划有最优块大小——DuckDB 2048 行、ClickHouse ~65k、FTS v2 posting 块 256——但主键锁死在 ANN 聚类的 100–200 个文档）。v3 的解法就是不按 ANN 地址做主键；已达成 CI 100% 通过的正确性里程碑，性能打磨公开进行中，基准数据将在达到并超越 v3 性能平价后上线生产。

## 为什么值得关注

ANN 从主键降为二级索引是一个品类信号：向量数据库的差异化护城河正在被通用检索引擎架构吸收，检索基建的走向是通用查询引擎。

## English Summary

turbopuffer announces v3: the ANN vector index is demoted from primary index to just another secondary index, with a new primary index enabling faster text/regex/vector search and a foundation for moving more SQL queries (GROUP BY, aggregations) onto turbopuffer. History: v1 used object storage as source of truth with a SPANN hierarchical clustering index (later SPFresh for incremental indexing), winning early customers like Cursor and Notion with extremely cheap, reasonably fast vector search; all document content was keyed by the ANN address (ClusterId+LocalId). v2 added attribute filtering (inverted index pointing at ANN addresses) and BM25 full-text search, and later aggregations, regex, fuzzy matching, and sparse vectors all grew on the same vector-primary layout. The vector-primary key has three costs: storage amplification (multi-vector documents such as late interaction duplicate full contents per vector), write amplification (SPFresh rebalancing cascades to moving full documents and every inverted index referencing them, with tuning hitting diminishing returns), and limited vectorization (every query plan has an optimal block size - DuckDB 2048 rows, ClickHouse ~65k, FTS v2 postings at 256 - but the ANN primary key constrains blocks to cluster sizes of 100-200 documents). v3's fix is simply not keying on the ANN address; it hit 100% CI passes on correctness, with public benchmark grinding toward and beyond performance parity before production rollout.

## Obsidian 原文摘录（抓取正文头部）

```
# RIP, vector database
> 原文链接: https://turbopuffer.com/blog/rip-vector-database

---

# RIP, vector database

September 30, 2026•Dan Harrison (Engineer)

We are changing turbopuffer's storage architecture to take search to the next level. turbopuffer v3 changes how documents and indexes are laid out, written, compacted, and queried in turbopuffer. It will allow us to make search faster in every respect — including text, regex, and vector search — but it also lays the foundation to move many more SQL queries to turbopuffer and make them fast.

turbopuffer launched as a [serverless vector database (v1)](https://x.com/Sirupsen/status/1709602855160869275), highly specialized to the task of serving extremely cheap and reasonably fast vector searches. Object storage as the source of truth gave the economics, and tiered NVMe SSD/memory caches gave the performance. The value of these particular tradeoffs was validated by our earliest customers, including Cursor and Notion.

turbopuffer evolved to have very strong text and regex search (v2), and is being used for many non-search use cases, like [Linear's syncing engine](https://linear.app/now/rebuilding-delta-sync-read-path). The query engine has evolved along the way to support all of these query plans, but the storage architecture has remained largely unchanged: the ANN vector index was and still is the primary index around which all other indexes and query plans revolve. This design has constrained several query plans, like `GROUP BY` and aggregations.

We've pushed the vector-primary architecture as far as we can, and it's time to move on. We're in the process of moving to a new primary index, and making ANN "just another" secondary index. We thought it might be fun to open up the doors and let you follow along.

For this first update, we'll set the stage with why we're doing this in the first place. Walk with me on a short journey from tpuf v1 to today.

## [](#v1-an-id-and-a-vector)v1: an ID and a vector

In the first version of turbopuffer, documents consisted of nothing but an ID and a vector. The prevailing wisdom at the time was graph-based vector indexes, but a hierarchical clustering index plays better with object storage. We started with [SPANN](https://arxiv.org/abs/2111.08566), and eventually migrated to [SPFresh](https://arxiv.org/abs/2410.14452) to support incremental indexing. Vectors are clustered into groups, whose centroids are clustered in turn, repeated to form a tree with a single root.

```

                      ┌───────────────────┐
                      │   root centroid   │
                      └───────────────────┘
                     ╱          │          ╲
                    ╱           │           ╲
┌───────────────────┐ ┌───────────────────┐ ┌───────────────────┐
│   leaf centroid   │ │   leaf centroid   │ │   leaf centroid   │
└───────────────────┘ └───────────────────┘ └───────────────────┘
      ╱       ╲             ╱       ╲             ╱       ╲
     ╱         ╲           ╱         ╲           ╱         ╲
┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
│ vector │ │ vector │ │ vector │ │ vector │ │ vector │ │ vector │
└────────┘ └────────┘ └────────┘ └────────┘ └────────┘ └────────┘

```

```
      ┌───────────────┐
      │ root centroid │
      └───────────────┘
        ╱     │     ╲
       ╱      │      ╲
┌────────┐┌────────┐┌────────┐
│  leaf  ││  leaf  ││  leaf  │
│centroid││centroid││centroid│
└────────┘└────────┘└────────┘
   ╱  ╲      ╱  ╲      ╱  ╲
┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐
│vec││vec││vec││vec││vec││vec│
└───┘└───┘└───┘└───┘└───┘└───┘
```

We implemented this on top of a storage layer presenting as a key-value map, with sorted and unique keys. Each cluster is given a `ClusterId`, and vectors within each cluster are given a dense `LocalId`.

```rust
```

## Notes

- Content grounded in an opencli web read fetch of the full article (2026-10-03 (content-fetcher, opencli web read)).
- 中文导读 is the entry's summary_zh (light cleanup from the fetched source); 为什么值得关注 is the entry's one_liner; no claims beyond the fetched source text were added.
- Source file cached at /tmp/aaif_turbo.md during the run.
