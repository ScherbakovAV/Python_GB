# 1. Напишите программу вычисления арифметического выражения заданного строкой.
#    Используйте операции +,-,/,*. приоритет операций стандартный.
#    Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
#    Добавьте возможность использования скобок, меняющих приоритет операций.
#    Пример: 1+2*3 => 7; (1+2)*3 => 9;

# 1.а Моё решение

def Str_from_file(file):
    with open(file, 'r', encoding = "utf-8") as data:
        string = data.read()
    print(f'{string} =', end = '')
    return string

def Encode_str_to_math(string):
    string = string.replace(',', '.')
    list_math = []
    temp_str = ''
    for symbol in string:
        if symbol != '+' and symbol != '-' and symbol != '*' and symbol != '/':
            temp_str += symbol
        else:
            list_math.append(float(temp_str))
            temp_str = ''
            list_math.append(symbol)
    list_math.append(float(temp_str))
    return list_math

def Solution(operations):
    tmp = None
    i = 0

    while '*' in operations or '/' in operations:
        if '*' == operations[i] or '/' == operations[i]:
            if '*' == operations[i]: tmp = operations[i - 1] * operations[i + 1]
            elif '/' == operations[i]: tmp = operations[i - 1] / operations[i + 1]
            operations[i - 1] = tmp
            tmp = None
            del operations[i]
            del operations[i]
        else: i += 1
    
    i = 0

    while '+' in operations or '-' in operations:
        if '+' == operations[i] or '-' == operations[i]:
            if '+' == operations[i]: tmp = operations[i - 1] + operations[i + 1]
            elif '-' == operations[i]: tmp = operations[i - 1] - operations[i + 1]
            operations[i - 1] = tmp
            tmp = None
            del operations[i]
            del operations[i]
        else: i += 1

    return float(operations[0])

mathematic = Str_from_file('math.txt')
enc = Encode_str_to_math(mathematic)
print(Solution(enc))


# 1.б Решение с семинара

""" formula = '24/2*3+30'
lst = []
numbers = ''

def Action(array,sign):
    i = 0
    while sign in array:
        if array[i] == sign:
            if sign == '*':
                a = int(array[i-1])*int(array[i+1])
            elif sign == '/':
                a = int(array[i-1])/int(array[i+1])
            elif sign == '-':
                a = int(array[i-1])-int(array[i+1])
            elif sign == '+':
                a = int(array[i-1])+int(array[i+1])
            array[i-1] = a
            array.pop(i+1)
            array.pop(i)
            return(array)
        else:
            i+=1

for i in formula:
    if i.isdigit():
        numbers+=i
    else:
        lst.append(numbers)
        numbers=''
        lst.append(i)
lst.append(numbers)
print(lst)

i = 0
while '/' in lst or '*' in lst:
    if lst[i] == '/':
        print(Action(lst,'/'))
        i = 0
    elif lst[i] == '*':
        print(Action(lst,'*'))
        i = 0
    else:
        i+=1

i = 0
while '-' in lst or '+' in lst:
    if lst[i] == '-':
        print(Action(lst,'-'))
        i = 0
    elif lst[i] == '+':
        print(Action(lst,'+'))
        i = 0
    else:
        i+=1
print(lst)
 """

# 2. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
#    Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# Решение с семинара
""" import random

random_list = [random.randint(1, 20) for i in range(random.randint(10, 30))]
print(random_list)
print(list(set(random_list)))
uniq_list = [i for i in set(random_list) if random_list.count(i) == 1]
print(uniq_list) """
