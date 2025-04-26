t = [list(map(int, e.split(';'))) for e in open('./9_21408.csv')]

amount = 0
for e in t:
    st = set(e)
    if len(st) == 3 and sorted(e.count(n) for n in st) == [1,3,3]:
        np, pp = 0, 0
        for k in st:
            if e.count(k) == 1:
                nn = k
            else:
                pp = max(pp, k)
        if pp > nn:
            amount += 1

print(amount)  # 1
