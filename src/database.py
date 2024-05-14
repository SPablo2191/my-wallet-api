from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import  SQLModel,create_engine,Session

from src.config import settings as global_settings

engine = create_engine(global_settings.db_uri, echo=True)

@asynccontextmanager
async def lifespan(_: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

def get_session():
    with Session(engine) as session:
        yield session