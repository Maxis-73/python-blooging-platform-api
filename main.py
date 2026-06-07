from fastapi import FastAPI
from src.core.settings import settings
from src.core.database import engine, Base
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    lifespan=lifespan
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Blog Platform API"}

@app.get("/health")
async def health():
    return {"status": "OK"}