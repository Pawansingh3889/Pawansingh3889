```
$ whoami
```

# Pawan Singh Kapkoti

Data engineer. I break things, read source code, and ship fixes upstream.

`Python` `SQL` `Spark` `dbt` `Docker` `Ollama` `ChromaDB` · Leeds, UK

Open to remote contracts and collaborations.

[Portfolio](https://pawansingh3889.github.io) · [GitHub](https://github.com/Pawansingh3889) · [LinkedIn](https://linkedin.com/in/pawan-singh-kapkoti-100176347) · [Email](mailto:pawankapkoti3889@gmail.com)

---

```
$ cat ./what-i-build
```

**Data pipelines** — API ingestion into PostgreSQL, transformation with dbt (53 tests, staging/marts), batch processing with PySpark, CI/CD with GitHub Actions. Built an end-to-end pipeline processing 99,675 UK crime records from Police API to interactive Streamlit dashboard with 3 automated workflows.

**Factory AI** — on-prem AI assistant for food manufacturing ([OpsMind](https://github.com/Pawansingh3889/OpsMind)). Natural language to SQL, RAG document search via ChromaDB, compliance dashboards. Runs entirely on Ollama — no data leaves the network. 36 pytest tests.

**Compliance tools** — BRC/HACCP food safety dashboard ([live](https://manufacturing-compliance-dashboard-mjappkncanejzlfr5ngghik.streamlit.app)) with batch traceability, FEFO despatch, temperature monitoring, allergen matrix, shelf life risk scoring (EXPIRED/CRITICAL/WARNING), PySpark batch analytics (yield, OEE, excursion rates), one-click PDF audit reports. Running in production.

**Developer tools** — [SQL Ops Reviewer](https://github.com/Pawansingh3889/sql-ops-reviewer): GitHub Action that auto-reviews `.sql` files in PRs using local AI via Ollama. Catches anti-patterns, injection risks, style violations. Drop-in — one YAML file.

---

```
$ git log --oneline --author=pawan | head
```

Contributor to 9 projects. Recent work includes a Snowflake source connector for [drt-hub/drt](https://github.com/drt-hub/drt) (290 lines, 7 files, unit tests), Docker support, and pre-commit hooks — all merged.

| Project | What I shipped |
|---|---|
| `vllm-project/vllm` 75K★ | Improved DCP/PCP error messages with actionable backend guidance |
| `apache/superset` 65K★ | Renamed supersetCanCSV → supersetCanDownload across frontend |
| `pandas-dev/pandas` 45K★ | Clarified str.cat() return type docs; reviewed dropna PR (feedback implemented) |
| `chroma-core/chroma` 18K★ | Client/server version compat check; HNSW tuning guide (220 lines); asyncio fix |
| `dbt-labs/dbt-core` 10K★ | Removed unnecessary profiler context manager arg |
| `dlt-hub/dlt` 7K★ | Migrated flake8 config from tox.ini to ruff |
| `drt-hub/drt` | Snowflake connector ✓ Dockerfile ✓ pre-commit hooks ✓ Discord tests · MySQL PR review |
| `ollama/ollama-python` 5K★ | Added `exists()` method; fixed ShowResponse ValidationError; reviewed 3 PRs |
| `plotly/plotly.py` 17K★ | Dependabot config for uv.lock |
| `py-pdf/fpdf2` 1K★ | Fixed TextRegion.ln() double line break |

---

```
$ cat ./stack
```

```
languages    = ["Python", "SQL", "PySpark", "JavaScript"]
pipeline     = ["dbt", "PostgreSQL", "SQLite", "DuckDB", "SQLAlchemy", "Pandas"]
ai           = ["Ollama", "ChromaDB", "LangChain", "Scikit-Learn", "XGBoost"]
infra        = ["Docker", "GitHub Actions", "AWS", "Azure", "Flask", "Streamlit"]
practices    = ["CI/CD", "pre-commit", "ruff", "mypy", "pytest", "code review"]
```

---

```
$ cat ./current-focus
```

Contributing upstream to the tools I use. Exploring how local LLMs can replace cloud AI in regulated industries — food manufacturing, compliance, audit trails — where data can't leave the building.
