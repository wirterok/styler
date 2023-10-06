from fastapi import FastAPI, Request
from db.session import session as async_session

from .context import Context

app = FastAPI()

@app.middleware("http")
async def set_context(request: Request, call_next):
    setattr(request.state, "context", Context())
    return await call_next(request)

@app.middleware("http")
async def set_session(request: Request, call_next):
    async with async_session() as session:
        setattr(request.state.context, "session", session)
        return await call_next(request)