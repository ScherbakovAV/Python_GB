import math

# Теория №1. Строки
# 1.1. Написать программу которая принимает в строку и букву
# и определяет индексы первого и последнего вхождения буквы в строке.

print(f'Введите строку:')
text = input()

print(f'Введите искомую букву или сочетание букв: ')
letters = input()

first_found = -1
last_found = -1

for i in range(len(text)):
    if text[i] == letters:
        last_found = i
        if first_found == -1:
            first_found = i

print(f'Индекс первого вхождения символа {letters} - {first_found}')
print(f'Индекс последнего вхождения символа {letters} - {last_found}')
     
# 1.2. Написать программу, которая на основе заданной строки вида ХХХ
# выводит на экран “стихотворение” :
# ХХХХХХХХХХХХ
# ХХХХХХХХХ
# ХХХХХХ
# ХХХ

print(f'Введите строку:')
poem = input()

print(f'{poem * 4}\n{poem * 3}\n{poem * 2}\n{poem}\n')


# Теория №2. Списки

# 2.1.Получить список некоторых целых чисел, найдите значение 20 в нем
# и, если оно присутствует, замените его на 200.
# Выполнить только при первом вхождении числа 20.

numbers_list = []
N = int(input('Введите размер списка:'))

for i in range(N):
    element = int(input(f'Введите число №{i + 1}: '))
    numbers_list.append(element)

print(f'\n Этот список: {numbers_list}')

for i in range(len(numbers_list)):
    if numbers_list[i] == 20:
        numbers_list[i] = 200
        break

print(f'\n Этот список с заменой: {numbers_list}')

# 2.2. Получить список чисел. Превратите его в список квадратов этих чисел.

for i in range(len(numbers_list)):
    numbers_list[i] = math.pow(numbers_list[i], 2)

print(f'\n Этот список, в котором элементы заменены на их квадраты: {numbers_list}')


# Теория №3. Словари
# Заданы два списка одинаковой длины. Необходимо создать из них словарь
# таким образом, чтобы элементы первого списка были ключами,
# а элементы второго — соответственно значениями нашего словаря.

list_a = list('GEekBrains')
list_b = ['G','Ge','Gee','Geek', 'B','Br','Bra','Brai', 'Brain','Brains']

dict_a_b = {list_a[i]: list_b[i] for i in range(len(list_b))}

print(dict_a_b)

# 1. Напишите программу, которая принимает на вход
# число N и выдает последовательность из N членов.
# Пример: Для N = 5: 1, -3, 9, -27, 81

print('Введите число:')
element_number = int(input())
print(f'Для {element_number} элементов: ', end = '')

numbers_list = []

for i in range(1, element_number + 1):
    numbers_list.append(i * 2)

print(numbers_list)

# 2. Для натурального n создать словарь индекс-значение,
# состоящий из элементов последовательности 3n + 1
# Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

print(f'Введите число:')
n = int(input())
d = {a: (3 * a + 1) for a in range(1, n + 1)}

print(d)

# 3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# Для str_1 = ‘abcERDabcabc’
# str_2 = ‘abc’
# n = 3

text_1 = input('Введите строку 1: ')
text_2 = input('Введите строку 2: ')

count = 0
for i in range(len(text_1) - (len(text_2) - 1)):
    if text_1[i : i + len(text_2)] == text_2: count += 1
print(f'Количество вхождений строки "{text_2}"в строке "{text_1}" равно {count}')

# Втроенная функция:
# S.count(str, [start],[end])