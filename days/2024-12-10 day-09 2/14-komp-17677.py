def to6(dec):
    res = ''
    while dec > 0:
        res = str(dec%6) + res
        dec //= 6
    return res

for x in range(1, 2031):
    v = to6(6**260 + 6**160 + 6**60 - x)
    if v.count('0') == 202:
        print(x)  # 1944
