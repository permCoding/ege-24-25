def f(s, w):
    d = 0
    s = s[::-1]
    p = 0
    while p < len(s):
        z = a.index(s[p])
        d += z * w**p
        p += 1
    return d

    
a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ['  # 36

for p in range(2, 37):
    for s in range(2, 35):
        n1 = 'R4'
        n2 = 'B0'
        n3 = 'T3NK4'
        if f(n1, p-1) + f(n2, s+2) + f(n3, p) == 23593399:
            print(p*s)
            break

##a = '0123456789'
##a += ''.join([chr(e) for e in range(65, 92)])
