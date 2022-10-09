print("hello world")

a = 123
b = 1.23
c = None
#print(a, b, c)
#print(type(a))
s = 'Hello world'
print(s)

# комментарий

print(a, ' - ', b ,' - ', s)
print('{1} - {0} - {2}'.format(a, b, s))

f = True
print(f)

list1 = ['1', '2', '3']
print(list1)

print("Введите число 1")
e = int(input())
print("Введите число 2")
f = int(input())
print(e + f)

g = 1.3
h = 3
c = g * h
print(c)
print(round(c, 5)) # округление
print(h)
h += 2
print(h)

k = 1 > 4
print(k)

l = 'qwe'
m = 'qwe'
print(l == m)

func = 1
T = 4
x = 123
print(func<T>x)

f = 1 > 2 or 4 < 6

fi = [1,2,3,4]
print(fi)
print(not 2 in fi)
is_odd = fi[0] % 2 == 0
# is_odd = not fi[0] % 2 - аналогично
print(is_odd)

# if и if-else
if e > f:
    print(e)
# elif:
# ...
else:
    print(f)

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Хватит')
print(inverted)

for i in 1,2,3,4,5:
    print(i ** 2)

list2 = range(1, 10, 2)
for j in list2:
    print(j)

text2 = 'Ты чего?'
print(len(text2)) # длина строки

numbers = []
ran = range(1, 6)
print(type(ran))
numbers = list(ran) # приведение типа range к типу list
print(type(numbers))
for k in numbers:
    k *= 2
    print(k)

print(numbers)
numbers.append(6)
print(numbers)

