t = [list(map(int, e.split(';'))) for e in open('./9_21408.csv')]
k = 0
for e in t:
    d = {n:0 for n in e}
    for n in e:
        d[n] += 1
    if sorted(d.values()) == [1,3,3]:
        print(d)
        np, pp = 0, 0
        for key in d.keys():
            if d[key] == 1:
                np = key
            else:
                pp = max(pp, key)
        if pp > np:
            k += 1

print(k)  # 1
