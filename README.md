# Pawan Singh Kapkoti

Data & Analytics Engineer. I build robust data pipelines, read source code, and ship fixes upstream (pandas, drt, ChromaDB).

MSc Data Analytics. Building pipelines and dev tools on the side. I believe compliance shouldn't mean spreadsheets and AI shouldn't require the cloud. Yorkshire, UK.

[Portfolio](https://pawansingh3889.github.io)

---

**[Production Analytics Pipeline](https://github.com/Pawansingh3889/production-analytics-pipeline)**
Incremental ETL from fish production ERP. Extracts 15K+ rows daily from 4 SI tables.
- Batch-centric run tracking | waterfall yield (RSPCA/GG/Almaria) | OCM scan-back lineage
- Shelf life automation | Dimarco validation | paperwork digitisation
- FastAPI REST API (11 endpoints) | Next.js dashboard | Power BI CSV export
- Prefect orchestration | Sentry monitoring | n8n visual workflows
- OpenTofu IaC | Docker sandbox | Pydantic validation | ruff + mypy | 53 tests

**[OpsMind](https://github.com/Pawansingh3889/OpsMind)** — on-prem AI query tool for manufacturing. NL-to-SQL in 5 seconds. 19 tables, 7 domains, 8 pre-built queries, 3 alerts. LangGraph multi-step agent. PostgreSQL pgvector + ChromaDB RAG backends. Gemma 3 12B via Ollama. Read-only — no data leaves the network. [docs](https://pawansingh3889.github.io/OpsMind/)

**[Compliance Dashboard](https://github.com/Pawansingh3889/manufacturing-compliance-dashboard)** — BRC/HACCP food safety for fish production. Batch traceability from catch area to packed product including OCM scan-back lineage. Temperature monitoring linked to shelf life extensions (+2/+3 superchill). Allergen matrix (fish, crustaceans, molluscs, wheat, egg, milk, mustard). Weight variance reconciliation. Golden rule enforcement: RSPCA cascades down, GG never goes up, tails never in RSPCA. z-score anomaly detection. [live](https://manufacturing-compliance-dashboard-mjappkncanejzlfr5ngghik.streamlit.app)

**[sql-sop](https://github.com/Pawansingh3889/sql-guard)** — rule-based SQL linter published to PyPI. 15 rules, 21 tests, compiled regex for 0.08s scans across 200 files. Pre-commit hook + GitHub Action. Used in production pipelines to lint SQL before it reaches ERP databases. Part of a 6-layer safety architecture preventing accidental writes to SI tables. 195+ monthly downloads. [`pip install sql-sop`](https://pypi.org/project/sql-sop/)

**[UK Crime Pipeline](https://github.com/Pawansingh3889/uk-crime-pipeline)** — 99,675 records across PostgreSQL and BigQuery. dbt staging/marts with 65 tests (53 PostgreSQL + 12 BigQuery). 3 CI/CD workflows, idempotent upserts, retry with backoff. Looker Studio dashboard on BigQuery marts, Streamlit on PostgreSQL. [streamlit](https://uk-crime-pipeline-6nydeza7je8kiwsfl6deuw.streamlit.app/) · [looker studio](https://lookerstudio.google.com/reporting/9ee83425-04d3-4192-b4e4-de6a73d10211)

**[SQL Ops Reviewer](https://github.com/Pawansingh3889/sql-ops-reviewer)** — GitHub Action that reviews `.sql` in PRs using local AI. Pairs with sql-sop for two-layer SQL quality: rule-based pre-commit (instant) + AI review in CI (deep).

---

Open source — contributed 5 destination connectors to [drt](https://github.com/drt-hub/drt) (ClickHouse, Parquet, Teams, CSV/JSON) now shipping in v0.5, plus the official connector tutorial. Also contributed to [pandas](https://github.com/pandas-dev/pandas), [ChromaDB](https://github.com/chroma-core/chroma), [pgcli](https://github.com/dbcli/pgspecial), [Electricity Maps](https://github.com/electricitymaps/electricitymaps-contrib), and [Open Climate Fix](https://github.com/openclimatefix/open-source-quartz-solar-forecast).

---

**Stack:**
[Python](https://python.org) | [SQL](https://en.wikipedia.org/wiki/SQL) | [Bash](https://www.gnu.org/software/bash/) |
[FastAPI](https://fastapi.tiangolo.com) | [Next.js](https://nextjs.org) | [Streamlit](https://streamlit.io) |
[dbt](https://www.getdbt.com) | [Prefect](https://www.prefect.io) | [n8n](https://n8n.io) |
[PostgreSQL](https://www.postgresql.org) | [BigQuery](https://cloud.google.com/bigquery) | [SQLite](https://www.sqlite.org) | [DuckDB](https://duckdb.org) |
[pgvector](https://github.com/pgvector/pgvector) | [ChromaDB](https://www.trychroma.com) |
[Pydantic](https://docs.pydantic.dev) | [SQLAlchemy](https://www.sqlalchemy.org) | [pandas](https://pandas.pydata.org) |
[LangGraph](https://langchain-ai.github.io/langgraph/) | [Ollama](https://ollama.com) (Gemma 3 12B) |
[Docker](https://www.docker.com) | [OpenTofu](https://opentofu.org) |
[Sentry](https://sentry.io) | [ruff](https://docs.astral.sh/ruff/) | [mypy](https://mypy-lang.org) | [pytest](https://docs.pytest.org) |
[GitHub Actions](https://github.com/features/actions) | [pre-commit](https://pre-commit.com) |
[Power BI](https://powerbi.microsoft.com) (PL-300) | [Looker Studio](https://lookerstudio.google.com)
