t = [int(e) for e in open('./17_21712.txt')]

mp = min(e for e in t if e > 0 and e%10==6 and 999<e<10000)

k, mx = 0, -300_000
for i in range(len(t)-2):
    p = t[i:i+3]
    u1 = sum(1 for e in p if abs(e)%10==6 and 999<abs(e)<10000) == 1
    u2 = sum(p) <= mp
    if u1 and u2:
        k += 1
        mx = max(mx, sum(p))

print(k, mx)  # 507 1042
