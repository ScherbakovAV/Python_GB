def sort_file_to_list(file, sort_by = 0):
    lines = []
    line_to_list = []

    with open(file, 'r', encoding="utf-8") as data:
        for line in data:
            line_to_list = line.replace('id-', '').split(', ')
            lines.append(line_to_list)
  
    return sorted(lines, key = lambda field: field[sort_by])


def write_base_from_list(file, lst):
    with open(file,'w', encoding = 'utf-8') as data:
        for index in range(len(lst)):
            data.write(", ".join(lst[index]))