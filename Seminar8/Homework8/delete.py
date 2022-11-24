def delete_str(file, string):  # удаление строки с первым вхождением

    lines = ''
    is_unique = False
    
    with open(file, 'r', encoding="utf-8") as data:
            for line in data:
                if not str(string) in line and not is_unique: lines += line
                elif str(string) in line and is_unique: lines += line
                else: is_unique = True

    with open(file, 'w', encoding="utf-8") as data:
            data.writelines(lines)
