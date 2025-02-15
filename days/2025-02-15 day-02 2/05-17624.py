for n in range(1, 400):
    b = bin(n)[2:]
    sm = b.count('1')
    b += str(sm%2)
    sm = b.count('1')
    b += str(sm%2)
    r = int(b, 2)
    if r > 75:
        print(n, r)  # 78