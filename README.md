# Pawan Singh Kapkoti

**Factory-floor data engineer.** Yorkshire, UK · MSc Data Analytics (Aston)

Production team leader at a fish-processing plant by day. I turn the problems I
hit on a shift — yield, waste, BRCGS traceability, the numbers that prove all of
it — into reviewable open-source tools any mid-size manufacturing team could
pick up on a Monday.

[Portfolio](https://pawansingh3889.github.io) · [LinkedIn](https://www.linkedin.com/in/pawan-singh-kapkoti-100176347/)

---

## Projects, grouped by where they run

### In the factory

Three tools already deployed at work. All on-prem-first, audit-friendly, no cloud AI.

**[OpsMind](https://github.com/Pawansingh3889/OpsMind)** — on-prem AI query tool. [docs](https://pawansingh3889.github.io/OpsMind/)
English → SQL in 5 seconds. LangGraph 6-node agent · 5-stage SQL validation · MCP servers for database + doc search · Gemma 3 12B via Ollama. No data leaves the factory network. Golden-set eval harness (library + LLM paths) with failure-mode taxonomy.

**[Manufacturing Compliance Dashboard](https://github.com/Pawansingh3889/manufacturing-compliance-dashboard)** — BRC/HACCP food safety. [live](https://manufacturing-compliance-dashboard-mjappkncanejzlfr5ngghik.streamlit.app) · [HF Space](https://huggingface.co/spaces/pawankapkoti/manufacturing-compliance)
Full batch traceability from catch area to packed product in 2 seconds. 14-allergen matrix · z-score weight-variance anomaly detection · Four Golden Signals `/metrics` endpoint · MCP server exposing 5 compliance tools · regex-based NL query for auditors (no LLM required).

**[Production Analytics Pipeline](https://github.com/Pawansingh3889/production-analytics-pipeline)** — incremental ETL from the factory ERP.
15 000+ rows/day from 4 ERP tables · FastAPI (11 REST endpoints) · Next.js dashboard · Power BI export · Prefect orchestration · 53 tests · ScanAPI integration tests on every push · six-layer read-only safety model documented in `SECURITY.md`.

### On PyPI

One package, shipped and downloaded weekly by strangers.

**[sql-sop](https://pypi.org/project/sql-sop/)** — `pip install sql-sop` · **195+ monthly downloads**
SQL linter, 23 rules (10 errors + 13 warnings) covering `DELETE`/`UPDATE`-without-`WHERE`, implicit cross joins, nested subqueries, unused CTEs, plus a libCST-based Python scanner that catches SQL injection in `.execute()` / `.read_sql()` calls. 78 tests · fluent API · pre-commit hook · GitHub Action · v0.4.0.

### For the public

Two projects over UK open data. OGL v3.0 chain documented in `NOTICE`.

**[UK Crime Pipeline](https://github.com/Pawansingh3889/uk-crime-pipeline)** — Police UK API → PostgreSQL + BigQuery. [streamlit](https://uk-crime-pipeline-6nydeza7je8kiwsfl6deuw.streamlit.app/) · [looker studio](https://lookerstudio.google.com/reporting/9ee83425-04d3-4192-b4e4-de6a73d10211) · [HF Space](https://huggingface.co/spaces/pawankapkoti/uk-crime-analytics)
99 675 records · 10 cities · 6 dbt marts (incl. outcome analysis, YoY trends) · 65 tests · declarative data validation · SLO monitoring (freshness, completeness, volume) · Polars-based alternative ingestion · `diskcache` + `stamina` for API resilience.

**[ForThePeople UK](https://github.com/Pawansingh3889/forthepeople-uk)** — citizen transparency platform. [HF Space](https://huggingface.co/spaces/pawankapkoti/forthepeople-uk)
14 council-level dashboards (weather, population, housing, crime, health, transport, education, schemes, elections, jobs, news) · UK postcode slicer (auto-selects region and council) · "View whole UK" national rollup · BBC News + gov.uk announcements feed · explicit political-neutrality clause in `CODE_OF_CONDUCT.md`.

### Adjacent tooling

**[SQL Ops Reviewer](https://github.com/Pawansingh3889/sql-ops-reviewer)** — GitHub Action that AI-reviews SQL in pull requests. Rule-based pre-commit (instant, via sql-sop) + AI review in CI (deep). Two-layer quality.

---

## How these projects are shipped

Every repo above carries the full paperwork a reviewer, recruiter, or lawyer expects
to find: `LICENSE` (Apache 2.0 on apps, MIT on sql-sop for PyPI downstream stability),
`NOTICE` with third-party licence chain, `CONTRIBUTING`, `GOVERNANCE`, `SECURITY`,
`CODE_OF_CONDUCT`, `CHANGELOG`, issue templates, PR template with project-specific
checklist (anonymisation / BRCGS clause / rule-addition walkthrough), CODEOWNERS,
first-PR-wins assignment, welcome workflow, conventional-commit PR-title validator,
Codespaces devcontainers where contributors need them, golden-set eval harnesses on
the AI tools. No AI attribution in commit messages.

The point isn't paperwork theatre. It's that a factory ops team adopting one of these
knows what they're signing up for and what happens when a vulnerability is reported.

---

## Upstream

I learn tools by reading their source first. Recent merges:

- **[drt](https://github.com/drt-hub/drt)** · **Triage Collaborator** · 14 merged PRs including five destination connectors, parallel sync execution (`--threads N` + `--select tag:`), and the [official connector tutorial](https://github.com/drt-hub/drt/pull/332)
- **[Open Climate Fix](https://github.com/openclimatefix)** · vectorised evaluation pipeline (removed per-row iteration), DuckDB query layer for forecast data, prediction-accuracy docs
- **[Electricity Maps](https://github.com/electricitymaps/electricitymaps-contrib)** · GB solar capacity correction using Sheffield Solar's 22 126 MW figure
- **[Apache Superset](https://github.com/apache/superset)** · frontend feature-flag rename (`supersetCanCSV` → `supersetCanDownload`)
- Also: [pandas](https://github.com/pandas-dev/pandas) · [ChromaDB](https://github.com/chroma-core/chroma) · [pgcli](https://github.com/dbcli/pgspecial) · [ollama-python](https://github.com/ollama/ollama-python) · [Plotly](https://github.com/plotly/plotly.py) · [fpdf2](https://github.com/py-pdf/fpdf2) · [dlt](https://github.com/dlt-hub/dlt)

---

## Day job

Production team leader at [Copernus LTD](https://www.copernuslimited.co.uk), a fish-processing plant in Yorkshire. Three years managing yield, waste, BRCGS Issue 9 clauses 3.9 / 3.11 / 8.5.1 records, and the evidence trail that proves every shift ran compliantly.

Every tool in the *In the factory* section above exists because one of those things broke on a Tuesday. The tooling is now the thing I want to keep doing.

---

## Reach me

[LinkedIn](https://www.linkedin.com/in/pawan-singh-kapkoti-100176347/) · [Portfolio](https://pawansingh3889.github.io) · PyCon UK 2026 CFP in progress
