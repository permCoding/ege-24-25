from re import finditer

# s = 'q.eavncagwt@jhfg.www.qiezkigg@laazznchleqyy@d.eyh@b'
s = open('./24_19969.txt').readline()

reg = r'([a-z]+@[a-z]+\.[a-z]+)'


mx_len = 0
for match in finditer(reg, s):  # совпадения
    m = match.group()
    # print(m)
    mx_len = max(mx_len, len(m))

print(mx_len)
