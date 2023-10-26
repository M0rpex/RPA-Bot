import json
import asyncio

from tgbot.handlers.parser.site_parser import get_free_ofc_dates, get_available_hours, get_dates, post_to_ofc_date


async def last_ofc_update_scheduler():
    while True:
        try:
            print('b1b2')
            accept_later_date_for_ofc('b1b2', '42b535df-7450-ee11-a81c-001dd803dccb')

        except Exception:
            pass
        try:
            print('f1')
            accept_later_date_for_ofc('f1', '79d27ad7-7258-ee11-a81c-001dd80395a5')
        except Exception:
            pass

        await asyncio.sleep(180)

params_list_b1b2 = [
    ("3f6bf614-b0db-ec11-a7b4-001dd80234f6", "chennai", "b1b2", "42b535df-7450-ee11-a81c-001dd803dccb"),
    ("436bf614-b0db-ec11-a7b4-001dd80234f6", "hyderabad", "b1b2", "42b535df-7450-ee11-a81c-001dd803dccb"),
    ("466bf614-b0db-ec11-a7b4-001dd80234f6", "kolkata", "b1b2", "42b535df-7450-ee11-a81c-001dd803dccb"),
    ("486bf614-b0db-ec11-a7b4-001dd80234f6", "mumbai", "b1b2", "42b535df-7450-ee11-a81c-001dd803dccb"),
    ("4a6bf614-b0db-ec11-a7b4-001dd80234f6", "new_delhi", "b1b2", "42b535df-7450-ee11-a81c-001dd803dccb")
]

params_list_f1 = [
    ("3f6bf614-b0db-ec11-a7b4-001dd80234f6", "chennai", "f1", "79d27ad7-7258-ee11-a81c-001dd80395a5"),
    ("436bf614-b0db-ec11-a7b4-001dd80234f6", "hyderabad", "f1", "79d27ad7-7258-ee11-a81c-001dd80395a5"),
    ("466bf614-b0db-ec11-a7b4-001dd80234f6", "kolkata", "f1", "79d27ad7-7258-ee11-a81c-001dd80395a5"),
    ("486bf614-b0db-ec11-a7b4-001dd80234f6", "mumbai", "f1", "79d27ad7-7258-ee11-a81c-001dd80395a5"),
    ("4a6bf614-b0db-ec11-a7b4-001dd80234f6", "new_delhi", "f1", "79d27ad7-7258-ee11-a81c-001dd80395a5")
]


def main_process(visa_id):
    get_new_dates_dict_b1b2(visa_id)
    get_new_dict(visa_id)
    return get_date(visa_id)


def get_new_dates_dict_b1b2(visa_type):
    if visa_type == 'f1':
        for city, city_name, visa_id, primary_id in params_list_f1:
            try:
                get_free_ofc_dates(city, city_name, visa_id, primary_id)
            except Exception:
                pass
    else:
        for city, city_name, visa_id, primary_id in params_list_b1b2:
            try:
                get_free_ofc_dates(city, city_name, visa_id, primary_id)
            except Exception:
                pass

def get_new_dict(visa_id):
    id_date_data = []

    file_names = [f'tgbot/list/{visa_id}/ofc/chennai_dict.json', f'tgbot/list/{visa_id}/ofc/hyderabad_dict.json',
                  f'tgbot/list/{visa_id}/ofc/kolkata_dict.json', f'tgbot/list/{visa_id}/ofc/mumbai_dict.json',
                  f'tgbot/list/{visa_id}/ofc/new_delhi_dict.json']


    for file_name in file_names:
        with open(file_name, 'r') as file:
            data = json.load(file)
            schedule_days = data.get("ScheduleDays", [])
            name = file_name.split('/')
            # Извлекаем только первую запись (если она есть) из ScheduleDays
            if schedule_days:
                entry = schedule_days[0]
                id_date_data.append({
                    "ID": entry.get("ID"),
                    "Date": entry.get("Date"),
                    "File": name[4]
                })

    # Создаем новый файл и записываем в него данные
    output_file_name = f"tgbot/list/{visa_id}/dict_with_first.json"
    with open(output_file_name, 'w') as output_file:
        json.dump(id_date_data, output_file, indent=4)

    print(f"Первые записи из каждого файла успешно записаны в файл {output_file_name}")



def get_date(visa_id):
    import json
    from datetime import datetime

    # Чтение данных из файла
    with open(f"tgbot/list/{visa_id}/dict_with_first.json", 'r') as output_file:
        data = json.load(output_file)

    # Получение текущей даты
    current_date = datetime.now()

    # Начальные значения для поиска ближайшей даты
    closest_date = None
    closest_entry = None

    # Перебор данных и поиск ближайшей даты
    for entry in data:
        date_str = entry.get("Date")
        if date_str:
            entry_date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
            time_difference = abs((entry_date - current_date).total_seconds())

            # Если это ближайшая дата, обновляем значения
            if closest_date is None or time_difference < closest_date:
                closest_date = time_difference
                closest_entry = entry

    if closest_entry:
        print(f"Ближайшая дата к сегодняшней: ID = {closest_entry['ID']}, File = {closest_entry['File']}")
        return f"{closest_entry['ID']}={closest_entry['File']}"
    else:
        print("Нет данных или ближайшая дата не найдена.")


def which_city(file_name):
    city_mapping = {
        'chennai_dict.json': '3f6bf614-b0db-ec11-a7b4-001dd80234f6',
        'hyderabad_dict.json': '436bf614-b0db-ec11-a7b4-001dd80234f6',
        'kolkata_dict.json': '466bf614-b0db-ec11-a7b4-001dd80234f6',
        'mumbai_dict.json': '486bf614-b0db-ec11-a7b4-001dd80234f6',
        'new_delhi_dict.json': '4a6bf614-b0db-ec11-a7b4-001dd80234f6'
    }

    return city_mapping.get(file_name, None)


def accept_later_date_for_ofc(visa_id, primary_id):
    print('1')
    day_id_and_name = main_process(visa_id)
    print('2')
    day_id = day_id_and_name.split('=')[0]
    print(day_id)
    city_name = day_id_and_name.split('=')[1]
    print(city_name)
    city = which_city(city_name)
    available_hours_list = get_available_hours(city, visa_id, day_id, primary_id)
    print('3')
    first_available_date_id = get_dates(available_hours_list)
    print('4')
    post_to_ofc_date(which_city(city_name), visa_id, primary_id, day_id, first_available_date_id)


