def get(n, base=7):
    r = ''
    while n > 0:
        o = n%base
        n //= base
        r = str(o) + r
    return r

for x in range(0, 2031):
    n = 7**170 + 7**100 - x
    w = get(n)
    if w.count('0') == 71:
        print(x)  # 2029
