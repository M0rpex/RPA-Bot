from aiogram import Dispatcher
from aiogram.types import BotCommand, BotCommandScopeChat, BotCommandScopeDefault
from tgbot.data.config import get_admins


commands = [
    BotCommand("start", "Перезапуск бота")
]

adm_commands = [
    BotCommand("start", "Перезапуск бота"),
    BotCommand("startadmin", "Запуск команд для админа")
]


async def set_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(commands, scope=BotCommandScopeDefault())

    for admin in get_admins():
        await dp.bot.set_my_commands(adm_commands, scope=BotCommandScopeChat(chat_id=admin))



