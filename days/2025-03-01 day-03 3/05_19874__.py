def _trio(n):
    res = ''
    while n > 0:
        res = str(n%3) + res
        n //= 3
    return res


mn = 10**9
for n in range(10, 200):
    t = _trio(n)
    if n%4 == 0:
        t += t[-3:]
    else:
        t = '1' + t + '20'
    r = int(t, 3)
    if r > 423:
        mn = min(mn, r)
print(mn)
