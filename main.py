import telebot
import key
import menu
import func
import txt
import os

# Создаем экземпляр класса Telebot и помещаем его в переменную bot
bot = telebot.TeleBot(key.tgtoken, 'html', disable_web_page_preview=False)


# Создаем точку входа программы
if __name__ == '__main__':
    # Создаем декоратор-перехватчик для работы с командами /start, /help
    @bot.message_handler(['start', 'help'])
    def start_command(message):
        u_data = [message.from_user.id, message.message_id, message.from_user.first_name]
        if message.text == '/start':
            bot.send_message(u_data[0], txt.start.format(u_data[2]), reply_markup=menu.start())
        elif message.text == '/help':
            bot.send_message(u_data[0], txt.help, reply_markup=menu.help())

    # Обновления вопросов викторины через excel файл (только для админов)
    @bot.message_handler(content_types=['document'])
    def doc_process(message):
        u_data = [message.from_user.id, message.message_id]
        if u_data[0] in key.admin:
            try:
                file_info = bot.get_file(message.document.file_id)
                downloaded_file = bot.download_file(file_info.file_path)
                if os.path.exists('Викторина.xlsx'):
                    os.remove('Викторина.xlsx')
                file_path = os.path.join('Викторина.xlsx')
                # Сохранение файла в папку загрузки
                with open(file_path, 'wb') as new_file:
                    new_file.write(downloaded_file)
                bot.delete_message(u_data[0], u_data[1] - 1)
                bot.send_message(u_data[0], 'Викторина загружена\nОбрабатка...')
                # Загрузка данных из Excel-файла в базу данных
                success = func.question_update(file_path)
                if success:
                    bot.edit_message_text("Викторина успешна загружена!",
                                          u_data[0], u_data[1] + 1, reply_markup=menu.main())
                else:
                    bot.edit_message_text("Произошла ошибка при загрузке викторины!",
                                          u_data[0], u_data[1] + 1, reply_markup=menu.main())
            except Exception as e:
                print(f"Error handling document: {e}")
                bot.send_message(message.chat.id, "Произошла ошибка при обработке excel файла.",
                                 reply_markup=menu.main())
                bot.delete_message(u_data[0], u_data[1] - 1)
        else:
            bot.send_message(u_data[0], 'Бот не обрабатывает данный тип запроса!', reply_markup=menu.main())

    # Создаем декоратор-перехватчик для работы с текстом
    @bot.message_handler(content_types=['text'])
    def text_proc(message):
        bot.reply_to(message, 'Бот не обрабатывает данный тип запроса!', reply_markup=menu.main())

    # Создаем декоратор-перехватчик для работы с кнопками
    @bot.callback_query_handler(func=lambda call: True)
    def call_process(call):
        u_data = [call.from_user.id, call.message.message_id, call.from_user.first_name]
        if 'quiz' in call.data:
            c_data = call.data.split('_')
            if int(c_data[1]) <= int(c_data[2]):
                f_data = func.question_import(int(c_data[1]), int(c_data[2]))
                f_data['code'] = c_data[3]
                bot.edit_message_text(
                    f'<b>Вопрос №{f_data["id"]}</b>\n{f_data["question"]}',
                    u_data[0], u_data[1],
                    reply_markup=menu.quiz(f_data)
                )
            else:
                pass

        elif 'main' == call.data:
            bot.edit_message_text(txt.start.format(u_data[2]), u_data[0], u_data[1], reply_markup=menu.start())

    bot.polling(none_stop=True)
