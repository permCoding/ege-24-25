def toDec(s, base):
    al = '0123456789' + ''.join(chr(i) for i in range(65, 92))
    s = s[::-1]
    return sum(al.index(s[i])*base**i for i in range(len(s)))

for p in range(3, 37):
    for s in range(0, 35):
        a = toDec(f'R4', p-1)
        b = toDec(f'B0', s+2)
        c = toDec(f'T3NK4', p)
        if a+b+c == 23593399:
            print(p*s)  # 780
