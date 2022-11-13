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
        elif type == 2:
            try:
                value = float(input())
                break
            except:
                print("Ошибка! Введите число:")
    return value


# 1. Вычислить число c заданной точностью d
# Пример: - при d = 0.001, π = 3.141, 10^(-1) ≤ d ≤10^(-10)
# е = 1 + 1/1! + 1/2! + 1/3! + ... = 2,7182818284590452353602874713527…

def number_e(acc):
    acc = abs(acc)
    d = 1 / (10 ** acc)
    e = 1
    fact_e = 1

    count = 1
    while True:
        fact_e *= count
        temp_e = e + 1 / (fact_e)
        if (abs(e - temp_e) <= d):
            e = temp_e
            return e
        e = temp_e    
        count += 1

print(f'\n____1. Вычисление числа "e"c заданной точностью____\n')
accuracy = Enter_number('Введите требуемую точность числа "e" после запятой: ')
print(f'e = {number_e(accuracy):.{accuracy}f}')


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

print(f'\n____2. Вывод списка простых множителей введённого числа____\n')

while True:
    number = Enter_number('Введите натуральное число: ')
    if number > 0: break
    else: print('Натуральное число должно быть больше нуля!')

prime_factors(number)


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

""" 
Моя переработка:
def unique_elements(main_list):
    unique_list = [main_list[0]]

    for item in main_list:
        if not item in unique_list: unique_list.append(item)
    
    return unique_list """

print(f'\n____3. Вывод списка неповторяющихся элементов исходной последовательности____\n')

num_list = [random.randint(1, 9) for i in range(random.randint(1, 29))]
print(f'Заданная последовательность чисел:\n{num_list}')
print(f'Список неповторяющихся элементов исходной последовательности:\n{unique_elements(num_list)}')

""" 
Ещё вариант решения:
num_list = [random.randint(1, 9) for i in range(random.randint(1, 29))]
unique_list = set(num_list)
print(f'Заданная последовательность чисел:\n{num_list}')
print(f'Список неповторяющихся элементов исходной последовательности:\n{unique_list}') """

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

def poly_gen(pow): # генерация многочлена по заданной степени
    poly_list = []
    while pow != 0:
        k = str(random.randint(0, 100))
        if pow > 1:
            if k != '0' and k != '1': poly_list.append(f'{k}x^{str(pow)}')
            elif k == '1': poly_list.append(f'x^{str(pow)}')
        elif pow == 1:
            if k != '0' and k != '1': poly_list.append(f'{k}x')
            elif k == '1': poly_list.append(f'x')
        pow -= 1
    poly_list.append(str(random.randint(0, 100)))
    return poly_list

def list_to_file(lst, n = 1): # запись многочлена из списка в файл и вывод его на экран
    file = str(f'file{n}.txt')
    with open(file, 'w', encoding = "utf-8") as data:
        for i in range(len(lst) - 1):
            data.write(f'{lst[i]} + ')
        data.write(lst[-1])
    print(f'Создан файл file{n}.txt с многочленом:')
    with open(file, 'r', encoding = "utf-8") as data:
        print(f'{data.read()}\n')

print(f'\n____4. Запись в файл многочлена заданной степени со случайными коэффициентами____\n')

while True:
    power = Enter_number('Введите натуральную степень многочлена: ')
    if power > 0: break
    else: print('Натуральное число должно быть больше нуля!')

poly1 = poly_gen(power)
list_to_file(poly1)

poly2 = poly_gen(power)
list_to_file(poly2, 2)


# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def list_from_file(file): # возврат многочлена из файла в виде списка 
    with open(file, 'r', encoding = "utf-8") as data:
        str = data.read()
    pol_list = str.split(' + ')
    return pol_list

def strlist_to_intlist(lst): # преобразование многочлена из строкового списка членов в интовый список списков (коэффициент, степень члена)
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

def polynomials_sum(lst1, lst2): # возврат суммы двух интовых многочленов в виде интового списка списков
    lst_sum = []
    check = False

    if len(lst1) >= len(lst2):
        for i in range(len(lst1)):
            for j in range(len(lst2)):
                if lst1[i][1] == lst2[j][1]:
                    lst_sum.append([lst1[i][0] + lst2[j][0], lst1[i][1]])
                    check = True
            if check == False: lst_sum.append([lst1[i][0], lst1[i][1]])
            check = False
    else:
        for i in range(len(lst2)):
            for j in range(len(lst1)):
                if lst2[i][1] == lst1[j][1]:
                    lst_sum.append([lst2[i][0] + lst1[j][0], lst2[i][1]])
                    check = True
            if check == False: lst_sum.append([lst2[i][0], lst2[i][1]])
            check = False
    
    return lst_sum

def intlist_to_str(lst_of_lst): # преобразование интового списка списков многочлена в строку
    poly_str = ''

    for i in range(len(lst_of_lst)):
        if lst_of_lst[i][1] > 1:
            if lst_of_lst[i][0] != 1: poly_str += (f'{str(lst_of_lst[i][0])}x^{str(lst_of_lst[i][1])} + ')
            else: poly_str += (f'x^{str(lst_of_lst[i][1])} + ')
        elif lst_of_lst[i][1] == 1:
            if lst_of_lst[i][0] != 1: poly_str += (f'{str(lst_of_lst[i][0])}x + ')
            else: poly_str += (f'x + ')
        else:
            poly_str += (f'{str(lst_of_lst[i][0])}')        
        
    return poly_str

def str_to_file(str_poly, n = 1): # запись строки в файл и вывод результата на экран
    file = str(f'file{n}.txt')
    with open(file, 'w', encoding = "utf-8") as data:
        data.write(str_poly)
    print(f'Создан файл file{n}.txt с этим многочленом\n')


print(f'____5. Запись в файл многочлена из суммы двух многочленов, записанных в отдельных файлах____\n')

poly1_ext = list_from_file('file1.txt')
poly1_ext_int = strlist_to_intlist(poly1)

poly2_ext = list_from_file('file2.txt')
poly2_ext_int = strlist_to_intlist(poly2)

print(f'Сумма многочленов из предыдущей задачи:\n')
sum_pol = intlist_to_str(polynomials_sum(poly1_ext_int, poly2_ext_int))
print(sum_pol)
str_to_file(sum_pol, 3)