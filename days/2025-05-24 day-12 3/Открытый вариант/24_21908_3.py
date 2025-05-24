s = open('./24_21908.txt').readline()

al = ''.join([chr(i) for i in range(69,91)])
ch = '02468AC'

md, td = 0, 0
for c in s:
    if c not in al:
        if td == 0 and c == '0': continue
        td += 1
        if c in ch:
            md = max(md, td)
    else:
        td = 0

print(md)  # 2598
    