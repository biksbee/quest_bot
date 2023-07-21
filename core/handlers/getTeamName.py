from aiogram.types import Message


async def get_title(message: Message):
    team = message.chat.title
    match team:
        case "КОМАНДА 1 Chat":
            return "team1"
        case "КОМАНДА 2 Chat":
            return "team2"
        case "КОМАНДА 3 Chat":
            return "team3"
        case "КОМАНДА 4 Chat":
            return "team4"
