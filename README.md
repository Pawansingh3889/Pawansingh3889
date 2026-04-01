# Pawan Singh Kapkoti

MSc Data Analytics (Aston University) | Microsoft PL-300 Certified | Google Data Analytics | Hull, UK

---

## About

This portfolio contains data engineering, analytics, and AI projects. Each repository uses real data — government APIs, production databases, payslip records — not tutorials or sample datasets.

The work covers ingestion, transformation (dbt), orchestration (Prefect), validation, and delivery through Power BI and Streamlit dashboards.
---

## Key Numbers

| Metric | Value |
|---|---|
| Records processed | 196,000+ across all projects |
| dbt models | 11 models, 94+ automated quality checks |
| Live dashboards | 3 deployed (Streamlit + Power BI + MediAsk) |
| CI/CD pipelines | 3 GitHub Actions workflows (lint, test, deploy) |
| SQL queries | 14 analytical queries with window functions, CTEs |
| ML models | XGBoost (93% accuracy), Isolation Forest, Random Forest |
| AI integrations | Google Gemini 2.5 Flash, Mistral 7B |

---

## Featured Projects

### [OpsMind](https://pawansingh3889.github.io/OpsMind) | [GitHub](https://github.com/Pawansingh3889/OpsMind)
`Python` `Streamlit` `SQLAlchemy` `ChromaDB` `Ollama` `Phi3/Mistral`

This repo contains an on-premises AI assistant for food processing factories. It connects to SQL databases, ingests PDFs, and responds to natural language questions.

- Natural language to SQL query engine with automatic result explanation
- Document search (RAG) over SOPs, HACCP plans, and customer specifications using ChromaDB
- Waste prediction module with yield trend analysis and GBP cost calculations
- BRC/HACCP compliance dashboard with batch traceability and allergen matrix
- Smart alerts for temperature excursions, overtime breaches, order shortfalls, and expiring stock
- Runs fully on-premises via Ollama — zero cloud cost, no data leaves the building

---

### [MediAsk â€” Health Q&A for Workers](https://hackathon-ioqp.onrender.com) | [GitHub](https://github.com/Pawansingh3889/Hackathon-mediask)
`Python` `Flask` `PostgreSQL` `Google Gemini AI` `NHS API` `Docker` `Web Speech API` `Google Translate`

This repo contains a community health Q&A platform for factory workers, food processors, and manual labourers in the UK. Combines NHS-verified guidance, real worker experiences, and AI-powered responses.

- **70+ seeded health Q&A** across 18 categories including a dedicated Workers Health hub
- **Google Gemini 2.5 Flash** AI auto-responds to every question with practical, UK-specific advice
- **Voice input** â€” ask questions by speaking (Web Speech API), designed for workers with gloves
- **18-language support** via Google Translate (Hindi, Polish, Romanian, Urdu, Arabic, and more)
- **NHS API integration** â€” live condition search from official NHS data
- **Admin dashboard** â€” full content and user management with hazard report tracking
- **Reputation system** â€” gamified levels from Newcomer to Legend
- **Google OAuth** login + browser push notifications

---

### [Apex Data Migration](https://github.com/Pawansingh3889/Apex-Data-Migration) â€” Full Data Engineering Pipeline
`Python` `dbt` `DuckDB` `Polars` `XGBoost` `Isolation Forest` `Mistral 7B` `Prefect` `Docker` `Power BI`

Simulates diagnosing and migrating a failing production database â€” the right way, before touching production.

- **10-task Prefect pipeline** â€” parallel execution, retry logic, monitoring dashboard
- **XGBoost** CPU spike predictor â€” 93% accuracy, ROC-AUC 0.97, zero data leakage
- **Isolation Forest** â€” unsupervised anomaly detection, confirmed both injected faults
- **Mistral 7B via Ollama** â€” offline Portuguese sentiment analysis, zero API cost
- **dbt** â€” 7 models, 53 quality tests, full lineage graph
- **94 automated checks** caught a live LLM label corruption bug before Power BI
- **Power BI** 3-page dashboard â€” 96,470 orders analysed

---

### [UK Crime Analytics Pipeline](https://github.com/Pawansingh3889/uk-crime-pipeline) | [Live Dashboard](https://uk-crime-pipeline-6nydeza7je8kiwsfl6deuw.streamlit.app)
`Python` `PostgreSQL` `dbt` `Streamlit` `Neon` `GitHub Actions`

End-to-end pipeline ingesting real government crime data â€” publicly deployed.

- **99,675 crime records** from Police UK API across 10 cities
- **PostgreSQL** with idempotent upserts â€” safe to re-run
- **dbt** transforms into 4 mart models
- **Streamlit Cloud** + **Neon PostgreSQL** â€” zero infrastructure cost
- **3 GitHub Actions workflows** â€” CI (lint + dbt test), weekly scheduled ingestion, daily health monitoring

---

### [SQL Crime Analytics](https://github.com/Pawansingh3889/sql-crime-analytics)
`SQL` `PostgreSQL` `Window Functions` `CTEs`

This repo contains 14 analytical queries across 99,673 records. Covers RANK, ROW_NUMBER, LAG, LEAD, FILTER, STRING_AGG, self-joins, and CTEs. Includes a [reusable SQL cheatsheet](https://github.com/Pawansingh3889/sql-crime-analytics/blob/main/SQL_CHEATSHEET.md) and [complete SQL reference guide](https://github.com/Pawansingh3889/sql-crime-analytics/blob/main/SQL_COMPLETE_REFERENCE.md).

---

### [UK Employment Analysis â€” Excel](https://github.com/Pawansingh3889/uk-employment-excel)
`Excel` `AVERAGEIF` `INDEX/MATCH` `SUMPRODUCT` `Charts` `Data Validation` `CAGR`

Excel workbook analysing employment across 12 UK regions (2019-2024). Includes a **personal case study** â€” used this data to justify relocating from Birmingham to Hull in 2024 with under 1,000 in savings.

---

### [PSW Graduate Tax Contribution Analysis](https://github.com/Pawansingh3889/uk-immigration-tax-fairness)
`Python` `Jupyter` `Excel` `HMRC Data` `Payslip Analysis`

This repo contains a data-driven analysis from real payslips across two employers over 20 months. Net contribution: approximately 30,000 put into the UK economy, 150 taken out in NHS services. Includes pension tracker, NHS double-charge analysis (NI + IHS), and side-by-side comparison with a UK citizen.

---

### [UK Crime Data Analysis â€” AWS](https://github.com/Pawansingh3889/Crime_Analysis)
`AWS S3` `Glue` `Athena` `QuickSight`

This repo contains a serverless analytics pipeline across all 43 UK police forces (2022-2024). 5.9M+ violence and sexual offence records processed.

---

### [MSc Dissertation â€” Ethnicity & Academic Outcomes](https://github.com/Pawansingh3889/MSc-Dissertation-Project)
`Python` `SQL` `Random Forest` `Statistical Testing`

This repo contains analysis of HESA and National Pupil Database data under institutional approval. Identified a 15% performance gap. Random Forest model: 80% accuracy. Submitted to Aston University.

---

### [OnlyBuddy â€” Community Errand App](https://onlybuddy.vercel.app) | [GitHub](https://github.com/Pawansingh3889/onlybuddy)
`React 18` `Firebase` `Stripe` `Google Maps` `Vercel` `PWA`

This repo contains a community errand app for Hull. 25 deployments, Firebase auth, Stripe payments, PWA.

---

## Tech Stack

| Layer | Tools |
|---|---|
| **Languages** | Python 3.11, SQL (window functions, CTEs, aggregations), JavaScript |
| **Data Engineering** | dbt Core, Polars, DuckDB, PyArrow, PostgreSQL, ETL/ELT |
| **Orchestration** | Prefect 3 |
| **AWS** | S3, Glue, Athena, Redshift, QuickSight, CloudWatch, IAM |
| **Azure** | Databricks, Synapse Analytics |
| **ML / AI** | XGBoost, Isolation Forest, Scikit-Learn, Random Forest, Mistral 7B, Google Gemini |
| **BI & Viz** | Power BI, Streamlit, Plotly, Matplotlib, Seaborn |
| **Cloud DB** | Neon (PostgreSQL serverless), DuckDB |
| **DevOps** | Docker, GitHub Actions, Vercel CI/CD, Render |
| **Web** | Flask, React 18, Firebase, REST APIs, Web Speech API |

---

## Certifications

| Certification | Provider | Status |
|---|---|---|
| **Power BI Data Analyst Associate (PL-300)** | Microsoft | Active â€” [Verify](https://learn.microsoft.com/en-us/users/pawansinghkapkoti-3247/credentials/certification/data-analyst-associate) |
| **Google Data Analytics Professional Certificate** | Google / Coursera | Completed â€” 8 courses |
| **Azure for Data Engineering** | Microsoft / Coursera | Completed |
| **Cloud Practitioner Essentials** | AWS Training | Completed |
| **Python for Data Science & AI** | IBM | Completed |
| **Data Engineer Associate (DEA-C01)** | AWS | Preparing |
| **Microsoft Fabric Analytics Engineer (DP-600)** | Microsoft | Preparing |

---

## Background

Six years at Sainik School Ghorakhal (residential military school) â€” NCC A & B Certificate holder. After completing my MSc in March 2024, I worked in hospitality and stadium operations while self-studying for certifications. Currently Operational Team Leader at Copernus Fresh Fish â€” managing production data through SI (Integreater) ERP, production scheduling for 11+ operatives, and audit-ready traceability for Lidl and Iceland supply chains.

---

## Currently Looking For

**Remote data analyst/engineer roles** â€” available for full-time, contract, or freelance work across all time zones. Strong preference for companies that value real projects over whiteboard puzzles.

---

## Contact

| | |
|---|---|
| **Email** | pawankapkoti3889@gmail.com |
| **LinkedIn** | [linkedin.com/in/pawan-singh-kapkoti-100176347](https://linkedin.com/in/pawan-singh-kapkoti-100176347) |
| **Upwork** | [upwork.com/freelancers/~01f5815a5a7386a2c3](https://www.upwork.com/freelancers/~01f5815a5a7386a2c3) |
| **Arc.dev** | [arc.dev/@pawansinghkapkoti](https://arc.dev/@pawansinghkapkoti) |

