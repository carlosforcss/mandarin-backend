from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.config.db import init_db, close_db
from app.routes import hanzi, file, category, sentence


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await close_db()


def create_app() -> FastAPI:
    app = FastAPI(
        title="Mandarin Learning API",
        description="API for learning Mandarin Hanzis",
        version="1.0.0",
        lifespan=lifespan,
    )

    app.include_router(hanzi.router, prefix="/api/hanzi", tags=["hanzi"])
    app.include_router(file.router, prefix="/api/files", tags=["files"])
    app.include_router(category.router, prefix="/api/categories", tags=["categories"])
    app.include_router(sentence.router, prefix="/api/sentences", tags=["sentences"])

    return app
