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

Open `http://127.0.0.1:8000/` for the starter welcome response. Interactive
API documentation is available at `http://127.0.0.1:8000/docs`, and the health
check is available at `http://127.0.0.1:8000/health`.

The `app` package contains the application code, `tests` contains automated
tests, and `docs` contains the evolving project documentation. Students should
update the documentation as the design and implementation develop. Start with
the [software requirements specification template](docs/requirements.md) and
the [software architecture template](docs/architecture.md), replacing or
removing the prompts that do not apply to the project.

SQLAlchemy 2.x manages database connections and sessions. By default, the
application stores data in the local `data/app.db` SQLite database, which is
ignored by Git. The starter supplies the engine, session factory, declarative
base, and FastAPI database dependency. Students define their own ORM models,
relationships, constraints, and data operations as the project develops.

The starter provides the Python environment, dependencies, application
startup, database session setup, one endpoint, basic tests, CI, and Codex
instructions. Students are responsible for designing the schema, creating
SQLAlchemy ORM models and Pydantic schemas, building API endpoints and
application layers, expanding the test suite, extending CI validation, and
documenting their project decisions.

## Repository Layout

- `app/`: application package, including API, database, model, schema, and service areas
- `tests/`: automated tests
- `docs/`: SRS and architecture templates plus the AI development journal
- `.github/workflows/tests.yml`: continuous integration workflow

See [AGENTS.md](AGENTS.md) for expectations when using AI-assisted development.
