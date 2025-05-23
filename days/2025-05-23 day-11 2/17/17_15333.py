t = [int(e) for e in open('./17_15333.txt')]
x = max(n for n in t if n%19==0)

k, lst = 0, []
for i in range(len(t)-1):
    if t[i]>x or t[i+1]>x:
        k += 1
        lst.append(t[i]+t[i+1])

print(k, max(lst))  # 54 174513
