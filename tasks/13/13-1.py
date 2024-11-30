b1 = 172
b2 = 30
print(f"{b1:b}")
print(f"{b2:b}")

print(30 & 254)
print(f'{30:b}')


k = 8

amount = 0
for i in range(0, 2**17):
    s = f"{i:b}"
    if (k + s.count('1')) % 12 != 0:  # 128674
    # if not(s.count('1') == 4 or s.count('1') == 16):  # 128674
        amount += 1
print(amount)  # ответ в яндексе 128675

"""
Сеть задана IP-адресом 172.30.0.0 и маской сети 255.254.0.0. Сколько в этой сети IP-адресов, для которых количество единиц в двоичной записи IP-адреса не  кратно 12?

https://education.yandex.ru/ege/task/380757d9-1361-41c9-b23d-f25fc5439be8
"""