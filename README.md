# Pawan Singh Kapkoti

Data and AI engineer. I build the systems a regulated site actually runs on, and the
controls that make it safe to point a model at a real database.

At Copernus (Apr 2025 to Jul 2026), a BRC-audited 500-person manufacturing site: around
450 of those people work a production floor that BRCGS foreign-object rules keep
phone-free and email-free, so the people generating the data could not ask it a single
question. FloorMind put it in reach, as a natural-language interface over a 147-table ERP
with read-only boundaries, SQL validation, PII redaction and a tamper-evident audit ledger.

MSc Data Analytics, Aston University (2023-24). BCA in AI and ML, Amity University (2019-22).

[LinkedIn](https://www.linkedin.com/in/pawan-singh-kapkoti-100176347) ·
[PyPI](https://pypi.org/user/pawansingh3889/)

## How I build

**Fail loudly.** Missing or invalid data raises a typed error with the right status code,
never a `.get(key, default)` shrug over a value the system requires. A wrong number that
looks right is worse than a stack trace, because nobody goes looking for it.

**A gate nobody has watched fail is decoration.** Every architecture rule ships with a test
that plants a deliberate violation and asserts the gate rejects it. Without that you have a
green badge and no evidence the check still does anything.

**The model is a constrained collaborator, not the engine.** Anything an LLM produces that
the system acts on comes back through a schema-constrained tool call and is validated
before use. Whether a weak answer gets probed is a rule, not the model's mood.

**Cost is a number someone owns.** Per-call token and spend ledgers, prompt caching on the
tiers that support it, and a pre-validated query library so routine questions never reach a
model at all. That is the difference between a demo and something you can leave running.

**On-prem by default.** Regulated data does not have to leave the network for an agent to be
useful. Read-only access, PII redaction and a hash-chained audit ledger, so what the agent
did is reconstructable afterwards rather than taken on trust.

**One commit, one complete unit.** Committed only when it builds, migrations apply, lint
passes and tests pass. A refactor and a behaviour change never share a commit.

**Reproducible or it does not count.** Lockfiles committed, regenerable output ignored,
secrets in a password store. The suite runs with no credentials, because the client wrapper
is mocked at its boundary rather than the network being hoped away.

**Write for the next reader.** Comments explain why a decision was made, not what the line
does. Match the surrounding code's naming and idiom over any personal preference.

## Selected work

- **[governed-agent-stack](https://github.com/govern-agents/governed-agent-stack):** the stack assembled. FloorMind's factory chat, elenchus surveys, and the hash-chained audit ledger in one Next.js console, every backend proxied server-side.
- **[sql-steward](https://github.com/Pawansingh3889/sql-steward):** the agent never writes SQL. Queries compile from a semantic layer; blocked PII is refused before the query runs.
- **[sql-sop](https://github.com/Pawansingh3889/sql-sop):** rule-based SQL linter on PyPI. 48 rules, SARIF output, pre-commit hook.

36 merged PRs in [drt](https://github.com/drt-hub/drt) (three releases, destinations,
parallel orchestration, CI), plus merged fixes upstream in sqlglot, Apache Superset and
SQLFluff.

Python · SQL · dbt · FastAPI · Ollama / LangGraph · Docker · CI/CD with GitHub Actions.
