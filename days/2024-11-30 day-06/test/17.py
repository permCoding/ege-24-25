t = [int(w) for w in open('./17.txt')]
m = min(e for e in t if e%2025==0)
print(len(t), m)
k, mx = 0, 0
for i in range(len(t)-2):
    if t[i]%m==0 or t[i+1]%m==0 or t[i+2]%m==0:
        if 100000<=t[i]+t[i+1]+t[i+2]<=999999:
            k += 1
            mx = max(mx, t[i]+t[i+1]+t[i+2])
print(k, mx)
