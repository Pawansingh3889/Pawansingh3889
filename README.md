<div align="center">

# Pawan Singh Kapkoti

**MSc Data Analytics (Aston University) | Microsoft PL-300 Certified | Google Data Analytics**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/pawan-singh-kapkoti-100176347)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:pawankapkoti3889@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Pawansingh3889)

</div>

---

## About

This portfolio documents a progression from data analytics foundations to full-stack AI systems. Each project represents a step in that journey starting with SQL and pipelines, scaling into orchestration and ML, and arriving at production-grade AI tools.

Every repository uses real data. Government APIs, operational databases, not tutorials.

---

## Portfolio at a Glance

```
  Records Processed             Data Quality               Deployments
  ==================           ==================          ==================
  oooooooooooooooo 196K+       oooooooooooooooo 94+        oooooooooooo 3 Live
                                automated checks            dashboards

  ML Model Accuracy            CI/CD Pipelines             AI Models
  ==================           ==================          ==================
  oooooooooooooooo 93%         oooooooooooo 3              oooooooooooo 3
  XGBoost (ROC 0.97)           GitHub Actions              Gemini, Mistral, Phi3
```

---

## Tech Stack

<div align="center">

**Languages and Core**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

**Data Engineering**

![dbt](https://img.shields.io/badge/dbt-FF694B?style=flat-square&logo=dbt&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?style=flat-square&logo=duckdb&logoColor=black)
![Polars](https://img.shields.io/badge/Polars-CD792C?style=flat-square&logo=polars&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)

**ML / AI**

![XGBoost](https://img.shields.io/badge/XGBoost-017CEE?style=flat-square)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square)
![Gemini](https://img.shields.io/badge/Gemini_AI-8E75B2?style=flat-square&logo=google&logoColor=white)

**Cloud and Infrastructure**

![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonaws&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)

**BI and Visualization**

![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)

</div>

---

## Projects

### OpsMind | On-Premises AI for Operations
[Landing Page](https://pawansingh3889.github.io/OpsMind) | [GitHub](https://github.com/Pawansingh3889/OpsMind)

> The most recent project. Natural language queries against SQL databases and documents, running entirely locally.

```
Architecture:
                    +---------------+
  User Question --> |  Ollama LLM   |
                    | (Phi3/Mistral)|
                    +-------+-------+
                            |
              +-------------+-------------+
              v             v             v
        +----------+  +----------+  +----------+
        | SQL Agent|  | ChromaDB |  |  Pandas  |
        +----------+  +----------+  +----------+
              |             |             |
              v             v             v
        +-------------------------------------+
        |        Streamlit Dashboard          |
        |  KPIs | Charts | Alerts | Compliance|
        +-------------------------------------+
```

| Component | Detail |
|---|---|
| Query Engine | Natural language to SQL with result explanation |
| Document Search | RAG over SOPs, HACCP plans, specs (ChromaDB) |
| Waste Module | Yield trends, GBP cost impact, prediction |
| Compliance | Batch traceability, allergen matrix, temperature monitoring |
| Alerts | Overtime, order shortfalls, expiring stock, yield drops |
| Infrastructure | 100% on-premises via Ollama, zero cloud cost |

---

### MediAsk | Health Q&A Platform
[Live Demo](https://hackathon-ioqp.onrender.com) | [GitHub](https://github.com/Pawansingh3889/Hackathon-mediask)

> Evolved through multiple iterations from a basic Q&A board into a full-stack platform.

```
Evolution:
  v1: Basic Q&A --> v2: + Gemini AI --> v3: + Voice input
  --> v4: + 18 languages --> v5: + NHS API + Admin dashboard
```

| Component | Detail |
|---|---|
| Content | 70+ Q&A across 18 health categories |
| AI | Google Gemini 2.5 Flash auto-response |
| Accessibility | Voice input (Web Speech API), 18 languages |
| Data | NHS API, GOV.UK, WHO, CDC sources |
| Admin | User management, hazard reports, content moderation |

---

### Apex Data Migration | Database Migration and ML Pipeline
[GitHub](https://github.com/Pawansingh3889/Apex-Data-Migration)

> The most technically dense project. Diagnose, migrate, validate, deliver.

```
Pipeline (Prefect):
  +----------+   +----------+   +----------+   +----------+
  | Diagnose |-->| Migrate  |-->| Validate |-->| Deliver  |
  | XGBoost  |   | Polars   |   | dbt (53  |   | Power BI |
  | Isolation|   | DuckDB   |   |  tests)  |   | 3 pages  |
  | Forest   |   |          |   | 94 checks|   | 96K rows |
  +----------+   +----------+   +----------+   +----------+
```

| Component | Detail |
|---|---|
| Orchestration | 10-task Prefect pipeline, parallel execution, retry logic |
| ML | XGBoost 93% accuracy (ROC-AUC 0.97), Isolation Forest |
| NLP | Mistral 7B offline sentiment analysis, zero API cost |
| Data Quality | dbt: 7 models, 53 tests. 94 automated checks |
| Delivery | 3-page Power BI dashboard, 96,470 orders |

---

### UK Crime Analytics | Live Deployed Pipeline
[Live Dashboard](https://uk-crime-pipeline-6nydeza7je8kiwsfl6deuw.streamlit.app) | [GitHub](https://github.com/Pawansingh3889/uk-crime-pipeline)

> The foundation project. Established the patterns used in everything after it.

```
Data Flow:
  Police UK API --> PostgreSQL --> dbt (4 marts) --> Streamlit Dashboard
       |                                                    |
       +---- GitHub Actions (3 workflows) ------------------+
             CI: lint + dbt test
             Weekly: scheduled ingestion
             Daily: health monitoring
```

| Component | Detail |
|---|---|
| Source | Police UK API, 99,675 records, 10 cities |
| Storage | PostgreSQL (Neon serverless), idempotent upserts |
| Transform | dbt Core, 4 mart models |
| CI/CD | 3 GitHub Actions workflows |

---

## Certifications

<div align="center">

![PL-300](https://img.shields.io/badge/Microsoft_PL--300-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)
![Google](https://img.shields.io/badge/Google_Data_Analytics-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Azure](https://img.shields.io/badge/Azure_Data_Engineering-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![AWS](https://img.shields.io/badge/AWS_Cloud_Practitioner-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)
![IBM](https://img.shields.io/badge/IBM_Python_for_DS-054ADA?style=for-the-badge&logo=ibm&logoColor=white)

</div>

---

## Data Sources

| Project | Source | Records |
|---|---|---|
| UK Crime Pipeline | [Police UK API](https://data.police.uk/docs/) | 99,675 |
| Apex Data Migration | Synthetic production database (DuckDB) | 96,470 |
| OpsMind | Synthetic operational database (SQLite) | 5,600+ |
| MediAsk | [NHS UK](https://www.nhs.uk/), [GOV.UK HSE](https://www.hse.gov.uk/), [WHO](https://www.who.int/), [CDC](https://www.cdc.gov/) | 70+ Q&A |

---

<div align="center">

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Pawansingh3889&show_icons=true&theme=default&hide_border=true&count_private=true)

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=Pawansingh3889&layout=compact&theme=default&hide_border=true)

![Streak](https://github-readme-streak-stats.herokuapp.com/?user=Pawansingh3889&theme=default&hide_border=true)

</div>
