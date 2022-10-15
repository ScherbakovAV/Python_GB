import FunctHW3

# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка,стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

print(f'\n___1. Сумма элементов списка, стоящих на нечётных позициях___\n')

while True:
    string1_length = abs(FunctHW3.Enter_number('Введите количество элементов списка'))
    if string1_length != 0: break
    else: print('Количество не может быть равным 0!')

string1 = []
sum_odd_elements = 0

for i in range(string1_length):
    string1.append(FunctHW3.My_random())
    if i % 2 != 0 and i != 0:
        sum_odd_elements += string1[i]

print(f'Для списка {string1}\nсумма элементов с нечётными индексами равна {sum_odd_elements}')

print(input('Для перехода к следующей задаче нажмите "Enter"'))

# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

print(f'\n___2. Произведение пар элементов списка___\n')

while True:
    string2_length = abs(FunctHW3.Enter_number('Введите количество элементов списка'))
    if string2_length != 0: break
    else: print('Количество не может быть равным 0!')

string2 = []
product_pairs = []

for i in range(string2_length):
    string2.append(FunctHW3.My_random())

for j in range((len(string2) + 1) // 2):
    product_pairs.append(string2[j] * string2[-(j + 1)])

print(f'Для списка {string2}\nпроизведение пар элементов: {product_pairs}')

print(input('Для перехода к следующей задаче нажмите "Enter"'))

# 3. Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

print(f'\n___3. Нахождение разницы между максимальным и минимальным значением дробной части элементов списка вещественных чисел___\n')

while True:
    string3_length = abs(FunctHW3.Enter_number('Введите количество элементов списка'))
    if string3_length != 0: break
    else: print('Количество не может быть равным 0!')

string3 = []
string3.append(round(FunctHW3.My_random() + FunctHW3.My_random(2) / 100, 2))
temp = round(string3[0] % 1, 2)
max = temp
min = temp

for i in range(1, string3_length):
    string3.append(round(FunctHW3.My_random() + FunctHW3.My_random(2) / 100, 2))
    temp = round(string3[i] % 1, 2)
    if temp > max: max = temp
    if temp < min and temp != 0: min = temp

print(f'Для списка {string3}\nразница между максимальным ({max}) и минимальным ({min}) значением дробной части элементов равна {round(max - min, 2)}\n')

print(input('Для перехода к следующей задаче нажмите "Enter"'))

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

print(f'\n___4. Преобразование десятичного числа в различные системы счисления___\n')

Dec_number = abs(FunctHW3.Enter_number('Введите целое число для преобразования'))
tmp_bin = Dec_number
tmp_oct = Dec_number
tmp_hex = Dec_number
Bin_number = ""
Oct_number = ""
Hex_number = ""
new_digit_hex = ""

while tmp_bin != 0:
    Bin_number = str(tmp_bin % 2) + Bin_number
    tmp_bin = tmp_bin // 2

while tmp_oct != 0:
    Oct_number = str(tmp_oct % 8) + Oct_number
    tmp_oct = tmp_oct // 8

while tmp_hex != 0:
    new_digit_hex = tmp_hex % 16
    
    if new_digit_hex == 10: new_digit_hex = str("A")
    elif new_digit_hex == 11: new_digit_hex = str("B")
    elif new_digit_hex == 12: new_digit_hex = str("C")
    elif new_digit_hex == 13: new_digit_hex = str("D")
    elif new_digit_hex == 14: new_digit_hex = str("E")
    elif new_digit_hex == 15: new_digit_hex = str("F")

    Hex_number = str(new_digit_hex) + Hex_number
    tmp_hex = tmp_hex // 16

print(f'DEC({Dec_number}) -> BIN = {Bin_number}')
print(f'DEC({Dec_number}) -> OCT = {Oct_number}')
print(f'DEC({Dec_number}) -> HEX = {Hex_number}')

print(input('Для перехода к следующей задаче нажмите "Enter"'))

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

print(f'\n___5. Вывод списка чисел Фибоначчи (положительные и отрицательные индексы)___\n')

len = abs(FunctHW3.Enter_number('Введите количество положительных элементов списка чисел Фибоначчи:'))

if len != 0:
    fibo = [0] * (len * 2 + 1)

    fibo[len + 1] = 1
    fibo[len - 1] = fibo[len + 1]

    for i in range(2, len + 1):
        fibo[len + i] = fibo[len + i - 2] + fibo[len + i - 1]
        fibo[len - i] = fibo[len - i + 2] - fibo[len - i + 1]
else: fibo = 0

print(f'\n{fibo}\n\nПрограмма завершена.')
