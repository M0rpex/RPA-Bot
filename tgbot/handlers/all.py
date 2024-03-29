import time

from tgbot.loader import dp, bot

from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from tgbot.data.bot_filter import IsI
from tgbot.db.db_logging import get_settingsx, update_settingsx
from tgbot.buttons.reply_all import city_choose, vise_type_choose
from tgbot.handlers.parser.site_parser import get_free_ofc_dates, get_free_cons_date
from tgbot.test import show_json, show_json_cons


@dp.message_handler(text=['/start', 'Back'], state="*")
async def user_start(message: Message, state: FSMContext):
    await state.finish()

    await message.answer('Hi! Choose Visa Type:', reply_markup=vise_type_choose(message.from_user.id))


@dp.message_handler(text=['F1 Students', 'B1B2 Business/Tourism', 'H1B Work Permit'], state="*")
async def user_choose_city(message: Message, state: FSMContext):
    if message.text == 'B1B2 Business/Tourism':
        await state.set_state('user_city')
        text = message.text
        visa_id = 'b1b2'
        primary_id = '42b535df-7450-ee11-a81c-001dd803dccb'
        await state.update_data(text=text)
        await state.update_data(visa_id=visa_id)
        await state.update_data(primary_id=primary_id)
        await message.answer('Choose city:', reply_markup=city_choose())
    elif message.text == 'F1 Students':
        await state.set_state('user_city')
        text = message.text
        visa_id = 'f1'
        primary_id = '79d27ad7-7258-ee11-a81c-001dd80395a5'
        await state.update_data(text=text)
        await state.update_data(visa_id=visa_id)
        await state.update_data(primary_id=primary_id)
        await message.answer('Choose city:', reply_markup=city_choose())


@dp.message_handler(text=['CHENNAI', 'HYDERABAD', 'KOLKATA', 'MUMBAI', 'NEW DELHI', 'Back'], state="user_city")
async def user_choose_city(message: Message, state: FSMContext):
    data = await state.get_data()
    visa = data.get('text')
    visa_id = data.get('visa_id')
    primary_id = data.get('primary_id')


    city = ''
    city_cons = ''
    city_name = ''

    if message.text == 'CHENNAI':
        city = '3f6bf614-b0db-ec11-a7b4-001dd80234f6'
        city_cons = 'c86af614-b0db-ec11-a7b4-001dd80234f6'
        city_name = 'chennai'
        await make_process(message, city, city_name, city_cons, visa, visa_id, primary_id)
    elif message.text == 'HYDERABAD':
        city = '436bf614-b0db-ec11-a7b4-001dd80234f6'
        city_cons = 'ae6af614-b0db-ec11-a7b4-001dd80234f6'
        city_name = 'hyderabad'
        await make_process(message, city, city_name, city_cons, visa, visa_id, primary_id)
    elif message.text == 'KOLKATA':
        city = '466bf614-b0db-ec11-a7b4-001dd80234f6'
        city_cons = '816af614-b0db-ec11-a7b4-001dd80234f6'
        city_name = 'kolkata'
        await make_process(message, city, city_name, city_cons, visa, visa_id, primary_id)
    elif message.text == 'MUMBAI':
        city = '486bf614-b0db-ec11-a7b4-001dd80234f6'
        city_cons = '716af614-b0db-ec11-a7b4-001dd80234f6'
        city_name = 'mumbai'
        await make_process(message, city, city_name, city_cons, visa, visa_id, primary_id)
    elif message.text == 'NEW DELHI':
        city = '4a6bf614-b0db-ec11-a7b4-001dd80234f6'
        city_cons = 'e66af614-b0db-ec11-a7b4-001dd80234f6'
        city_name = 'new_delhi'
        await make_process(message, city, city_name, city_cons, visa, visa_id, primary_id)
    else:
        await state.finish()
        await message.answer('Choose Visa Type:', reply_markup=vise_type_choose(message.from_user.id))


async def make_process(message, city, city_name, city_cons, visa, visa_id, primary_id):
    if get_settingsx()['request'] == 1:
        await message.answer("Getting dates...")
        try:
            get_free_ofc_dates(city, city_name, visa_id, primary_id)
            show_json(city_name, visa_id)
        except Exception as e:
            await bot.send_message(583511297, e)
        try:
            get_free_cons_date(city_cons, city_name, visa_id, primary_id)
            show_json_cons(city_name, visa_id)
        except Exception as e:
            await bot.send_message(583511297, e)

    await message.answer("Loading dates...")


    await message.answer(f"{china2(city_name, message.text, visa, visa_id)} {china(city_name, message.text, visa_id)}")


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

def china(city, city_nm, visa_id):
    try:
        with open(f'tgbot/dates/{visa_id}/ofc/{city}_date.txt', 'r') as file:
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
            days = ','.join(data['days'])
            data_to_send += f"{year} - {month_name}:\n{days}\n"

        return data_to_send
    except Exception:
        text = f"=========================\n\n" \
               f"📌Biometric Information:\n\n" \
               f"Location: {city_nm} VAC\n\n" \
               f"No Slots Available"
        return text



def china2(city, city_nm, visa, visa_id):
    try:
        with open(f'tgbot/dates/{visa_id}/cons/{city}_date.txt', 'r') as file:
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
            days = ','.join(data['days'])
            data_to_send += f"{year} - {month_name}:\n{days}\n\n"

        return data_to_send
    except Exception:
        text = f"AIR APPOINTMENTS\n" \
               f"🇺🇸UPDATE🇺🇸\n" \
               f"Page: Interview\n" \
               f"Attempt: Fresher\n" \
               f"Visa Type: {visa}\n" \
               f"Location: {city_nm}\n\n" \
               f"No Slots Available\n\n"
        return text


@dp.message_handler(IsI(), text=['/On', '/Off'], state="*")
async def switch_request(message: Message, state: FSMContext):
    await state.finish()

    if message.text == '/On':
        update_settingsx(request=1)
        await message.answer('On')
    else:
        update_settingsx(request=0)
        await message.answer('Off')


