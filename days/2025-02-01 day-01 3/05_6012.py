def f(n):
    b = bin(n)[2:]
    sm = b.count('1')
    if sm%2 == 0:
        b = '1' + b[2:] + '0'
    else:
        b = '11' + b[2:] + '1'
    return int(b, 2)

print(min((f(n),n) for n in range(1, 88) if f(n) > 49))
