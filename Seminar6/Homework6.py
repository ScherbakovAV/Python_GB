from random import randint
from random import random

# 1.
# ДЗ 3, задача №3: Нахождение разницы между максимальным и минимальным
# значением дробной части элементов списка вещественных чисел

""" Исходная задача """

string1 = []
string1.append(round(randint(1, 9) + random(), 2))
temp = round(string1[0] % 1, 2)
max_number = temp
min_number = temp

for i in range(1, 10):
    string1.append(round(randint(1, 9) + random(), 2))
    temp = round(string1[i] % 1, 2)
    if temp > max_number: max_number = temp
    elif temp < min_number and temp != 0: min_number = temp

print(f'1.1) Для списка {string1}\nразница между максимальным ({max_number}) и минимальным ({min_number}) значениями дробных частей элементов равна {round(max_number - min_number, 2)}\n')

""" C улучшениями """

string2 = list(map(lambda value: round(value, 2), (randint(1, 9) + random() for i in range(10)))) # имитация ввода списка дробных значений
string2_fract = list(map(lambda num: round(num % 1, 2), string2)) # обрезание целой части элементов списка
max_num = max(string2_fract)
min_num = min(string2_fract)
print(f'1.2) Для списка {string2}\nразница между максимальным ({max(string2_fract)}) и минимальным ({min(string2_fract)}) значениями дробных частей элементов равна {round(max(string2_fract) - min(string2_fract), 2)}\n')


#_______________________________________________________________________________

# 2.
# ДЗ 5, задача №1: Программа, удаляющая из текста все слова, содержащие ""абв"".

text = 'авб абввв баа абв ывваабв ыукк абв вууа ыабвуу'
print(text)

""" Исходная задача """

lst = text.split(' ')

i = len(lst) - 1

while i >= 0:
    if 'абв' in lst[i]:
        lst.remove(lst[i])
    i -= 1
print(f'2.1) {lst}')

""" C улучшениями """

lst2 = list(filter(lambda text: not 'абв' in text, text.split()))
print(f'2.2) {lst2}')


#_______________________________________________________________________________

# 3.
# Задача из семинара 4: Задайте два числа. Напишите программу,
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

""" Исходная задача """
max_n = 0
min_n = 0

if (a != b):
    if (a > b):
        max_n = a
        min_n = b
    elif (a < b):
        max_n = b
        min_n = a

    for i in range(min_n, min_n * max_n + 1):
        if (i % min_n == 0 and i % max_n == 0):
            print(f'3.1) Наименьшее общее кратное {a} и {b} - {i}')
            break


""" C улучшениями """
maximal = max(a, b)
minimal = min(a, b)
mult_list = list(filter(lambda value: value % maximal == 0 and value % minimal == 0, list(i for i in range(minimal, minimal * maximal + 1))))
print(f'3.2) Наименьшее общее кратное {a} и {b} - {min(mult_list)}')