def dist(pA, pB):
    return ((pA[0]-pB[0])**2 + (pA[1]-pB[1])**2) ** .5


def f(cl):
    minI, minSum = 0, 2**32
    for i in range(len(cl)):
        sumI = sum(dist(cl[i], cl[j]) for j in range(len(cl)))
        if sumI < minSum:
            minI, minSum = i, sumI
    return minI

p = [tuple(map(float, e.split())) for e in open('./27_B_21720.txt')]

clA, clB, clC = [], [], []
for e in p:
    if e[1] < 0:
        clA.append(e)
    elif e[0] > -6:
        clB.append(e)
    else:
        clC.append(e)
        
mnA = clA[f(clA)]
mnB = clB[f(clB)]
mnC = clC[f(clC)]

Px = (mnA[0] + mnB[0] + mnC[0])/3
print(10000*Px)  # 47031

Py = (mnA[1] + mnB[1] + mnC[1])/3
print(10000*Py)  # 25263