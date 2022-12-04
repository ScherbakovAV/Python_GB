# К аналитику обратился риэлтор c задачей выставить ценник для продажи объектов недвижимости площадью 48м2 и 54м2. В ходе работы над задачей аналитик выяснил, что:
# объект 31м2 стоит $19310
# объект 51м2 стоит $52150
# объект 61м2 стоит $74570
# Вопрос: что. сказать риелтору?

from sympy import *

squares = [31, 51, 61]
prices = [19310, 52150, 74570]

a, b, c = symbols('a b c')

eq1 = Eq(squares[0] ** 2 * a + squares[0] * b + c, prices[0])
eq2 = Eq(squares[1] ** 2 * a + squares[1] * b + c, prices[1])
eq3 = Eq(squares[2] ** 2 * a + squares[2] * b + c, prices[2])

result = linsolve([eq1, eq2, eq3], a, b, c)
print(result)

def fan(x):
    return 20 * x **2 + 2 * x + 28

print(f'48 м2 -> {fan(48)}')
print(f'54 м2 -> {fan(54)}')