from aiogram import Dispatcher
from aiogram.types import BotCommand, BotCommandScopeChat, BotCommandScopeDefault
from tgbot.data.config import get_admins


user_commands = [
    BotCommand("start", "Restart bot"),
    BotCommand("f1", "F1 Premium"),
    BotCommand("b1b2", "B1/B2 Premium"),
    BotCommand("h1bh4", "H1B/H4 Premium"),
    BotCommand("h1b", "H1B Dropbox Premium"),
    BotCommand("whatsapp", "Our Whatsapp Channel"),
    BotCommand("contacts", "Contact Us")
]

adm_commands = [
    BotCommand("start", "Restart bot"),
    BotCommand("f1", "F1 Premium"),
    BotCommand("b1b2", "B1/B2 Premium"),
    BotCommand("h1bh4", "H1B/H4 Premium"),
    BotCommand("h1b", "H1B Dropbox Premium"),
    BotCommand("whatsapp", "Our Whatsapp Channel"),
    BotCommand("contacts", "Contact Us")
]


async def set_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(user_commands, scope=BotCommandScopeDefault())

    for admin in get_admins():
        await dp.bot.set_my_commands(adm_commands, scope=BotCommandScopeChat(chat_id=admin))



