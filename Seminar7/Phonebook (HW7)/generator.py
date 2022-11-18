import datetime
dt = datetime.datetime.today()

base = 'phonebook.csv'

def Write_contact(BD, contact):  # запись контакта в базу данных

    with open(BD, 'a', encoding="utf-8") as data:
        data.write(f'{contact}\n')


def Del_contact(BD): # Удаление последнего контакта из справочника
    print(f'Вы уверены? Введите "y" для подтверждения и любую клавишу для отмены...')
    choise = input().lower()
    
    if choise == 'y' or choise == 'н':

        with open(BD, 'r', encoding="utf-8") as data:
            lines = data.readlines()
            lines = lines[:-1]

        with open(BD, 'w', encoding="utf-8") as data:
            data.writelines(lines)
        
        print('Удаление произведено...')
    
    return


def Base_to_file(file, export_type = 'type_1'):  # Экспорт базы данных справочника в файл

    file_name = (f'{export_type}_{dt.year}-{dt.month}-{dt.day}_{dt.hour}-{dt.minute}-{dt.second}.txt')
    contact_number = 1

    if export_type == 'type_1':
        with open(file, 'r', encoding="utf-8") as source, open(file_name, 'w', encoding="utf-8") as target:
            
            for line in source:
                export_str = line.replace('\n', '').replace(' ', '-').replace('_', ' ')
                target.write(f'{contact_number}: {export_str}\n')
                contact_number += 1

    elif export_type == 'type_2':
        with open(file, 'r', encoding="utf-8") as source, open(file_name, 'w', encoding="utf-8") as target:
            
            for line in source:
                export_lst = line.replace('\n', '').split('_')

                target.write(f'{contact_number}:\n')

                for element in export_lst:
                    target.write(element + '\n')

                target.write(f'\n')
                contact_number += 1

    print(f'Создан файл {file_name}')


def File_to_base(base_file, file_to_copy): # запись внешнего файла в базу данных
    count = 1

    with open(file_to_copy, 'r', encoding="utf-8") as file, open(base_file, 'a', encoding="utf-8") as base:

        if 'type_1' in file_to_copy: 
            for line in file:
                base.write(line.replace(f'{count}: ', '').replace(f' ', '_'))
                count += 1
                
            print('Операция выполнена успешно')
            return

        elif 'type_2' in file_to_copy:
            string = ''
            for line in file:
                if line == f'{count}:\n':
                    continue

                elif line == '\n':
                    string = string[:-1]
                    base.write(string + '\n')
                    string = ''
                    count += 1

                else: string += line.replace('\n', '') + '_'

            print('Операция выполнена успешно')
            return