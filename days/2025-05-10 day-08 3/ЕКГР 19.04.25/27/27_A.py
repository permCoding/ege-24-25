def dist(pA, pB):
    return ((pA[0]-pB[0])**2 + (pA[1]-pB[1])**2) ** .5


def f(cl):
    minI, minSum = 0, 2**32
    for i in range(len(cl)):
        sumI = sum(dist(cl[i], cl[j]) for j in range(len(cl)))
        if sumI < minSum:
            minI, minSum = i, sumI
    return minI

p = [tuple(map(float, e.split())) for e in open('./27_A_21720.txt')]

clA, clB = [], []
for e in p:
    if e[1] > -1:
        clA.append(e)
    else:
        clB.append(e)
        
mnA = clA[f(clA)]
mnB = clB[f(clB)]

Px = (mnA[0] + mnB[0])/2
print(10000*Px)  # 32540 abs

Py = (mnA[1] + mnB[1])/2
print(10000*Py)  # 13646 abs