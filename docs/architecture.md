# Architecture

Document the system's major components, responsibilities, and interactions.
Include diagrams or decision records when they clarify the design.

The starter uses FastAPI for HTTP handling and SQLite for local persistence.
The connection helper enables foreign-key enforcement without prescribing a
student schema. Students should document how their schema and application
layers build on this foundation.

## Components

- `app/api`: external interfaces and request handling
- `app/models`: domain and data representations
- `app/services`: application and business logic
- `app/database`: persistence and database access

## Architecture Decisions

Record important decisions, alternatives considered, and the reason for the
chosen approach.