"""Generate a professional PDF resume for Pawan Singh Kapkoti."""
from fpdf import FPDF


class Resume(FPDF):
    def header(self):
        pass

    def footer(self):
        pass


def build():
    pdf = Resume("P", "mm", "A4")
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pw = pdf.w - 20  # page width minus margins

    # ── Name & Title ──
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(pw, 9, "Pawan Singh Kapkoti", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(pw, 5, "Data & Analytics Engineer", ln=True)
    pdf.set_font("Helvetica", "", 8.5)
    pdf.cell(pw, 4, "Yorkshire, UK  |  pawankapkoti3889@gmail.com  |  github.com/Pawansingh3889  |  linkedin.com/in/pawan-singh-kapkoti-100176347", ln=True)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(1)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(2)

    # ── Summary ──
    section(pdf, "SUMMARY")
    body(pdf, "Data engineer building production pipelines (Python, SQL, dbt, BigQuery, PostgreSQL), "
         "publishing tools to PyPI, and contributing to open source (12 merged PRs across pandas, drt, ChromaDB). "
         "MSc Data Analytics. PL-300 certified. Open to DE roles, remote or hybrid, UK/EU.")
    pdf.ln(1)

    # ── Skills ──
    section(pdf, "SKILLS")
    skill_line(pdf, "Languages", "Python, SQL, Bash")
    skill_line(pdf, "Data Engineering", "dbt (staging/marts, tests, macros), BigQuery, PostgreSQL, Snowflake, Prefect")
    skill_line(pdf, "Tools & Infra", "Docker, Git, GitHub Actions, pre-commit, Linux (Ubuntu/WSL)")
    skill_line(pdf, "Visualisation", "Power BI (PL-300), Looker Studio, Streamlit, Plotly, matplotlib")
    skill_line(pdf, "Libraries", "pandas, SQLAlchemy, openpyxl, typer, pytest, ChromaDB, Ollama")
    pdf.ln(1)

    # ── Experience ──
    section(pdf, "EXPERIENCE")

    job(pdf, "Copernus Ltd", "Team Leader", "Apr 2025 -Present", "Yorkshire, UK")
    bullet(pdf, "Lead production team; manage shift scheduling, quality checks, and compliance reporting.")
    bullet(pdf, "Built internal data tools for tracking output and traceability using Python and Excel automation.")

    job(pdf, "Cranswick Convenience Foods", "Production Operative", "Jul 2024 -Apr 2025", "Yorkshire, UK")
    bullet(pdf, "Managed production data, batch records, and temperature compliance across food safety protocols.")
    bullet(pdf, "Identified reporting inefficiencies; prototyped automated compliance dashboard (BRC/HACCP).")
    pdf.ln(1)

    # ── Projects ──
    section(pdf, "PROJECTS")

    project(pdf, "UK Crime Pipeline", "github.com/Pawansingh3889/uk-crime-pipeline")
    bullet(pdf, "End-to-end pipeline: Police UK API -> PostgreSQL -> dbt -> Streamlit + BigQuery -> Looker Studio.")
    bullet(pdf, "99,675 records. dbt staging/marts with 65 tests (53 PostgreSQL + 12 BigQuery). 3 CI/CD workflows.")
    bullet(pdf, "Idempotent upserts (ON CONFLICT DO NOTHING), retry with exponential backoff, daily health checks.")

    project(pdf, "sql-sop", "pypi.org/project/sql-sop")
    bullet(pdf, "SQL linter published to PyPI. 15 rules, 21 tests, compiled regex (0.08s/200 files). Pre-commit + GitHub Action.")

    project(pdf, "OpsMind", "github.com/Pawansingh3889/OpsMind")
    bullet(pdf, "On-prem NL-to-SQL for manufacturing. 147-table schema, RAG search, 36 pytest tests. Runs on Ollama.")

    project(pdf, "Compliance Dashboard", "github.com/Pawansingh3889/manufacturing-compliance-dashboard")
    bullet(pdf, "BRC/HACCP food safety: batch traceability, z-score anomaly detection, allergen matrix. Live on Streamlit.")
    pdf.ln(1)

    # ── Open Source ──
    section(pdf, "OPEN SOURCE")
    bullet(pdf, "drt-hub/drt: 5 destination connectors (ClickHouse, Parquet, Teams, CSV/JSON), connector tutorial. 12 merged PRs.")
    bullet(pdf, "Contributed to pandas, ChromaDB, pgcli, Electricity Maps, Open Climate Fix, ScanAPI.")
    pdf.ln(1)

    # ── Education ──
    section(pdf, "EDUCATION")
    job(pdf, "MSc Data Analytics", "University (completing 2026)", "", "UK")
    job(pdf, "BCA (Bachelor of Computer Applications)", "Amity University, Noida", "2019 -2022", "India")
    pdf.ln(1)

    # ── Certifications ──
    section(pdf, "CERTIFICATIONS")
    bullet(pdf, "Microsoft PL-300: Power BI Data Analyst  |  Google Data Analytics  |  AWS Cloud Practitioner Essentials")
    bullet(pdf, "National Cadet Corps (2012-2018) - Veteran Support")

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
    pdf.cell(32, 5, label + ":")
    pdf.set_font("Helvetica", "", 9.5)
    pdf.cell(0, 5, value, ln=True)


def job(pdf, company, role, dates, location):
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(100, 5, company)
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 5, dates, ln=True, align="R")
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", "I", 9.5)
    loc_role = role
    if location:
        loc_role = f"{role}  |  {location}"
    pdf.cell(0, 5, loc_role, ln=True)


def project(pdf, name, url):
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(60, 5, name)
    pdf.set_font("Helvetica", "", 8.5)
    pdf.set_text_color(60, 60, 180)
    pdf.cell(0, 5, url, ln=True, align="R")
    pdf.set_text_color(0, 0, 0)


def bullet(pdf, text):
    pdf.set_font("Helvetica", "", 9.5)
    pdf.cell(0, 4.5, f"  -  {text}", ln=True)


if __name__ == "__main__":
    build()
