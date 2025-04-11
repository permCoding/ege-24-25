s = '51I0UBQ09PA700BRJT42HQ04R'
s = open('./24_21421.txt').readline()
mx, p = 0, ''
for q in s:
    if len(p) == 0 and q == '0': continue
    if q in '0123456789AB':
        p += q
        if int(p, 12) % 2 == 0:
            mx = max(mx, len(p))
    else:
        p = ''

print(mx)  # 19
