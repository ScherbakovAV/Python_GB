import telebot
from formatting import format_complex, complex_to_string, format_real
from solve import real_solve, complex_solve
from log import logger, show_log

token = ''
bot = telebot.TeleBot(token)
base = 'D:\Geek Brains\Python_education\Seminar10\Homework10\log.csv'

log_file = 'Seminar10\Homework10\Calc_bot_my_functions\log.csv'

# ________________________________________________________________________________________

@bot.message_handler(commands = ["start", "menu"]) # вывод главного меню
def menu(message):
    
    bot.send_message(message.chat.id, f'{message.chat.first_name}, Вас приветствует мини калькулятор.')

    bot.send_message(message.chat.id, 'Выберите режим работы:\n'\
                                        '/1 - калькулятор действительных чисел\n'\
                                        '/2 - калькулятор комплексных чисел\n'\
                                        '/3 - вывод истории на экран\n'\
                                        '/help для вызова справки.')

# ________________________________________________________________________________________

@bot.message_handler(commands=["help"])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()  
    keyboard.add(telebot.types.InlineKeyboardButton('Написать разработчику', url='telegram.me/AnatolySc'))  
    bot.send_message(message.chat.id,'Калькулятор выполняет следующие операции с логированием:\n'\
        '   - сложение, вычитание, умножение, деление.\n\n'\
        'Поддерживается три режима:\n'\
        '1) работа с действительными числами:\n'\
        'для вычисления выражения введите его в формате:\n'\
        '"a + b * c / d - e...",\n'\
        'используя только математические операторы "*", "/", "+", "-".\n\n'\
        '2) работа с комплексными числами (в арифметической форме):\n'\
        'Поддерживается произведение, деление, сложение и вычитание'\
        'двух комплексных чисел в формате "a + bi" или "a - bi", '\
        'где "a" и "b" - натуральные числа.\n'\
        'Для вычисления введите первое комплексное число, нажмите "enter",'\
        'затем введите один математический оператор "*", "/", "+", "-", нажмите "enter",'\
        'далее введите второе комплексное число и нажмите "enter".\n\n'\
        '3) Вывод истории (лога) на экран.\n\n'\
        'Если у Вас остались вопросы или предложения, можете написать свой вопрос по кнопке ниже.'\
        , reply_markup = keyboard)

# ________________________________________________________________________________________

# работа с действительными числами
@bot.message_handler(commands = ["1"]) 
def real_nums_calc(message):
    bot.send_message(message.chat.id, f'Введите математическое выражение')
    bot.register_next_step_handler(message, solve_real)

def solve_real(message):
    math_formula = format_real(message.text)
    result_real = real_solve(math_formula)
    if result_real == None:
        bot.send_message(message.chat.id, f'Деление на 0')
        logger(f'{message.text} - деление на 0', log_file)
    else: 
        logger(f'{message.text} = {result_real}', log_file)
        bot.send_message(message.chat.id, f'{message.text} = {result_real}')

# ___________________________________________________________________________

# работа с комплексными числами
@bot.message_handler(commands = ["2"]) 
def coplex_nums_calc(message):
    bot.send_message(message.chat.id, f'Введите первое комплексное число в формате "a + bi" или "a - bi":')
    bot.register_next_step_handler(message, first_complex_input)

def first_complex_input(message): # ввод первого комплексного числа
    global complex_first
    complex_first = message.text
    global f_complex_first
    f_complex_first = format_complex(complex_first)
    bot.send_message(message.chat.id, f'Введите математический оператор "*", "/", "+", "-":')
    bot.register_next_step_handler(message, math_operator)
    return f_complex_first

def math_operator(message): # ввод оператора
    global oper
    oper = message.text
    bot.send_message(message.chat.id, f'Введите второе комплексное число в формате "a + bi" или "a - bi":')
    bot.register_next_step_handler(message, second_complex_input_and_solve)

def second_complex_input_and_solve(message): # ввод второго комплексного числа, расчёт и вывод результата
    complex_second = message.text
    f_complex_second = format_complex(complex_second)
    result_complex_list = complex_solve(f_complex_first, f_complex_second, oper)
    if result_complex_list == None:
        bot.send_message(message.chat.id, f'Деление на 0')
        logger(f'{message.text} - деление на 0', log_file)
    else:
        result_complex = complex_to_string(result_complex_list)
        logger(f'({complex_first}) {oper} ({complex_second}) = {result_complex}', log_file)
        bot.send_message(message.chat.id, f'{complex_first} {oper} {complex_second} = {result_complex}')

# ___________________________________________________________________________

@bot.message_handler(commands = ["3"]) 
def coplex_nums_calc(message):
    log_text = show_log(log_file)
    bot.send_message(message.chat.id, log_text)
    
# ___________________________________________________________________________

print('Сервер запущен...')
bot.polling(none_stop = True, interval = 0)