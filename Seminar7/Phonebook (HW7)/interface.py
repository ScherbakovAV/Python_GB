from view import Print_phonebook
from generator import Write_contact
from inputs import Input_contact
from generator import Del_contact
from view import Print_file
from generator import Base_to_file
from generator import File_to_base

base = 'phonebook.csv'


def Greetings():
    print('Добро пожаловать!')
    Mode_selection(base)

def Mode_selection(database): # выбор режима работы
    print(f'Выберите действие со справочником...\n'\
            '1: вывод справочника на экран\n'\
            '2: добавление контакта в справочник\n'\
            '3: удаление последнего контакта из справочника\n'\
            '4: открытие файла справочника пользователя\n'\
            '5: экспорт справочника в файл пользователя\n'\
            'enter: выход из программы')
    modes = input()
    match modes:
        case '1':
            Print_phonebook(database)
            return 1
        case '2':
            Write_contact(database, Input_contact())
            return 2
        case '3':
            Del_contact(database)
            return 3
        case '4':
            name_export = Print_file()
            do_copy = Is_copy_file()
            if do_copy: File_to_base(database, name_export)
            return 4
        case '5':
            Base_to_file(database, Export_type())
            return 5
        case _:
            exit


def Button(): # действие после завершения функции
    print(f'Выберите дальнейшее действие...\n'\
            '1: переход в основное меню\n'\
            'enter: выход из программы')
    modes = input()
    match modes:
        case '1':
            Mode_selection()
            return
        case _:
            exit

def Export_type(): # выбор типа экспорта базы в внешний файл
    print(f'Выберите тип экспорта...\n'\
            '1: каждый контакт одной строкой\n'\
            '2: запись данных контактов построчно\n'\
            'enter: отмена и переход в основное меню')
    modes = input()
    match modes:
        case '1': return 'type_1'
        case '2': return 'type_2'
        case _: Mode_selection()


def Is_copy_file(): # выбор копирования файла в БД
    print(f'Скопировать содержимое файла в базу данных?\n'\
            '"y": да, enter: переход в основное меню')

    choice = input().lower()

    if choice == 'y' or choice == 'н': return True
    else: Mode_selection()
