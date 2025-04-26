def trio(dec):
    res = ''
    while dec > 0:
        res = str(dec % 3) + res
        dec //= 3
    return res

for n in range(999, 2, -1):
    res = trio(n)
    res += res[-2:] if n%3 == 0 else trio((n%3) * 3)
    if int(res, 3) <= 150:
        print(n)
        break
    