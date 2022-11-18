from fastapi.applications import FastAPI

from .routers import register_routers


def init_application():
    app = FastAPI(title="Talana Kombat")
    register_routers(app)
    return app
