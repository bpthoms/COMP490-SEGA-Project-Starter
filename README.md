# COMP490-SEGA Project Starter

Starter template for COMP490-SEGA-Project-Starter.

## Getting Started

Create a virtual environment and install the development dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Run the test suite:

```bash
pytest
```

Start the development server:

```bash
uvicorn app.main:app --reload
```

The starter health check is available at `http://127.0.0.1:8000/health`.

The `app` package contains the application code, `tests` contains automated
tests, and `docs` contains the evolving project documentation. Students should
update the documentation as the design and implementation develop. SQLite is
configured to use `data/app.db`, which is ignored by Git.

The starter provides the Python environment, dependencies, application
startup, database connection setup, one endpoint, one test, basic CI, and
Codex instructions. Students are responsible for designing the schema,
building API endpoints and application layers, expanding the test suite,
extending CI validation, and documenting their project decisions.

## Repository Layout

- `app/`: application package and feature areas
- `tests/`: automated tests
- `docs/`: requirements, architecture, and AI development journal
- `.github/workflows/tests.yml`: continuous integration workflow

See [AGENTS.md](AGENTS.md) for expectations when using AI-assisted development.
