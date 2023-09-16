import json

from datetime import datetime

from tgbot.loader import dp

from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from tgbot.buttons.reply_all import city_choose
from tgbot.handlers.parser.site_parser import get_free_dates
from tgbot.test import show_json


@dp.message_handler(text='/start', state="*")
async def user_start(message: Message, state: FSMContext):
    await state.finish()

    await message.answer('Hi!, Choose city:', reply_markup=city_choose())


@dp.message_handler(text=['CHENNAI', 'HYDERABAD', 'KOLKATA', 'MUMBAI', 'NEW DELHI'], state="*")
async def user_choose_city(message: Message, state: FSMContext):
    await state.finish()
    city = ''
    city_name = ''

    if message.text == 'CHENNAI':
        city = '3f6bf614-b0db-ec11-a7b4-001dd80234f6'
        city_name = 'chennai'

    elif message.text == 'HYDERABAD':
        city = '436bf614-b0db-ec11-a7b4-001dd80234f6'
        city_name = 'hyderabad'

    elif message.text == 'KOLKATA':
        city = '466bf614-b0db-ec11-a7b4-001dd80234f6'
        city_name = 'kolkata'

    elif message.text == 'MUMBAI':
        city = '486bf614-b0db-ec11-a7b4-001dd80234f6'
        city_name = 'mumbai'

    elif message.text == 'NEW DELHI':
        city = '4a6bf614-b0db-ec11-a7b4-001dd80234f6'
        city_name = 'new_delhi'


    get_free_dates(city, city_name)

@dp.message_handler(text="/check", state="*")
async def check_check(message: Message, state: FSMContext):
    await state.finish()

    print(show_json())

    months = {}
    text = ''
    first_month = ''

    for data_dict in show_json():
        date_str = data_dict["Date"]  # Предполагаем, что дата хранится в поле "date" словаря
        date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
        month_key = date.strftime("%B")  # Форматируем месяц и год в строку-ключ
        if month_key not in months:
            months[month_key] = []
        months[month_key].append(date.strftime("%d"))  # Форматируем дату в строку и добавляем в список

    # Выводим результат
    for month, date_list in months.items():
        print(month)

        first_month = month

        for date in date_list:

            text += f"{date}"

            print(f"{date}")

    await message.answer(f"{first_month}:\n"
                         f"{text}")

    #for days in show_json():
    #    date = days.get('Date', '')
    #    date_object = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
    #    formatted_date = date_object.strftime("%B %d")

    #    await message.answer(formatted_date)


@dp.message_handler(text="/show", state="*")
async def show_info(message: Message, state: FSMContext):
    await state.finish()

    text = f"AIR APPOINTMENTS\n" \
           f"UPDATE\n" \
           f"Page: Interview\n" \
           f"Attempt: Fresher\n" \
           f"Visa Type: B1/B2\n\n\n" \
           f"======================\n\n" \
           f"Biometric Information:\n\n" \
           f"Location: CHENNAI VAC\n" \
           f""

    info = """
    AIR APPOINTMENTS
    UPDATE
    Page: Interview
    Attempt: Fresher
    Visa Type: B1/B2
    
    ======================
    
    Biometric Information:
    Location: CHENNAI VAC
    January:
    21, 22, 23, 24, 28, 30
    February:
    2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 21, 22
    """

    await message.answer(info)



