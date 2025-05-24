t = [int(e) for e in open('./17_21903.txt')]
x = min(n for n in t if abs(n)%100 == 15 and 99<abs(n)<1000)

lst = []
for i in range(len(t)-2):
    w = t[i:i+3]
    u1 = (w[0]<0 and w[1]<0 and w[2]<0) or (w[0]>=0 and w[1]>=0 and w[2]>=0)
    u2 = min(w) * max(w) > x * x
    if u1 and u2:
        lst.append(min(w) * max(w))

print(len(lst), min(lst))  # 3507 863808
    