# Занесение данных от виртуальных датчиков в файл лога 

import datetime

def logging(array, file):
    print(f'Data from sensors is logged in file {file}:')

    for i in array: print(f'<{i}>', end = ' ')

    with open(file, 'a', encoding = "utf-8") as data:
        date = datetime.datetime.today()
        data.write(f'Log at {date}: ')
        index = 1
        for info in array:
            data.write(f'Sensor{index}: {info}   ')
            index += 1
        data.write('\n')