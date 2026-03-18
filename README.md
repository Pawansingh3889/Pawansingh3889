# Pawan Singh Kapkoti

**Data Engineer · Analytics Engineer**
MSc Data Analytics (Aston University, 2:1) · AWS Certified DEA-C01 · Microsoft PL-300 · Remote, UK

---

## What I build

Data pipelines — ingestion, transformation, validation, and deployment. Python ETL, dbt, cloud analytics on AWS and Azure, PostgreSQL, and Streamlit dashboards. Some projects include ML components (XGBoost, Isolation Forest) and local LLM integration.

---

## Projects

### [Apex Data Migration](https://github.com/Pawansingh3889/Apex-Data-Migration)
`Python` `dbt` `DuckDB` `Polars` `XGBoost` `Isolation Forest` `Mistral 7B` `Prefect` `Docker` `Power BI`

Simulates diagnosing and migrating a failing production database — the right way, before touching production.

- **10-task Prefect pipeline** orchestrates all phases automatically with parallel execution, retry logic, and monitoring dashboard
- **Containerised with Docker** — reproducible environment, one command to run the full pipeline
- **XGBoost** CPU spike predictor — 93% accuracy, ROC-AUC 0.97, no data leakage
- **Isolation Forest** unsupervised anomaly detection — independently confirmed both injected production faults
- **Mistral 7B via Ollama** replaced VADER for Portuguese sentiment — fully offline, zero API cost
- **dbt** transformation layer — 7 models, 53 automated quality tests, lineage graph
- **94 automated checks** caught a live LLM label corruption bug before it reached Power BI
- **Power BI** 3-page dashboard — delivery performance (96,470 orders), product sentiment, server health

---

### [UK Crime Analytics Pipeline](https://github.com/Pawansingh3889/uk-crime-pipeline) · [Live Dashboard ↗](https://uk-crime-pipeline-6nydeza7je8kiwsfl6deuw.streamlit.app)
`Python` `PostgreSQL` `dbt-postgres` `Streamlit` `Neon` `GitHub Actions`

Live end-to-end pipeline ingesting real government crime data — publicly deployed.

- Ingests **99,675 crime records** from the Police UK API across 10 cities and 6 months — real live API, not static CSVs
- Loads into **PostgreSQL** with idempotent upserts — safe to re-run without duplicating data
- **dbt** transforms raw data into 4 mart models: crime trends, city comparisons, category breakdowns, street-level hotspots
- **Streamlit dashboard** deployed on Streamlit Cloud with **Neon cloud PostgreSQL** — fully public, zero infrastructure cost
- **GitHub Actions CI/CD** — automated linting, API health checks, dbt validation against a Postgres service container on every push. Weekly scheduled ingestion and daily health monitoring

---

### [UK Crime SQL Analytics](https://github.com/Pawansingh3889/sql-crime-analytics)
`SQL` `PostgreSQL` `Window Functions` `CTEs`

14 analytical SQL queries against 99,673 crime records. Covers city rankings, temporal trends, resolution analysis, and hotspot identification using RANK, ROW_NUMBER, LAG, LEAD, FILTER, STRING_AGG, and self-joins.

---

### [UK Regional Employment Analysis — Excel](https://github.com/Pawansingh3889/uk-employment-excel)
`Excel` `AVERAGEIF` `INDEX/MATCH` `SUMPRODUCT` `Charts` `Data Validation`

Excel workbook analysing employment rates, wages, and unemployment across 12 UK regions (2019–2024). Includes a personal case study using the data to justify relocating from Birmingham to Hull. 5 business questions answered with formulas and charts.

---

### [UK Crime Data Analysis](https://github.com/Pawansingh3889/Crime_Analysis)
`AWS S3` `Glue Crawler` `Athena` `QuickSight`

Serverless AWS analytics pipeline across all 43 UK police forces, 2022–2024. Violence and sexual offences: 5.9M+ incidents. Metropolitan Police volume declined from 1.1M (2022) to 0.95M (2024).

---

### [MSc Dissertation — Ethnicity & Academic Outcomes](https://github.com/Pawansingh3889/MSc-Dissertation-Project)
`Python` `SQL` `Random Forest` `Statistical Testing`

Processed HESA and National Pupil Database data under institutional approval. Identified a 15% performance gap across ethnic groups. Random Forest model: 80% accuracy identifying at-risk students. Submitted to Aston University Mathematics Department.

---

### [OnlyBuddy — Hull Errand App](https://onlybuddy.vercel.app) · [GitHub](https://github.com/Pawansingh3889/onlybuddy)
`React 18` `Firebase` `Stripe` `Google Maps` `Vercel CI/CD` `PWA`

Live production app — community errand and grocery service for Hull. 25 Vercel deployments, Firebase auth + real-time database, Stripe payments, PWA.

---

## Tech stack

| | |
|---|---|
| **Core** | Python 3.11, SQL (window functions, CTEs, aggregations), Git |
| **Data engineering** | dbt Core, Polars, DuckDB, PyArrow, PostgreSQL, ETL/ELT design |
| **Orchestration** | Prefect 3 |
| **AWS** | S3, Glue, Athena, Redshift, QuickSight, CloudWatch, IAM |
| **Azure** | Databricks, Synapse Analytics |
| **ML / AI** | XGBoost, Isolation Forest, Scikit-Learn, Random Forest, Mistral 7B via Ollama |
| **BI & Viz** | Power BI, Streamlit, Plotly, Matplotlib, Seaborn |
| **Cloud DB** | Neon (PostgreSQL serverless) |
| **DevOps** | Docker, Vercel CI/CD, GitHub Actions |
| **Web** | React 18, Firebase, REST APIs |

---

## Certifications

- Microsoft Power BI Data Analyst (PL-300)
- AWS Data Engineer Associate (DEA-C01)
- AWS Cloud Practitioner (CLF-C02)
- Google Data Analytics Professional Certificate
- Microsoft Azure for Data Engineering (Azure Databricks)
- Python for Data Science & AI — IBM

---

## Background

Six years at Sainik School Ghorakhal (residential military school) — NCC A & B Certificate holder. After graduating in March 2024, worked in hospitality and stadium operations while self-studying for and passing two AWS certifications independently. Currently Team Leader at Copernus Fresh Fish — managing production lines, traceability, and compliance for Lidl and Iceland retailer codes of practice.

---

📧 pawankapkoti3889@gmail.com
💼 [linkedin.com/in/pawan-singh-kapkoti-100176347](https://linkedin.com/in/pawan-singh-kapkoti-100176347)
