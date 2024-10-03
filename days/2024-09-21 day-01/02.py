from math import pi, pow, ceil, floor


R = float(input("Введите радиус круга - "))

S = pi * pow(R, 2)

# до 2-х зн

print(f"Площадь круга равна = {round(S, 2)}")
print(f"Площадь круга равна = {ceil(S)}")
print(f"Площадь круга равна = {floor(S)}")

print(f"Площадь круга равна = {S:.2f}")
print("Площадь круга равна = {:.3f}".format(S))
