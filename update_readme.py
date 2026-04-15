"""Auto-update profile README with live project data from GitHub API.

Runs via GitHub Actions on a schedule. Fetches repo metadata, recent commits,
and open PR counts, then rebuilds the README from a template.
"""

import json
import os
import urllib.request
from datetime import datetime, timezone

GITHUB_USER = "Pawansingh3889"
TOKEN = os.environ.get("GH_TOKEN", "")

# Projects to track — order matters (this is the display order)
PROJECTS = [
    {
        "repo": "OpsMind",
        "name": "OpsMind",
        "desc": "On-prem NL-to-SQL tool for manufacturing. LangGraph agent, pgvector + ChromaDB retrieval, SQL validation layer, Gemma 3 12B via Ollama.",
        "links": [],
    },
    {
        "repo": "production-analytics-pipeline",
        "name": "Production Analytics Pipeline",
        "desc": "Incremental ETL from fish production ERP. FastAPI, Next.js dashboard, Prefect orchestration, dbt transforms.",
        "links": [],
    },
    {
        "repo": "uk-crime-pipeline",
        "name": "UK Crime Pipeline",
        "desc": "Police UK API to PostgreSQL and BigQuery. dbt staging/marts, data validation with SLO monitoring.",
        "links": [
            ("streamlit", "https://uk-crime-pipeline-6nydeza7je8kiwsfl6deuw.streamlit.app/"),
            ("looker studio", "https://lookerstudio.google.com/reporting/9ee83425-04d3-4192-b4e4-de6a73d10211"),
        ],
    },
    {
        "repo": "manufacturing-compliance-dashboard",
        "name": "Compliance Dashboard",
        "desc": "BRC/HACCP food safety. Batch traceability, temperature monitoring, allergen matrix.",
        "links": [
            ("live", "https://manufacturing-compliance-dashboard-mjappkncanejzlfr5ngghik.streamlit.app"),
        ],
    },
    {
        "repo": "sql-guard",
        "name": "sql-sop",
        "desc": "SQL linter on PyPI. Pre-commit hook + fluent API.",
        "links": [
            ("pypi", "https://pypi.org/project/sql-sop/"),
        ],
        "install": "pip install sql-sop",
    },
    {
        "repo": "sql-ops-reviewer",
        "name": "SQL Ops Reviewer",
        "desc": "GitHub Action that reviews SQL in pull requests. Pairs with sql-sop.",
        "links": [],
    },
]

OPEN_SOURCE_REPOS = [
    ("drt", "drt-hub/drt"),
    ("pandas", "pandas-dev/pandas"),
    ("ChromaDB", "chroma-core/chroma"),
    ("pgcli", "dbcli/pgspecial"),
    ("ollama", "ollama/ollama-python"),
    ("superset", "apache/superset"),
    ("plotly", "plotly/plotly.py"),
    ("fpdf2", "py-pdf/fpdf2"),
]


def api_get(url):
    """Fetch JSON from GitHub API."""
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github.v3+json")
    req.add_header("User-Agent", GITHUB_USER)
    if TOKEN:
        req.add_header("Authorization", f"token {TOKEN}")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"  Warning: {url} failed: {e}")
        return None


def get_repo_info(repo_name):
    """Get stars, language, and last push date for a repo."""
    data = api_get(f"https://api.github.com/repos/{GITHUB_USER}/{repo_name}")
    if not data:
        return {"stars": 0, "language": "Python", "pushed_at": "", "description": ""}
    return {
        "stars": data.get("stargazers_count", 0),
        "language": data.get("language", "Python"),
        "pushed_at": data.get("pushed_at", ""),
        "description": data.get("description", ""),
    }


def get_latest_commit(repo_name):
    """Get the latest commit message and date."""
    data = api_get(f"https://api.github.com/repos/{GITHUB_USER}/{repo_name}/commits?per_page=1")
    if not data or not isinstance(data, list) or len(data) == 0:
        return {"message": "", "date": ""}
    commit = data[0].get("commit", {})
    msg = commit.get("message", "").split("\n")[0]  # first line only
    date = commit.get("committer", {}).get("date", "")
    return {"message": msg, "date": date}


def get_test_count(repo_name):
    """Try to extract test count from repo description or README badge."""
    data = api_get(f"https://api.github.com/repos/{GITHUB_USER}/{repo_name}")
    if not data:
        return None
    desc = data.get("description", "") or ""
    # Look for patterns like "53 tests" or "65 tests" in description
    import re
    match = re.search(r"(\d+)\s*tests?", desc, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None


def get_open_pr_count():
    """Get total open PRs by user across all repos."""
    data = api_get(
        f"https://api.github.com/search/issues?q=author:{GITHUB_USER}+is:open+is:pr&per_page=1"
    )
    if not data:
        return 0
    return data.get("total_count", 0)


def format_date(iso_str):
    """Convert ISO date to 'Apr 2026' format."""
    if not iso_str:
        return ""
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        return dt.strftime("%b %Y")
    except (ValueError, TypeError):
        return ""


def days_ago(iso_str):
    """Convert ISO date to 'X days ago' format."""
    if not iso_str:
        return ""
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        delta = datetime.now(timezone.utc) - dt
        if delta.days == 0:
            return "today"
        elif delta.days == 1:
            return "yesterday"
        elif delta.days < 30:
            return f"{delta.days}d ago"
        else:
            return format_date(iso_str)
    except (ValueError, TypeError):
        return ""


def build_readme():
    """Build the full README from live data."""
    print("Fetching project data...")

    lines = []
    lines.append("# Pawan Singh Kapkoti\n")
    lines.append("Data & Analytics Engineer. MSc Data Analytics. Yorkshire, UK.\n")
    lines.append("I build data pipelines for manufacturing and public data. I care about data quality, testing, and keeping things simple.\n")
    lines.append("[Portfolio](https://pawansingh3889.github.io)\n")
    lines.append("---\n")
    lines.append("### Projects\n")
    lines.append("| Project | Latest Change | Updated |")
    lines.append("|---|---|---|")

    for proj in PROJECTS:
        repo = proj["repo"]
        print(f"  Fetching {repo}...")
        info = get_repo_info(repo)
        commit = get_latest_commit(repo)

        # Build name with link
        name_link = f"[**{proj['name']}**](https://github.com/{GITHUB_USER}/{repo})"

        # Add extra links
        extra = ""
        if proj.get("links"):
            link_parts = [f"[{label}]({url})" for label, url in proj["links"]]
            extra = " " + " / ".join(link_parts)
        if proj.get("install"):
            extra += f" `{proj['install']}`"

        # Stars badge
        star_str = ""
        if info["stars"] > 0:
            star_str = f" ({info['stars']} star{'s' if info['stars'] != 1 else ''})"

        # Latest commit
        commit_msg = commit["message"][:60] if commit["message"] else ""
        updated = days_ago(info["pushed_at"])

        # Description line
        desc_line = proj["desc"]

        lines.append(f"| {name_link}{star_str}{extra} | {commit_msg} | {updated} |")

    # Add descriptions below table
    lines.append("")
    for proj in PROJECTS:
        name_link = f"**[{proj['name']}](https://github.com/{GITHUB_USER}/{proj['repo']})**"
        lines.append(f"{name_link} — {proj['desc']}\n")

    lines.append("---\n")

    # Open source
    lines.append("### Open source\n")
    lines.append("I contribute where I can — docs, bug fixes, small features.\n")

    # Get open PR count
    pr_count = get_open_pr_count()
    if pr_count > 0:
        lines.append(f"*{pr_count} open PRs across external repos*\n")

    os_links = [f"[{name}](https://github.com/{full})" for name, full in OPEN_SOURCE_REPOS]
    lines.append(" / ".join(os_links) + "\n")

    lines.append("---\n")

    # Stack
    lines.append("### Stack\n")
    lines.append("Python, SQL, dbt, PostgreSQL, BigQuery, FastAPI, Streamlit, Prefect, LangGraph, Ollama, Docker, Polars, pandas, Pydantic, pytest, GitHub Actions\n")

    # Footer
    lines.append("---\n")
    now = datetime.now(timezone.utc).strftime("%d %b %Y")
    lines.append(f"<sub>Last updated: {now} — auto-generated by [update_readme.py](update_readme.py)</sub>\n")

    return "\n".join(lines)


def main():
    readme = build_readme()
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)
    print(f"README.md updated ({len(readme)} bytes)")


if __name__ == "__main__":
    main()
