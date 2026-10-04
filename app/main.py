from fastapi import FastAPI
from sqlalchemy import text

from app.db.database import engine

app = FastAPI(
    title="Rowdy API",
    version="0.1.0",
)


@app.get("/health")
async def health_check():
    async with engine.connect() as connection:
        result = await connection.execute(text("SELECT 1"))
        return {
            "status": "ok",
            "database": result.scalar(),
        }
