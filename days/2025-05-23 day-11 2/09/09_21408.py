amount = 0
for e in open('./09_21408.csv'):
    t = list(map(int, e.split(';')))
    pn, nn = set(), set()
    for n in t:
        if t.count(n) > 1:
            pn.add(n)
        else:
            nn.add(n)
    if len(pn) == 2 and len(nn) == 1:
        a, b = list(pn), list(nn)
        if t.count(a[0]) == 3 and max(a) > b[0]:
                amount += 1
                print(t)
print(amount)  # 1
