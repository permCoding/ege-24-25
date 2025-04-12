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


pairs = [list(map(float, s.replace(',','.').split())) for s in open('./27_B_21425.txt')]

k1, k2, k3 = [], [], []
for pair in pairs:
    if pair[1] > 10:
        k1.append(pair)
    elif pair[0] > 10:
        k2.append(pair)
    else:
        k3.append(pair)

mnT1, mnT2, mnT3 = f(k1), f(k2), f(k3)

print((mnT1[0]+mnT2[0]+mnT3[0])/3*10_000)  # 122627
print((mnT1[1]+mnT2[1]+mnT3[1])/3*10_000)  # 29105