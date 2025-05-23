s = open('./24_21717.txt').readline().replace('RSQ', '#')

t = []
l, r = 0, 0
k = 0
for r in range(0, len(s)):
    if s[r] == '#': k += 1
    if k == 130: t += [r-l+1]
    while k > 130:
        if s[l] == '#': k -= 1
        l += 1
mn = min(t)
print(mn-130 + 130*3)  # 497
