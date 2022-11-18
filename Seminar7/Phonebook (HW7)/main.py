import interface
import view
import inputs
import generator

base = 'phonebook.csv'

def Mode_selection(database):

    while True:
        print(f'Выберите действие со справочником...\n'\
                '1: вывод справочника на экран\n'\
                '2: добавление контакта в справочник\n'\
                '3: удаление последнего контакта из справочника\n'\
                '4: открытие и импорт файла справочника пользователя\n'\
                '5: экспорт справочника в файл пользователя\n'\
                'enter: выход из программы')
            
        modes = input()

        match modes:

            case '1':
                view.Print_phonebook(database)
                if not interface.Button(): return False

            case '2':
                generator.Write_contact(database, inputs.Input_contact())
                if not interface.Button(): return False

            case '3':
                generator.Del_contact(database)
                if not interface.Button(): return False

            case '4':
                name_export = view.Print_file()

                if name_export != 'stop':
                    do_copy = interface.Is_copy_file()
                    if do_copy: generator.File_to_base(database, name_export)
                    
                if not interface.Button(): return False

            case '5':
                generator.Base_to_file(database, interface.Export_type())
                if not interface.Button(): return False
            
            case _: return
    

interface.Greetings()

Mode_selection(base)