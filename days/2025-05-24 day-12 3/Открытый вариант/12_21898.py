for n in range(4, 10_000):
    s = '1' + n * '9'
    while ('19' in s) or ('399' in s) or ('999' in s):
        if '19' in s: s = s.replace('19','9',1)
        if '399' in s: s = s.replace('399','91',1)
        if '999' in s: s = s.replace('999','3',1)
    if sum(int(e) for e in s) == 33:
        print(n)  # 46
        break
