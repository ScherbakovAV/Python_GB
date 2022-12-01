import telebot
from log import logger, show_log

token = ''
bot = telebot.TeleBot(token)

log_file = 'Seminar10\Homework10\Calc_bot_simple\log.csv'

# ________________________________________________________________________________________

@bot.message_handler(commands = ["start", "menu"]) # вывод главного меню
def start(message, res=False):
    
    bot.send_message(message.chat.id, 'Введите математическое выражение для вычисления,\n'\
                                        'Либо введите для выбора:\n'\
                                        '/1 - калькулятор комплексных чисел\n'\
                                        '/2 - вывод истории на экран')

# ___________________________________________________________________________

# работа с комплексными числами
@bot.message_handler(commands = ["1"]) 
def coplex_nums_calc(message):
    bot.send_message(message.chat.id, f'Введите первое комплексное число в формате "a + bj" или "a - bj":')
    bot.register_next_step_handler(message, first_complex_input)

def first_complex_input(message): # ввод первого комплексного числа
    global complex_first
    try: complex_first = eval(message.text)
    except: bot.send_message(message.chat.id, f'Неверный формат')

    bot.send_message(message.chat.id, f'Введите математический оператор "*", "/", "+", "-":')
    bot.register_next_step_handler(message, math_operator)

def math_operator(message): # ввод оператора
    global oper
    oper = message.text
    if not oper in ["*", "/", "+", "-"]:
        bot.send_message(message.chat.id, f'Введён неверный математический оператор')

    bot.send_message(message.chat.id, f'Введите второе комплексное число в формате "a + bj" или "a - bj":')
    bot.register_next_step_handler(message, second_complex_input_and_solve)

def second_complex_input_and_solve(message): # ввод второго комплексного числа, расчёт и вывод результата
    try: complex_second = eval(message.text)
    except: bot.send_message(message.chat.id, f'Неверный формат')
    
    result_complex = eval(f'{complex_first}{oper}{complex_second}')

    logger(f'{complex_first} {oper} {complex_second} = {result_complex}', log_file)
    bot.send_message(message.chat.id, f'{complex_first} {oper} {complex_second} = {result_complex}')

# ___________________________________________________________________________

@bot.message_handler(commands = ["2"]) 
def coplex_nums_calc(message):
    log_text = show_log(log_file)
    bot.send_message(message.chat.id, log_text)

# ________________________________________________________________________________________

@bot.message_handler(func=lambda message: True, content_types = ['text'])
def get_text_messages(message):

    math_formula = message.text.replace(' ', '')
    print(math_formula)

    try:
        math_formula_str = str(eval(math_formula))
        print(math_formula_str)
        result_real = f'{math_formula} = {math_formula_str}'
        print(result_real)
        logger(result_real, log_file)
        bot.send_message(message.chat.id, result_real)         
    except:
        logger(f'ошибка ввода', log_file)
        bot.send_message(message.chat.id, 'Ошибка! Повторите ввод...')

print('Сервер запущен...')
bot.polling(none_stop = True, interval = 0)