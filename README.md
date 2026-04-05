# Pawan Singh Kapkoti

Data engineer. I break things, read source code, and ship fixes upstream.

Python · SQL · Spark · dbt · Docker · Ollama · ChromaDB · Leeds, UK

Open to remote contracts and collaborations.

[Portfolio](https://pawansingh3889.github.io) · [GitHub](https://github.com/Pawansingh3889) · [LinkedIn](https://linkedin.com/in/pawan-singh-kapkoti-100176347) · [Email](mailto:pawankapkoti3889@gmail.com)

---

## What I build

**Data pipelines** — API ingestion into PostgreSQL, transformation with dbt (53 tests, staging/marts), batch processing with PySpark, CI/CD with GitHub Actions. Built an end-to-end pipeline processing 99,675 UK crime records from Police API to interactive Streamlit dashboard with 3 automated workflows.

**Factory AI** — on-premises AI assistant for food manufacturing ([OpsMind](https://github.com/Pawansingh3889/OpsMind)). Natural language to SQL, RAG document search via ChromaDB, compliance dashboards. Runs entirely on Ollama — no data leaves the network. 36 pytest tests.

**Compliance tools** — BRC/HACCP food safety dashboard ([live](https://manufacturing-compliance-dashboard-mjappkncanejzlfr5ngghik.streamlit.app)) with batch traceability, FEFO despatch, temperature monitoring, allergen matrix, shelf life risk scoring (EXPIRED/CRITICAL/WARNING), PySpark batch analytics (yield, OEE, excursion rates), and one-click PDF audit reports. Used in production at a food manufacturing site.

**Developer tools** — [SQL Ops Reviewer](https://github.com/Pawansingh3889/sql-ops-reviewer): GitHub Action that auto-reviews `.sql` files in pull requests using local AI via Ollama. Catches performance anti-patterns, injection risks, and style violations. Drop-in — one YAML file.

---

## Open source

Contributor to 9 projects. 3 merged PRs to [drt-hub/drt](https://github.com/drt-hub/drt) in a single day — Snowflake source connector (290 lines, 7 files, unit tests), Dockerfile + docker-compose, and pre-commit hooks. Maintainer called the code quality "noticeably above average."

| Project | What I did |
|---|---|
| **vLLM** (75K★) | Improved DCP/PCP error messages with actionable backend guidance |
| **Apache Superset** (65K★) | Renamed supersetCanCSV → supersetCanDownload across frontend |
| **pandas** (45K★) | Clarified str.cat() return type docs; reviewed dropna docstring PR (feedback implemented by author) |
| **ChromaDB** (18K★) | Client/server version compatibility check; HNSW index tuning guide (220 lines); deprecated asyncio fix |
| **dbt-core** (10K★) | Removed unnecessary profiler context manager arg |
| **dlt** (7K★) | Migrated flake8 config from tox.ini to ruff |
| **drt** (Reverse ETL) | Snowflake connector (merged), Dockerfile (merged), pre-commit hooks (merged), Discord tests, MySQL PR code review |
| **ollama-python** (5K★) | Added `exists()` method; fixed ShowResponse ValidationError; reviewed 3 community PRs |
| **Plotly** (17K★) | Dependabot config for uv.lock |
| **fpdf2** (1K★) | Fixed TextRegion.ln() double line break |

---

## Skills

**Languages & data** — Python, SQL, PySpark, JavaScript

**Pipeline & transformation** — dbt, PostgreSQL, SQLite, DuckDB, SQLAlchemy, Pandas

**AI & ML** — Ollama, ChromaDB, LangChain, Scikit-Learn, XGBoost

**Infrastructure** — Docker, GitHub Actions, AWS, Azure, Flask, Streamlit

**Practices** — CI/CD, pre-commit (ruff, mypy), pytest, code review, open source contribution

---

## Current focus

Contributing upstream to the tools I use. Exploring how local LLMs can replace cloud AI in regulated industries — food manufacturing, compliance, audit trails — where data can't leave the building.
