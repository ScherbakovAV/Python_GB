import math

""" Задача 1
Напишите программу, которая принимает на вход два числа и проверяет,
является ли одно число квадратом другого. """

print('Введите число 1:')
num1 = int(input())
print('Введите число 2:')
num2 = int(input())

def Is_cube(a, b):
    if a == b ** 2 or b == a ** 2:
        return True
    return False

print(Is_cube(num1, num2))

""" Задача 2
Напишите программу, которая на вход принимает 5 чисел
и находит максимальное из них. """

max = int(input(f'Введите 1 число: '))

for i in range(4):
    i += 1
    N = int(input(f'Введите {i+1} число: '))
    if N > max:
        max = N
print(max)

""" Задача 3
Напишите программу, которая будет на вход принимать число N
и выводить числа от -N до N """

print('Введите число диапазона:')
num = abs(int(input()))
for i in range(-num, num):
    print(i, end = ', ')
print(num)

""" Задача 4
Напишите программу, которая будет принимать на вход дробь
и показывать первую цифру дробной части числа.

Примеры:
6,78 -> 7
5 -> нет
0,34 -> 3 """

print('Введите дробное число:')
number = float(input())
if number % 1 == 0:
    number = number * 10
    number = int(number % 10)
    if number == 0: number = None
    print(number) 
else:
    print(0)

""" Задача 5
Напишите программу, которая принимает на вход число и проверяет,
кратно ли оно 5 и 10 или 15, но не 30
 """
print('Введите число:')
k = int(input())
if ((k % 10 == 0 or k % 15 == 0) and k % 30 != 0):
    print(True)
else: print(False)

""" Задача 5
Напишите программу нахождения факториала """

print('Введите число для нахождения его факториала:')
f = int(input())
factorial = 1
for i in range(f):
    factorial *= (i + 1)
print(f'Факториал числа {f} равен {factorial}')
