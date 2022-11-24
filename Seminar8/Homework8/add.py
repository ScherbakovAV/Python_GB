def new_entry(file, id, sirname, name,father_name, phone, spec, city):  # введение новой записи
    with open(file,'a', encoding = 'utf-8') as book:
        book.write(f'{id}, {sirname}, {name}, {father_name}, {phone}, {spec}, {city};\n')