import json

from datetime import datetime

def show_json(city):
    with open(f'tgbot/list/{city}_dict.json', 'r') as file:
        data = json.load(file)

    # Извлекаем список объектов ScheduleDays из данных
    schedule_days = data.get('ScheduleDays', [])

    # Проходимся по объектам ScheduleDays и выводим информацию
    for day in schedule_days:
        date_str = day.get('Date', '')
        date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
        full_date = date.strftime("%d-%m-%Y")
        print(full_date)
        file_path = f"tgbot/dates/{city}_date.txt"
        with open(file_path, "w") as file:
            for date1 in schedule_days:
                dn = date1.get('Date', '')
                date = datetime.strptime(dn, "%Y-%m-%dT%H:%M:%S")
                full_date = date.strftime("%d-%m-%Y")
                file.write(full_date + "\n")


#### Отслеживание изменений в словаре с использованием ID и Date

def dont_touch():

    saved_dict_path = 'saved_dict.json'
    new_dict_path = 'new_dict.json'

    # Загрузка сохраненного словаря из файла
    with open(saved_dict_path, 'r') as saved_file:
        saved_dict = json.load(saved_file)

    # Загрузка нового словаря из файла
    with open(new_dict_path, 'r') as new_file:
        new_dict = json.load(new_file)

    # Проверяем, одинаковы ли словари
    if saved_dict == new_dict:
        print("Словари идентичны, ничего не делать")
    else:
        # Проверяем наличие ключей 'ScheduleDays' в обоих словарях
        if 'ScheduleDays' in new_dict and 'ScheduleDays' in saved_dict:
            saved_schedule_days = saved_dict['ScheduleDays']
            new_schedule_days = new_dict['ScheduleDays']

            # Проверяем, что saved_schedule_days и new_schedule_days являются списками
            if isinstance(saved_schedule_days, list) and isinstance(new_schedule_days, list):
                # Извлекаем только уникальные записи из нового списка, которых нет в старом списке
                unique_new_entries = [entry for entry in new_schedule_days if entry not in saved_schedule_days]

                if unique_new_entries:
                    print("Найдены новые записи:")
                    for entry in unique_new_entries:
                        print(f"ID: {entry['ID']}, Date: {entry['Date']}")
                else:
                    print("Новых записей не найдено.")
            else:
                print("ScheduleDays не является списком в одном из словарей")
        else:
            print("Отсутствует ключ 'ScheduleDays' в одном из словарей")