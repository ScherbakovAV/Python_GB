from inputs import Input_text

def Print_phonebook(base): # Печать справочника

    import os
    print('-----')

    with open(base, 'r', encoding="utf-8") as file:

        if os.stat(base).st_size == 0:
            print('Справочник пуст! Для добавления контакта используйте меню.')
            return

        for line in file:
            print(line.replace('\n', '').replace('_', ' '))
    print(f'-----\n')


def Print_file(): # вывод на печать внешнего файла
    print('Внимание! Поддерживаются только файлы, созданные с помощью данной программы.')
    type_f = 1
      
    while True:
        file_name = Input_text('имя файла ("q" для отмены)').lower()

        if 'type_1' in file_name:
            type_f = 1
            break
        elif 'type_2' in file_name:
            type_f = 2
            break
        elif file_name == 'q' or file_name == 'й': return 'stop'
        else: print('Имя файла некорректно!')

    while True:
        try:
            count = 1
            
            with open(file_name, 'r', encoding="utf-8") as file:

                print(f'Содержимое файла:\n')
                
                if type_f == 1: 
                    for line in file:
                        print(line.replace('\n', ''))
                        count += 1
                    return file_name

                elif type_f == 2:
                    string = ''
                    for line in file:

                        if line == '\n':
                            print(f'{string}')
                            string = ''
                            count += 1

                        else: string += line.replace('\n', '') + ' '
                    
                    print(f'{string}')
                    return file_name
        except:
            print('Такого файла не существует!')
