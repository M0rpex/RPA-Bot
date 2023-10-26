from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext

from tgbot.loader import dp, bot
from tgbot.db.db_logging import get_userx, get_all_users_user_idx, update_userx, get_all_usersx
from tgbot.data.bot_filter import IsAdmin
from tgbot.buttons.reply_all import vise_type_choose
from tgbot.buttons.inline_admin import user_control, admin_user_control
from tgbot.buttons.inline_pages.show_users_page import users_swipe_fp


@dp.message_handler(IsAdmin(), text='Show users', state="*")
async def show_subscribed_users(message: Message, state: FSMContext):
    await state.finish()

    await message.answer(f'<b>Choose user:</b>\n<u>Number of users:</u> <b>{len(get_all_usersx())}</b>',
                         reply_markup=users_swipe_fp(0))


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


@dp.message_handler(IsAdmin(), text='Make advertisement', state="*")
async def make_ad(message: Message, state: FSMContext):
    keyboard = ReplyKeyboardRemove()

    await message.answer('Write a post to promote it', reply_markup=keyboard)

    await state.set_state('promotion')


@dp.message_handler(state='promotion')
async def if_need_photo(message: Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('Add photo')
    keyboard.row('Skip')
    keyboard.row('Cancel')

    await state.update_data(text=message.text)
    await state.set_state('promotion_second')
    await message.answer('Click the button below if you need to add a photo to your text', reply_markup=keyboard)


@dp.message_handler(text='Add photo', state='promotion_second')
async def get_photo(message: Message):
    keyboard = ReplyKeyboardRemove()

    await message.answer('Send the photo', reply_markup=keyboard)


@dp.message_handler(content_types=['photo'], state='promotion_second')
async def photo_processing(message: Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('Send')
    keyboard.row('Cancel')

    data = await state.get_data()
    text = data.get('text')
    file_id = message.photo[-1]
    photo = file_id.file_id

    await state.update_data(photo=photo)
    await message.answer('Your message, will look like?', reply_markup=keyboard)
    await bot.send_photo(message.from_user.id, photo, caption=text)


@dp.message_handler(text=['Skip', 'Send', 'Cancel'], state='promotion_second')
async def send_message_to_users(message: Message, state: FSMContext):
    user_id = get_all_users_user_idx()
    user_ids = [user['user_id'] for user in user_id]
    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo')

    await message.answer('Main menu', reply_markup=vise_type_choose(message.from_user.id))

    if message.text == 'Cancel':
        await state.finish()
    elif message.text == 'Send':
        try:
            for user_id in user_ids:
                await bot.send_photo(user_id, photo, caption=text)
            await message.answer("Ads sent to users")
            await state.finish()
        except Exception as e:
            print(e)
    else:
        try:
            for user_id in user_ids:
                await bot.send_message(user_id, text)
            await message.answer("Ads sent to users")
            await state.finish()
        except Exception as e:
            print(e)


@dp.message_handler(IsAdmin(), text='Find subscriber', state="*")
async def find_user(message: Message, state: FSMContext):
    await state.finish()
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('Back')

    await message.answer("Write the user's nickname or name(ex. of nickname without @: username)",
                         reply_markup=keyboard)

    await state.set_state('show_subscribers')


@dp.message_handler(state='show_subscribers')
async def show_user_info(message: Message, state: FSMContext):
    user_query = message.text

    try:
        if message.text == 'back':
            await state.finish()
            await message.answer('Main menu', reply_markup=vise_type_choose(message.from_user.id))
        else:
            user = get_user_by_login_or_name(user_query)
            if user:
                admin_status = 'Yes' if user['admin'] == 1 else 'No'
                text = f"<b>User Information</b>\n" \
                       f"Name: {user['user_name']}\n" \
                       f"Nickname: @{user['user_login']}\n" \
                       f"Admin access: {admin_status}"
                await message.answer(text, reply_markup=admin_user_control(user['user_id']))
            else:
                await message.answer('user not found')
    except Exception as e:
        print(e)


def get_user_by_login_or_name(user_query):
    user = get_userx(user_login=user_query)
    if user is None:
        user = get_userx(user_name=user_query)
    return user


@dp.callback_query_handler(text_startswith='switch_access', state="*")
async def switch_user_access(query: CallbackQuery, state: FSMContext):
    await state.finish()
    data = query.data.split(":")[1]
    user_id = query.data.split(":")[2]

    if data not in ['give', 'remove']:
        await query.message.delete()
        await query.message.answer('Main menu:', reply_markup=vise_type_choose(query.from_user.id))
    else:
        admin_value = 1 if data == 'give' else 0
        update_userx(user_id, admin=admin_value)
        get_user = get_userx(user_id=user_id)
        admin_status = 'Yes' if get_user['admin'] == 1 else 'No'
        text = f"<b>User Information</b>\n" \
               f"Name: {get_user['user_name']}\n" \
               f"Nickname: @{get_user['user_login']}\n" \
               f"Admin access: {admin_status}"
        await query.message.edit_text(text, reply_markup=admin_user_control(user_id))
