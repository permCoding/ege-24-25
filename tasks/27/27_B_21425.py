def r(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**.5

def f(t_):
    mnR, mnI = 2**32, 0
    for i in range(0, len(t_)):
        mnT = 0
        for j in range(0, len(t_)):
            if i != j:
                mnT += r(t_[i], t_[j])
        if mnT < mnR:
            mnR = mnT
            mnI = i
    return mnI

t = [list(map(float, s.replace(',','.').split())) for s in open("./27_B_21425.txt")]
tA, tB, tC = [], [], []
for e in t:
    if e[1] > 10:
        tA.append(e)
    elif e[0] < 5:
        tB.append(e)
    else:
        tC.append(e)

mnA = tA[f(tA)]
mnB = tB[f(tB)]
mnC = tC[f(tC)]
print(mnA)
print(mnB)
print(mnC)
avgX = (mnA[0]+mnB[0]+mnC[0])/3
avgY = (mnA[1]+mnB[1]+mnC[1])/3
print(avgX*10_000, avgY*10_000)

# A 167990 73043
# B 122627 29105