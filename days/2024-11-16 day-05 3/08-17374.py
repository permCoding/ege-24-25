from itertools import product

k = 0
for q in product('0123456', repeat=7):
    if q[0] != '0':
        if len([e for e in q if int(e)%2==0])==2:
            k += 1
print(k)  # 75816

"""
Сколько существует семизначных семеричных чисел,
которые содержат в своей записи
ровно две чётные цифры?
"""
