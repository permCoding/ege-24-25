def f(n):
    return len(str(abs(n)))==5 and str(n)[-2:]=='43'

t = [int(e) for e in open('./17_19249.txt')]
x = max(n for n in t if f(n))

k, lst = 0, []
for i in range(len(t)-2):
    w = t[i:i+3]
    if f(w[0]) or f(w[1]) or f(w[2]):
        sm = w[0]**2+w[1]**2+w[2]**2
        if sm <= x**2:
            k += 1
            lst.append(sm)

print(k, min(lst))  # 92 838850571
