from itertools import product

k = 0
al = '0123456789AB'
for s in product(al, repeat=5):
    if s[0] != '0' and s.count('7') == 1:
        c9 = s.count('9')
        cA = s.count('A')
        cB = s.count('B')
        if c9 + cA + cB <= 3:
            k += 1
print(k)

"""
Определите количество 12-ричных
пятизначных чисел, в записи которых
ровно одна цифра 7 и
не более трёх цифр с числовым значением,
превышающим 8.
"""
##01
##01234567
##0123456789
##0123456789ABCDEF
##bin()
##oct()
##int()
##hex()
