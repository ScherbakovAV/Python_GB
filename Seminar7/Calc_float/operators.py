import interface
import mult
import sum
import div
import sub
import logger


def operator(a,b):
    print('Выберите действие: ')
    print(f"1: умножение, 2: деление' 3: сложение, 4: вычитание")
    while True:
        try:
            operators = int(input())
            match operators:
                case 1:
                    result= mult.mult_numbers(a,b)
                    logger.mult_logger(a,b, result)
                    return result
                case 2:
                    result= div.Div(a,b)
                    logger.div_logger(a, b, result)
                    return result
                case 3:
                    result= sum.Sum(a,b)
                    logger.sum_logger(a, b, result)
                    return result
                case 4:
                    result= sub.sub(a,b)
                    logger.sub_logger(a, b, result)
                    return result
        except: print("Ошибка! Введите число:")



