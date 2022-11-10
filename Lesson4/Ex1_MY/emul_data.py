# Эмуляция получения данных путём перезаписи в файл случайных дробных данных (виртуальных сенсоров в количестве 5 шт)

import random

def emul_sensors(file):
    with open(file, 'w', encoding = "utf-8") as data:
        for sensor_data in range(5):
            sensor_data = round((random.randint(0, 99) + random.random()), 2)
            data.write(f'{sensor_data}\n')