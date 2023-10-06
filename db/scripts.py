from typing import List
from sqlmodel import SQLModel
from sqlalchemy.schema import CreateTable
from sqlalchemy import inspect

from .session import async_engine, session
from apps.looks.models import *


async def init_db(*args):
    models: List[SQLModel] = []
    for name, cls in globals().items():
        try:
            if issubclass(cls, SQLModel) and cls != SQLModel:
                models.append(cls)
        except:
            continue
    
    for model in models:
        async with async_engine.begin() as conn:
            table = model.__tablename__
            tables = await conn.run_sync(conn.dialect.get_table_names)
            if table in tables:
                    continue
            await conn.run_sync(SQLModel.metadata.create_all, tables=[model.__table__])