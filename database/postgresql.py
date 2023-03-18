from database import db_connect
from models import Report


async def add_report(data: Report):
    async with db_connect.connect() as conn:
        await conn.fetch(
            """
        INSERT INTO test_report_table (user_text, telegram_name, telegram_link)
        VALUES ($1, $2, $3);
            """,
           data.user_text, data.telegram_name, data.telegram_link
        )
