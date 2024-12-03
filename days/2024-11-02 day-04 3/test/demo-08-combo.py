k = 0
al = '0123456789ab'
for e1 in al[1:]:
    for e2 in al:
        for e3 in al:
            for e4 in al:
                for e5 in al:
                    v = e1+e2+e3+e4+e5
                    if v.count('7') == 1:
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