import random

def Enter_number(text = '', type = 1): # функция ввода числа с проверкой 
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

# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

""" print(f'\n____1. Удаление из текста все слова, содержащие "абв"____\n')

# text = input('Введите текст для проверки: ')
text = 'Незабвенный зимбабвийский главбух'
print(text)
lst1 = i for i in text.split() if 'абв' not in i
print(' '.join(lst1))

input('Нажмите Enter для перехода к следующей задаче...') """

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

print(f'\n____2. Игра с конфетами____\n')

def game_mode():
    print('Выберите тип игры:\n1 - "Игрок против игрока"\n2 - "Игрок против бота"\n3 - "Игрок против умного бота"', end = '')

    while True:
        game_type = Enter_number()
        match game_type:
            case 1: return game_type
            case 2: return game_type
            case 3: return game_type
            case _: print('Такого режима нет. Введите число от 1 до 3: ', end = '')

def Candies_game(candies = 2021, candies_max = 28, game_type = 1):

    move = random.randint(1,2)
    round = 1
    candies_given = 0

    print(f'\nНа столе лежат конфеты в количестве {candies} шт. Игроки 1 и 2 ходят по очереди.\nЗа один ход можно забрать не более чем {candies_max} конфет.')
    print(f'Все конфеты оппонента достаются сделавшему последний ход.')

    if game_type == 1:
        print(f'\nРежим игры "Игрок против игрока"\nПервый ход делает {move} игрок')

        while candies!= 0:
            print(f'\nРаунд {round}. Конфет на столе - {candies} шт.')

            if candies < candies_max: candies_max = candies

            print(f'Ход игрока {move}. Возьмите не более {candies_max} шт. конфет: ', end = '')

            while True:
                candies_given = Enter_number()
                if 1 <= candies_given <= candies_max: break
                else: print(f'Введите число от 1 до {candies_max}: ', end = '')

            candies -= candies_given

            if candies == 0:
                print(f'\nИгрок {move} победил!!! Все конфеты Ваши!')
                break
            
            round += 1

            if move == 1: move = 2
            else: move = 1

    if game_type == 2 or game_type == 3:
        if game_type == 2: print(f'\nРежим игры "Игрок против компьютера (упрощённый вариант)"\nПервый ход делает {move} игрок')
        elif game_type == 3: print(f'\nРежим игры "Игрок против компьютера (интеллектуальный бот)"\nПервый ход делает {move} игрок')

        if move == 1:            
            while candies!= 0:
                print(f'\nРаунд {round}. Конфет на столе - {candies} шт.')

                if candies < candies_max: candies_max = candies

                print(f'Ваш ход. Возьмите не более {candies_max} шт. конфет: ', end = '')

                while True:
                    candies_given = Enter_number()
                    if 1 <= candies_given <= candies_max: break
                    else: print(f'Введите число от 1 до {candies_max}: ', end = '')
                
                candies -= candies_given

                if candies == 0:
                    print(f'\nВы победили!!! Все конфеты Ваши!')
                    break

                if candies < candies_max: candies_max = candies
                
                print(f'Ход компьютера. Нажмите "enter" для продолжения...', end = '')
                input()

                if game_type == 2:
                    candies_bot = random.randint(1, candies_max)
                    candies -= candies_bot
                elif game_type == 3:
                    candies_bot = candies % (candies_max + 1)
                    if candies_bot == 0: candies_bot = random.randint(1, candies_max)
                    candies -= candies_bot

                if candies == 0:
                    print(f'\nПоражение! Компьютер взял {candies_bot} шт. конфет и победил. Все конфеты достаются ему.')
                    break
                else:
                    print(f'Компьютер взял {candies_bot} шт. конфет. Осталось {candies}')
                
                round += 1

                if move == 1: move = 2
                else: move = 1
            
        if move == 2:
            while candies!= 0:
                print(f'\nРаунд {round}. Конфет на столе - {candies} шт.')
                
                if candies < candies_max: candies_max = candies

                print(f'Ход компьютера. Нажмите "enter" для продолжения...', end = '')
                input()

                if game_type == 2:
                    candies_bot = random.randint(1, candies_max)
                    candies -= candies_bot
                elif game_type == 3:
                    candies_bot = candies % (candies_max + 1)
                    if candies_bot == 0: candies_bot = random.randint(1, candies_max)
                    candies -= candies_bot

                if candies == 0:
                    print(f'\nПоражение! Компьютер взял {candies_bot} шт. конфет и победил. Все конфеты достаются ему.')
                    break
                else:
                    print(f'Компьютер взял {candies_bot} шт. конфет. Осталось {candies}')

                if candies < candies_max: candies_max = candies

                print(f'Ваш ход. Возьмите не более {candies_max} шт. конфет: ', end = '')

                while True:
                    candies_given = Enter_number()
                    if 1 <= candies_given <= candies_max: break
                    else: print(f'Введите число от 1 до {candies_max}: ', end = '')
                
                candies -= candies_given

                if candies == 0:
                    print(f'\nВы победили!!! Все конфеты Ваши!')
                    break

                round += 1

                if move == 1: move = 2
                else: move = 1

candies_num = random.randint(50, 100)
maximum = random.randint(5, 30)

""" Candies_game(candies = candies_num, candies_max = maximum, game_type = game_mode())
input('Нажмите Enter для перехода к следующей задаче...') """

# 3. Создайте программу для игры в ""Крестики-нолики"".
# X |   |X
#    |O|
# O|   |O
#[[0,O,X],[0,O,X],[0,O,X]]

print(f'\n____3. Игра в крестики-нолики____\n')

listXO = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

def Enter_XO(player): # ввод строки и столбца от пользователя
    if player == 1: print('Введите через пробел номер строки и номер столбца для ввода X...')
    elif player == 2: print('Введите через пробел номер строки и номер столбца для ввода O...')
    while True:
        lst = input().split(' ')
        if len(lst) == 2:
            if int(lst[0]) in range(1, 4):
                if int(lst[1]) in range(1, 4):
                    if player == 1:
                        lst.append('X')
                        break
                    elif player == 2:
                        lst.append('O')
                        break
                else: print('Такого столбца нет. Повторите ввод...')
            else: print('Такой строки нет. Повторите ввод...')
        else: print('Вы ввели неверное количество данных. Повторите ввод...')
    return lst

def XO_to_table(table, filler): # запись введённого значения в поле игры по координатам
    table[int(filler[0]) - 1][int(filler[1]) - 1] = filler[2]

def Is_exists(XOtable, lst_value): # проверка наличия введённого значения в по его координатам в поле игры
    check = False
    if XOtable[int(lst_value[0]) - 1][int(lst_value[1]) - 1] == 'X' or XOtable[int(lst_value[0]) - 1][int(lst_value[1]) - 1] == 'O':
        check = True
    return check

def Print_XOtable(table): # печать поля игры
    print(f"\n{'  '.join(table[0])}")
    print(f"{'  '.join(table[1])}")
    print(f"{'  '.join(table[2])}\n")

def Is_won(XOtable): # проверка выйгрыша
    win = False
    if XOtable[0][0] == XOtable[1][1] == XOtable[2][2] == 'X' or XOtable[0][0] == XOtable[1][1] == XOtable[2][2] == 'O':
        win = True
        return win
    elif XOtable[2][0] == XOtable[1][1] == XOtable[0][2] == 'X' or XOtable[2][0] == XOtable[1][1] == XOtable[0][2] == 'O':
        win = True
        return win
    else:
        for i in range(0, 3):
            if XOtable[i][0] == XOtable[i][1] == XOtable[i][2] == 'X' or XOtable[i][0] == XOtable[i][1] == XOtable[i][2] == 'O':
                win = True
                return win
            elif XOtable[0][i] == XOtable[1][i] == XOtable[2][i] == 'X' or XOtable[0][i] == XOtable[1][i] == XOtable[2][i] == 'O':
                win = True
                return win
    return win

def GameXO(game_table):
    player = 1
    count = 1
    while True:
        print(f'Ход игрока {player}')

        while True:
            valueXO = Enter_XO(player)
            if not Is_exists(game_table, valueXO):
                XO_to_table(game_table, valueXO)
                break
            else: print('На данной позиции уже есть значение! Повторите ввод...')

        Print_XOtable(game_table)
        if Is_won(game_table):
            print(f'Игрок {player} победил!!!\n')
            return        

        if player == 1: player = 2
        else: player = 1

        count += 1
        if count == 10:
            print('Игра окончена. Ничья!')
            return

GameXO(listXO)

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE => 6A1F2D7C1A17E