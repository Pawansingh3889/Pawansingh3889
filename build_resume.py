"""Generate a professional 2-3 page CV for Pawan Singh Kapkoti."""
from fpdf import FPDF


class Resume(FPDF):
    def header(self):
        pass
    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, f"Pawan Singh Kapkoti  |  Page {self.page_no()}", align="C")


def build():
    pdf = Resume("P", "mm", "A4")
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.add_page()
    pw = pdf.w - 20

    # ── Name & Title ──
    pdf.set_font("Helvetica", "B", 22)
    pdf.cell(pw, 10, "Pawan Singh Kapkoti", ln=True)
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(pw, 6, "Data & Analytics Engineer", ln=True)
    pdf.set_font("Helvetica", "", 9)
    pdf.cell(pw, 5, "Yorkshire, UK  |  pawankapkoti3889@gmail.com  |  github.com/Pawansingh3889", ln=True)
    pdf.cell(pw, 5, "linkedin.com/in/pawan-singh-kapkoti-100176347", ln=True)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(1)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(3)

    # ── Bio / Profile ──
    section(pdf, "PROFILE")
    body(pdf, "I build robust data pipelines, read source code, and ship fixes upstream "
         "(pandas, drt, ChromaDB). MSc Data Analytics. Working in food manufacturing, "
         "building pipelines and dev tools on the side.")
    pdf.ln(1)
    body(pdf, "I believe compliance shouldn't mean spreadsheets and AI shouldn't require "
         "the cloud.")
    pdf.ln(3)

    # ── Skills ──
    section(pdf, "SKILLS")
    skill_line(pdf, "Languages", "Python, SQL, Bash")
    skill_line(pdf, "Data Engineering", "dbt (staging/marts, tests, macros), BigQuery, PostgreSQL, Snowflake, Prefect")
    skill_line(pdf, "Tools & Infra", "Docker, Git, GitHub Actions, pre-commit, Linux (Ubuntu/WSL)")
    skill_line(pdf, "Visualisation", "Power BI (PL-300), Looker Studio, Streamlit, Plotly, matplotlib")
    skill_line(pdf, "Libraries", "pandas, SQLAlchemy, openpyxl, typer, pytest, ChromaDB, Ollama")
    skill_line(pdf, "ERP / Industry", "SI (Integreater), BRC/HACCP, batch traceability, allergen management")
    pdf.ln(3)

    # ── Experience ──
    section(pdf, "EXPERIENCE")

    job(pdf, "Copernus Fresh Fish, Yorkshire", "Team Leader", "Apr 2025 - Present")
    bullet(pdf, "Led production team of 11+ operatives, coordinating shift patterns and operational data workflows.")
    bullet(pdf, "Operated SI (Integreater) ERP system for production data management and yield KPI monitoring.")
    bullet(pdf, "Managed batch traceability reports and weight variance reconciliation for BRC compliance (Lidl, Iceland).")
    pdf.ln(2)

    job(pdf, "Cranswick Convenience Foods, Yorkshire", "Cover Team Lead", "Oct 2024 - Apr 2025")
    bullet(pdf, "Managed batch-level traceability data for M&S and Tesco premium product lines.")
    bullet(pdf, "Nav Code and Vector tag validation, allergen cross-reference checks, full audit trail documentation.")
    bullet(pdf, "Identified reporting inefficiencies; prototyped automated compliance dashboard (BRC/HACCP).")
    pdf.ln(2)

    job(pdf, "Cranswick Convenience Foods, Yorkshire", "Food Operative", "Jul 2024 - Oct 2024")
    bullet(pdf, "Collaborated with NPD and Production teams on product specifications and traceability systems.")
    bullet(pdf, "Managed production data, batch records, and temperature compliance across food safety protocols.")
    pdf.ln(3)

    # ── Projects ──
    section(pdf, "PROJECTS")

    project(pdf, "UK Crime Pipeline", "github.com/Pawansingh3889/uk-crime-pipeline")
    body(pdf, "End-to-end data pipeline ingesting 99,675 crime records from the Police UK API into "
         "PostgreSQL and BigQuery, transforming with dbt into staging views and mart tables, and "
         "serving interactive dashboards via Streamlit and Looker Studio.")
    pdf.ln(1)
    bullet(pdf, "dbt staging/marts pattern with 65 tests (53 PostgreSQL + 12 BigQuery).")
    bullet(pdf, "3 CI/CD workflows: lint on push, weekly auto-ingest, daily health checks.")
    bullet(pdf, "Idempotent upserts (ON CONFLICT DO NOTHING), retry with exponential backoff.")
    bullet(pdf, "Service account auth for BigQuery, Neon serverless PostgreSQL with pool_pre_ping.")
    bullet(pdf, "Looker Studio dashboard with dark theme, city filters, category donut chart, trend analysis.")
    pdf.ln(2)

    project(pdf, "sql-sop", "pypi.org/project/sql-sop")
    body(pdf, "Rule-based SQL linter published to PyPI. Catches dangerous patterns like DELETE without "
         "WHERE, SELECT *, and implicit joins before they reach production.")
    pdf.ln(1)
    bullet(pdf, "15 rules (5 errors, 10 warnings), 21 tests, compiled regex for 0.08s scans across 200 files.")
    bullet(pdf, "Ships as pre-commit hook + GitHub Action for two-layer SQL quality enforcement.")
    bullet(pdf, "Built with typer CLI framework. Handles encoding edge cases (UTF-8, Latin-1, BOM).")
    pdf.ln(2)

    project(pdf, "OpsMind", "github.com/Pawansingh3889/OpsMind")
    body(pdf, "On-premises AI assistant for manufacturing environments. Natural language to SQL across "
         "a 147-table schema registry, with RAG document search using ChromaDB and HNSW indexing.")
    pdf.ln(1)
    bullet(pdf, "36 pytest tests. Read-only SQL enforcement blocks INSERT/UPDATE/DELETE.")
    bullet(pdf, "Runs entirely on Ollama - no data leaves the factory network.")
    bullet(pdf, "CI/CD pipeline on every push with automated testing.")
    pdf.ln(2)

    project(pdf, "Compliance Dashboard", "github.com/Pawansingh3889/manufacturing-compliance-dashboard")
    body(pdf, "BRC/HACCP food safety dashboard: batch traceability, z-score temperature anomaly "
         "detection, allergen matrix. Error handling on all I/O modules with pytest coverage.")
    pdf.ln(1)
    bullet(pdf, "Colour-coded temperature readings with 30-day trend charts per location.")
    bullet(pdf, "Live on Streamlit with graceful error pages and connection retry logic.")
    pdf.ln(2)

    project(pdf, "Production Analytics Pipeline", "github.com/Pawansingh3889/production-analytics-pipeline")
    body(pdf, "Daily workflow extracting 15K+ rows from 4 ERP tables (RunNumber, Transactions, PLU, Totals) "
         "into a Docker sandbox with read-only SQL Server, SQL injection guards, and Pydantic validation.")
    pdf.ln(1)
    bullet(pdf, "53 tests covering models, extraction, and safety guards.")
    bullet(pdf, "Watermark-based incremental loading with dbt staging/marts transformation layer.")
    bullet(pdf, "Fully containerised: Docker Compose with read-only database connection enforcement.")
    pdf.ln(2)

    project(pdf, "SQL Ops Reviewer", "github.com/Pawansingh3889/sql-ops-reviewer")
    body(pdf, "GitHub Action that reviews .sql files in PRs using local AI. Pairs with sql-sop for "
         "two-layer SQL quality: rule-based pre-commit (instant) + AI review in CI (deep analysis).")
    pdf.ln(3)

    # ── Open Source ──
    section(pdf, "OPEN SOURCE CONTRIBUTIONS")
    body(pdf, "Active contributor to open source with 12 merged PRs across multiple projects:")
    pdf.ln(1)
    bullet(pdf, "drt-hub/drt: 5 destination connectors (ClickHouse, Parquet, Teams, CSV/JSON) shipping "
           "in v0.5, plus the official connector tutorial for new contributors.")
    bullet(pdf, "pandas (pandas-dev/pandas): Documentation and code contributions.")
    bullet(pdf, "ChromaDB (chroma-core/chroma): Vector database improvements.")
    bullet(pdf, "pgcli (dbcli/pgspecial): PostgreSQL CLI tool contributions.")
    bullet(pdf, "Electricity Maps: Open energy data contributions.")
    bullet(pdf, "Open Climate Fix: Solar forecast model contributions.")
    bullet(pdf, "ScanAPI: API testing framework improvements.")
    pdf.ln(3)

    # ── Education ──
    section(pdf, "EDUCATION")
    job(pdf, "University, UK", "MSc Data Analytics", "Completing 2026")
    bullet(pdf, "Modules: Statistics, Machine Learning, Data Visualisation, Research Methods.")
    pdf.ln(2)
    job(pdf, "Amity University, Noida, India", "BCA (Bachelor of Computer Applications)", "2019 - 2022")
    bullet(pdf, "Core: Data Structures, Algorithms, Database Management, Python Programming.")
    pdf.ln(3)

    # ── Certifications ──
    section(pdf, "CERTIFICATIONS")
    bullet(pdf, "Microsoft PL-300: Power BI Data Analyst Associate")
    bullet(pdf, "Google Data Analytics Professional Certificate")
    bullet(pdf, "AWS Cloud Practitioner Essentials")
    bullet(pdf, "IBM Data Science Professional Certificate")
    bullet(pdf, "Algorithmic Toolbox (UC San Diego)")
    bullet(pdf, "Python Programming (University of Michigan)")
    pdf.ln(3)

    # ── Volunteer ──
    section(pdf, "VOLUNTEER & OTHER")
    bullet(pdf, "National Cadet Corps (NCC), India (2012-2018) - 6 years of service, veteran support.")
    bullet(pdf, "Published sql-sop to PyPI - first open source package (pip install sql-sop).")
    bullet(pdf, "Attending PyCon DE 2026 (April 14-17, online).")

    # ── Save ──
    out = "Pawan_Singh_Kapkoti_Resume.pdf"
    pdf.output(out)
    print(f"Resume saved: {out}")


# ── Helpers ──

def section(pdf, title):
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(30, 58, 95)
    pdf.cell(0, 6, title, ln=True)
    pdf.set_draw_color(30, 58, 95)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(2)
    pdf.set_text_color(0, 0, 0)


def body(pdf, text):
    pdf.set_font("Helvetica", "", 9.5)
    pdf.multi_cell(0, 4.5, text)


def skill_line(pdf, label, value):
    pdf.set_font("Helvetica", "B", 9.5)
    pdf.cell(35, 5, label + ":")
    pdf.set_font("Helvetica", "", 9.5)
    pdf.cell(0, 5, value, ln=True)


def job(pdf, company, role, dates):
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(130, 5, company)
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 5, dates, ln=True, align="R")
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", "I", 9.5)
    pdf.cell(0, 5, role, ln=True)


def project(pdf, name, url):
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(60, 5, name)
    pdf.set_font("Helvetica", "", 8.5)
    pdf.set_text_color(60, 60, 180)
    pdf.cell(0, 5, url, ln=True, align="R")
    pdf.set_text_color(0, 0, 0)


def bullet(pdf, text):
    pdf.set_font("Helvetica", "", 9.5)
    left = pdf.l_margin
    pdf.set_x(left + 5)
    pdf.multi_cell(pdf.w - pdf.l_margin - pdf.r_margin - 5, 4.5, f"-  {text}")


if __name__ == "__main__":
    build()
