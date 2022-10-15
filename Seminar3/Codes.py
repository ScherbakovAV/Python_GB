# 1. Реализуйте алгоритм задания случайных чисел без
# использования встроенного генератора псевдослучайных чисел.
# А. Реализовать создание списка случайных элементов
# Б.Реализовать создание списка случайных элементов - строк

import datetime

# моё - числа
print(f'\nTask1A - my solution\n')

def My_random(count = 1):
    import time
    random = ''
    for i in range(1, count + 1):
        random_digit = str((datetime.datetime.now()).microsecond % 10)
        random += random_digit
        time.sleep(0.01)
    return int(random)

print(My_random(10))

# с семинара - числа
print(f'\nTask1A\n')

b1 = 1
b2 = 100
a = (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
a = a % 1

new = round(b1 + (b2 - b1) * a)

print(new)

# с семинара - строки
print(f'\nTask1B - my solution\n')
mas = list(map(chr, range(97, 123)))
n = 15
b1 = 0
b2 = 25
a = (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
a = a % 1

st = ''
for i in range(3):
    a *= (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
    a = (a * 1000) % 1
    new_string = mas[round(b1 + (b2 - b1) * a)]
    st += new_string
    
print(st)

# 2. Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке некое число.
# Пример:
# строка (1, 4, 2, 7, 3, 10, 4, 13, 5, 16, 6, 19) число 16 -> да

# Моё решение
print(f'\nTask2\n')

length = 10
new_str = []
finded_num = 5
is_find = False

for i in range(length):
    new_str.append(My_random())
    if new_str[i] == finded_num:
        is_find = True

print(f'Список из {length} элементов: {new_str}')

if is_find == True:
    print(f'Число {finded_num} есть в этом списке')
else: print(f'Числа {finded_num} в этом списке нет')

# 3. Напишите программу, которая определит позицию второго вхождения
# строки в списке либо сообщит, что её нет.
# Примеры:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# Моё решение
print(f'\nTask3\n')

def Second_entry_element(test_string):
    answer = -1
    for i in range(1, len(test_string)):
        if test_string[0] == test_string[i]: answer = i
    return answer

print(Second_entry_element(["qwe", "asd", "zxc", "qwe", "ertqwe"]))
print(Second_entry_element(["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]))
print(Second_entry_element(["йцу", "фыв", "ячс", "цук", "йцукен"]))
print(Second_entry_element(["123", "234", 123, "567"]))
print(Second_entry_element([]))