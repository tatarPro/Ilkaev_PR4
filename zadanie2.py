from math import sqrt
from math import pi
a = int(input("Введите сторону квадрата"))
s = a**2
p = a * 4
d = a * sqrt(2)
print(f"Площадь: {s}, периметр: {p}, диагональ: {d}")
okruzh = input("Введите 1 если окружность описанная или 2 если вписанная")
if okruzh == "1":
    sokr = round(pi * (d/2)**2)
    l = round(pi * (d/2) * 2)
    stortreu = (d/2) * sqrt(3)
    streu = ((stortreu**2) * sqrt(3)) / 4
    print(f"Площадь описанной вокруг квадрата окружности равна: {sokr}, длина окружности: {l}, площадь треугольника: {streu}")
elif okruzh == "2":
    sokr = round(pi) * (a/2)**2
    l = round(pi * (a/2) * 2)
    osno = int(input("Введите основание"))
    h = (a/2) * 3
    streu = (h * osno) / 2
    print(f"Площадь описанной вокруг квадрата окружности равна: {sokr}, длина окружности: {l}, площадь треугольника: {streu}")
else:
    print("Ошибка")
