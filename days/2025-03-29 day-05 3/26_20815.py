f = open('./26_20815.txt')
k, g = map(int, f.readline().split())

pers = []
for line in f:
    t = list(map(int, line.split()))
    pers.append({'id':t[0], 'sm':sum(t[1:5]), 'so':t[4]})

pers.sort(key=lambda x: (-x['sm'], -x['so'], +x['id']))

ppb = 0 if pers[g-1]['sm'] != pers[g]['sm'] else pers[g]['sm']

cnt = sum(1 for p in pers if p['sm'] == ppb)
print(cnt)

for pos in range(g-1, 0, -1):
    if pers[pos]['sm'] > ppb:
        print(pers[pos]['id'])
        break
