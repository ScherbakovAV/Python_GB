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

def My_random(count = 1): # фунцкция вывода псевдослучайных чисел заданной разрядности
    import time
    import datetime
    random = ''
    for i in range(1, count + 1):
        random_digit = str((datetime.datetime.now()).microsecond % 10)
        random += random_digit
        time.sleep(0.02)
    return int(random)