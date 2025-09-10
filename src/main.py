from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.app.auth.interfaces.routes.user import routes as user_routes
from src.app.shared.database.database_config import database


@asynccontextmanager
async def lifespan(app: FastAPI):

    # Startup
    await database.connect()
    yield
    # Shutdown
    await database.disconnect()

app = FastAPI(lifespan=lifespan)


app.include_router(user_routes)