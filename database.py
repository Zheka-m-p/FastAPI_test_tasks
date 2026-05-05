from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

SQLALCHEMY_DATABASE_URL = 'sqlite+aiosqlite:///urls.db'
engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
new_session = async_sessionmaker(engine, expire_on_commit=False)

host="127.0.0.1"
port=8080

async def get_session():  #
    async with new_session() as session:
        try:
            yield session
        finally:
            await session.close()