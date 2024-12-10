al = '0123456789' + ''.join(chr(i) for i in range(65,75))
amount = 0
for a in al[1:]:
    for b in al:
        for c in al:
            for d in al:
                for e in al:
                    if al.index(a) + al.index(e) == 26:
                        n = (a,b,c,d,e)
                        if all(al.index(n[i])%2!=al.index(n[i+1])%2 for i in range(4)):
                            amount += 1
print(amount)

"""
10000

в записи которых 
четные и нечетные цифры чередуются и 
сумма числовых значений крайних цифр данного числа равна 26


"""