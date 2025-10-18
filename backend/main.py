from fastapi import FastAPI
from backend.config import settings

app = FastAPI(title="FastAPI Project")


@app.get("/")
def root():
    return {"url": settings.DATABASE_URL}
