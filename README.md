<div align="center">

<a href="https://pawansingh3889.github.io">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=22C55E&center=true&vCenter=true&multiline=true&repeat=true&width=600&height=80&lines=I+break+things%2C+read+source+code;and+ship+fixes+upstream." alt="Typing SVG" />
</a>

# Pawan Singh Kapkoti

Data engineer in food manufacturing. I build pipelines, compliance tools, and local AI for factories where data can't leave the building. I also hack on the open-source tools I depend on.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-FF694B?style=flat-square&logo=dbt&logoColor=white)
![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=flat-square&logo=apacheairflow&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white)
![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=flat-square&logo=databricks&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-4A154B?style=flat-square&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=flat-square&logo=apachespark&logoColor=white)
![Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)

[![Portfolio](https://img.shields.io/badge/Portfolio-0f172a?style=flat-square&logo=googlechrome&logoColor=white)](https://pawansingh3889.github.io)
[![Resume](https://img.shields.io/badge/Resume-PDF-22c55e?style=flat-square&logo=adobeacrobatreader&logoColor=white)](https://github.com/Pawansingh3889/Pawansingh3889/blob/main/Pawan_Singh_Kapkoti_Resume.pdf)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/pawan-singh-kapkoti-100176347)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:pawankapkoti3889@gmail.com)

</div>

---

### What I'm building

<table>
<tr>
<td width="50%" valign="top">

#### [OpsMind](https://github.com/Pawansingh3889/OpsMind)
On-prem AI for food factories. Ask your database questions in English.

```
$ ollama pull phi3:mini
$ streamlit run app.py

> "What was yesterday's yield?"
  → SELECT ... FROM ProductionRuns
  → 94.2% yield, 38kg waste
  → "Yesterday's yield was above target..."
```

`Ollama` `ChromaDB` `LangChain` `SQLAlchemy` `36 tests`

[Docs](https://pawansingh3889.github.io/OpsMind/) &#183; [Code](https://github.com/Pawansingh3889/OpsMind)

</td>
<td width="50%" valign="top">

#### [Compliance Dashboard](https://github.com/Pawansingh3889/manufacturing-compliance-dashboard)
BRC/HACCP food safety. Replaces the Excel spreadsheets.

```
$ make setup && make run

  Traceability score:  97.2%
  Temperature control: 99.1%
  Overall compliance:  PASS
  Batches tracked:     674
  Temp readings:       8,640
```

`Streamlit` `PySpark` `Databricks` `z-score anomaly detection`

[Live](https://manufacturing-compliance-dashboard-mjappkncanejzlfr5ngghik.streamlit.app) &#183; [Code](https://github.com/Pawansingh3889/manufacturing-compliance-dashboard)

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### [UK Crime Pipeline](https://github.com/Pawansingh3889/uk-crime-pipeline)
End-to-end: live API &rarr; PostgreSQL &rarr; dbt &rarr; Streamlit.

```
$ python ingestion/fetch_crimes.py
  Fetching 10 cities × 6 months...
  Loaded 99,675 records (ON CONFLICT DO NOTHING)

$ dbt run && dbt test
  4 models, 53 tests passed
  fct_crimes_by_city: 814 rows
  fct_crime_hotspots: top 100 streets
```

`PostgreSQL` `dbt` `Prefect` `3 CI/CD workflows` `weekly auto-ingest`

[Live](https://uk-crime-pipeline-6nydeza7je8kiwsfl6deuw.streamlit.app/) &#183; [Code](https://github.com/Pawansingh3889/uk-crime-pipeline)

</td>
<td width="50%" valign="top">

#### [SQL Ops Reviewer](https://github.com/Pawansingh3889/sql-ops-reviewer)
GitHub Action that reviews `.sql` in PRs using local AI.

```yaml
# One file. That's the setup.
- uses: Pawansingh3889/sql-ops-reviewer@v1
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
```

```
⚠ WARNING: SELECT * fetches all columns
✗ ERROR: String concatenation → injection risk
  Total: 2 findings across 1 file
```

`GitHub Actions` `Ollama` `zero API keys`

[Code](https://github.com/Pawansingh3889/sql-ops-reviewer)

</td>
</tr>
</table>

---

### Upstream contributions

I fix bugs and ship features in the tools I depend on. 11 projects, 200K+ combined stars.

```
$ git log --oneline --author=pawan | head

drt-hub/drt        → Snowflake connector (290 lines, 7 files, unit tests) ✓ Dockerfile ✓ pre-commit hooks — all merged
vllm (75K★)        → Improved DCP/PCP error messages with actionable backend guidance
superset (65K★)    → Renamed supersetCanCSV → supersetCanDownload across frontend
pandas (45K★)      → Clarified str.cat() return type docs for Index
chromadb (18K★)    → Client/server version compat check + 220-line HNSW tuning guide
plotly (17K★)      → Dependabot config for uv.lock
dbt-core (10K★)    → Removed unnecessary profiler context manager arg
dlt (7K★)          → Migrated flake8 config from tox.ini to ruff
ollama-python (5K★)→ Added exists() method + fixed ShowResponse ValidationError
fpdf2 (1K★)        → Fixed TextRegion.ln() double line break
```

```
merged_prs    = 3    # drt — Snowflake connector, Dockerfile, pre-commit hooks
open_prs      = 10   # vLLM, Superset, ChromaDB, dlt, ollama-python, drt, Qdrant
code_reviews  = 7    # drt, pandas, ollama-python, langsmith-sdk
tests_written = 14   # 8 Snowflake + 6 Discord destination
```

---

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=Pawansingh3889&show_icons=true&theme=github_dark&hide_border=true&count_private=true&include_all_commits=true" alt="GitHub Stats" height="170">
<img src="https://github-readme-streak-stats.herokuapp.com?user=Pawansingh3889&theme=github-dark-blue&hide_border=true" alt="GitHub Streak" height="170">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=Pawansingh3889&theme=github-compact&hide_border=true&area=true" alt="Activity Graph" width="100%">

</div>

---

<div align="center">

*I break things, read source code, and ship fixes upstream.*

Leeds, UK &#183; Open to remote work &#183; [pawankapkoti3889@gmail.com](mailto:pawankapkoti3889@gmail.com)

</div>
