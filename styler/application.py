from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from .middleware import set_context, set_session
from apps.routes import router

def make_fastapi_app(*args, **kwargs):
    app = FastAPI()

    app.add_middleware(BaseHTTPMiddleware, dispatch=set_session)
    app.add_middleware(BaseHTTPMiddleware, dispatch=set_context)

    app.include_router(router)

    return app