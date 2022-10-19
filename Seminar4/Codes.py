import math

# 1. Задайте строку из набора чисел. Напишите программу, которая покажет
# большее и меньшее число. В качестве символа-разделителя используйте пробел

""" str_for_minmax = [int(number) for number in input("Введите целые числа через пробел: ").split(' ')]

print(str_for_minmax)
 """
# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# с помощью математических формул нахождения корней квадратного уравнения
# с помощью дополнительных библиотек Python

# Дискриминант квадратного уравнения — это выражение, равное b2 − 4ac.

""" print('Решение квадратного уравнения вида ax² + bx + c = 0...')
a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))

D = b**2 - 4 * a * c

if (D > 0):
    x1 = (math.sqrt(D) - b) / (2 * a)
    x2 = (-math.sqrt(D) - b) / (2 * a)
    print(f'x1 = {x1}, x2 = {x2}')
elif (D == 0):
    x = (-b / 2* a)
    print(f'x = {x}')
else:
    print('Корней в уравнении нет') """

# С семинара:
""" from scipy.optimize import fsolve
def func(x):
    return x*math.cos(x-4)

x0 = fsolve(func, 0.0) """


# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# Вариант 1
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
max = 0
min = 0

if (a != b):
    if (a > b):
        max = a
        min = b
    elif (a < b):
        max = b
        min = a

    for i in range(min, min * max + 1):
        if (i % min == 0 and i % max == 0):
            print(f'Наименьшее общее кратное {a} и {b} - {i}')
            break

# Вариант 2

while (max != 0):
    min, max = max, min % max
    # =
    # C= a%b
    # a=b
    # b=c

    
print(a * b / min)

# Вариант 3
def gin(): # get valid int number
    try:
        user_input = int(input('Введите целое число '))
        return user_input
    except ValueError as v:
        print(v)         
        return gin()

n1 = gin()
n2 = gin()
a = True
b = 1
while a:
    if (n1*b) % n2 == 0:
        print(n1*b)
        a = False        
    b += 1
