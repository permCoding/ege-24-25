def get(points):
    mn, mni = 2**30, 0
    for i in range(len(points)):
        smd = 0
        for j in range(len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            dist = (x2-x1)**2 + (y1-y2)**2
            smd += dist
        if smd < mn:
            mn = smd
            mni = i
    return points[mni]
            

f = open('./demo_2025_27_A.txt')
a, b, c = [], [], []
for line in f:
    line = line.replace(',', '.')
    t = tuple(map(float, line.split('\t')))
    if t[1] < 4:
        a.append(t)
    elif t[0] > 5:
        b.append(t)
    else:
        c.append(t)
f.close()

ax, ay = get(a)
bx, by = get(b)
cx, cy = get(c)

print(ax, ay)
print(bx, by)
print(cx, cy)
print((ax+bx+cx)/3*10_000, (ay+by+cy)/3*10_000)