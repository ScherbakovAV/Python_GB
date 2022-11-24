def edit_entry(file, id, index, replacer): # изменение строки

    lines = []
    temp_list = []
    is_unique = False
    
    with open(file, 'r', encoding="utf-8") as data:
        for line in data:
            temp_list = line.replace('id-', '').split(', ')

            if str(id) != temp_list[0] and not is_unique: lines += line
            elif str(id) == temp_list[0] and is_unique: lines += line
            else:
                if int(index) == 7:
                    temp_list[int(index) - 1] = replacer
                    line = ", ".join(temp_list)
                    lines += line + ';\n'
                else:
                    temp_list[int(index) - 1] = replacer
                    line = ", ".join(temp_list)
                    lines += line

    with open(file, 'w', encoding="utf-8") as data:
            data.writelines(lines)         
    
    return