import sqlite3
from tgbot.data.config import PATH_DATABASE
from aiogram import types



################################################################################################################################
def log_user(user: types.User):   # Добавление информации о пользователях в базу данных
    conn = sqlite3.connect(PATH_DATABASE)
    cursor = conn.cursor()
    user_id = user.id
    user_login = user.username
    user_name = user.full_name
    cursor.execute('SELECT * FROM storage_users WHERE user_id = ?', (user_id,))
    data = cursor.fetchone()

    if data is None:
        # Insert user data into the database
        cursor.execute('INSERT INTO storage_users (user_id, user_login, user_name) VALUES (?, ?, ?)',
                    (user_id, user_login, user_name))
    conn.commit()
    cursor.close()
    conn.close()


################################################################################################################################
################################################################################################################################

#Удаление данных из ДБ
def remove_requisitesx(**kwargs):
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_factory
        sql = "DELETE FROM storage_requests"
        sql, parameters = update_format_args(sql, kwargs)
        con.execute(sql, parameters)
        con.commit()

#Обновление данных
def update_requisitesx(req_ran_id, **kwargs):
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_factory
        sql = f"UPDATE storage_requests SET"
        sql, parameters = update_format(sql, kwargs)
        parameters.append(req_ran_id)
        con.execute(sql + "WHERE req_ran_id = ?", parameters)
        con.commit()



# Получение пользователя
def get_userx(**kwargs):
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_factory
        sql = "SELECT * FROM storage_users"
        sql, parameters = update_format_args(sql, kwargs)
        return con.execute(sql, parameters).fetchone()
    print("get")



# Преобразование полученного списка в словарь
def dict_factory(cursor, row):
    save_dict = {}

    for idx, col in enumerate(cursor.description):
        save_dict[col[0]] = row[idx]

    return save_dict


####################################################################################################
##################################### ФОРМАТИРОВАНИЕ ЗАПРОСА #######################################
# Форматирование запроса без аргументов
def update_format(sql, parameters: dict):
    if "XXX" not in sql: sql += " XXX "

    values = ", ".join([
        f"{item} = ?" for item in parameters
    ])
    sql = sql.replace("XXX", values)

    return sql, list(parameters.values())


# Форматирование запроса с аргументами
def update_format_args(sql, parameters: dict):
    sql = f"{sql} WHERE "

    sql += " AND ".join([
        f"{item} = ?" for item in parameters
    ])

    return sql, list(parameters.values())


####################################################################################################