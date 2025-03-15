k = 0
for line in open('./09-17863.csv'):
    t = [int(e) for e in line.split(';')]
    tp = [e for e in set(t) if t.count(e) == 3]
    pp = [e for e in set(t) if t.count(e) > 1]
    if len(tp) == 1 and len(pp) == 1:
        np = [e for e in t if e != tp[0]]
        if tp[0]*3 > sum(np):
            k += 1
print(k)  # 273


# line = '5;5;45;45;5;12'
# t = [int(e) for e in line.split(';')]
# tp = [e for e in set(t) if t.count(e) == 3]
# np = [e for e in set(t) if t.count(e) > 1]
# print(t, tp, np)
