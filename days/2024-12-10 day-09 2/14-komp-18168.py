def to5(dec):
    res = ''
    while dec > 0:
        res = str(dec%5) + res
        dec //= 5
    return res

cnt4 = 0
for x in range(10, 70_001):
    if x % 1000 == 0: print(x)
    v = to5(5**2025 + 5**400 - x)
    cnt = v.count('4')
    if cnt >= cnt4:
        print(f'x = {x} {cnt}')  # x = 62501 399
        cnt4 = cnt
