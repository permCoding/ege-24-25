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

t = [list(map(float, s.replace(',','.').split())) for s in open("./27_A_21911.txt")]
tA, tB = [], []
for e in t:
    if e[1] > 2:
        tA.append(e)
    else:
        tB.append(e)

mnA = tA[f(tA)]
mnB = tB[f(tB)]
print(mnA)
print(mnB)
avgX = (mnA[0]+mnB[0])/2
avgY = (mnA[1]+mnB[1])/2
print(avgX*10_000, avgY*10_000)

# A 26216 24182
# B 150891 63754