mx = 0
for i,e in enumerate(open('./09_19241.csv'), start=1):
    t = list(map(int, e.split(';')))
    d = {key:t.count(key) for key in t}
    if sorted(d.values()) == [1, 3, 3]:
        pp = sum(n for n in t if t.count(n) > 1)
        np = sum(n for n in t if t.count(n) < 2)
        if pp / 6 < np:
            mx = i
    
print(mx)  # 17975
