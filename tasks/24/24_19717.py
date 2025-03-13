# s = 'MLRAERRIEIAGALLRMGLGRMMLEL'
s = open('./24_19717.txt').readline()

cnt = 0
l = 0
mx = 0

for r in range(0, len(s)):
    if s[r] == 'M':
        cnt += 1
    while cnt > 278:
        if s[l] == 'M':
            cnt -= 1
        l += 1
    mx = max(mx, r-l+1)

print(mx)  # 2471
