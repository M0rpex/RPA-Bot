import math

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton as ikb

from tgbot.db.db_logging import get_all_usersx

def users_swipe_fp(remover):
    keyboard = InlineKeyboardMarkup()

    get_users = get_all_usersx()

    remover_page = len(get_users) + (10 - (len(get_users) % 10))

    if remover >= len(get_users): remover -= 10

    for count, a in enumerate(range(remover, len(get_users))):
        if count < 10:
            keyboard.add(ikb(
                f"@{get_users[a]['user_login']} | {get_users[a]['user_name']}",
                callback_data=f"users_open_info:{get_users[a]['user_id']}:{remover}",
            ))
    if len(get_users) <= 10:
        pass
    elif len(get_users) > 10 and remover < 10:
        if len(get_users) > 20:
            keyboard.add(
                ikb(f"1/{math.ceil(len(get_users) / 10)}", callback_data="..."),
                ikb("➡", callback_data=f"users_open_swipe:{remover + 10}"),
                ikb("⏩", callback_data=f"users_open_swipe:{remover_page}"),
            )
        else:
            keyboard.add(
                ikb(f"1/{math.ceil(len(get_users) / 10)}", callback_data="..."),
                ikb("➡", callback_data=f"users_open_swipe:{remover + 10}")
            )
    elif remover + 10 >= len(get_users):
        if len(get_users) > 20:
            keyboard.add(
                ikb("⏪", callback_data=f"users_open_swipe:0"),
                ikb("⬅", callback_data=f"users_open_swipe:{remover - 10}"),
                ikb(f"{str(remover + 10)[:-1]}/{math.ceil(len(get_users) / 10)}", callback_data="..."),
            )
        else:
            keyboard.add(
                ikb("⬅", callback_data=f"users_open_swipe:{remover - 10}"),
                ikb(f"{str(remover + 10)[:-1]}/{math.ceil(len(get_users) / 10)}", callback_data="...")
            )
    else:
        if len(get_users) > 20:
            keyboard.add(
                ikb("⏪", callback_data=f"users_open_swipe:0"),
                ikb("⬅", callback_data=f"users_open_swipe:{remover - 10}"),
                ikb(f"{str(remover + 10)[:-1]}/{math.ceil(len(get_users) / 10)}", callback_data="..."),
                ikb("➡", callback_data=f"users_open_swipe:{remover + 10}"),
                ikb("⏩", callback_data=f"users_open_swipe:{remover_page}"),
            )
        else:
            keyboard.add(
                ikb("⬅", callback_data=f"users_open_swipe:{remover - 10}"),
                ikb(f"{str(remover + 10)[:-1]}/{math.ceil(len(get_users) / 10)}", callback_data="..."),
                ikb("➡", callback_data=f"users_open_swipe:{remover + 10}"),
            )

    return keyboard