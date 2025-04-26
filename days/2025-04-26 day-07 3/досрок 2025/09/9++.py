t = [list(map(int, e.split(';'))) for e in open('./9_21408.csv')]

amount = 0
for e in t:
    d = {n:e.count(n) for n in e}
    if sorted(d.values()) == [1,3,3]:
        nn, pp = 0, 0
        for key in d.keys():
            if d[key] == 1:
                nn = key
            else:
                pp = max(pp, key)
        if pp > nn:
            amount += 1

print(amount)
