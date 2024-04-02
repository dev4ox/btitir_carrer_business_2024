import sqlite3
db_name = 'db.sqlite'


def create():
    conn = sqlite3.connect(db_name)
    try:
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS quiz (
                        id INTEGER PRIMARY KEY,
                        fac INTEGER,
                        question TEXT,
                        answer TEXT,
                        correct TEXT
                        )''')
        conn.commit()
        return True
    except Exception as e:
        print('Не удалось создать таблицу', e)
        return False
    finally:
        conn.close()


if create():
    print(f'Таблица "{db_name}" успешно создана!')

