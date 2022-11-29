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

