# Pawan Singh Kapkoti

I am an early-career data and AI engineer, still learning and very much a junior. I finished an MSc in Data Analytics at Aston University, worked as a data analyst at a UK seafood processor, and now build small products under [Kapkoti Solution](https://kapkotisolution.com), where I am technical lead on [Rigel ERP](https://rigel.kapkotisolution.com).

Most of what is below is me learning in public: some of it is live, a lot of it is unfinished, and I try to say which is which. Feedback and code review are very welcome.

Looking for a junior Data, Analytics or AI Engineering role in India or remote, ideally on a team I can learn from.

## What I am building

An honest snapshot, checked on 23 Oct 2026. Numbers come from the repos themselves. Status means what it says: live is running today, in development is not finished, and private means the code is not public yet.

| Project | Status | Code | What it is |
| --- | --- | --- | --- |
| [Rigel ERP](https://rigel.kapkotisolution.com) | Live, I am technical lead | Private | ERP for Indian workshops and traders: GST billing, inventory, purchasing, BOM production runs, payments and returns. React, TypeScript, Supabase (469 migrations, 29 edge functions), Playwright browser tests, deployed on Cloudflare Pages. |
| [FloorMind](https://floormind.pages.dev) | Live site, product in development | [Public](https://github.com/Pawansingh3889/governed-agent-stack/tree/main/apps/floormind) | Offline AI assistant for food and FMCG factories. Ask production data questions in plain English with a local LLM; queries are read-only, linted by sql-sop and audit-logged. 128 tests plus an eval harness. |
| [Governed Agent Stack](https://github.com/Pawansingh3889/governed-agent-stack) | In development | Public | The monorepo FloorMind now lives in: free, on-prem building blocks (schema-scout, sql-explorer-mcp, agent-blackbox, pii-veil and more) for an AI agent you can point at a real database and audit. |
| [sql-sop](https://github.com/Pawansingh3889/sql-sop) | Released, v0.11.0 | Public | SQL linter on [PyPI](https://pypi.org/project/sql-sop/): 48 core rules plus contracts and dbt packs, 489 tests, 14 releases, 3,100+ downloads in the last 180 days excluding mirrors ([pypistats](https://pypistats.org/packages/sql-sop)). |
| [Vega](https://github.com/Pawansingh3889/vega) | In development, phase 3 (invoicing) | Public, AGPL-3.0 | UK-first ERP for small British businesses with MTD VAT, EU trade and product carbon in the schema. First target is small UK food manufacturers; that is still a hypothesis with no customer discovery behind it. |
| [Elenchus](https://frontend-three-zeta-45.vercel.app) | Live demo | [Public](https://github.com/Pawansingh3889/elenchus) | Survey service where respondents answer through a guided AI conversation. FastAPI, PostgreSQL, Next.js. |
| [pay-warden](https://github.com/Pawansingh3889/pay-warden) and [steward](https://github.com/Pawansingh3889/steward) | Hackathon build, finished | Public | Prava agentic payments hackathon: an MCP policy firewall that checks budgets and limits before an AI agent can spend, and an agent that spends delegated funds under a sponsor's policy (584 tests). |
| [canibuy](https://github.com/Pawansingh3889/canibuy) | Hackathon build, finished | Public | Probes whether an AI agent can actually check out at a merchant. Graded 23 merchants across 4 browser clients: only 9% had a checkout path an agent could use today. |
| [uk-crime-pipeline](https://github.com/Pawansingh3889/uk-crime-pipeline) | Learning project, weekly ingest | Public | A learning project: Police UK API to PostgreSQL with dbt staging and marts, pytest health and SLO checks and 3 CI workflows. 99,675 records across 10 cities. dbt data tests are next on my list. [Dashboard on Hugging Face](https://huggingface.co/spaces/pawankapkoti/uk-crime-analytics). |

**Also right now:** a data science internship with YuvaIntern ([notebooks](https://github.com/Pawansingh3889/yuvaintern), [Sephora review analysis](https://github.com/Pawansingh3889/beauty-review-analysis)), which is why Jupyter Notebook shows up in my language mix.

## Toolbox

Tools I have used in the projects above. I am comfortable with some and still learning most of them.

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,postgres,ts,js,react,nextjs,tailwind,fastapi,flask,docker,aws,gcp,cloudflare,supabase,githubactions,threejs,terraform,linux&perline=9" alt="Python, PostgreSQL, TypeScript, JavaScript, React, Next.js, Tailwind, FastAPI, Flask, Docker, AWS, GCP, Cloudflare, Supabase, GitHub Actions, Three.js, Terraform, Linux">
</p>

<p align="center">
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
