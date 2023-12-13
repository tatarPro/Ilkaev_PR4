from math import pi
rad = int(input("Введите радиус круга: "))
s = round(pi * rad**2)
l = round(2 * pi * rad)
print(f"Площадь: {s}, длина окружности: {l}")