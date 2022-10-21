# 1.В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.

""" with open('lesson1.txt') as file:
    str1 = file.read()

lst = str1.split(' ')

for i in range(len(lst)):
    lst[i] = int(lst[i])

print(lst)

for i in range(1, len(lst)):
    if lst[i] != lst[i - 1] + 1:
        print(lst[i - 1] + 1)
        break """

# 1*/ Несколько наборов натуральных чисел, из каждого удаляем одно число.
# Найти эти пропущенные числа.


# 2. Дан список чисел. Создайте список, в который попадают числа, описываемые
# возрастающую последовательность. Порядок элементов менять нельзя.
# 2.1 Найти все такие последовательности и выбрать тот, который самый длинный.
# 2.2 Из этих последовательностей выбрать ту, в котрой сумма элементов максимальна.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

# import random

# lst = [0] * random.randint(5, 19)

# for i in range(len(lst)):
#     lst[i] = random.randint(1, 9)
# print(lst)

""" lst = [1, 5, 2, 3, 4, 6, 1, 7]

new_list = [lst[0]]
min = new_list[0]

for j in range(len(lst) - 1):
    for i in range(1, len(lst)):
        if lst[i] > min:
            new_list.append(lst[i])
            min = new_list[-1]
    print(new_list)
    new_list = [lst[j]]
    min = new_list[j] """

# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'авб абввв баа абв ывваабв ыукк абв'
lst1 = text.split(' ')
print(lst1)

i = len(lst1) - 1

while i >= 0:
    if 'абв' in lst1[i]:
        lst1.remove(lst1[i])
    i -= 1
print(lst1)

""" for i in lst1:
    if "абв" in i:
        print(i)
        lst1.remove(i)
print(lst1) """

# Для ДЗ:
# X |   |X
#    |O|
# O|   |O

#[[0,O,X],[0,O,X],[0,O,X]]

