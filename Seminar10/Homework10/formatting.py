def format_complex(string): # преобразование комплексного числа из строки в список строк и оператора
    print(string, end = ' -> ')
    compl = [0, 0]
    temp = []

    if string[0] == '-':
        
        string = string[1:]

        if 'i' in string:
            if '+' in string:
                temp = string.replace(' ', '').split('+')

                if 'i' in temp[0]:
                    if temp[0].replace('i', '') == '':
                        compl[0] = float(temp[1])
                        compl[1] = -float(1)
                else:
                    compl[0] = -float(temp[0]) 

                    if temp[1].replace('i', '') == '': compl[1] = float(1)
                    else: compl[1] = float(temp[1].replace('i', ''))
                
            elif '-' in string:
                temp = string.replace(' ', '').split('-')

                if 'i' in temp[0]:
                    if element.replace('i', '') == '':
                        compl[0] = -float(temp[1])
                        compl[1] = float(1)
                else:
                    compl[0] = -float(temp[0]) 

                    if temp[1].replace('i', '') == '': compl[1] = float(-1)
                    else: compl[1] = -float(temp[1].replace('i', ''))

            else:
                if string.replace('i', '') == '': compl[1] = -float(1)
                else: compl[1] = -float(string.replace('i', ''))
                
        else: compl[0] = -float(string)

    else:
        if 'i' in string:
            if '+' in string:
                temp = string.replace(' ', '').split('+')

                for element in temp:
                    if 'i' in element:
                        if element.replace('i', '') == '': compl[1] = float(1)
                        else: compl[1] = float(element.replace('i', ''))
                    else: compl[0] = float(element)
                
            elif '-' in string:
                temp = string.replace(' ', '').split('-')

                if 'i' in temp[0]:
                    if element.replace('i', '') == '':
                        compl[0] = float(temp[1])
                        compl[1] = float(1)
                else:
                    compl[0] = float(temp[0])

                    if temp[1].replace('i', '') == '': compl[1] = float(-1)
                    else: compl[1] = -float(temp[1].replace('i', ''))

            else:
                if string.replace('i', '') == '': compl[1] = float(1)
                else: compl[1] = float(string.replace('i', ''))
                
        else: compl[0] = float(string)
   
    return compl

def complex_to_string(complex_list): # обратное преобразование списка комплексного числа в строку для вывода на печать

    if complex_list[0] != 0 and complex_list[1] != 0:

        if complex_list[0] % 1 == 0: real = int(complex_list[0])
        else: real = round(complex_list[0], 3) 

        if complex_list[1] % 1 == 0: imagine = int(complex_list[1])
        else: imagine = round(complex_list[1], 3)

        if complex_list[1] >= 0:
            if complex_list[1] == 1: return f'{real} + i'
            else: return f'{real} + {imagine}i'
        else:
            if complex_list[1] == -1: return f'{real} - i'
            else: return f'{real} - {-imagine}i'
    
    elif complex_list[0] == 0 and complex_list[1] != 0:

        if complex_list[1] % 1 == 0: imagine = int(complex_list[1])
        else: imagine = round(complex_list[1], 3)
        
        return f'{imagine}i'
    
    elif complex_list[0] != 0 and complex_list[1] == 0:

        if complex_list[0] % 1 == 0: real = int(complex_list[0])
        else: real = round(complex_list[0], 3) 
        
        return f'{real}'

def format_real(line): # преобразование введённого строчного выражения в список чисел и операторов

    line = line.replace(',', '.')
    math_list = []
    temp = ''

    for symbol in line:     
        if symbol.isdigit() or symbol == '.': temp += symbol

        elif symbol in ['*', '/', '+', '-']:
            if temp != '': math_list.append(float(temp))
            math_list.append(symbol)
            temp = ''
        
        elif symbol == ' ': continue

    math_list.append(float(temp))
    if math_list[0] == '': math_list.pop(0)

    return math_list
