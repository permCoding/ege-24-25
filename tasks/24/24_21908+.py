s = open('./24_21908.txt').readline()

md = 0
td = 0
for c in s:
    if c in '0123456789ABCD':
        if td == 0 and c == '0': continue
        td += 1
        if c in '02468AC':
            md = max(md, td)
    else:
        td = 0
print(md)  # 2598
