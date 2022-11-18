def reading():
    contacts = [0] * 4
    contacts[0] = input("Введите фамилию: ")
    contacts[1] = input("Введите имя: ")
    contacts[2] = input("Введите Телефон: ")
    contacts[3] = input("Введите описание: ")
    return contacts

def newstring(contacts):
    bazaopen = open("BAZA.txt", "a", encoding = 'utf-8')
    bazaopen.write(contacts + '\n')
    bazaopen.close()
