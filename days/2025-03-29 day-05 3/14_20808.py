def get(x):
    n = v - x
    t = ''
    while n > 0:
        t = str(n%7) + t
        n //= 7
    return t


v = 7**170 + 7**100
mx = 0
for x in range(2030, 0, -1):
    t = get(x)
    mx = max(mx, t.count('0'))
    if mx == 73:
        print(x)
        break
print(mx)
