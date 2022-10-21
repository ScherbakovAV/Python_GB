import random

def Enter_number(text, type = 1): # функция ввода числа с проверкой 
    print(text)
    while True:
        if type == 1:
            try:
                value = int(input())
                break
            except:
                print("Ошибка! Введите целое число:")
        elif type == 2 or type == 3:
            try:
                if type == 2:
                    value = float(input())
                    break
                elif type == 3:
                    from decimal import Decimal
                    value = Decimal(input())
                    break
            except:
                print("Ошибка! Введите число:")
    return value

# 1. Вычислить число c заданной точностью d
# Пример: - при d = 0.001, π = 3.141.    10^(-1) ≤ d ≤10^(-10)
# е = 1 + 1/1! + 1/2! + 1/3! + ... = 2,7182818284590452353602874713527…

def number_e(acc):
    d = 1 / (10 ** acc)
    e = 1
    fact_e = 1

    count = 1
    while True:
        print(e)
        fact_e *= count
        temp_e = e + 1 / (fact_e)
        if (abs(e - temp_e) <= d):
            e = temp_e
            return e
        e = temp_e    
        count += 1

""" accuracy = abs(Enter_number('Введите требуемую точность числа "e" после запятой: '))
print(f'e = {number_e(accuracy)}\n') """

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def prime_factors(num):
    temp = num
    factors_list = []
    prime_num = 2
    while temp != 1:
        while not temp % prime_num:
            factors_list.append(prime_num)
            temp /= prime_num
        prime_num += 1
    if num != factors_list[0]:
        print(f'{num} = ', end = '')
        for i in range(len(factors_list)):
            if i != len(factors_list) - 1: print(f'{factors_list[i]}', end = ' * ')
            else: print(factors_list[i])
    else: print(f'Число {num} - простое')

""" while True:
    number = Enter_number('Введите натуральное число: ')
    if number > 0: break
    else: print('Натуральное число должно быть больше нуля!')

prime_factors(number) """

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

def unique_elements(main_list):
    unique_list = [main_list[0]]
    is_equals = False

    for item in main_list:
        for i in range(len(unique_list)):
            if item == unique_list[i]: is_equals = True
        if is_equals == False:
            unique_list.append(item)
        is_equals = False
    
    return unique_list

""" num_list = [random.randint(1, 9) for i in range(random.randint(1, 29))]
print(f'Заданная последовательность чисел:\n{num_list}')
print(f'Список неповторяющихся элементов исходной последовательности:\n{unique_elements(num_list)}') """

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

def polynomial_generate(number):
    pol_list = []
    while number != 0:
        k = str(random.randint(0, 100))
        if number > 1:
            if k != '0' and k != '1': pol_list.append(f'{k}x^{str(number)}')
            elif k == '1': pol_list.append(f'x^{str(number)}')
        elif number == 1:
            if k != '0' and k != '1': pol_list.append(f'{k}x')
            elif k == '1': pol_list.append(f'x')
        number -= 1
    pol_list.append(str(random.randint(1, 100)))
    return pol_list

def list_to_file(lst, n = 1):
    file = str(f'file{n}.txt')
    with open(file, 'w') as data:
        for i in range(len(lst) - 1):
            data.write(f'{lst[i]} + ')
        data.write(lst[-1])
    print(f'Создан файл file{n}.txt с этим многочленом')

""" while True:
    power = Enter_number('Введите натуральную степень многочлена: ')
    if power > 0: break
    else: print('Натуральное число должно быть больше нуля!')

polynomial1 = polynomial_generate(power)
print(polynomial1)
list_to_file(polynomial1)

polynomial2 = polynomial_generate(power)
print(polynomial2)
list_to_file(polynomial2, 2) """

# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# text = text.encode('utf8')

# with open('file.txt', 'w', encoding = "utf-8") as data:
    # data.write('текст')


def list_from_file(file):
    with open(file, 'r') as data:
        str = data.read()
    pol_list = str.split(' + ')
    return pol_list

def strlist_to_intlist(lst):
    list_of_lst = []

    for i in range(len(lst)):
        if 'x^' in lst[i]:
            list_of_lst.append((lst[i]).split('x^'))
        elif 'x' in lst[i]:
            list_of_lst.append((lst[i]).split('x'))
        else:
            list_of_lst.append([lst[i], '0'])
    
    for j in range(len(list_of_lst)):
        for k in range(len(list_of_lst[i])):
            if list_of_lst[j][k] == '': list_of_lst[j][k] = '1'
            list_of_lst[j][k] = int(list_of_lst[j][k])

    return list_of_lst

def polynomials_sum(lst1, lst2):
    lst_sum = []

    if len(lst1) >= len(lst2):
        for i in range(len(lst1)):
            for j in range(len(lst1[i])):
                for k in range(len(lst2)):
                    for l in range(len(lst2[k])):
                        if lst1[i][j] == lst1[k][l]:
                            lst_sum.append()

    return lst_sum

poly1 = list_from_file('file1.txt')
#print(poly1)
print(f'{strlist_to_intlist(poly1)}\n')

poly2 = list_from_file('file2.txt')
#print(poly2)
print(f'{strlist_to_intlist(poly2)}\n')

# poly2 = list_from_file('file2.txt')
# print(poly2)
# poly_sum = list(zip(poly1, poly2))
# print(poly_sum)