# Pawan Singh Kapkoti

Data engineer based in the UK. I build small, free, on-prem tools for data and
SQL work, and send fixes upstream to the projects I use. MSc Data Analytics,
Aston.

[Portfolio](https://pawan-portfolio.pawankapkoti3889.workers.dev) ·
[Governed Agent Stack](https://github.com/Pawansingh3889/governed-agent-stack) ·
[LinkedIn](https://www.linkedin.com/in/pawan-singh-kapkoti-100176347) ·
[PyPI](https://pypi.org/user/pawansingh3889/)

## On-prem AI / agents

- **[governed-agent-stack](https://github.com/Pawansingh3889/governed-agent-stack)**:
  free, on-prem building blocks for an AI agent you can point at a real database
  and audit. schema-scout maps the data, sql-explorer-mcp and sql-sop fence in
  read-only access, FloorMind reasons, and agent-blackbox keeps a tamper-evident
  record.
- **[FloorMind](https://github.com/Pawansingh3889/FloorMind)**: on-prem
  natural-language-to-SQL over manufacturing data. A LangGraph agent, a local
  LLM via Ollama, sql-sop validation, and a tamper-evident audit log.
  Eval-measured.
- **[agent-blackbox](https://github.com/Pawansingh3889/agent-blackbox)**: an
  append-only, hash-chained ledger that gives agent actions a tamper-evident
  audit trail. On-prem, zero dependencies.
- **[sql-explorer-mcp](https://github.com/Pawansingh3889/sql-explorer-mcp)**:
  read-only MCP server for SQL Server, Postgres, and SQLite, with a three-layer
  safety stack. `pip install sql-explorer-mcp`

## Tools

- **[schema-scout](https://github.com/Pawansingh3889/schema-scout)**:
  reverse-engineers a SQL Server database into an AI-ready catalog. Infers the
  undeclared foreign keys, flags PII, scores how AI-ready the schema is, and
  renders an offline dashboard. Runs entirely on-prem.
- **[sql-sop](https://github.com/Pawansingh3889/sql-guard)**: a SQL linter
  that catches dangerous and non-conforming SQL in CI and pre-commit.
  `pip install sql-sop` · [browser playground](https://pawansingh3889.github.io/sql-guard/)
- **[sql-sop-mcp](https://github.com/Pawansingh3889/sql-sop-mcp)**: an MCP
  server wrapping the linter, so Claude / Cursor / any MCP client can call it.
  `pip install sql-sop-mcp`
- **[pr-sop](https://github.com/Pawansingh3889/pr-sop)**: small PR-governance
  checks: changelog drift, version mismatch, stale pre-commit pins.
  `pip install pr-sop`
- **[morning-brief](https://github.com/Pawansingh3889/morning-brief)**:
  rule-based Gmail triage, read-only, no LLM. `pip install morning-brief`

## Data pipelines

- **[production-analytics-pipeline](https://github.com/Pawansingh3889/production-analytics-pipeline)**:
  incremental ETL from a manufacturing ERP. FastAPI + Next.js + Power BI,
  Prefect orchestration, 53 tests.
- **[uk-crime-pipeline](https://github.com/Pawansingh3889/uk-crime-pipeline)**:
  Police UK API into PostgreSQL and BigQuery. dbt marts, ~100k records,
  Polars ingestion.

## Tech

Python · SQL Server / PostgreSQL · dbt · pandas / Polars · FastAPI ·
Ollama / LangGraph (on-prem AI) · Docker · GitHub Actions

## Open source

[My pull requests across OSS projects](https://github.com/search?q=is%3Apr+author%3APawansingh3889&type=pullrequests).
