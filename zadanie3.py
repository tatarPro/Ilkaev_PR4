from math import pi
from math import sqrt
rad = int(input("Введите радиус круга: "))
s = round(pi * rad**2)
l = round(2 * pi * rad)
print(f"Площадь: {s}, длина окружности: {l}")
kvadrat = input("Введите 1 если квадрат описанный или 2 если вписанный")
if kvadrat == "1":
    stor = rad * 2
    skvad = stor ** 2
    pkvad = stor * 4
    print(f"Площадь: {skvad}, периметр: {pkvad}")
elif kvadrat == "2":
    stor = rad / sqrt(2)
    skvad = stor ** 2
    pkvad = stor * 4
    print(f"Площадь: {skvad}, периметр: {pkvad}")
else:
    print("Error")