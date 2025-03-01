def trio(n):
    if n == 0: return '0'
    res = ''
    while n > 0:
        res = str(n%3) + res
        n //= 3
    return res

for n in range(4, 200):
    t = trio(n)
    if t[-2:] == '10':
        t = '2' + t
    else:
        t = '1' + t
    r = int(t, 3)
    if r > 130:
        print(n, r)
        break