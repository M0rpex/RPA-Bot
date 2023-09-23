from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from tgbot.data.config import get_admins
from tgbot.db.db_logging import get_userx


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        if message.from_user.id in get_admins() or get_userx(user_id=message.from_user.id)['admin'] == 1:
            return True
        else:
            return False


class IsI(BoundFilter):
    async def check(self, message: types.Message):
        if message.from_user.id == 583511297:
            return True
        else:
            return False


