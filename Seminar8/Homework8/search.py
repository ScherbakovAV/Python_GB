def search_from_id(file, id): # поиск первой записи в базе по id (точное совпадение) 

    id = str(id)
    temp_list = []
    check = 0

    with open(file, 'r', encoding="utf-8") as data:
            for line in data:
                temp_list = line.replace('\n', '').replace(',', '').split()
                if id == temp_list[0]:
                    check = 1
                    return line
            
            if check == 0: return False
    

def search_all_entry(file, for_find): # поиск и вывод всех вхождений в базе 

    for_find = str(for_find).lower()
    find_strings = ''
    check = 0

    with open(file, 'r', encoding="utf-8") as data:
            for line in data:
                if for_find in line.lower():
                    find_strings += line + '\n'
                    check = 1
            
    if check == 0: return False
    else: return find_strings
