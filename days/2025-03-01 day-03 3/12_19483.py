for n in range(4, 10_000):

    s = '2' + n * '5'
    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '5', 1)
        if '355' in s:
            s = s.replace('355', '522', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)

    # if sum(1 for e in s if e == '2') == 10:
    if s.count('2') == 10:
        print(n, s)
        break