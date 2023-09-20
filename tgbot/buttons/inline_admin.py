from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def user_control(remover):
    keyboard = InlineKeyboardMarkup(
    ).add(
        InlineKeyboardButton('Back', callback_data=f'users_open_swipe:{remover}')
    )
    return keyboard
