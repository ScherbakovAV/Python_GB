def Input_text(what_entering):
    print(f'Введите {what_entering}: ')
    while True:
        text = input()
        if text != '': return text
        else: print('Вы ввели пустую строку. Повторите ввод:')


def Input_contact(): # добавление введённого контакта в базу данных
    print(f'Режим добавления контакта в справочник...')
    last_name = Input_text('фамилию')
    first_name = Input_text('имя')
    phone = Input_text('номер телефона')
    info = input(f'Введите описание (не обязательно):\n')

    if info != '': return f'{last_name}_{first_name}:_т.{phone}_({info})'
    else: return f'{last_name}_{first_name}:_т.{phone}'