
@dp.message_handler(regexp='ебень|зага|любимка')
async def zaga(message: types.Message):
    with open('/media/img.png', 'rb') as photo:
        # await message.reply_photo(photo, caption='Cats are here 😺')
        await message.reply_photo(photo)


@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    with open('/media/img.png', 'rb') as photo:
        # await message.reply_photo(photo, caption='Cats are here 😺')
        await message.reply_photo(photo)