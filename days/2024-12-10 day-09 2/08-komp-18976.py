al = '0123456789' + ''.join(chr(i) for i in range(65,75))
amount = 0
for a in al[1:]:
    for b in al:
        for c in al:
            for d in al:
                for e in al:
                    if al.index(a) + al.index(e) == 26:
                        u1 = al.index(a)%2!=al.index(b)%2
                        u2 = al.index(b)%2!=al.index(c)%2
                        u3 = al.index(c)%2!=al.index(d)%2
                        u4 = al.index(d)%2!=al.index(e)%2
                        if all([u1,u2,u3,u4]):
                            amount += 1
print(amount)

"""
10000

в записи которых 
четные и нечетные цифры чередуются и 
сумма числовых значений крайних цифр данного числа равна 26


"""