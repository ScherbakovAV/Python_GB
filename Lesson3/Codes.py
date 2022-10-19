""" List Comprehension
[exp for item in iterable]
[exp for item in iterable (if conditional)]
[exp <if conditional> for item in iterable (if conditional)] """

print(f'\n-List Comprehension-\n')
list1 = []
for i in range (1, 101):
    if (i % 2 == 0):
        list1.append(i)
print(list1)
# =
list1 = [i for i in range (1, 101) if i % 2 == 0] # создание списка
print(list1)

def f(x):
    return x**3
list2 = [(i, f(i)) for i in range(1, 21) if i % 2 == 0] # создание кортежа
print(list2)

""" Анонимные, lambda функции """

print(f'\n-Lambda-\n')

sum = lambda x: x + 10
mult = lambda x: x**2
def h(f, g, x):
    return f(g(x))
result = h(sum, mult, 5)
print(result)
# =
h = lambda f, g, x: f(g(x))
result = h(lambda x: x+10, lambda x: x**2, 5)
print(result)

path = 'D:\Geek Brains\Python_education\Lesson3\\file.txt' # 1
f = open(path, 'r')
data = f.read() + ' '
f.close()
numbers = []
while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]
out = []
for e in numbers:
    if not e % 2:
        out.append((e,e **2))
print(out)


def select(f, col): # 1 -> 2
    return [f(x) for x in col]
def where(f, col):
    return [x for x in col if f(x)]
data = '1 2 3 5 8 15 23 38'.split()
data = select(int, data)
data = where(lambda e: not e % 2, data)
data = list(select(lambda e: (e, e**2), data))
print(data)


""" Функция map """

""" f(x) ⇒ x + 10
    map(f, [ 1, 2, 3, 4, 5])
             ↓  ↓  ↓  ↓  ↓
            [11,12,13,14,15]
Нельзя пройтись дважды """

print(f'\n-Map-\n')

li = [x for x in range (1, 20)]
print(li)
li = list(map(lambda x: x + 10, li))
print(li)

""" Функция filter
    f(x) ⇒ x - чётное
    filter(f, [ 1, 2, 3, 4,5])
                      ↓
                   [ 2, 4 ]
Нельзя пройтись дважды """

print(f'\n-Filter-\n')

data = [x for x in range(10)]
res = list(filter(lambda x: x % 2 == 0, data))
print(res)

""" Функция zip
    zip ([1, 2, 3], ['о', 'д', 'т'], ['f', 's', 't'])
                           ↓
      [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
Нельзя пройтись дважды """

print(f'\n-Zip-\n')

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data)

""" Функция enumerate
enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
                               ↓
[(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
Нельзя пройтись дважды """

print(f'\n-Enumerate-\n')

data = list(enumerate(users))
print(data)

print(f'\n-Задача Lambda с Map и Filter-\n')

data = '1 2 3 5 8 15 23 38'.split() # 2 -> 3
data = list(map(int, data))
data = list(filter(lambda e: not e % 2, data))
data = list(map(lambda e: (e, e**2), data))
print(data)