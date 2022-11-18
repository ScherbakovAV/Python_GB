file = 'employees.csv'


def Delete_str(file):  # удаление строки

    print(f'Введите имя сотрудника для удаления данных о нём из БД')
    name = input()
    lines = []

    with open(file, 'r', encoding="utf-8") as data:
        for line in data:
            if not name in line:
                lines += line

    with open(file, 'w', encoding="utf-8") as data:
        data.writelines(lines)

    print('Удаление произведено...')


def New_Entry():  # введение новой записи
    ID = input('Введите ID: ')
    sirname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    father_name = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    department = input('Введите отдел: ')
    position = input('Введите должность: ')
    
    with open('employees.csv', 'a', encoding='utf-8') as book:
        book.write(
            f'{ID}, {sirname}, {name}, {father_name}, {phone}, {department}, {position};\n')


def Print_all_to_console(file):  # вывод базы данных на печать
    
    with open(file, 'r') as data:
        for line in data:
            print(line.replace(',', ' ') + '\n')
        


def Edit_Entry(file): # изменение строки

    print(f'Введите ID сотрудника для изменения данных о нём в БД: ')
    ids = input()
    editing_string = ''

    with open(file, 'r', encoding="utf-8") as data:
        for line in data:
            if ids in line: editing_string = line.split(', ')
    
    print(f'Эта строка:\n{editing_string}')  

    with open(file, 'w', encoding="utf-8") as data:
            data.writelines(lines)
        
    print('Изменение произведено...')
