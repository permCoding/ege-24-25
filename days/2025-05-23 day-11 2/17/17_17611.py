def f(n):
    return str(n)[-1]=='7' and len(str(abs(n)))==4

t = [int(e) for e in open('./17_17611.txt')]
x = max(n for n in t if f(n))

k, lst = 0, []
for i in range(len(t)-2):
    w = t[i:i+3]
    if sum(1 for n in w if f(n)) > 1:
        if sum(w) > x:
            k += 1
            lst.append(sum(w))

print(k, max(lst))  # 6 84385
