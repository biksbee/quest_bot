import asyncio
import logging
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.methods.get_file import GetFile

from core.handlers.basic import get_photo
from core.handlers.get_time_left import get_time_left
from core.handlers.getTeamName import get_title

# from core.keyboards.date_markup import get_keyboard, get_inline_keyboard

TOKEN = "6316182906:AAGPOsasElZGkMJ9757CCOd3yB98Tvq9ZKE"
ADMIN_ID = 503192108

router = Router()


@router.message(Command(commands=["start"]))
async def command_start_handler(message: Message, bot: Bot) -> None:
    team_name = await get_title(message)
    time_left = await get_time_left(team_name)
    if message.from_user.id == ADMIN_ID and time_left != 0:
        await bot.send_message(chat_id=message.chat.id,
                               text=f"Для {message.chat.title} квест начнется через: {time_left}")
    elif message.from_user.id != ADMIN_ID:
        await bot.send_message(chat_id=message.chat.id,
                               text=f"{message.from_user.first_name}, не_лезь_блядь_дибил_сука_ебаный!")
    else:
        await bot.send_message(chat_id=message.chat.id,
                               text=f"Квест начался")
    while time_left != 0:
        await asyncio.sleep(10)
        time_left = await get_time_left(team_name)
    await send_video(message, bot)


@router.message(Command(commands=["date"]))
async def date_handler(message: Message, bot: Bot):
    team_name = await get_title(message)
    time_left = await get_time_left(team_name)
    if time_left != 0:
        await bot.send_message(chat_id=message.chat.id,
                               text=f"Для {message.chat.title} квест начнется через: {time_left}")
    else:
        await bot.send_message(chat_id=message.chat.id,
                               text="Квест уже начался")


async def send_video(message, bot):
    pass
    # video = open("video/1.webm", 'rb')
    # photo = open("image/1.jpg", 'rb')
    # await bot.send_video(message.chat.id, video=video)
    # await bot.send_photo(chat_id=message.chat.id, photo=photo")


@router.message(F.photo)
async def get_photo(message: Message, bot: Bot):
    file: File = await bot(GetFile(message.photo[-1].file_id))
    await bot.download_file(file.file_path)
    await bot.send_message(message.chat.id, text="Downloading successful!!!")


async def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    # ... and all other routers should be attached to Dispatcher
    dp.include_router(router)
    dp.message.filter(get_photo, F.photo)
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode="HTML")
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
