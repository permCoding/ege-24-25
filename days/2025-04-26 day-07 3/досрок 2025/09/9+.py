t = [list(map(int, e.split(';'))) for e in open('./9_21408.csv')]

amount = 0
for e in t:
    st = set(e)
    if len(st) == 3 and sorted(e.count(n) for n in st) == [1,3,3]:
        nn = [k for k in st if e.count(k) == 1][0]
        pp = max(k for k in st if e.count(k) == 3)
        if pp > nn:
            amount += 1

print(amount)  # 1
