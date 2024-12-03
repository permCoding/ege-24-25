def get7(a):
    res = ''
    while a > 0:
        res = str(a % 7) + res
        a //= 7
    return res

b = 7**170 + 7**100
for x in range(1, 2030+1):
    a = b - x
    r = get7(a)
    if r.count('0') == 71:
        print(x)  # 2029
