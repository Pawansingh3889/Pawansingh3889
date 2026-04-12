# Pawan Singh Kapkoti

Data & Analytics Engineer. I build robust data pipelines, read source code, and ship fixes upstream.

MSc Data Analytics. Building pipelines and dev tools on the side. I believe compliance shouldn't mean spreadsheets and AI shouldn't require the cloud. Yorkshire, UK.

[Portfolio](https://pawansingh3889.github.io)

---

### [Production Analytics Pipeline](https://github.com/Pawansingh3889/production-analytics-pipeline)
Incremental ETL from fish production ERP. Extracts 15K+ rows daily from 4 SI tables.
- Batch-centric run tracking | waterfall yield (RSPCA/GG/Almaria) | OCM scan-back lineage
- Shelf life automation | Dimarco validation | paperwork digitisation
- [FastAPI](https://fastapi.tiangolo.com) REST API (11 endpoints) | [Next.js](https://nextjs.org) dashboard | [Power BI](https://powerbi.microsoft.com) CSV export
- [Prefect](https://www.prefect.io) orchestration | [Sentry](https://sentry.io) monitoring | [n8n](https://n8n.io) visual workflows
- [OpenTofu](https://opentofu.org) IaC | [Docker](https://www.docker.com) sandbox | [Pydantic](https://docs.pydantic.dev) validation | [ruff](https://docs.astral.sh/ruff/) + [mypy](https://mypy-lang.org) | 53 tests

### [OpsMind](https://github.com/Pawansingh3889/OpsMind)
On-prem AI query tool for manufacturing. NL-to-SQL in 5 seconds. [docs](https://pawansingh3889.github.io/OpsMind/)
- 19 tables | 7 business domains | 8 pre-built queries | 3 production alerts
- [LangGraph](https://langchain-ai.github.io/langgraph/) multi-step agent (6-node state graph)
- [PostgreSQL](https://www.postgresql.org) [pgvector](https://github.com/pgvector/pgvector) + [ChromaDB](https://www.trychroma.com) RAG backends
- [Gemma 3 12B](https://ai.google.dev/gemma) via [Ollama](https://ollama.com) | read-only SQL enforcement | [Sentry](https://sentry.io) monitoring

### [Compliance Dashboard](https://github.com/Pawansingh3889/manufacturing-compliance-dashboard)
BRC/HACCP food safety for fish production. [live](https://manufacturing-compliance-dashboard-mjappkncanejzlfr5ngghik.streamlit.app)
- Batch traceability: catch area to packed product including OCM scan-back lineage
- Temperature monitoring linked to shelf life extensions (+2/+3 superchill)
- Allergen matrix (fish, crustaceans, molluscs, wheat, egg, milk, mustard)
- Weight variance reconciliation | golden rule enforcement | z-score anomaly detection | [Sentry](https://sentry.io) monitoring

### [sql-sop](https://github.com/Pawansingh3889/sql-guard)
Rule-based SQL linter published to [PyPI](https://pypi.org/project/sql-sop/). 195+ monthly downloads. [`pip install sql-sop`](https://pypi.org/project/sql-sop/)
- 15 rules | 21 tests | compiled regex for 0.08s scans across 200 files
- Pre-commit hook + GitHub Action | 6-layer safety architecture
- Used in production pipelines to lint SQL before it reaches ERP databases

### [UK Crime Pipeline](https://github.com/Pawansingh3889/uk-crime-pipeline)
99,675 records across PostgreSQL and BigQuery. [streamlit](https://uk-crime-pipeline-6nydeza7je8kiwsfl6deuw.streamlit.app/) · [looker studio](https://lookerstudio.google.com/reporting/9ee83425-04d3-4192-b4e4-de6a73d10211)
- [dbt](https://www.getdbt.com) staging/marts with 65 tests (53 PostgreSQL + 12 BigQuery)
- 3 CI/CD workflows | idempotent upserts | retry with backoff
- [Looker Studio](https://lookerstudio.google.com) dashboard on [BigQuery](https://cloud.google.com/bigquery) | [Streamlit](https://streamlit.io) on [PostgreSQL](https://www.postgresql.org)

### [SQL Ops Reviewer](https://github.com/Pawansingh3889/sql-ops-reviewer)
GitHub Action reviewing `.sql` in PRs using local AI.
- Pairs with sql-sop for two-layer SQL quality
- Rule-based pre-commit (instant) + AI review in CI (deep)

---

**Open source** — contributed 5 destination connectors to [drt](https://github.com/drt-hub/drt) (ClickHouse, Parquet, Teams, CSV/JSON) shipping in v0.5, plus the official connector tutorial. Also contributed to [pandas](https://github.com/pandas-dev/pandas), [ChromaDB](https://github.com/chroma-core/chroma), [pgcli](https://github.com/dbcli/pgspecial), [Electricity Maps](https://github.com/electricitymaps/electricitymaps-contrib), and [Open Climate Fix](https://github.com/openclimatefix/open-source-quartz-solar-forecast).

---

**Stack:** [Python](https://python.org) · [SQL](https://en.wikipedia.org/wiki/SQL) · [Bash](https://www.gnu.org/software/bash/) · [FastAPI](https://fastapi.tiangolo.com) · [Next.js](https://nextjs.org) · [Streamlit](https://streamlit.io) · [dbt](https://www.getdbt.com) · [Prefect](https://www.prefect.io) · [n8n](https://n8n.io) · [PostgreSQL](https://www.postgresql.org) · [BigQuery](https://cloud.google.com/bigquery) · [SQLite](https://www.sqlite.org) · [DuckDB](https://duckdb.org) · [pgvector](https://github.com/pgvector/pgvector) · [ChromaDB](https://www.trychroma.com) · [Pydantic](https://docs.pydantic.dev) · [SQLAlchemy](https://www.sqlalchemy.org) · [pandas](https://pandas.pydata.org) · [LangGraph](https://langchain-ai.github.io/langgraph/) · [Ollama](https://ollama.com) · [Docker](https://www.docker.com) · [OpenTofu](https://opentofu.org) · [Sentry](https://sentry.io) · [ruff](https://docs.astral.sh/ruff/) · [mypy](https://mypy-lang.org) · [pytest](https://docs.pytest.org) · [GitHub Actions](https://github.com/features/actions) · [pre-commit](https://pre-commit.com) · [Power BI](https://powerbi.microsoft.com) (PL-300) · [Looker Studio](https://lookerstudio.google.com)
