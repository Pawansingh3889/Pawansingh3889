# Pawan Singh Kapkoti

Data engineer. I break things, read source code, and ship fixes upstream.

MSc Data Analytics. Building pipelines and dev tools on the side. I believe compliance shouldn't mean spreadsheets and AI shouldn't require the cloud. Yorkshire, UK.

### Find me around the web

[Portfolio](https://pawansingh3889.github.io) · [LinkedIn](https://www.linkedin.com/in/pawan-singh-kapkoti-100176347) · [Email](mailto:pawankapkoti3889@gmail.com)

---

### Dev tools on PyPI

**[sql-sop](https://github.com/Pawansingh3889/sql-guard)** — SQL linter on [PyPI](https://pypi.org/project/sql-sop/). 37 rules (5 T-SQL specific), 143 tests, libCST-based injection scanner, inline `-- sql-guard: disable` directives, `.sql-guard.yml` config, SARIF output for GitHub Code Scanning. 195+ monthly downloads. `pip install sql-sop`

**[pr-sop](https://github.com/Pawansingh3889/pr-sop)** — PR governance checker on [PyPI](https://pypi.org/project/pr-sop/). 3 config-driven checks (CHANGELOG drift, version consistency, pre-commit rev pins), 29 tests, pydantic v2 config, runs as CLI, pre-commit hook, or GitHub Action. First external consumer: sql-sop itself. `pip install pr-sop`

**[morning-brief](https://github.com/Pawansingh3889/morning-brief)** — Rule-based daily Gmail triage on [PyPI](https://pypi.org/project/morning-brief/). Zero LLM, read-only OAuth. Classifies last day of mail into HIGH / MEDIUM / LOW / SPAM via YAML rules, writes a markdown digest, fires a desktop toast. v0.3.0 adds sub-day windows, thread collapse, and `preview` / `why` commands for rule debugging. `pip install morning-brief`

---

### Data pipelines

**[Production Analytics Pipeline](https://github.com/Pawansingh3889/production-analytics-pipeline)** — Incremental ETL from fish production ERP. 15K+ rows/day, FastAPI (11 endpoints) + Next.js + Power BI, Prefect orchestration, Docker + OpenTofu. 53 tests.

**[UK Crime Pipeline](https://github.com/Pawansingh3889/uk-crime-pipeline)** — Police UK API → PostgreSQL + BigQuery. 99,675 records, 6 dbt marts, 65 tests, Polars ingestion, SLO monitoring. [streamlit](https://uk-crime-pipeline-6nydeza7je8kiwsfl6deuw.streamlit.app/) · [looker studio](https://lookerstudio.google.com/reporting/9ee83425-04d3-4192-b4e4-de6a73d10211) · [hugging face](https://huggingface.co/spaces/pawankapkoti/uk-crime-analytics)

---

### AI / on-prem apps

**[OpsMind](https://github.com/Pawansingh3889/OpsMind)** — On-prem AI for manufacturing. NL-to-SQL in 5s, LangGraph agent, MCP server architecture, pgvector + ChromaDB RAG, Gemma 3 12B via Ollama. Golden-set eval harness with failure-mode taxonomy. [docs](https://pawansingh3889.github.io/OpsMind/)

**[Manufacturing Compliance Dashboard](https://github.com/Pawansingh3889/manufacturing-compliance-dashboard)** — BRC/HACCP food safety compliance. MCP server exposes 5 compliance tools for LLM agents, NL query interface for auditors, z-score anomaly detection, Four Golden Signals `/metrics` endpoint. [live](https://manufacturing-compliance-dashboard-mjappkncanejzlfr5ngghik.streamlit.app)

**[SQL Ops Reviewer](https://github.com/Pawansingh3889/sql-ops-reviewer)** — GitHub Action that auto-reviews `.sql` files in PRs using local AI. Catches injection risks, performance anti-patterns, style violations. One YAML file to set up, runs on the CI runner, zero API keys.

**[MediAsk](https://github.com/Pawansingh3889/Hackathon-mediask)** — Health Q&A platform for factory workers. NHS-verified guidance, Gemini responses, voice input, 18 languages. Flask + PostgreSQL, Dockerised. [live](https://hackathon-ioqp.onrender.com)

---

### Open source

**[drt](https://github.com/drt-hub/drt)** — Triage Collaborator. Shipped multi-sync orchestration (`drt run --all`, `--select tag:`, `--threads N`) with a thread-safe StateManager and 11 parallel-dispatch tests. Plus 5 destination connectors, the official [connector tutorial](https://github.com/drt-hub/drt/pull/332), Docker support, and pre-commit hooks — all merged.

**[sql-sop](https://github.com/Pawansingh3889/sql-guard)** — Maintainer. Review and merge community PRs (W011 union-without-all, W012 group-by-ordinal, W005-template adoption), publish to PyPI, maintain governance + security policy, triage issues. First-PR-wins soft-assignment policy in place.

**[pr-sop](https://github.com/Pawansingh3889/pr-sop)** — Creator and maintainer. Shipped v0.1.0 (initial three checks), v0.1.1 (fix for third-party `rev:` pin false positives), and v0.1.2 (fix for CI-merge-commit tag lookup) to PyPI in 24 hours. Full governance, security, contributing, and code-of-conduct documents published.

---

### Signature upstream PRs

Merged contributions into projects I use every day.

- [scanapi/scanapi#868](https://github.com/scanapi/scanapi/pull/868) — `docs: add missing docstrings to spec_evaluator.py` (First Contribution)
- [pyOpenSci/python-package-guide#622](https://github.com/pyOpenSci/python-package-guide/pull/622) — added Turing Way links for `CITATION.cff` and software citation guidance
- [dlt-hub/dlt#3830](https://github.com/dlt-hub/dlt/pull/3830) — updated source count from 5,000 to 8,000+ in intro docs
- [py-pdf/fpdf2#1805](https://github.com/py-pdf/fpdf2/pull/1805) — added Punjabi (`pa`) tutorial translation

---

I learn tools by reading their source: reverse-engineer the architecture, find the gap, ship the fix.

[drt](https://github.com/drt-hub/drt) · [pandas](https://github.com/pandas-dev/pandas) · [ChromaDB](https://github.com/chroma-core/chroma) · [pgcli](https://github.com/dbcli/pgspecial) · [ollama](https://github.com/ollama/ollama-python) · [superset](https://github.com/apache/superset) · [plotly](https://github.com/plotly/plotly.py) · [fpdf2](https://github.com/py-pdf/fpdf2)

---

### Stack

Python, SQL, dbt, PostgreSQL, BigQuery, FastAPI, Streamlit, Prefect, LangGraph, Ollama, Docker, Polars, pandas, Pydantic, pytest, GitHub Actions
