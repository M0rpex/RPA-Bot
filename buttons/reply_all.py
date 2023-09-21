from aiogram.types import ReplyKeyboardMarkup

from tgbot.data.config import get_admins


def city_choose():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("CHENNAI", "HYDERABAD", "KOLKATA")
    keyboard.row("MUMBAI", "NEW DELHI")
    keyboard.row("Back")
    return keyboard


def vise_type_choose(user_id):

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("F1 Students", "B1B2 Business/Tourism", "H1B Work Permit")

    if user_id in get_admins():
        keyboard.row("Show users", "Make advertisement")

    return keyboard
