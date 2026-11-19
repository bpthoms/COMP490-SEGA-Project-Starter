from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database.connection import engine, get_db


def test_sqlite_foreign_keys_are_enabled() -> None:
    with engine.connect() as connection:
        foreign_keys_enabled = connection.scalar(text("PRAGMA foreign_keys"))

    assert foreign_keys_enabled == 1


def test_get_db_yields_session() -> None:
    database_dependency = get_db()

    try:
        session = next(database_dependency)
        assert isinstance(session, Session)
    finally:
        database_dependency.close()
