"""SQLite connection setup for the application."""

import sqlite3
from pathlib import Path


DATABASE_PATH = Path("data/app.db")


def get_connection(database_path: Path = DATABASE_PATH) -> sqlite3.Connection:
    """Open a SQLite connection and enable foreign-key enforcement."""
    database_path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(database_path)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection