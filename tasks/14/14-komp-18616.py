def f(s):
    d = 0
    s = s[::-1]
    p = 0
    while p < len(s):
        z = a.index(s[p])
        d += z*37**p
        p += 1
    return d

    
a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ['
for x in a:
    n1 = f'C59{x}BA98F'
    n2 = f'E3{x}5DA9C6'
    if (f(n1) * f(n2)) % 36 == 0:
        print(f(f'2{x}1'))  # 4071


##a = '0123456789'
##a += ''.join([chr(e) for e in range(65, 92)])
