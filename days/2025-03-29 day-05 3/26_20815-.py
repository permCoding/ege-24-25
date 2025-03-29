f = open('./26_20815.txt')
k, g = map(int, f.readline().split())

pers = []
for line in f:
    t = list(map(int, line.split()))
    pers.append( (sum(t[1:5]), t[4], t[0]) )
pers.sort(key=lambda x: (-x[0], -x[1], +x[2]))

ppb = 0 if pers[g-1][0] != pers[g][0] else pers[g][0]

cnt = 0
for p in pers:
    if p[0] == ppb:
        cnt += 1
print(cnt)

for pos in range(g-1, 0, -1):
    if pers[pos][0] > ppb:
        print(pers[pos][2])
        break
