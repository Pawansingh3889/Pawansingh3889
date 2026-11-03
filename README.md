# Pawan Singh Kapkoti

<a href="https://linkedin.com/in/pawan-singh-kapkoti-100176347/details/connected-accounts/"><img src="https://img.shields.io/badge/GitHub%20Copilot%20Proficiency-Intermediate%20(verified)-8957e5?style=for-the-badge&logo=githubcopilot&logoColor=white" alt="GitHub Copilot Proficiency: Intermediate, verified by GitHub Learn"></a>

I am an early-career data engineer, still learning and very much a junior. I work with SQL, Python, dbt, Snowflake and Airflow. I finished an MSc in Data Analytics at Aston University, worked as a data analyst at a UK seafood processor, and I co-founded [Rigel ERP](https://rigel.kapkotisolution.com), where I lead the technical side.

Most of what is below is me learning in public: some of it is live, a lot of it is unfinished, and I try to say which is which. Feedback and code review are very welcome.

Looking for a junior Data Engineering or Analytics Engineering role in India (ready to relocate) or remote, ideally on a team I can learn from.

## What I am building

An honest snapshot, checked on 4 Nov 2026. Numbers come from the repos themselves. Status means what it says: live is running today, in development is not finished, and private means the code is not public yet.

| Project | Status | Code | What it is |
| --- | --- | --- | --- |
| [UK Crime Pipeline](https://github.com/Pawansingh3889/uk-crime-pipeline) | Live dashboard | [Public](https://github.com/Pawansingh3889/uk-crime-pipeline) | Police UK data for 10 cities. Loads into Snowflake through a stage, COPY INTO and an idempotent MERGE, then dbt builds and tests 6 models (31 tests), all run by an Airflow DAG. The same models also run on PostgreSQL behind a [Streamlit dashboard](https://uk-crime-pipeline-6nydeza7je8kiwsfl6deuw.streamlit.app/). |
| [sql-sop](https://pypi.org/project/sql-sop) | Live on PyPI | [Public](https://github.com/Pawansingh3889/sql-sop) | Open-source SQL linter that catches dangerous SQL, like a DELETE with no WHERE, before it reaches production. 48 rules including a dbt pack; runs as a CLI, pre-commit hook and GitHub Action. |
| [Rigel ERP](https://rigel.kapkotisolution.com) | Live, I co-founded it and lead the tech | Private | ERP for Indian workshops and traders: GST billing, inventory, purchasing, BOM production runs, payments and returns. React, TypeScript, Supabase (469 migrations, 29 edge functions), Playwright browser tests, deployed on Cloudflare Pages. |
| [Governed Agent Stack](https://github.com/Pawansingh3889/governed-agent-stack) | In development | Public | The monorepo FloorMind now lives in: free, on-prem building blocks (schema-scout, sql-explorer-mcp, agent-blackbox, pii-veil and more) for an AI agent you can point at a real database and audit. |
| [Elenchus](https://frontend-three-zeta-45.vercel.app) | Live demo | [Public](https://github.com/Pawansingh3889/elenchus) | Survey service where respondents answer through a guided AI conversation. FastAPI, PostgreSQL, Next.js. |

**Also right now:** a data science internship with YuvaIntern ([notebooks](https://github.com/Pawansingh3889/yuvaintern), [Sephora review analysis](https://github.com/Pawansingh3889/beauty-review-analysis)), which is why Jupyter Notebook shows up in my language mix.

## Toolbox

Tools I have used in the projects above. I am comfortable with some and still learning most of them.

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,postgres,ts,js,react,nextjs,tailwind,fastapi,flask,docker,aws,gcp,cloudflare,supabase,githubactions,threejs,terraform,linux&perline=9" alt="Python, PostgreSQL, TypeScript, JavaScript, React, Next.js, Tailwind, FastAPI, Flask, Docker, AWS, GCP, Cloudflare, Supabase, GitHub Actions, Three.js, Terraform, Linux">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white" alt="Snowflake">
  <img src="https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white" alt="Apache Airflow">
  <img src="https://img.shields.io/badge/dbt-FF694B?style=for-the-badge" alt="dbt">
  <img src="https://img.shields.io/badge/Prefect-070E10?style=for-the-badge&logo=prefect&logoColor=white" alt="Prefect">
  <img src="https://img.shields.io/badge/DuckDB-1A1A1A?style=for-the-badge&logo=duckdb&logoColor=white" alt="DuckDB">
  <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="scikit-learn">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langgraph&logoColor=white" alt="LangGraph">
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain">
  <img src="https://img.shields.io/badge/MCP-000000?style=for-the-badge&logo=modelcontextprotocol&logoColor=white" alt="MCP">
  <img src="https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white" alt="Ollama">
  <img src="https://img.shields.io/badge/Claude-D97757?style=for-the-badge&logo=claude&logoColor=white" alt="Claude">
  <img src="https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white" alt="Gemini">
</p>

<p align="center"><b>Also:</b> SQL Server (T-SQL), SSRS, Power BI, Looker Studio, SI Integreater ERP, pgvector, ChromaDB, RAG, Playwright</p>

<p align="center"><img src="https://www.gitskins.com/api/section/stats?username=Pawansingh3889&theme=aurora" alt="GitHub stats" width="100%"></p>

<p align="center"><img src="https://www.gitskins.com/api/section/stack?username=Pawansingh3889&theme=aurora" alt="Language stack" width="100%"></p>

## Contact

[Email](mailto:pawankapkoti3889@gmail.com) · [LinkedIn](https://linkedin.com/in/pawan-singh-kapkoti-100176347) · [kapkotisolution.com](https://kapkotisolution.com)
