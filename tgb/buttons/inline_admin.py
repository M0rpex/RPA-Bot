from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from tgbot.db.db_logging import get_userx
def user_control(remover):
    keyboard = InlineKeyboardMarkup(
    ).add(
        InlineKeyboardButton('Back', callback_data=f'users_open_swipe:{remover}')
    )
    return keyboard

def admin_user_control(user_id):
    get_user = get_userx(user_id=user_id)

    if get_user['admin'] == 1:
        text = 'Remove access'
        cdm = 'remove'
    else:
        text = 'Give access'
        cdm = 'give'

    keyboard = InlineKeyboardMarkup(
    ).add(
        InlineKeyboardButton(text, callback_data=f'switch_access:{cdm}:{user_id}')
    ).add(
        InlineKeyboardButton('Close', callback_data=f'switch_access:close:{user_id}')
    )
    return keyboard
