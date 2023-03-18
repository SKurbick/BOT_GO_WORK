from database.postgresql import add_report
import re
import logging
import hashlib
from aiogram import Bot, Dispatcher, executor, types

from models import Report
from settings import settings
from aiogram.types import InlineQuery, \
    InputTextMessageContent, InlineQueryResultArticle, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

# API_TOKEN = settings.TOKEN_SALAM_BOT
# API_TOKEN = settings.TOKEN_ANUBIS_BOT
API_TOKEN = settings.TOKEN_GOWORK_BOT
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.inline_handler()
async def inline_echo(inline_query: InlineQuery):
    text = f"{inline_query.query}\n, {inline_query.id}\n,{inline_query.from_user.username}\n,{inline_query.location}\n"
    # text2 =
    # text3 =
    # text4 = inline_query.location
    # print(text)
    input_content = InputTextMessageContent(text)
    # print(input_content)
    result_id: str = hashlib.md5(text.encode()).hexdigest()

    item = InlineQueryResultArticle(

        id=result_id,

        title=f'Result {text!r}',

        input_message_content=input_content,

    )
    # print(item)
    # don't forget to set cache_time=1 for testing (default is 300s or 5m)

    await bot.answer_inline_query(inline_query.id, results=[item], cache_time=1)


@dp.message_handler(regexp='#отчет')
async def report(message: types.Message):

    data = Report(
        user_text=message.text[6:],
        telegram_name=message.from_user.full_name,
        telegram_link=message.from_user.username,
    )

    await add_report(data)
    # await message.answer(f"ОТЧЕТ ОТПРАВЛЕН {message.from_user}\n "
    #                      f"{message.contact}\n"
    #                      f"{message.text}\n")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
