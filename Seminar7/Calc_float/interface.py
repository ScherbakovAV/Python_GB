def enter_float():
    while True:
        try:
            value = float(input())
            break
        except:
            print("Ошибка! Введите число:")
    return value

def enter_numbers(): # функция ввода чисел с проверкой
    print('Введите два числа: ')
    a = enter_float()
    b = enter_float()
    return (a, b)
