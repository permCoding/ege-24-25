f = open('./26_21719.txt')
# f = open('./26_test.txt')
n = int(f.readline())
# t = [[int(u) for u in e.split()] for e in f]
t = [tuple(map(int, e.split())) for e in f]
t.sort(key=lambda x: (x[0], x[1]))

st = 0
mx, k = 1, 1
a, b = t[0][0], t[0][1]
for i in range(1, len(t)):
    if t[i][0] == a:
        if t[i][1] == b: continue
        if t[i][1] - b == 2:
            k += 1
            if k > mx:
                mx = k
                st = a
            b = t[i][1]
    else:
        a, b = t[i][0], t[i][1]
        k = 1

print(st, mx)

