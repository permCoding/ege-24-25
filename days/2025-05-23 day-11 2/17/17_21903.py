t = [int(e) for e in open('./17_21903.txt')]

x = min(n for n in t if len(str(abs(n)))==3 and str(abs(n))[-2:]=='15')

k, lst = 0, []
for i in range(len(t)-2):  # len(t)-3
    w = t[i:i+3]
    if abs(sum((-1 if n<0 else 1) for n in w)) == 3:
        if min(w) * max(w) > x*x:
            k += 1
            lst.append(min(w) * max(w))

print(k, min(lst))  # 3507 863808
