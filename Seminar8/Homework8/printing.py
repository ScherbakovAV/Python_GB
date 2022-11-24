def print_base(file):  # вывод базы данных на печать
    message = ''

    with open(file, encoding="utf-8") as data:
        for line in data:
            message += 'id-' + line + '\n'

    return message