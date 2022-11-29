def format_complex(string):
    print(string, end = ' -> ')
    compl = [''] * 2
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

""" print(format_complex('15 + 8i'))
print(format_complex('-15 + 8i'))
print(format_complex('8i + 15'))
print(format_complex('15 - 8i'))
print(format_complex('-15 - 8i'))
print(format_complex('i + 15'))
print(format_complex('-i + 15'))
print(format_complex('15 - i'))
print(format_complex('15'))
print(format_complex('-15'))
print(format_complex('8i'))
print(format_complex('-8i'))
print(format_complex('i'))
print(format_complex('-i')) """

def str_to_mathlist(line): # преобразование введённого строчного выражения в список чисел и операторов

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

def real_solve(math): # нахождение результата выражения из списка чисел и операторов

    i = 0
    while '*' in math or '/' in math:
        if math[i] == '*' or math[i] == '/':
            if math[i] == '*': math[i] = math[i - 1] * math[i + 1]
            elif math[i] == '/': math[i] = math[i - 1] / math[i + 1]
            math.pop(i + 1)
            math.pop(i - 1)
        else: i += 1

    if math[0] == '-':
        math[1] = - math[1]
        math.pop(0)
    
    i = 0    
    while '+' in math or '-' in math:
        if math[i] == '+' or math[i] == '-':
            if math[i] == '+': math[i] = math[i - 1] + math[i + 1]
            elif math[i] == '-': math[i] = math[i - 1] - math[i + 1]
            math.pop(i + 1)
            math.pop(i - 1)
        else: i += 1
    
    if math[0] % 1 == 0: math[0] = int(math[0])
    return math[0]

""" a = '24/2*3+30'
b = '-8+5.2 -2,4/1 - 0.21 * 2'
c = '1+5-7+5*4'
d = '1*2*3/2'
string_lst = str_to_mathlist(d)
print(string_lst)
print(real_solve(string_lst)) """
