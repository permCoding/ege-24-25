# f = open('./26_20815_.txt')
f = open('./26_20815.txt')
k, g = map(int, f.readline().split())

pers = []
for line in f:
    t = list(map(int, line.split()))
    _id = t[0]
    _sm = sum(t[1:5])
    _so = t[4]
    pers.append( (_sm, _so, _id) )
pers.sort(key=lambda x: (-x[0], -x[1], +x[2]))

# for p in pers: print(p)

ppb = 0
if pers[g-1][0] == pers[g][0]:
    ppb = pers[g][0]
# print(ppb)

cnt = 0
for p in pers:
    if p[0] == ppb:
        cnt += 1
print(cnt)

for pos in range(g-1, 0, -1):
    if pers[pos][0] > ppb:
        print(pers[pos][2])
        break
