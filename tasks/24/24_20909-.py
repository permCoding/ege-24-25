s = open('./24_20909.txt').readline().replace('AB', '#')
s = 'ABABFFAB'.replace('AB', '#')
g = 3 # 100
t = []
l, k = 0, 0
for r in range(0, len(s)):
    if s[r] == '#': k += 1
    if k == g:
        ln = r-l+1
        t += [ln]
    while k > g:
        if s[l] == '#': k -= 1
        l += 1

m = max(t)
print(m+g)  # 748 - а должно быть => 750
