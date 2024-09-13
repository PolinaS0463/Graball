import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from .models import Base

load_dotenv()
engine = create_async_engine(url='', echo=True)
session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def create_database():
    async with engine.begin() as con:
        await con.run_sync(Base.metadata.create_all)

async def drop_database():
    async with engine.begin() as con:
        await con.run_sync(Base.metadata.drop_all)