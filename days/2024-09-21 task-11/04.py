from module import get_sqr_circle as get


R = float(input("Введите радиус круга - "))
K = int(input("Введите кол-во знаков после зап - "))
print(f"Площадь круга равна = {round(get(R), K)}")
