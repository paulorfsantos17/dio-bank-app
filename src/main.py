from fastapi import FastAPI

from src.app.auth.interfaces.routes.user import routes as user_routes

app = FastAPI()

app.include_router(user_routes)