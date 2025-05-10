s = open('./24_21717.txt').readline()
# s = 'RSQFRSQRSQF'
s = s.replace('RSQ', '#')

cnt = 130
t = []
k = 0
l, r = 0, 0
for r in range(len(s)):
    if s[r] == '#': k += 1
    if k == cnt: t.append(r-l+1)
    while k > 130:
        if s[l] == '#': k -= 1
        l += 1

ln = min(t)
print(cnt*3 + ln-cnt)  # 497

'RSQRS'
'RSQR'
'RSQ'
'RSQRSQ'