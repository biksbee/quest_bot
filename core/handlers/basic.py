from aiogram import Bot
from aiogram.types import Message
from aiogram import Bot, Router, F

router = Router()


@router.message(F.text.regexp(r"^(\d+)$").as_("digits"))
async def any_digits_handler(message: Message):
    await message.answer(message.text)


@router.message(F.text.casefold() == 'куба')
async def get_photo(message: Message, bot: Bot):
    await message.answer(f'you send me a text')
    # file = await bot.get_file(message.photo[-1].file_id)
    # await bot.download_file(file.file_path, 'photo.jpg')

