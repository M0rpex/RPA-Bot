import json
import time

from datetime import datetime

from tgbot.loader import dp

from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from tgbot.buttons.reply_all import city_choose
from tgbot.handlers.parser.site_parser import get_free_ofc_dates, get_free_cons_date
from tgbot.test import show_json


@dp.message_handler(text='/start', state="*")
async def user_start(message: Message, state: FSMContext):
    await state.finish()

    await message.answer('Hi! Choose city:', reply_markup=city_choose())


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


    await message.answer("Getting dates... 10 seconds")
    get_free_ofc_dates(city, city_name)
    get_free_cons_date(city, city_name)
    time.sleep(10)
    await message.answer("Loading dates... 10 seconds")
    show_json(city_name)
    time.sleep(10)
    await message.answer(f"{china2(city, city_name)} {china(city_name, message.text)}")



@dp.message_handler(text="/check", state="*")
async def check_check(message: Message, state: FSMContext):
    await state.finish()

    print(show_json())
    show_json()

    test = """
    
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
    """


month_names = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}

def china(city, city_nm):
    with open(f'tgbot/dates/{city}_date.txt', 'r') as file:
        lines = file.readlines()

    formatted_data = {}  # Создаем словарь для хранения отформатированных данных

    for line in lines:
        parts = line.strip().split('-')  # Разделяем строку на части по символу "-"
        if len(parts) == 3:  # Убеждаемся, что строка содержит дату в формате "день-месяц-год"
            day, month, year = parts
            month_name = month_names.get(month, '')  # Получаем название месяца из словаря
            if month_name:
                if month_name not in formatted_data:
                    formatted_data[month_name] = {'year': year, 'days': []}  # Если месяц встречается впервые, создаем структуру данных для него
                formatted_data[month_name]['days'].append(day)  # Добавляем день в список

    # Отправляем данные в чат бота
    data_to_send = f"=================\n\n" \
                   f"📌Biometric Information:\n\n" \
                   f"Location: {city_nm} VAC\n\n"
    for month_name, data in formatted_data.items():
        year = data['year']
        days = ', '.join(data['days'])
        data_to_send += f"{year} - {month_name}:\n{days}\n"

    return data_to_send


def china2(city, city_nm):
    with open(f'tgbot/dates/cons/{city}_date.txt', 'r') as file:
        lines = file.readlines()

    formatted_data = {}  # Создаем словарь для хранения отформатированных данных

    for line in lines:
        parts = line.strip().split('-')  # Разделяем строку на части по символу "-"
        if len(parts) == 3:  # Убеждаемся, что строка содержит дату в формате "день-месяц-год"
            day, month, year = parts
            month_name = month_names.get(month, '')  # Получаем название месяца из словаря
            if month_name:
                if month_name not in formatted_data:
                    formatted_data[month_name] = {'year': year, 'days': []}  # Если месяц встречается впервые, создаем структуру данных для него
                formatted_data[month_name]['days'].append(day)  # Добавляем день в список

    # Отправляем данные в чат бота
    data_to_send = f"AIR APPOINTMENTS\n" \
                   f"🇺🇸UPDATE🇺🇸\n" \
                   f"Page: Biometric\n" \
                   f"Attempt: Fresher\n" \
                   f"Visa Type: B1/B2\n" \
                   f"Location: {city_nm}\n\n"
    for month_name, data in formatted_data.items():
        year = data['year']
        days = ', '.join(data['days'])
        data_to_send += f"{year} - {month_name}:\n{days}\n"

    return data_to_send