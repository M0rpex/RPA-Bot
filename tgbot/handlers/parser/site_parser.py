import time

import requests
import json
import os
import asyncio

from tgbot.dict import b1, f1


session = requests.Session()

headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}


def update_session():
    url1 = 'https://www.usvisascheduling.com/en-US/custom-actions/?route=/api/v1/navigation/link&cacheString=1698264810127&parameters={%22applicationId%22:%2242b535df-7450-ee11-a81c-001dd803dccb%22}'
    url2 = 'https://www.usvisascheduling.com/en-US/custom-actions/?route=/api/v1/navigation/link&cacheString=1698267142890&parameters={%22applicationId%22:%2279d27ad7-7258-ee11-a81c-001dd80395a5%22}'
    data1 = {
        "parameters": '{"applicationId":"42b535df-7450-ee11-a81c-001dd803dccb"}'
    }
    data2 = {
        "parameters": '{"applicationId":"79d27ad7-7258-ee11-a81c-001dd80395a5"}'
    }
    cookie1 = {
        'Cookie': f'{b1}'
    }
    cookie2 = {
        'Cookie': f'{f1}'
    }

    responce1 = session.get(url=url1, data=data1, headers=headers, cookies=cookie1).text
    responce2 = session.get(url=url2, data=data2, headers=headers, cookies=cookie2).text
    print(responce1)
    print(responce2)


async def session_update_scheduler():
    while True:

        update_session()

        await asyncio.sleep(60)


def choose_visa(visa_id):
    if visa_id == 'f1':
        cookie = {
            'Cookie': f'{f1}'
        }
    else:
        cookie = {
            'Cookie': f'{b1}'
        }

    return cookie


def get_free_cons_date(city_cons, city_name, visa_id, primary_id):
    url = 'https://www.usvisascheduling.com/en-US/custom-actions/?route=/api/v1/schedule-group/get-family-consular-schedule-days&cacheString=1695381667916'
    
    data = {
        "parameters": '{{"primaryId":"{}","applications":["{}"],"scheduleDayId":"","scheduleEntryId":"","postId":"{}","isReschedule":"False"}}'.format(
            primary_id, primary_id, city_cons
        )
    }

    cookie = choose_visa(visa_id)

    response = session.post(url=url, data=data, headers=headers, cookies=cookie).text

    file_path = f"tgbot/list/{visa_id}/cons/{city_name}_dict.json"
    with open(file_path, "w") as json_file:
        json.dump(json.loads(response), json_file, indent=4, ensure_ascii=False)


def get_free_ofc_dates(city, city_name, visa_id, primary_id):
    url = 'https://www.usvisascheduling.com/en-US/custom-actions/?route=/api/v1/schedule-group/get-family-ofc-schedule-days&cacheString=1694637530696'
    data = {
        "parameters": '{{"primaryId":"{}","applications":["{}"],"scheduleDayId":"","scheduleEntryId":"","postId":"{}"}}'.format(
            primary_id, primary_id, city)
    }

    cookie = choose_visa(visa_id)

    response = session.post(url=url, data=data, headers=headers, cookies=cookie)
    save = response.text
    print(city_name)
    file_path = f"tgbot/list/{visa_id}/ofc/{city_name}_dict.json"
    #json.load(response.json())


    print('GET')
    with open(file_path, "w") as json_file:
        json.dump(json.loads(save), json_file, indent=4, ensure_ascii=False)








def get_available_hours(city, visa_id, day_id, primary_id):
    url = 'https://www.usvisascheduling.com/en-US/custom-actions/?route=/api/v1/schedule-group/get-family-ofc-schedule-entries&cacheString=1697379211159'


    data = {
        "parameters": f'{{"primaryId":"{primary_id}","applications":["{primary_id}"],"scheduleDayId":"{day_id}","scheduleEntryId":"","postId":"{city}"}}'
    }

    cookies = choose_visa(visa_id)

    response = session.post(url=url, data=data, headers=headers, cookies=cookies).json()
    return response


def get_dates(data):
    schedule_entries = data.get('ScheduleEntries', [])

    if schedule_entries:
        first_entry = schedule_entries[0]
        first_id = first_entry.get('ID')

        if first_id:
            return first_id
        else:
            print('ID в первой записи отсутствует')
    else:
        print('Список ScheduleEntries пуст')


def post_to_ofc_date(city, visa_id, primary_id, day_id, entry_day_id):
    url = 'https://www.usvisascheduling.com/en-US/custom-actions/?route=/api/v1/schedule-group/schedule-ofc-appointments-for-family&cacheString=1695812975989'


    data = {
        "parameters": f'{{"primaryId":"{primary_id}","applications":["{primary_id}"],"scheduleDayId":"{day_id}","scheduleEntryId":"{entry_day_id}","postId":"{city}"}}'
    }

    cookies = choose_visa(visa_id)

    response = session.post(url=url, data=data, headers=headers, cookies=cookies).text
    print(data)
    print(response)





