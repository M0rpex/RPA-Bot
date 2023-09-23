from tgbot.loader import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup


@dp.message_handler(text=['/f1', '/b1b2', '/h1bh4', '/h1b', '/contacts', '/whatsapp'], state="*")
async def user_commands(message: Message, state: FSMContext):
    await state.finish()

    f1b = InlineKeyboardMarkup(
    ).add(
        InlineKeyboardButton("Link", url='https://t.me/+E35o9Txp8wI4N2U0')
    )

    b1b2b = InlineKeyboardMarkup(
    ).add(
        InlineKeyboardButton("Link", url='https://t.me/+Oe-hZdtmfoE5NzI0')
    )
    h1bh4b = InlineKeyboardMarkup(
    ).add(
        InlineKeyboardButton("Link", url='https://t.me/+8WkX-7RJZgsyYWFk')
    )
    h1bb = InlineKeyboardMarkup(
    ).add(
        InlineKeyboardButton("Link", url='https://t.me/+4s53hmB1ECY5N2Q0')
    )
    walinkb = InlineKeyboardMarkup(
    ).add(
        InlineKeyboardButton("Link", url='https://whatsapp.com/channel/0029Va4nHJd05MUocdJ77912')
    )

    if message.text == '/f1':
        await message.answer('<strong>F1 Premium</strong>', reply_markup=f1b)
    elif message.text == '/b1b2':
        await message.answer('<strong>B1/B2 Premium</strong>', reply_markup=b1b2b)
    elif message.text == '/h1bh4':
        await message.answer('<strong>H1B/H4 Premium</strong>', reply_markup=h1bh4b)
    elif message.text == '/h1b':
        await message.answer('<strong>H1B Dropbox Premium</strong>', reply_markup=h1bb)
    elif message.text == '/whatsapp':
        await message.answer('<strong>Our Whatsapp Channel</strong>', reply_markup=walinkb)
    elif message.text == '/contacts':
        await message.answer('<b>royalkhan9501@gmail.com | WhatsApp - +91 7719467596</b>')








