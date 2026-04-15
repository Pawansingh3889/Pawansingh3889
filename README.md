# Pawan Singh Kapkoti

Data & Analytics Engineer. MSc Data Analytics. Yorkshire, UK.

I build data pipelines for manufacturing and public data. I care about data quality, testing, and keeping things simple.

[Portfolio](https://pawansingh3889.github.io)

---

### Projects

**[OpsMind](https://github.com/Pawansingh3889/OpsMind)** — On-prem AI query tool for manufacturing. Factory managers type a question in plain English, OpsMind converts it to SQL and returns results in under 5 seconds. Built with a LangGraph multi-step agent (6-node state graph), pgvector + ChromaDB for document retrieval, and a SQL validation layer that checks for injection patterns, validates table/column names against the live schema, and enforces row limits. Runs Gemma 3 12B locally via Ollama — no data leaves the factory. Covers 7 business domains: production, waste, orders, compliance, staff, suppliers, and traceability. [docs](https://pawansingh3889.github.io/OpsMind/)

**[Production Analytics Pipeline](https://github.com/Pawansingh3889/production-analytics-pipeline)** — Incremental ETL from a fish production ERP. Extracts 15K+ rows daily from 4 SI Integreater tables, validates with Pydantic, transforms with dbt into staging views and mart tables. Serves data through a FastAPI REST API (11 endpoints) and a Next.js dashboard for shift managers. Orchestrated with Prefect, monitored with Sentry, deployed with Docker and OpenTofu. Covers batch tracking, waterfall yield analysis (RSPCA/GG/Almaria tiers), shelf life management, and OCM scan-back traceability. 53 automated tests.

**[UK Crime Pipeline](https://github.com/Pawansingh3889/uk-crime-pipeline)** — End-to-end pipeline pulling crime data from the Police UK API for 10 UK cities, loading into PostgreSQL and BigQuery, and transforming with dbt. 99,675 records, 65 dbt tests, 3 CI/CD workflows (lint, daily health check, weekly auto-ingest). Includes a declarative data validation layer checking bounds, nulls, and categories before warehouse load, plus SLO monitoring for freshness, completeness, and volume. [streamlit](https://uk-crime-pipeline-6nydeza7je8kiwsfl6deuw.streamlit.app/) / [looker studio](https://lookerstudio.google.com/reporting/9ee83425-04d3-4192-b4e4-de6a73d10211)

**[Compliance Dashboard](https://github.com/Pawansingh3889/manufacturing-compliance-dashboard)** — BRC/HACCP food safety dashboard for fish production. Replaces Excel-based compliance tracking with a live Streamlit app. Full batch traceability from catch area to packed product, real-time temperature monitoring with automatic alerts, allergen matrix covering all 14 EU allergens, and weight variance analysis with z-score anomaly detection. Built for auditors who need answers in seconds, not minutes. [live](https://manufacturing-compliance-dashboard-mjappkncanejzlfr5ngghik.streamlit.app)

**[sql-sop](https://github.com/Pawansingh3889/sql-guard)** — Rule-based SQL linter published on [PyPI](https://pypi.org/project/sql-sop/). 15 rules (5 errors, 10 warnings), 46 tests, 0.08s scans. Catches dangerous patterns like DELETE without WHERE, SQL injection via string concatenation, and SELECT * before they reach production. Runs as a CLI tool, pre-commit hook, and GitHub Action. v0.2.0 adds a fluent API: `SqlGuard().enable("E001").scan(sql)`. `pip install sql-sop`

**[SQL Ops Reviewer](https://github.com/Pawansingh3889/sql-ops-reviewer)** — GitHub Action that reviews .sql files in pull requests using local AI. Pairs with sql-sop for two-layer SQL quality: rule-based pre-commit checks (instant) + AI-powered review in CI (deep analysis).

---

### Open source

I contribute where I can — docs, bug fixes, small features.

[drt](https://github.com/drt-hub/drt) · [pandas](https://github.com/pandas-dev/pandas) · [ChromaDB](https://github.com/chroma-core/chroma) · [pgcli](https://github.com/dbcli/pgspecial) · [ollama](https://github.com/ollama/ollama-python) · [superset](https://github.com/apache/superset) · [plotly](https://github.com/plotly/plotly.py) · [fpdf2](https://github.com/py-pdf/fpdf2)

---

### Stack

Python, SQL, dbt, PostgreSQL, BigQuery, FastAPI, Streamlit, Prefect, LangGraph, Ollama, Docker, Polars, pandas, Pydantic, pytest, GitHub Actions
