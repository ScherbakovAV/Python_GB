import telebot

tokenID = ''

telegram1 = telebot.TeleBot(tokenID)

employee1 = []

@telegram1.message_handler(commands = ['start'])
def Show_Menu(message):
    telegram1.send_message(message.chat.id,f'Меню:\n1. Вывести все записи.\n2. Добавить запись.\n3. Найти запись.\n4. Изменить запись.\n5. Удалить запись.\n6. Вывести колонки.\n7. Выход.\n')
@telegram1.message_handler(content_types=['text'])

def Controller(message):
    t = message.text
    if t == '1':
        empl_list = print1.Veiw_all('employees.csv')
        for i in empl_list:
            telegram1.send_message(message.chat.id, i)
    if t == '2':
        telegram1.send_message(message.chat.id,'Введите ID')
        telegram1.register_next_step_handler(message,Get_ID)
        # write.New_Entry('employees.csv')
    if t == '3':
        search.Search_Entry('employees.csv')

def Get_ID(message):
    IDm = message.text
    global employee1
    employee1.append(IDm)
    telegram1.send_message(message.chat.id,'Введите фамилию')
    telegram1.register_next_step_handler(message,Get_Sirname)

def Get_Sirname(message):
    sirname = message.text
    global employee1
    employee1.append(sirname)
    write.New_Entry('employees.csv',employee1)
    employee1 = []
    Show_Menu(message)
    telegram1.register_next_step_handler(message,Controller)

telegram1.polling(non_stop=True)
