# Дана функция f(x) = 5x^2 + 10x - 30
# - Определить корни
# - Найти интервалы, на которых функция возрастает
# - Найти интервалы, на которых функция убывает
# - Построить график
# - Вычислить вершину
# - Определить промежутки, на котором f > 0
# - Определить промежутки, на котором f < 0

# ________________________________________________________________________________
# Найти интервалы, на которых функция возрастает и убывает
""" Теория...
f(x) = x^4 - 2x + 4. Найдем производную:
f`(x) = 4х^3 - 2.
Найдем нули производной: f`(x) = 0; 4х^3 - 2 = 0.
Решаем уравнение:
перенесем (-2) в правую часть: 4х^3 = 2;
поделим уравнение на 4: х^3 = 2/4; х^3 = 1/2.
Отсюда х = 3√1/2 (корень третьей степени из 1/2).
Получается два промежутка: (-∞; 3√1/2) и (3√1/2; +∞).
Определим знаки:
(- ∞; 3√1/2); пусть  х = 0; 4 * 0^3 - 2 = -2, знак (-), функция убывает.
(3√1/2; + ∞), пусть х = 1; 4 * 1^3 - 2 = 4 -2 = 2, знак (+), функция возрастает.
Значит, х(минимальный) = 3√1/2. """

# Моё решение (простое)

funct = '5x^2 + 10x - 30'
funct_der = '10x + 10'
x = -10 / 10

result_minus = 10 * (x - 1) + 10
print(result_minus)

result_plus = 10 * (x + 1) + 10
print(result_plus)

if result_minus < 0:
    print(f'В интервале до {x} функция {funct} убывает')
    print(f'В интервале после {x} функция {funct} возрастает')
else:
    print(f'В интервале до {x} функция {funct} возрастает')
    print(f'В интервале после {x} функция {funct} убывает')


# Моя попытка решить через свои функции:

def func_to_derivative(source): # нахождение производной функции

    funct = source.split()
    funct_derivative = []

    for item in funct:
        if 'x' in item:
            if '^' in item:
                temp = item.replace('x', '').split('^')

                if temp[0] == '': funct_derivative.append(
                    temp[1] + 'x^' + str(int(temp[1]) - 1))
                else: funct_derivative.append(str(int(temp[0]) * int(temp[1])) + 'x^' + str(int(temp[1]) - 1))

            else:
                funct_derivative.append(item.replace('x', ''))

        elif '+' in item:
            funct_derivative.append('+')

        elif '-' in item:
            funct_derivative.append('-')

    if funct_derivative[-1] == '+' or funct_derivative[-1] == '-': funct_derivative.pop()

    return funct_derivative

print(func_to_derivative(funct))

# На этом всё...
#_________________________________________________________________________________________

# Решение других задач Евгением с преподавателем:

# Вершина параболы: (-1.0, -35.0)

import matplotlib.pyplot as plt
#import numpy as np

def roots(a, b, c):
    D = b ** 2 - 4 * a * c
    d = D ** 0.5
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)
    if D > 0:
        return x1, x2
    elif x1 == x2:
        return x1
    else:
        exit('Complex roots')


k1, k2, k3 = 5, 10, -30

roots = roots(k1, k2, k3)
print(roots)

list_x = list(range(-200, 0))
f = lambda x: x/100
list_x = list(map(f, list_x))
print(list_x)

f = lambda x: 5 * x * x + 10 * x - 30
list_y = list(map(f, list_x))
print(list_y)

plt.plot(list_x, list_y)
plt.show()

roots = list(roots)
roots.sort()
print(roots)

roots_mod = []
roots_mod.append(roots[0]-1)
roots_mod.append((roots[0]+roots[1])/2)
roots_mod.append(roots[1]+1)
print(roots_mod)

list_y_new = list(map(f, roots_mod))
print(list_y_new)

sign = lambda x: 'f>0' if x >= 0 else 'f<0'
sign = list(map(sign, list_y_new))

print(roots)
print(sign)

sign_list = []
sign_list.append(sign[0])
sign_list.append(roots[0])
sign_list.append(sign[1])
sign_list.append(roots[1])
sign_list.append(sign[2])
print(sign_list)

# Примеры от преподавателя:
""" from scipy.optimize import fsolve

def func(x):
	return x*math.cos(x-4)

x0 = fsolve(func, 0.0) """

""" from sympy import diff, symbols, cos, sin
x, y = symbols('x y')
print(diff(cos(x))) - sin(x)
print(diff(cos(x) + 1j*sin(y), x)) """