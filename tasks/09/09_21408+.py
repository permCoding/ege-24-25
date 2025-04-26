t = [list(map(int, e.split(';'))) for e in open('./9_21408.csv')]
k = 0
for e in t:
    st = set(e)
    if len(st) == 3:
        np, pp = 0, 0
        for n in st:
            if e.count(n) == 1:
                np = n
            else:
                pp = max(pp, n)
        if pp > np:
            k += 1

print(k)  # 1
