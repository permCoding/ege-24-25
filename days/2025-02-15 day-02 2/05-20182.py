def trio(n):
    t, sm = '', 0
    while n > 0:
        ost = n%3
        n //= 3
        t = str(ost) + t
        sm += ost
    return t, sm


for n in range(1, 200):
    t, sm = trio(n)
    if sm%2 == 0:
        t = '12' + t[2:] + '0'
    else:
        t = '10' + t[2:] + '2'
    r = int(t, 3)
    if r > 105:
        print(n, r)
        break
