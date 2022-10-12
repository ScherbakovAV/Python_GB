from decimal import Decimal

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

def Enter_decimal(text): # функция ввода дробного числа Decimal с проверкой
    print(text)
    while True:
        try:
            value = Decimal(input())
            break
        except:
            print("Ошибка! Введите число:")
    return value

# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

""" print(f'\n___1. Сумма цифр вещественного числа___\n')

number = abs(Enter_decimal("Введите вещественное число:"))

while number % 1 != 0:
    number *= 10

number_sum = 0
while number >= 1:
    number_sum += number % 10
    number = number // 10

print(f'Сумма цифр этого числа равна {int(number_sum)}')
print(input('Для перехода к следующей задаче нажмите "Enter"')) """

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

""" print(f'\n___2. Вывод произведений чисел от 1 до введённого числа___\n')

number_count = abs(Enter_int("Введите целое положительное число:"))

new_element = 1
numbers_list = [new_element]

for i in range(2, number_count + 1):
    new_element *= i
    numbers_list.append(new_element)

print(numbers_list) """

# 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.


# 5. Реализуйте алгоритм перемешивания списка.