def dist(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**.5


def f(kl):
    smA, mnI = 2**24, 0
    for i in range(len(kl)):
        smI = 0
        for j in range(len(kl)):
            smI += dist(kl[i], kl[j])
        if smI < smA:
            smA = smI
            mnI = i
    return kl[mnI]


pairs = [list(map(float, s.replace(',','.').split())) for s in open('./27_A_21425.txt')]

k1, k2 = [], []
for pair in pairs:
    if pair[1] > 10:
        k1.append(pair)
    else:
        k2.append(pair)

mnT1, mnT2 = f(k1), f(k2)

print((mnT1[0]+mnT2[0])/2*10_000)  # 167990
print((mnT1[1]+mnT2[1])/2*10_000)  # 73043