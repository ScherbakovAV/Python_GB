from inputs import Input_text
from interface import Mode_selection

def Print_phonebook(base): # Печать справочника
    with open(base, 'r', encoding="utf-8") as file:
        for line in file:
            print(line.replace('\n', ''))


def Print_file(): # вывод на печать внешнего файла
    print('Внимание! Поддерживаются только файлы, созданные с помощью данной программы.')
    type_f = 1
      
    while True:
        file_name = Input_text('имя файла ("q" для выхода в основное меню)')

        if 'type_1' in file_name:
            type_f = 1
            break
        elif 'type_2' in file_name:
            type_f = 2
            break
        elif file_name == 'q' or file_name == 'Q' or file_name == 'й' or file_name == 'Й':
            Mode_selection()
            return
        else:
            print('Имя файла некорректно!')

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
