import sqlite3
from tgbot.data.config import PATH_DATABASE



def db():
    conn = sqlite3.connect(PATH_DATABASE)
    cur = conn.cursor()

    if len(cur.execute("PRAGMA table_info(storage_users)").fetchall()) == 4:
        print("DB storage_users was found | (1/2)")
    else:
        cur.execute("CREATE TABLE IF NOT EXISTS storage_users("
                    "id INTEGER PRIMARY KEY,"
                    "user_id INTEGER NOT NULL,"
                    "user_login TEXT,"
                    "user_name TEXT)")
        print("DB storage_users was not found | (1/2) | Creating...")

    if len(cur.execute("PRAGMA table_info(settings_bot)").fetchall()) == 1:
        print("DB settings_bot was found | (2/2)")
    else:
        cur.execute("CREATE TABLE IF NOT EXISTS settings_bot("
                    "request INTEGER)")
        print("DB settings_bot was not found | (2/2) | Creating...")

    conn.commit()

    cur.close()
    conn.close()




