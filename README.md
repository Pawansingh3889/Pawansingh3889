# Pawan Singh Kapkoti

Data & Analytics Engineer. I build robust data pipelines, read source code, and ship fixes upstream (pandas, drt, ChromaDB).

MSc Data Analytics. I believe compliance shouldn't mean spreadsheets and AI shouldn't require the cloud. Yorkshire, UK.

[Portfolio](https://pawansingh3889.github.io) · [Resume](https://github.com/Pawansingh3889/Pawansingh3889/blob/main/Pawan_Singh_Kapkoti_Resume.pdf) · [LinkedIn](https://linkedin.com/in/pawan-singh-kapkoti-100176347)

---

**[sql-sop](https://github.com/Pawansingh3889/sql-guard)** — rule-based SQL linter I built and published to PyPI. 15 rules, 21 tests, compiled regex for 0.08s scans. Pre-commit hook + GitHub Action — catches DELETE without WHERE before it hits production. [`pip install sql-sop`](https://pypi.org/project/sql-sop/)

**[OpsMind](https://github.com/Pawansingh3889/OpsMind)** — on-prem AI for factories. NL-to-SQL across 147 tables, RAG document search, 36 pytest tests, CI/CD on every push. Read-only SQL enforcement blocks INSERT/UPDATE/DELETE. Runs on Ollama — no data leaves the network. [docs](https://pawansingh3889.github.io/OpsMind/)

**[UK Crime Pipeline](https://github.com/Pawansingh3889/uk-crime-pipeline)** — 99,675 records across PostgreSQL and BigQuery. dbt staging/marts pattern with 12 BigQuery tests + 53 PostgreSQL tests. 3 CI/CD workflows, idempotent upserts, retry with backoff. Looker Studio dashboard on BigQuery marts, Streamlit on PostgreSQL. [streamlit](https://uk-crime-pipeline-6nydeza7je8kiwsfl6deuw.streamlit.app/) · [looker studio](https://lookerstudio.google.com/reporting/9ee83425-04d3-4192-b4e4-de6a73d10211)

**[SQL Ops Reviewer](https://github.com/Pawansingh3889/sql-ops-reviewer)** — GitHub Action that reviews `.sql` in PRs using local AI. Pairs with sql-sop for two-layer SQL quality: rule-based pre-commit (instant) + AI review in CI (deep).

**[Compliance Dashboard](https://github.com/Pawansingh3889/manufacturing-compliance-dashboard)** — BRC/HACCP food safety. Batch traceability, z-score temperature anomaly detection, allergen matrix. Error handling on all I/O modules, pytest coverage on core paths. [live](https://manufacturing-compliance-dashboard-mjappkncanejzlfr5ngghik.streamlit.app)

---

Open source — contributed 5 destination connectors to [drt](https://github.com/drt-hub/drt) (ClickHouse, Parquet, Teams, CSV/JSON) now shipping in v0.5, plus the official connector tutorial. Also contributed to [pandas](https://github.com/pandas-dev/pandas), [ChromaDB](https://github.com/chroma-core/chroma), [pgcli](https://github.com/dbcli/pgspecial), [Electricity Maps](https://github.com/electricitymaps/electricitymaps-contrib), and [Open Climate Fix](https://github.com/openclimatefix/open-source-quartz-solar-forecast).
