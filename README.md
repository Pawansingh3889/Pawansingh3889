# Pawan Singh Kapkoti

Data & Analytics Engineer. I build robust data pipelines, read source code, and ship fixes upstream.

MSc Data Analytics. Building pipelines and dev tools on the side. I believe compliance shouldn't mean spreadsheets and AI shouldn't require the cloud. Yorkshire, UK.

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
- Docker deployment with isolated Ollama container, structured JSONL audit logging
- Golden-set eval harness (library + LLM paths) with failure-mode taxonomy
- Governance, security policy, and code of conduct published — first-PR-wins assignment

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
- MCP server (5 compliance tools), NL query for auditors, declarative validation, SLO monitoring
- Four Golden Signals `/metrics` endpoint (latency, traffic, errors, saturation) over a rolling window
- Explicit scope-and-limitations contract so users don't form ChatGPT-style expectations

**[sql-sop](https://github.com/Pawansingh3889/sql-guard)** — SQL linter on [PyPI](https://pypi.org/project/sql-sop/). `pip install sql-sop`
- 23 rules (10 errors, 13 warnings) covering DELETE/UPDATE-without-WHERE, implicit cross joins, nested subqueries, unused CTEs, SELECT *, and more
- 78 tests, sqlparse AST parsing, fluent API (`SqlGuard().enable(...).scan(...)`)
- libCST-based Python scanner catches SQL injection in `.execute()` / `.read_sql()` calls (v0.4.0)
- Pre-commit hook + GitHub Action for CI/CD integration, 195+ monthly downloads

**[SQL Ops Reviewer](https://github.com/Pawansingh3889/sql-ops-reviewer)** — GitHub Action reviewing SQL in PRs
- Rule-based pre-commit (instant) + AI review in CI (deep)
- Pairs with sql-sop for two-layer quality

**[ForThePeople UK](https://github.com/Pawansingh3889/forthepeople-uk)** — UK citizen transparency platform. [hugging face](https://huggingface.co/spaces/pawankapkoti/forthepeople-uk)
- 13 council-level dashboards: weather, population, housing, crime, health, transport, education
- 50+ government schemes directory, essential services links
- API response caching and validation layer

---

### Open source

I learn tools by reading their source. I reverse-engineered the [drt](https://github.com/drt-hub/drt) connector architecture, shipped 5 destination connectors, and wrote the official [connector tutorial](https://github.com/drt-hub/drt/pull/332) — all merged. Same approach everywhere: read the internals, find the gap, ship the fix.

[drt](https://github.com/drt-hub/drt) · [pandas](https://github.com/pandas-dev/pandas) · [ChromaDB](https://github.com/chroma-core/chroma) · [pgcli](https://github.com/dbcli/pgspecial) · [ollama](https://github.com/ollama/ollama-python) · [superset](https://github.com/apache/superset) · [plotly](https://github.com/plotly/plotly.py) · [fpdf2](https://github.com/py-pdf/fpdf2)

---

### Stack

Python, SQL, dbt, PostgreSQL, BigQuery, FastAPI, Streamlit, Prefect, LangGraph, Ollama, Docker, Polars, pandas, Pydantic, pytest, GitHub Actions
