import math

def Enter_int(text): # функция ввода целого числа с проверкой 
    print(text)
    while True:
        try:
            value = int(input())
            break
        except:
            print("Ошибка! Введите целое число:")
    return value 

def Enter_float(text): # функция ввода дробного числа с проверкой
    print(text)
    while True:
        try:
            value = float(input())
            break
        except:
            print("Ошибка! Введите число:")
    return value 

def Holiday_checker(month, day): # функция, проверяющая, выходной ли день в месяце
    months_names = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    if month == 1:
        holidays = [1, 2, 3, 4, 5, 6, 7, 8, 13, 14, 20, 21, 27, 28]
        max_days = 31
    elif month == 2:
        holidays = [3, 4, 10, 11, 17, 18, 23, 24, 25]
        max_days = 28
    elif month == 3:
        holidays = [3, 4, 8, 10, 11, 17, 18, 24, 25, 31]
        max_days = 31
    elif month == 4:
        holidays = [1, 7, 8, 14, 15, 21, 22, 28, 29]
        max_days = 30
    elif month == 5:
        holidays = [1, 5, 6, 9, 12, 13, 19, 20, 26, 27]
        max_days = 31
    elif month == 6:
        holidays = [2, 3, 9, 10, 12, 16, 17, 23, 24, 30]
        max_days = 30
    elif month == 7:
        holidays = [1, 7, 8, 14, 15, 21, 22, 28, 29]
        max_days = 31
    elif month == 8:
        holidays = [4, 5, 11, 12, 18, 19, 25, 26]
        max_days = 31
    elif month == 9:
        holidays = [1, 2, 8, 9, 15, 16, 22, 23, 29, 30]
        max_days = 30
    elif month == 10:
        holidays = [6, 7, 13, 14, 20, 21, 27, 28]
        max_days = 31
    elif month == 11:
        holidays = [3, 4, 10, 11, 17, 18, 24, 25]
        max_days = 30
    elif month == 12:
        holidays = [1, 2, 8, 9, 15, 16, 22, 23, 29, 30]
        max_days = 31
    else:
        print('Такого месяца не существует!')
        return None
    checker = 0
    for i in holidays:
        if day == i: checker += 1
    if checker != 0: print(f'{day} {months_names[month - 1]} - выходной день')
    elif 1 <= day_num <= max_days: print(f'{day} {months_names[month - 1]} - рабочий день')
    else: print('Такого дня в этом месяце нет!')
    
# 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print(f'\n___1. Определение, является ли вводимый день недели выходным___\n')

number_of_day = Enter_int('Введите цифру дня недели:')
days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
if 1 <= number_of_day <= 5:
    print(f'Этот день - {days[number_of_day - 1]}, и это рабочий день')
elif number_of_day == 6 or number_of_day == 7:
    print(f'Этот день - {days[number_of_day - 1]}, и это выходной день')
else:
    print('Такого дня недели нет!')

# 1*. Напишите программу, которая принимает на вход 2 числа:
# номер месяца и номер дня в месяце, проверяет является ли день выходным.
# Принимаем начало года на понедельник и считая год не високосным.
# Учитываем только гос праздники (НГ, 9 мая и т.д.)

print(f'\n___1*. Определение по вводимым номеру месяца и номеру дня, является ли этот день выходным___\n')

month_num = Enter_int('Введите номер месяца:')
day_num = Enter_int('Введите номер дня в этом месяце:')

Holiday_checker(month_num, day_num)

# 1*. Решение Наташи

""" num_day = int(input("Цифра, обозначающая номер дня в месяце:  "))
num_month = int(input("Цифра, обозначающая месяц (1-12):  "))
day = num_day
for i in range(1, num_month):
    if i == 4 or i == 6 or i == 9 or i == 11:
        day += 30
    elif i == 2:
        day += 28
    else:
        day += 31
day_status = "working day"
for i in range(6,365,7):
    if i==day:
        day_status = "weekend"
for i in range(7,365,7):
    if i==day:
        day_status = "weekend"

if (num_day == 23 and num_month == 2) or (num_day == 8 and num_month == 3) or (
            num_day == 1 or num_day == 9 and num_month == 5) or (num_day == 12 and num_month == 6) or (
            num_day >= 1 and num_day <= 8 and num_month == 1):
    day_status = "public holidays"

print(day_status) """

# 2. Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print(f'\n___2. Определение истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z___\n')

for i in range(2):
    for j in range(2):
        for k in range(2):
            X = i; Y = j; Z = k
            print(f'Для X={X}, Y={Y}, Z={Z} выражение {not(X or Y or Z) == ((not X) and (not Y) and (not Z))}')

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой
# находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print(f'\n___2. Определение координатной плоскости по вводимым координатам___\n')

x = Enter_float('Введите координату точки по оси X:')
y = Enter_float('Введите координату точки по оси Y:')

if x != 0 and y != 0:
    if x > 0 and y > 0: print('Эта точка находится в 1 четверти координатной плоскости')
    elif x < 0 and y > 0: print('Эта точка находится во 2 четверти координатной плоскости')
    elif x < 0 and y < 0: print('Эта точка находится в 3 четверти координатной плоскости')
    else: print('Эта точка находится в 4 четверти координатной плоскости')
else:
    if x == 0 and y != 0: print('Эта точка находится на координатной оси Y')
    elif x != 0 and y == 0: print('Эта точка находится на координатной оси X')
    else: print("Точка находится в начале координат")

# 4. Напишите программу, которая по заданному номеру четверти
# показывает диапазон возможных координат точек в этой четверти (x и y).

print(f'\n___4. Вывод диапазона координат точек по вводимой четверти___\n')

number_of_quarter = Enter_int('Введите номер четверти:')

if number_of_quarter == 1: print(f'В {number_of_quarter} четверти возможный диапазон координат точек:\nX>0, Y>0')
elif number_of_quarter == 2: print(f'В {number_of_quarter} четверти возможный диапазон координат точек:\nX<0, Y>0')
elif number_of_quarter == 3: print(f'В {number_of_quarter} четверти возможный диапазон координат точек:\nX<0, Y<0')
elif number_of_quarter == 4: print(f'В {number_of_quarter} четверти возможный диапазон координат точек:\nX>0, Y<0')
else: print('Такой координатной четверти нет!')

# 5. Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print(f'\n___5. Определение расстояния между двумя точками в 2D по вводимым координатам___\n')

x1 = Enter_float('Введите координату точки 1 по оси X:')
y1 = Enter_float('Введите координату точки 1 по оси Y:')
x2 = Enter_float('Введите координату точки 2 по оси X:')
y2 = Enter_float('Введите координату точки 2 по оси Y:')

distance = round(math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2)), 3)
print(f'Расстояние между  точками с координатами ({x1};{y1}) и ({x2};{y2}) равно {distance}')

