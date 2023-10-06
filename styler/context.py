from pydantic import BaseModel
from fastapi import Request

from sqlalchemy.ext.asyncio import AsyncSession

class Context(BaseModel):
    request: Request = None
    session: AsyncSession = None

    class Config:
        arbitrary_types_allowed = True