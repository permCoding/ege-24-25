k = 0
for e in open('./09_10091.csv'):
    t = list(map(int, e.split(';')))
    d = {n:t.count(n) for n in t}
    if sorted(d.values()) == [1, 1, 1, 2, 2]:
        pn = sum(n for n in t if t.count(n) > 1)
        if pn / 4 < sum(t) / 7:
            k += 1
print(k)

# 1 1 1 2 2