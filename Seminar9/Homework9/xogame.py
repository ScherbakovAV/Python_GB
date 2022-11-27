def Is_exists(cell): # Проверка заполнения ячейки игрового поля
    check = False
    if cell['text'] == 'X' or cell['text'] == 'O':
        check = True
    return check

def Is_won(XOtable): # проверка выйгрыша

    if XOtable[0]['text'] == XOtable[4]['text'] == XOtable[8]['text'] == 'X'\
        or XOtable[6]['text'] == XOtable[4]['text'] == XOtable[2]['text'] == 'O'\
        \
        or XOtable[2]['text'] == XOtable[4]['text'] == XOtable[6]['text'] == 'X'\
        or XOtable[8]['text'] == XOtable[4]['text'] == XOtable[0]['text'] == 'O':
        return True
    
    for i in [0, 3, 6]:
        if XOtable[i]['text'] == XOtable[i + 1]['text'] == XOtable[i + 2]['text'] == 'X'\
            or XOtable[i]['text'] == XOtable[i + 1]['text'] == XOtable[i + 2]['text'] == 'O':
            return True

    for i in range(3):
        if XOtable[i]['text'] == XOtable[i + 3]['text'] == XOtable[i + 6]['text'] == 'X'\
            or XOtable[i]['text'] == XOtable[i + 3]['text'] == XOtable[i + 6]['text'] == 'O':
            return True
