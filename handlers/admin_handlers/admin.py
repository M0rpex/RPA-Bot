
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from tgbot.loader import dp, bot
from tgbot.db.db_logging import get_userx, get_all_users_user_idx
from tgbot.data.bot_filter import IsAdmin
from tgbot.buttons.inline_admin import user_control
from tgbot.buttons.inline_pages.show_users_page import users_swipe_fp


@dp.message_handler(IsAdmin(), text='Show users', state="*")
async def show_subscribed_users(message: Message, state: FSMContext):
    await state.finish()

    await message.answer('<b>Choose user:</b>', reply_markup=users_swipe_fp(0))

@dp.callback_query_handler(text_startswith='users_open_info', state="*")
async def show_user_info(query: CallbackQuery, state: FSMContext):
    await state.finish()

    user_id = query.data.split(":")[1]
    remover = query.data.split(":")[2]

    get_user = get_userx(user_id=user_id)

    text = f"<strong>USER INFO</strong>\n\n" \
           f"Name: {get_user['user_name']}\n" \
           f"Login: @{get_user['user_login']}"

    await query.message.edit_text(text, reply_markup=user_control(remover))

@dp.callback_query_handler(text_startswith='users_open_swipe', state="*")
async def show_user_info_swipe(query: CallbackQuery, state: FSMContext):
    await state.finish()

    remover = int(query.data.split(":")[1])

    await query.message.edit_text('<b>Choose user:</b>', reply_markup=users_swipe_fp(remover))


# Dorobity advertisment
@dp.message_handler(IsAdmin(), text='Make advertisement', state="*")
async def make_ad(message: Message, state: FSMContext):

    await message.answer('Write a post to promote it')

    await state.set_state('promotion')


@dp.message_handler(state='promotion')
async def send_message_to_users(message: Message, state: FSMContext):

    user_id = get_all_users_user_idx()
    user_ids = [user['user_id'] for user in user_id]

    try:
        for user_id in user_ids:
            await bot.send_message(user_id, message.text)

        await message.answer("Ads sent to users")
        await state.finish()
    except Exception:
        pass


