from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlmodel import create_engine
from sqlalchemy.orm import sessionmaker

from styler.config import config

async_engine = create_async_engine(config.alchemy_host, echo=True)
# engine = create_engine(config.alchemy_host, echo=True)

session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
