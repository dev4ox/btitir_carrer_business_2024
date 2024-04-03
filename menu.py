from telebot import types
import random


CODE_REQUEST = {
    'И': 1,
    'Р': 10,
    'Э': 100,
    'О': 1000
}


def main():
    'Функция создания кнопоки назад'

    # Создаем объект разметки (изменения прикрепленного интерфейса)
    markup = types.InlineKeyboardMarkup(row_width=1)

    # Создаем объекты кнопок для добавления в разметку
    btn_1 = types.InlineKeyboardButton('⬅️ Назад', callback_data='main')

    # Добавляем кнопки в разметку и возвращаем нашу разметку чтобы прикрепить её к исходящему сообщению
    return markup.add(btn_1)


def start():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn_1 = types.InlineKeyboardButton('🕹️ Викторина', callback_data='quiz_1_1_0000')
    btn_2 = types.InlineKeyboardButton('ℹ️ О нас', url='https://doninteh.ru')
    return markup.add(btn_1, btn_2)


def help():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn_1 = types.InlineKeyboardButton('🆘 Поддержка', url='https://t.me/fckdfox')
    return markup.add(btn_1)


'''
max_quest: 12
id: 1
fac: И
question: Какой язык программирования используется для разработки веб-приложений?
answer: JavaScript;Python;Java;HTML
correct: JavaScript
code: 0000
'''
def quiz(data: dict):
    answer_list = data['answer'].split(';')
    random.shuffle(answer_list)
    print(answer_list)
    callback_list = []
    for i in answer_list:
        if i == data['correct']:
            new_code = str(int(data['code']) + CODE_REQUEST[data['fac']]).zfill(len(data['code']))
            callback_list.append(f'quiz_{int(data["id"]) + 1}_{data["max_quest"]}_{new_code}')
        else:
            callback_list.append(f'quiz_{int(data["id"]) + 1}_{data["max_quest"]}_{data["code"]}')

    print(callback_list)
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn_1 = types.InlineKeyboardButton(answer_list[0], callback_data=callback_list[0])
    btn_2 = types.InlineKeyboardButton(answer_list[1], callback_data=callback_list[1])
    btn_3 = types.InlineKeyboardButton(answer_list[2], callback_data=callback_list[2])
    btn_4 = types.InlineKeyboardButton(answer_list[3], callback_data=callback_list[3])
    btn_5 = types.InlineKeyboardButton('⬅️ Главное меню', callback_data='main')
    return markup.add(btn_1, btn_2, btn_3, btn_4, btn_5)
