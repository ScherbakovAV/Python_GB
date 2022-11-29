import telebot
from enter import format_complex

# sys.exit() - функция завершения

token = ''
bot = telebot.TeleBot(token)
base = 'D:\Geek Brains\Python_education\Seminar10\Homework10\log.csv'


# ________________________________________________________________________________________

@bot.message_handler(commands = ["start"]) # вывод главного меню
def menu(message):
    bot.send_message(message.chat.id, 'Вас приветствует мини калькулятор.')
    
    bot.send_message(message.chat.id, 'Он поддерживает следующие операции с действительными числами\n'\
                                        'и комплексными числами (в арифметической форме):\n'\
                                        '- сложение\n'\
                                        '- вычитание\n'\
                                        '- умножение\n'\
                                        '- деление\n'\
                                        '- возведение в степень')

    bot.send_message(message.chat.id, 'Выберите режим работы:\n'\
                                        '/1 - калькулятор действительных чисел\n'\
                                        '/2 - калькулятор комплексных чисел\n'\
                                        'Для вызова справки введите /h')

# ________________________________________________________________________________________

@bot.message_handler(commands = ["h"]) # вызов справки
def help_menu(message):
    bot.send_message(message.chat.id, f'ЗАГЛУШКА 1!')
    bot.register_next_step_handler(message, help_all)

def help_all(message):
    if message.text == '1': return 'ЗАГЛУШКА 2!'

# ________________________________________________________________________________________

@bot.message_handler(commands = ["1"]) # работа с действительными числами
def real_nums_calc(message):
    bot.send_message(message.chat.id, f'ЗАГЛУШКА 1!')
    bot.register_next_step_handler(message, help_all)

# ___________________________________________________________________________




# ___________________________________________________________________________


@bot.message_handler(commands = ["2"]) # добавление записи в БД
def add_to_db(message):
    bot.send_message(message.chat.id, f'Режим добавления новой записи в БД...\nВведите ID студента: ')
    bot.register_next_step_handler(message, enter_student_id)

def enter_student_id(message):
    global s_id
    s_id = message.text

    if search.search_from_id(base, s_id):
        bot.send_message(message.chat.id, f'В базе данных уже есть запись с таким id...')
        return
    else:
        bot.send_message(message.chat.id, f'Введите фамилию: ')  
        bot.register_next_step_handler(message, enter_sirname)
        return s_id

def enter_sirname(message):
    bot.send_message(message.chat.id, f'Введите имя: ')  
    bot.register_next_step_handler(message, enter_name)
    global s_sname
    s_sname = message.text
    return s_sname

def enter_name(message):
    bot.send_message(message.chat.id, f'Введите отчество: ')  
    bot.register_next_step_handler(message, enter_father_name)
    global s_name
    s_name = message.text
    return s_name

def enter_father_name(message):
    bot.send_message(message.chat.id, f'Введите номер телефона: ')  
    bot.register_next_step_handler(message, enter_phone)
    global s_fname
    s_fname = message.text
    return s_fname

def enter_phone(message):
    bot.send_message(message.chat.id, f'Введите специализацию: ')  
    bot.register_next_step_handler(message, enter_spec)
    global s_phone
    s_phone = message.text
    return s_phone

def enter_spec(message):
    bot.send_message(message.chat.id, f'Введите город проживания: ')  
    bot.register_next_step_handler(message, enter_city_and_add_student)
    global s_spec
    s_spec = message.text
    return s_spec
    
def enter_city_and_add_student(message):
    s_city = message.text
    add.new_entry(base, s_id, s_sname, s_name,s_fname, s_phone, s_spec, s_city)
    bot.send_message(message.chat.id, f'Запись успешно добавлена') 


# ___________________________________________________________________________

# поиск и вывод записей БД
@bot.message_handler(commands = ["3"])
def finder_message(message):
    bot.send_message(message.chat.id, f'Введите информацию для поиска:')
    bot.register_next_step_handler(message, finder_and_print)

def finder_and_print(message):
    found = search.search_all_entry(base, message.text)
    if found == False: bot.send_message(message.chat.id, f'Записей в БД, содержащих "{message.text}", нет')
    else: bot.send_message(message.chat.id, f'Записи базы данных, сожержащие "{message.text}":\n\n{found}')


# ___________________________________________________________________________

# изменение записи
@bot.message_handler(commands = ["4"])
def edit_message(message):
    bot.send_message(message.chat.id, f'Введите ID сотрудника для изменения данных о нём в БД:')
    bot.register_next_step_handler(message, is_edit_entry)

def is_edit_entry(message):
    global id_edit
    id_edit = str(message.text)
    string = search.search_from_id(base, id_edit)
    if not string: bot.send_message(message.chat.id, f'Записи в БД с ID {id_edit} нет')
    else:
        bot.send_message(message.chat.id, f'Запись в БД с ID {id_edit}:\n{string}\nВведите номер элемента для замены:')
        bot.register_next_step_handler(message, enter_element_num)

def enter_element_num(message):
    global element_num
    element_num = message.text

    try: int(element_num)
    except:
        bot.send_message(message.chat.id, f'Ошибка ввода! Нужно вводить цифры!')
        return

    if int(element_num) == 1:
        bot.send_message(message.chat.id, f'Заменить id студента нельзя!\nПри необходимости изменения id удалите запись и добавьте заново.')
        return
    
    if int(element_num) > 7:
        bot.send_message(message.chat.id, f'Номер элемента не может быть больше количества элементов!')
        return

    bot.send_message(message.chat.id, f'Введите, на что заменить:')
    bot.register_next_step_handler(message, edit_entry)

def edit_entry(message):
    replacement = message.text
    editting.edit_entry(base, id_edit, element_num, replacement)
    bot.send_message(message.chat.id, f'Изменение данных произведено')


# ___________________________________________________________________________

# удаление записи из БД
@bot.message_handler(commands = ["5"])
def del_from_bd(message):
    bot.send_message(message.chat.id, f'Введите ID студента для удаления данных о нём из БД:')
    bot.register_next_step_handler(message, search_student_id)
    

def search_student_id(user_id): # ввод и поиск id
    global id
    id = user_id.text
    
    string = search.search_from_id(base, id)

    if not string: bot.send_message(user_id.chat.id, f'Записи в БД с ID {id} нет')
    else:
        bot.send_message(user_id.chat.id, f'Запись в БД с ID {id}:\n{string}\nПродолжить удаление? ("Y" - да)')
        bot.register_next_step_handler(user_id, del_user)


def del_user(confirm): # удаление записи пользователя
    global id
    
    if confirm.text == 'y' or confirm.text == 'Y':
        delete.delete_str(base, id)
        bot.send_message(confirm.chat.id, f'Удаление записи студента с ID {id} произведено')
    
    else: bot.send_message(confirm.chat.id, f'Отмена процедуры удаления...')


# ___________________________________________________________________________

# Сортировка БД
@bot.message_handler(commands = ["6"])
def start_sort(message):
    bot.send_message(message.chat.id, f'Введите номер поля данных студента, по которому будет осуществляться сортировка БД:\n'\
                                        '1 - id\n'\
                                        '2 - фамилия\n'\
                                        '3 - имя\n'\
                                        '4 - отчество\n'\
                                        '5 - номер телефона\n'\
                                        '6 - специализация\n'\
                                        '7 - город проживания\n')
    bot.register_next_step_handler(message, enter_sort_by)
    

def enter_sort_by(message):
    global sort_by

    try: sort_by = int(message.text) - 1
    except:
        bot.send_message(message.chat.id, f'Ошибка ввода! Необходимо ввести число, отмена ввода.')
        return

    if sort_by < 0 or sort_by > 6: bot.send_message(message.chat.id, f'Такого поля нет! Отмена ввода.')
    else:
        sorting.write_base_from_list(base, sorting.sort_file_to_list(base, sort_by))
        bot.send_message(message.chat.id, f'Сортировка завершена. Для вывода результата введите "/1"')


# ___________________________________________________________________________


print('Сервер запущен...')
bot.polling(none_stop = True, interval = 0) """