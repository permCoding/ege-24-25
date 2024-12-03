al = '0123456789AB'
k = 0
for e1 in al[1:]:
    for e2 in al:
        for e3 in al:
            for e4 in al:
                for e5 in al:
                    s = e1+e2+e3+e4+e5
                    if s.count('7') == 1:
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
