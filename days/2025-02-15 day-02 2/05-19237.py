def trio(n):
    t = ''
    while n > 0:
        ost = n%3
        n //= 3
        t = str(ost) + t
    return t

for n in range(1, 400):
    t = trio(n)
    if n%3 == 0:
        t += t[-2:]
    else:
        t += trio(sum(int(e) for e in t))
    r = int(t, 3)
    if r%2 == 0 and r > 220:
        print(n, r)  # 222
