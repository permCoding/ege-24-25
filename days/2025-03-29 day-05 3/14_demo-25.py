def get(x):
    n = v - x
    t = ''
    while n > 0:
        t = str(n%7) + t
        n //= 7
    return t


v = 7**170 + 7**100
for x in range(2030, 0, -1):
    t = get(x)
    if t.count('0') == 71:
        print(x)  # 2029
        break