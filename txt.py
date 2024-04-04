SPECIALIST_LIST = ['Информационные системы и программирование', 'Разработка электронных устройств и систем',
                   'Экономика и бухгалтерский учет (по отраслям)', 'Оператор информационных систем и ресурсов']

start = '''
{}, добро пожаловать в бота-викторину
<b>"Кто ты из Донинтеха"</b>

👇👇👇 Чтобы приступить, нажми на кнопку ниже '''

help = '''
<b>"ГБПОУ РО БТИТиР"
Батайск, 2024</b>

Чтобы вернуться в главное меню: <b>/start</b>

Если у вас возникли проблемы при работе с ботом,
свяжитесь через кнопку ниже 👇👇👇'''

specialists = (f'<b>Список направлений для обучения</b>\n'
               f'Специалисты:\n'
               f'1. <b>{SPECIALIST_LIST[0]}</b>\n'
               f'<i>09.02.07 | Основное общее | Очная | 3 года 10 месяцев</i>\n'
               f'2. <b>{SPECIALIST_LIST[1]}</b>\n'
               f'<i>11.02.17 | Основное общее | Очная | 2 года 10 месяцев</i>\n'
               f'3. <b>{SPECIALIST_LIST[2]}</b>\n'
               f'<i>38.02.01 | Основное общее | Очная | 2 года 10 месяцев</i>\n'
               f'Профессии:'
               f'1. <b>{SPECIALIST_LIST[3]}</b>\n'
               f'<i>09.01.03 | Основное общее | Очная | 1 года 10 месяцев</i>\n')


def quiz_final(result_code: str):
    if not result_code == '0000':
        result_code = [int(i) for i in result_code]
        result_index = [index for index, value in enumerate(result_code) if value == max(result_code)]
        if len(result_index) > 1:
            result_text = ''
            for i in range(len(result_index)):
                result_text = result_text + f'{i + 1}. {SPECIALIST_LIST[result_index[i]]}\n'
            return f'⭐⭐⭐ Воу воу, полегче! ⭐⭐⭐\nДля тебя есть целый список направлений:\n{result_text}'
        else:
            return (f'🤩🤩🤩 А ты хорош! 🤩🤩🤩\nРекомендую тебе направление:\n'
                    f'<b>{SPECIALIST_LIST[result_index[0]]}</b>')
    else:
        return f'Ууупс, тебе стоит попробовать ещё раз!'
