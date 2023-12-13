from math import sqrt
from math import pi
a = int(input("Введите первые координаты первой точки "))
a2 = int(input("Введите вторые координаты первой точки "))
b = int(input("Введите первые координаты второй точки "))
b2 = int(input("Введите вторые координаты второй точки "))
c = sqrt((a-a2)**2+(b-b2)**2)
print('Ответ: ', c)
stor = int(input("Введите боковую сторону трапеции"))
bol = int(input("Введите большее основание трапеции"))
mal = int(input("Введите большее основание трапеции"))
l = round(2 * pi * c)
s = round(pi * c**2)
strap = c**2
ptrap = bol + mal + stor + stor
print(f"Площадь круга: {s}, длина окружности: {l}, площадь трапеции {strap}, периметр трапеции {ptrap}")