def f(n):
    b = bin(n)[2:]
    sm = b.count('1')
    b += str(sm%2)
    sm = b.count('1')
    b += str(sm%2)
    return int(b, 2)


t = []
for n in range(1, 100):
    r = f(n)
    if r > 123:
        t.append([r,n])
print(min(t))
