import math
n = int(input('Введите количество цифр после запятой: '))
print('Число 𝜋: {:.100f}'.format(math.pi))
a = math.pi
b = round(a,n+1)*10**n
c = math.modf(b)
a = c[1] / 10**n
print(f'Число 𝜋 с заданной точностью:  {a:.100f}  ')