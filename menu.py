from telebot import types
from random import choices


def start():
    'Функция создания кнопок стартовому сообщению'

    # Создаем объект разметки (изменения прикрепленного интерфейса)
    markup = types.InlineKeyboardMarkup(row_width=1)

    # Создаем объекты кнопок для добавления в разметку
    btn_1 = types.InlineKeyboardButton('🕹️ Викторина', callback_data='quiz_1_0_0000')
    btn_2 = types.InlineKeyboardButton('ℹ️ О нас', url='https://doninteh.ru')

    # Добавляем кнопки в разметку и возвращаем нашу разметку чтобы прикрепить её к исходящему сообщению
    return markup.add(btn_1, btn_2)


def help():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn_1 = types.InlineKeyboardButton('🆘 Поддержка', url='https://t.me/fckdfox')
    return markup.add(btn_1)


def main():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn_1 = types.InlineKeyboardButton('⬅️ Назад', callback_data='main')
    return markup.add(btn_1)


def quiz(data: dict):
    pass