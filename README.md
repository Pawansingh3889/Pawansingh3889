# Pawan Singh Kapkoti

MSc Data Analytics (Aston University) | Microsoft PL-300 Certified | Google Data Analytics | Hull, UK

---

## About

This portfolio documents a progression from data analytics foundations to full-stack AI systems. Each project represents a step in that journey — starting with SQL and pipelines, scaling into orchestration and ML, and arriving at production-grade AI tools.

Every repository uses real data. Government APIs, operational databases, payslip records — not tutorials.

---

## Projects

### [OpsMind](https://pawansingh3889.github.io/OpsMind) | [GitHub](https://github.com/Pawansingh3889/OpsMind)
`Python` `Streamlit` `SQLAlchemy` `ChromaDB` `Ollama` `Phi3/Mistral`

The most recent project. This repo contains an on-premises AI assistant for operational environments — the result of combining database querying, document search, and local LLMs into a single operational tool.

Started with a question: can a manager ask "Why did we lose money today?" and get an answer in seconds, without cloud costs or data leaving the building?

What the repo has:
- Natural language to SQL engine — converts plain English into database queries, runs them, explains results
- RAG document search over SOPs, HACCP plans, and customer specifications using ChromaDB
- Waste prediction module with yield trend analysis and GBP cost impact on every number
- BRC/HACCP compliance dashboard with batch traceability, allergen matrix, and temperature excursion detection
- Smart alerts — overtime breaches, order shortfalls, expiring stock, yield drops
- Full production dashboard with 30-day trends, customer breakdown, and per-product yield analysis
- Runs entirely on-premises via Ollama — zero cloud cost

---

### [MediAsk](https://hackathon-ioqp.onrender.com) | [GitHub](https://github.com/Pawansingh3889/Hackathon-mediask)
`Python` `Flask` `PostgreSQL` `Google Gemini AI` `NHS API` `Docker`

A hackathon project that grew into a full platform. This repo contains a community health Q&A system designed for frontline workers — people who face occupational health risks but rarely find answers tailored to their situation.

The platform evolved through several iterations: starting as a basic Q&A board, then adding AI responses via Gemini, then voice input for workers with gloves, then multi-language support for a multilingual workforce.

What the repo has:
- 70+ health Q&A across 18 categories including a dedicated Workers Health section
- Google Gemini 2.5 Flash auto-responding to every question with UK-specific, practical advice
- Voice input (Web Speech API) and 18-language support (Google Translate)
- NHS API integration for live condition search
- Admin dashboard with full content moderation, user management, and hazard report tracking
- Reputation system, Google OAuth, browser push notifications

---

### [Apex Data Migration](https://github.com/Pawansingh3889/Apex-Data-Migration)
`Python` `dbt` `DuckDB` `Polars` `XGBoost` `Isolation Forest` `Mistral 7B` `Prefect` `Docker` `Power BI`

The most technically dense project. This repo contains a simulated production database migration — designed to practice every stage of a real migration before touching live systems.

The approach: diagnose the failing database first (anomaly detection, ML-based spike prediction), then migrate with automated validation at every step, then deliver through dashboards.

What the repo has:
- 10-task Prefect pipeline with parallel execution, retry logic, and monitoring dashboard
- XGBoost CPU spike predictor — 93% accuracy, ROC-AUC 0.97, zero data leakage
- Isolation Forest anomaly detection confirming both injected faults
- Mistral 7B via Ollama for offline Portuguese sentiment analysis — zero API cost
- dbt layer with 7 models, 53 quality tests, and full lineage graph
- 94 automated checks that caught a live LLM label corruption bug before Power BI
- 3-page Power BI dashboard across 96,470 orders

---

### [UK Crime Analytics Pipeline](https://github.com/Pawansingh3889/uk-crime-pipeline) | [Live Dashboard](https://uk-crime-pipeline-6nydeza7je8kiwsfl6deuw.streamlit.app)
`Python` `PostgreSQL` `dbt` `Streamlit` `Neon` `GitHub Actions`

The foundation project. This repo contains a publicly deployed pipeline that ingests real government crime data — the first end-to-end system in this portfolio, and the one that established the patterns used in everything after it.

What the repo has:
- 99,675 crime records from Police UK API across 10 cities
- PostgreSQL with idempotent upserts — safe to re-run at any point
- dbt transforms into 4 mart models
- Streamlit Cloud + Neon PostgreSQL — zero infrastructure cost
- 3 GitHub Actions workflows — CI (lint + dbt test), weekly scheduled ingestion, daily health monitoring

---

## Tech Stack

| Layer | Tools |
|---|---|
| **Languages** | Python 3.11, SQL (window functions, CTEs, aggregations), JavaScript |
| **Data Engineering** | dbt Core, Polars, DuckDB, PyArrow, PostgreSQL, ETL/ELT |
| **Orchestration** | Prefect 3 |
| **AWS** | S3, Glue, Athena, Redshift, QuickSight, CloudWatch, IAM |
| **Azure** | Databricks, Synapse Analytics |
| **ML / AI** | XGBoost, Isolation Forest, Scikit-Learn, Random Forest, Mistral 7B, Google Gemini, Ollama |
| **BI & Viz** | Power BI, Streamlit, Plotly, Matplotlib, Seaborn |
| **Cloud DB** | Neon (PostgreSQL serverless), DuckDB |
| **DevOps** | Docker, GitHub Actions, Vercel CI/CD, Render |
| **Web** | Flask, React 18, Firebase, REST APIs, Web Speech API |

---

## Certifications

| Certification | Provider | Status |
|---|---|---|
| **Power BI Data Analyst Associate (PL-300)** | Microsoft | Active — [Verify](https://learn.microsoft.com/en-us/users/pawansinghkapkoti-3247/credentials/certification/data-analyst-associate) |
| **Google Data Analytics Professional Certificate** | Google / Coursera | Completed — 8 courses |
| **Azure for Data Engineering** | Microsoft / Coursera | Completed |
| **Cloud Practitioner Essentials** | AWS Training | Completed |
| **Python for Data Science & AI** | IBM | Completed |

---

## Availability

Open to full-time, contract, or remote data analyst/engineer roles across all time zones.

---

## Contact

| | |
|---|---|
| **Email** | pawankapkoti3889@gmail.com |
| **LinkedIn** | [linkedin.com/in/pawan-singh-kapkoti-100176347](https://linkedin.com/in/pawan-singh-kapkoti-100176347) |
| **GitHub** | [github.com/Pawansingh3889](https://github.com/Pawansingh3889) |
