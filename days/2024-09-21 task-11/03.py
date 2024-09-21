from math import pi, pow, ceil, floor


def get_sqr_circle(R):
    return pi * pow(R, 2)


R = float(input("Введите радиус круга - "))
K = int(input("Введите кол-во знаков после зап - "))
print(f"Площадь круга равна = {round(get_sqr_circle(R), K)}")
