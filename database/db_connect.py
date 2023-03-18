import asyncpg
from contextlib import asynccontextmanager
from settings import settings


@asynccontextmanager
async def connect():
    try:
        conn = await asyncpg.connect(
            host=settings.POSTGRES_HOSTNAME,
            database=settings.POSTGRES_DATABASE,
            user=settings.POSTGRES_USER,
            password=settings.POSTGRES_PASSWORD.get_secret_value(),
            port=settings.POSTGRES_PORT)

        yield conn
        await conn.close()

    except Exception as ex:
        print(ex)
