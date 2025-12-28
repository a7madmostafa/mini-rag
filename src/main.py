from fastapi import FastAPI
from routes import base, data
from pymongo import AsyncMongoClient
from helpers.config import get_settings
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()

    app.mongo_conn = AsyncMongoClient(settings.MONGODB_URL)
    app.db_client  = app.mongo_conn[settings.MONGODB_DATABASE]

    yield  # 👈 app is running

    app.mongo_conn.close()  # graceful shutdown

app = FastAPI(lifespan=lifespan)


app.include_router(base.base_router)
app.include_router(data.data_router)