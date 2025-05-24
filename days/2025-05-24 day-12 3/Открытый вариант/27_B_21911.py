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

clA, clB, clC = [], [], []
for e in open('./27_B_21911.txt'):
    t = tuple(map(float, e.split()))
    if t[0] < 10:
        clA.append(t)
    elif t[1] > 6:
        clB.append(t)
    else:
        clC.append(t)

cA = get(clA)
cB = get(clB)
cC = get(clC)

print((cA[0]+cB[0]+cC[0])/3 * 10_000)  # 150891
print((cA[1]+cB[1]+cC[1])/3 * 10_000)  # 63754
