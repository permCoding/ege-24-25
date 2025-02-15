def trio(n):
    t = ''
    while n > 0:
        ost = n%3
        n //= 3
        t = str(ost) + t
    return t

    
def get(n):
    t = trio(n)
    t = t \
        .replace('2','#') \
        .replace('0','2') \
        .replace('#','0')
    r = int(t, 3)
    return abs(n-r)


for n in range(1, 1_000):
    # print(n, get(n))
    if get(n) == 378:
        print(n)
        break
