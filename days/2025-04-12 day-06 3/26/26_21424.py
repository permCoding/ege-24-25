f = open('./26_21424.txt')
f.readline()
t = sorted([int(s) for s in f], reverse=True)

v = [t[0]]
for e in t[1:]:
    if v[-1] - e >= 9:
        v += [e]
print(len(v), v[-1])
