s = open('./24_21421.txt').readline()
# s = '00I0UBQ09P000700A132RJT42HQ04R3XV'

al = '0123456789AB'

mx, tmp = 0, ''
for ch in s:
    if tmp == '' and ch == '0': continue
    if ch in al:  # 12-ричное
        tmp += ch
        if int(tmp, 12) % 2 == 0:  # чётное
            mx = max(mx, len(tmp))
    else:
        tmp = ''

print(mx)
