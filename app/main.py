"""FastAPI application entry point."""

from fastapi import FastAPI


app = FastAPI(title="COMP 490 Software Engineering Project")


@app.get("/")
def root() -> dict[str, str]:
    """Welcome users and point them to the starter's useful endpoints."""
    return {
        "message": "Welcome to the COMP 490 Software Engineering Project",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    """Return the basic application health status."""
    return {"status": "ok"}
