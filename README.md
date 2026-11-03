# Pawan Singh Kapkoti

**Data engineer.** I build pipelines and data products where the numbers can be trusted: checked before they move, loaded once, and defined in one place.

<a href="https://linkedin.com/in/pawan-singh-kapkoti-100176347/details/connected-accounts/"><img src="https://img.shields.io/badge/GitHub%20Copilot%20Proficiency-Intermediate%20(verified)-8957e5?style=flat-square&logo=githubcopilot&logoColor=white" alt="GitHub Copilot Proficiency: Intermediate, verified by GitHub Learn"></a>
<a href="https://pypi.org/project/sql-sop"><img src="https://img.shields.io/pypi/v/sql-sop?style=flat-square&label=sql-sop&color=3775A9" alt="sql-sop on PyPI"></a>
<a href="https://linkedin.com/in/pawan-singh-kapkoti-100176347"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"></a>

MSc Data Analytics, Aston University. Previously a data analyst at a UK seafood processor (batch traceability, yield and audit data on SQL Server). Co-founder of [Rigel ERP](https://rigel.kapkotisolution.com), where I lead the technical side.

## Selected work

### [UK Crime Pipeline](https://github.com/Pawansingh3889/uk-crime-pipeline): Snowflake, dbt, Airflow

Police UK data for 10 cities, from API to tested marts.

- **Idempotent loads.** Files land in a Snowflake stage, `COPY INTO` a temporary table, then `MERGE` on the natural key with `QUALIFY ROW_NUMBER()` to drop in-batch duplicates. Loading the same month twice inserted 17,534 rows, then 0.
- **One set of models, two warehouses.** The dbt project (6 models, 31 tests, source freshness) runs on Snowflake and PostgreSQL. Postgres-only SQL was replaced with portable SQL to get there.
- **Least privilege.** Separate loader and transformer roles, a key-pair service user, an X-Small auto-suspend warehouse and a monthly credit limit.
- **Orchestration with honest trade-offs.** An Airflow DAG (load, freshness, `dbt build`, retries) for the Snowflake path; a weekly GitHub Actions schedule for the free hosted Postgres version, because an always-on Airflow server is not worth the cost for it.

[Live dashboard](https://uk-crime-pipeline-6nydeza7je8kiwsfl6deuw.streamlit.app/) · [Runbook](https://github.com/Pawansingh3889/uk-crime-pipeline/blob/main/RUNBOOK.md)

### [Rigel ERP](https://rigel.kapkotisolution.com): reporting layer for an ERP I co-founded

A live, phone-first ERP for Indian workshops and traders (code is private).

- **One definition per number.** A metric registry of 25 headline figures, one function each, shared by the dashboard, reports, Excel, PDF and the AI assistant, so they cannot disagree.
- **Permissions inside the database,** checked per figure and per login, so a storekeeper sees stock but never margins, on every surface.
- **History that does not drift.** Nightly snapshots; a missed night shows "not available", never zero.
- **AI that cannot invent numbers.** The model picks an approved metric and period; code computes the value. A money question with no approved metric is refused.

PostgreSQL on Supabase, 469 append-only migrations, 29 edge functions, CI with type checks, unit and browser tests on every pull request.

### [sql-sop](https://github.com/Pawansingh3889/sql-sop): SQL safety linter on PyPI

Catches dangerous SQL before it reaches production: a `DELETE` or `UPDATE` with no `WHERE`, injection-prone string building, T-SQL pitfalls, SQL inside Python, and dbt project issues. 48 rules, 489 tests, 14 releases, 3,100+ downloads in six months. Runs as a CLI, pre-commit hook and GitHub Action.

### [Governed Agent Stack](https://github.com/Pawansingh3889/governed-agent-stack): auditable database agents

On-prem building blocks for pointing an AI agent at a real database safely: read-only access, schema discovery, a query linter in the loop and an audit trail. Home of FloorMind, a plain-English query tool for factory data. In development.

## How I work

- **Make it safe to run twice.** Retries and backfills should never duplicate data.
- **Fail loudly.** Zero rows from a source is an error, not a successful run.
- **Define once, reuse everywhere.** Metrics, permissions and tests live in one place.
- **Least privilege by default,** for people, services and AI.
- **Tests and CI on every model and pull request.**
- **Write the trade-off down,** including what I chose not to build.

## Stack

**Data:** SQL (PostgreSQL, SQL Server, Snowflake) · dbt · Apache Airflow · Python (pandas, pytest) · Power BI
**Platform:** Docker · GitHub Actions · Supabase · Cloudflare · Git
**AI:** NL-to-SQL with guardrails · MCP servers · local LLMs (Ollama)

## Also built

- [Elenchus](https://github.com/Pawansingh3889/elenchus): surveys answered through a guided AI conversation. FastAPI, PostgreSQL, Next.js. [Demo](https://frontend-three-zeta-45.vercel.app)
- [morning-brief](https://github.com/Pawansingh3889/morning-brief): rule-based daily Gmail triage on PyPI. No LLM, read-only OAuth.
- [beauty-review-analysis](https://github.com/Pawansingh3889/beauty-review-analysis): Sephora review analysis from a data science internship.

## Now

Open to **Data Engineering** and **Analytics Engineering** roles in India (ready to relocate) or remote. Going deeper on Snowflake, dbt incremental models and Copilot-assisted workflows.

[Email](mailto:pawankapkoti3889@gmail.com) · [LinkedIn](https://linkedin.com/in/pawan-singh-kapkoti-100176347) · [kapkotisolution.com](https://kapkotisolution.com)
