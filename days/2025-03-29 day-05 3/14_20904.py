def get(x):
    n = v - x
    t = ''
    while n > 0:
        t = str(n%3) + t
        n //= 3
    return t


v = 3**100
for x in range(2030, 0, -1):
    t = get(x)
    if t.count('0') == 1:
        print(x)  # 1823
        break