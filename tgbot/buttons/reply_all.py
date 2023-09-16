from aiogram.types import ReplyKeyboardMarkup

def city_choose():

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("CHENNAI", "HYDERABAD", "KOLKATA")
    keyboard.row("MUMBAI", "NEW DELHI")
    return keyboard