f = open('./26_21719.txt')
n = int(f.readline())
t = [tuple(map(int, e.split())) for e in f]
t.sort(key=lambda x: (x[0], x[1]))


s, m, k = 0, 1, 1
a, b = t[0][0], t[0][1]
for i in range(1, len(t)):
    if t[i][0] == a:
        if t[i][1] == b: continue
        if t[i][1] - b == 2:
            k += 1
            if k > m:
                m = k
                s = a
            b = t[i][1]
    else:
        a, b = t[i][0], t[i][1]
        k = 1

print(s, m)  # 10135 42
