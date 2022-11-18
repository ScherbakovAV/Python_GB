def Greetings():
    print('Добро пожаловать!')


def Button(): # действие после завершения функции
    print(f'Выберите дальнейшее действие...\n'\
            '1: переход в основное меню\n'\
            'enter: выход из программы')
    modes = input()
    match modes:
        case '1': return True


def Export_type(): # выбор типа экспорта базы в внешний файл
    print(f'Выберите тип экспорта...\n'\
            '1: каждый контакт одной строкой\n'\
            '2: запись данных контактов построчно\n'\
            'enter: отмена и переход в основное меню')
    modes = input()
    
    match modes:
        case '1': return 'type_1'
        case '2': return 'type_2'
    
    return


def Is_copy_file(): # выбор копирования файла в БД
    print(f'Скопировать содержимое файла в базу данных?\n'\
            '"y": да, enter: отмена')

    choice = input().lower()

    if choice == 'y' or choice == 'н': return True

    return
