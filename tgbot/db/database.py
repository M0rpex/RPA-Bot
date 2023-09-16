import sqlite3
from tgbot.data.config import PATH_DATABASE



def db():
    conn = sqlite3.connect(PATH_DATABASE)
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS storage_users("
                "id INTEGER PRIMARY KEY,"
                "user_id INTEGER NOT NULL,"
                "user_login TEXT,"
                "user_name TEXT)")
    print("DB storage_users status GOOD | Start bot...")

    conn.commit()

    cur.close()
    conn.close()




