def dist(a ,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2) **.5

def get(cl):
    iMin, dMin = 0, 2**32
    for i in range(0, len(cl)):
        sm = 0
        for j in range(0, len(cl)):
            sm += dist(cl[i], cl[j])
        if sm < dMin:
            iMin = i
            dMin = sm
    return cl[iMin]

clA, clB = [], []
for e in open('./27_A_21911.txt'):
    t = tuple(map(float, e.split()))
    if t[1] > 3:
        clA.append(t)
    else:
        clB.append(t)


cA = get(clA)
cB = get(clB)

print((cA[0]+cB[0])/2 * 10_000)  # 26216
print((cA[1]+cB[1])/2 * 10_000)  # 24182
