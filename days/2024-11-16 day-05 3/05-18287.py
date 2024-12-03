mn = 2**32
for n in range(1, 1999):
    b = bin(n)[2:]
    if len(b)%2 == 0:
        b += '1'
    else:
        b = '1' + b + '0'
    r = int(b, 2)
    if r > 666:
        if r < mn:
            mn = r
            print(mn)  # 1025
