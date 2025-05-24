f = open('./26_21910.txt')
n = int(f.readline())
t = sorted([int(e) for e in f], reverse=True)

r = [t[0]]
for e in t[1:]:
    if r[-1] - e >= 9:
        r.append(e)
print(len(r), r[-1])

k, a = 1, t[0]
for i in range(1, len(t)):
    if a - t[i] >= 9:
        k += 1
        a = t[i]
print(k, a)  # 1040 57