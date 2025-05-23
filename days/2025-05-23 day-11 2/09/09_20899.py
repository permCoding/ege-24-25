k = 0
for e in open('./09_20899.csv'):
    t = sorted(map(int, e.split(';')))
    if t[3] < sum(t[:3]):
        if len(set(t)) == 3:
            k += 1
            print(t)
print(k)
