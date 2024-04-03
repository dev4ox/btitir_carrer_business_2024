import sqlite3
import openpyxl
import key


# Обновление бд с вопросами из excel файла
def question_update(excel_file:str) -> bool:
    conn = sqlite3.connect(key.db)
    wb = openpyxl.load_workbook(excel_file)
    try:
        cur = conn.cursor()
        cur.execute('DELETE FROM quiz')
        conn.commit()
        sheet = wb.worksheets[0]
        for row in sheet.iter_rows(2, values_only=True):
            fac, question, answer, correct = row
            cur.execute('INSERT INTO quiz (fac, question, answer, correct) VALUES (?, ?, ?, ?)',
                        (fac, question, answer, correct))
        conn.commit()
        return True
    except Exception as e:
        return False
    finally:
        conn.close()
        wb.close()


# Импорт вопроса из БД
def question_import(n_quest: int, max_quest: int) -> dict:
    result = dict()
    conn = sqlite3.connect(key.db)
    try:
        cur = conn.cursor()
        if max_quest <= 1:
            cur.execute(f"SELECT COUNT(*) FROM quiz")
            result['max_quest'] = cur.fetchone()[0]
        else:
            result['max_quest'] = max_quest
        cur.execute('SELECT * FROM quiz WHERE id = ?', (n_quest,))
        data = cur.fetchone()
        result['id'] = data[0]
        result['fac'] = data[1]
        result['question'] = data[2]
        result['answer'] = data[3]
        result['correct'] = data[4]

        return result
    except Exception as e:
        print(e)
    finally:
        conn.close()
