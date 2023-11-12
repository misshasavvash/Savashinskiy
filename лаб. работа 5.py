alfavit = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
ALFAVIT = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
sdvig = int(input('Шаг шифровки от 1 до 33: ')) % 33
stroka = input("Сообщение для Дешифровки: ")
result = ''
for i in stroka:
    mesto = alfavit.find(i)
    mestO = ALFAVIT.find(i)
    new_mesto = mesto + sdvig
    new_mestO = mestO + sdvig
    if i in alfavit:
        result += alfavit[new_mesto]
    elif i in ALFAVIT:
        result += ALFAVIT[new_mestO]
    else:
        result += i
print(result)
