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

def complex_solve(num_1, num_2, oper = '+'): # нахождение результата выражения из двух комплексных чисел
    result = [0, 0] 

    if oper == '+':
        result[0] = num_1[0] + num_2[0]
        result[1] = num_1[1] + num_2[1]

    elif oper == '-':
        result[0] = num_1[0] - num_2[0]
        result[1] = num_1[1] - num_2[1]

    if oper == '*':
        result[0] = num_1[0] * num_2[0] - num_1[1] * num_2[1]
        result[1] = num_1[0] * num_2[1] + num_1[1] * num_2[0]

    if oper == '/':
        if num_1[1] < 0:
            result[0] = (num_1[0] * num_2[0] + num_1[1] * num_2[1]) / (num_2[0] ** 2 + num_2[1] ** 2)
            result[1] = (num_1[0] * -num_2[1] + num_1[1] * num_2[0]) / (num_2[0] ** 2 + num_2[1] ** 2)
        else:
            result[0] = (num_1[0] * num_2[0] + num_1[1] * num_2[1]) / (num_2[0] ** 2 + num_2[1] ** 2)
            result[1] = (num_1[0] * -num_2[1] + num_1[1] * num_2[0]) / (num_2[0] ** 2 + num_2[1] ** 2)

    return result