from itertools import product


k = 0
a = '0123456789ab'
for v in product(a, repeat=5):
    if v.count('7') == 1 and v[0] != '0':
        a = v.count('9')
        b = v.count('a')
        c = v.count('b')
        if a+b+c < 4:
            k += 1
print(k)  # 67476

"""
Определите количество 12-ричных пятизначных чисел, в записи которых:
- ровно одна цифра 7 и 
- не более трёх цифр с числовым значением, превышающим 8.
"""