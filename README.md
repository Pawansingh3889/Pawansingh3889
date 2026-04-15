# Pawan Singh Kapkoti

Data & Analytics Engineer. MSc Data Analytics. Yorkshire, UK.

I build data pipelines for manufacturing and public data. I care about data quality, testing, and keeping things simple.

[Portfolio](https://pawansingh3889.github.io)

---

### Projects

**[OpsMind](https://github.com/Pawansingh3889/OpsMind)** — On-prem AI query tool for manufacturing. [docs](https://pawansingh3889.github.io/OpsMind/)
- Ask production questions in plain English, get SQL results in 5 seconds
- LangGraph multi-step agent (6-node state graph) with 5-stage SQL validation
- MCP server architecture: database + doc search as decoupled tool servers
- pgvector + ChromaDB retrieval, runtime-loaded domain docs
- Gemma 3 12B via Ollama — no data leaves the factory
- 7 business domains, formal agent specs, ty type checker in CI

**[Production Analytics Pipeline](https://github.com/Pawansingh3889/production-analytics-pipeline)** — Incremental ETL from fish production ERP
- 15K+ rows daily from 4 SI Integreater tables, validated with Pydantic
- FastAPI REST API (11 endpoints) + Next.js dashboard + Power BI export
- Prefect orchestration, Sentry monitoring, Docker + OpenTofu deployment
- Batch tracking, yield analysis, shelf life management, traceability | 53 tests

**[UK Crime Pipeline](https://github.com/Pawansingh3889/uk-crime-pipeline)** — Police UK API to PostgreSQL and BigQuery. [streamlit](https://uk-crime-pipeline-6nydeza7je8kiwsfl6deuw.streamlit.app/) / [looker studio](https://lookerstudio.google.com/reporting/9ee83425-04d3-4192-b4e4-de6a73d10211) / [hugging face](https://huggingface.co/spaces/pawankapkoti/uk-crime-analytics)
- 99,675 records, 10 cities, 6 dbt marts (including outcome analysis and YoY trends), 65 tests
- Declarative data validation + SLO monitoring (freshness, completeness, volume)
- Polars-based alternative ingestion, pipeline maturity scorecard
- 3 CI/CD workflows with ty type checker, diskcache + stamina for API resilience

**[Compliance Dashboard](https://github.com/Pawansingh3889/manufacturing-compliance-dashboard)** — BRC/HACCP food safety. [live](https://manufacturing-compliance-dashboard-mjappkncanejzlfr5ngghik.streamlit.app) / [hugging face](https://huggingface.co/spaces/pawankapkoti/manufacturing-compliance)
- Full batch traceability from catch area to packed product
- Real-time temperature monitoring with automatic alerts
- Allergen matrix (14 EU allergens), weight variance with z-score anomaly detection

**[sql-sop](https://github.com/Pawansingh3889/sql-guard)** — SQL linter on [PyPI](https://pypi.org/project/sql-sop/). `pip install sql-sop`
- 15 rules, 46 tests, 0.08s scans across 200 files
- Fluent API: `SqlGuard().enable("E001").scan(sql)` (v0.2.0)
- Pre-commit hook + GitHub Action for CI/CD integration

**[SQL Ops Reviewer](https://github.com/Pawansingh3889/sql-ops-reviewer)** — GitHub Action reviewing SQL in PRs
- Rule-based pre-commit (instant) + AI review in CI (deep)
- Pairs with sql-sop for two-layer quality

---

### Open source

I contribute where I can — docs, bug fixes, small features.

[drt](https://github.com/drt-hub/drt) · [pandas](https://github.com/pandas-dev/pandas) · [ChromaDB](https://github.com/chroma-core/chroma) · [pgcli](https://github.com/dbcli/pgspecial) · [ollama](https://github.com/ollama/ollama-python) · [superset](https://github.com/apache/superset) · [plotly](https://github.com/plotly/plotly.py) · [fpdf2](https://github.com/py-pdf/fpdf2)

---

### Stack

Python, SQL, dbt, PostgreSQL, BigQuery, FastAPI, Streamlit, Prefect, LangGraph, Ollama, Docker, Polars, pandas, Pydantic, pytest, GitHub Actions
