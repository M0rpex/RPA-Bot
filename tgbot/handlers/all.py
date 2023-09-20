import time

from tgbot.loader import dp

from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from tgbot.data.bot_filter import IsI
from tgbot.db.db_logging import get_settingsx, update_settingsx
from tgbot.buttons.reply_all import city_choose, vise_type_choose
from tgbot.handlers.parser.site_parser import get_free_ofc_dates, get_free_cons_date
from tgbot.test import show_json


@dp.message_handler(text=['/start', 'Back'], state="*")
async def user_start(message: Message, state: FSMContext):
    await state.finish()

    await message.answer("Hi! Choose Visa Type:", reply_markup=vise_type_choose(message.from_user.id))

@dp.message_handler(text=['F1 Students', 'B1B2 Business/Tourism', 'H1B Work Permit', 'Back'], state="*")
async def user_choose_city(message: Message, state: FSMContext):

    if message.text == 'B1B2 Business/Tourism':
        await state.set_state('user_city')
        text = message.text
        await state.update_data(text=text)
        await message.answer('Choose city:', reply_markup=city_choose())
    else:
        await message.answer('Visa Type Not Available')
        await state.finish()



@dp.message_handler(text=['CHENNAI', 'HYDERABAD', 'KOLKATA', 'MUMBAI', 'NEW DELHI'], state="user_city")
async def user_choose_city(message: Message, state: FSMContext):
    data = await state.get_data()
    visa = data.get('user_city')


    city = ''
    city_cons = ''
    city_name = ''

    if message.text == 'CHENNAI':
        city = '3f6bf614-b0db-ec11-a7b4-001dd80234f6'
        city_cons = 'c86af614-b0db-ec11-a7b4-001dd80234f6'
        city_name = 'chennai'
        await make_process(message, city, city_name, city_cons, visa)
    elif message.text == 'HYDERABAD':
        city = '436bf614-b0db-ec11-a7b4-001dd80234f6'
        city_cons = 'ae6af614-b0db-ec11-a7b4-001dd80234f6'
        city_name = 'hyderabad'
        await make_process(message, city, city_name, city_cons, visa)
    elif message.text == 'KOLKATA':
        city = '466bf614-b0db-ec11-a7b4-001dd80234f6'
        city_cons = '816af614-b0db-ec11-a7b4-001dd80234f6'
        city_name = 'kolkata'
        await make_process(message, city, city_name, city_cons, visa)
    elif message.text == 'MUMBAI':
        city = '486bf614-b0db-ec11-a7b4-001dd80234f6'
        city_cons = '716af614-b0db-ec11-a7b4-001dd80234f6'
        city_name = 'mumbai'
        await make_process(message, city, city_name, city_cons, visa)
    elif message.text == 'NEW DELHI':
        city = '4a6bf614-b0db-ec11-a7b4-001dd80234f6'
        city_cons = 'e66af614-b0db-ec11-a7b4-001dd80234f6'
        city_name = 'new_delhi'
        await make_process(message, city, city_name, city_cons, visa)
    else:
        await state.finish()
        await message.answer('Choose Visa Type:', reply_markup=vise_type_choose(message.from_user.id))


async def make_process(message, city, city_name, city_cons, visa):
    if get_settingsx()['request'] == 1:
        await message.answer("Getting dates...")
        get_free_ofc_dates(city, city_name)
        get_free_cons_date(city_cons, city_name)

    await message.answer("Loading dates...")
    show_json(city_name)
    await message.answer(f"{china2(city_name, message.text, visa)} {china(city_name, message.text)}")


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
    try:
        with open(f'tgbot/dates/ofc/{city}_date.txt', 'r') as file:
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
        data_to_send = f"=========================\n\n" \
                       f"📌Biometric Information:\n\n" \
                       f"Location: {city_nm} VAC\n\n"
        for month_name, data in formatted_data.items():
            year = data['year']
            days = ', '.join(data['days'])
            data_to_send += f"{year} - {month_name}:\n{days}\n"

        return data_to_send
    except Exception:
        text = f"=========================\n\n" \
               f"📌Biometric Information:\n\n" \
               f"Location: {city_nm} VAC\n\n" \
               f"No Slots Available"
        return text



def china2(city, city_nm, visa):
    try:
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
                       f"Page: Interview\n" \
                       f"Attempt: Fresher\n" \
                       f"Visa Type: {visa}\n" \
                       f"Location: {city_nm}\n\n"
        for month_name, data in formatted_data.items():
            year = data['year']
            days = ', '.join(data['days'])
            data_to_send += f"{year} - {month_name}:\n{days}\n\n"

        return data_to_send
    except Exception:
        text = f"AIR APPOINTMENTS\n" \
               f"🇺🇸UPDATE🇺🇸\n" \
               f"Page: Interview\n" \
               f"Attempt: Fresher\n" \
               f"Visa Type: B1/B2\n" \
               f"Location: {city_nm}\n\n" \
               f"No Slots Available\n\n"
        return text



@dp.message_handler(IsI(), text=['On', 'Off'], state="*")
async def switch_request(message: Message, state: FSMContext):
    await state.finish()

    if message.text == 'On':
        update_settingsx(request=1)
        await message.answer('On')
    else:
        update_settingsx(request=0)
        await message.answer('Off')


