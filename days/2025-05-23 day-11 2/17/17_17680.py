t = [int(n) for n in open('./17_17680.txt')]
x = min(n for n in t if n>0 and n%41==0)

k, lst = 0, []
for i in range(len(t)-1):
    if t[i] != t[i+1]:
        if abs(t[i]-t[i+1]) % x == 0:
            k += 1
            lst.append(t[i]+t[i+1])

print(k, max(lst))  # 10 92404
