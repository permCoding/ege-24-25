k = 0
for e in open('./09_17863.csv'):
    t = list(map(int, e.split(';')))
    pn = {n: t.count(n) for n in t}
    if sorted(pn.values()) == [1, 1, 1, 3]:
        sm = sum(w for w in t if t.count(w) == 1)
        if sum(t) > 2*sm:
            k += 1

print(k)  # 273

# 1 2 3 5 5 5
# 1 2 3 3 4 4
# t = [1, 5, 3, 5, 2, 5]
# t = [1, 2, 3, 3, 4, 4]
# pn = {n: t.count(n) for n in t}
# print(pn)
# print(sorted(pn.values()) == [1, 1, 1, 3])
# print(pn.keys())