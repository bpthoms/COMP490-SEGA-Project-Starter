"""FastAPI application entry point."""

from fastapi import FastAPI


app = FastAPI(title="COMP 490 Software Engineering Project")


@app.get("/health")
def health_check() -> dict[str, str]:
    """Return the basic application health status."""
    return {"status": "ok"}