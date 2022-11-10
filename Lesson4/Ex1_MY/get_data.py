# Получение данных от виртуальных сенсоров путём построчного извлечения из файла в список дробных чисел

def get_info(file):
    with open(file, 'r', encoding = "utf-8") as data:
        array = []
        index = 0
        for line in data:
            array.append(float(line))
            index += 1
    return array