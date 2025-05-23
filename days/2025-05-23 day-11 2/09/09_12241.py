k = 0
for e in open('./09_12241.csv'):
    t = list(map(int, e.split(';')))
    d = {n:t.count(n) for n in t}
    if sorted(d.values()) == [1, 2, 2, 2]:
        pp = [n for n in t if t.count(n) > 1]
        np = [n for n in t if t.count(n) < 2]
        if (min(pp)+max(pp)) / 2 < np[0]:
            k += 1

print(k)
