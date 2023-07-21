# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
#
#
# def inline_date_button() -> list[list[InlineKeyboardButton]]:
#     return [
#         [
#             InlineKeyboardButton(text='left', callback_data='time_left')
#         ]
#     ]
#
#
# async def get_inline_keyboard() -> InlineKeyboardMarkup:
#     keyboard = inline_date_button()
#     return InlineKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
#
#
# def get_date_button() -> list[list[KeyboardButton]]:
#     return [
#         [
#             KeyboardButton(text="time left", )
#         ]
#     ]
#
#
# async def get_keyboard() -> ReplyKeyboardMarkup:
#     keyboard = get_date_button()
#
#     return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)