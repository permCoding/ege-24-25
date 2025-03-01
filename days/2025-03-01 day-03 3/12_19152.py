for n in range(2, 10_000):
    s = '59' + n * '8'
    while '68' in s or '988' in s or '888' in s:
        if '68' in s: s = s.replace('68', '8', 1)
        if '988' in s: s = s.replace('988', '86', 1)
        if '888' in s: s = s.replace('888', '9', 1)
    sm = sum(int(e) for e in s)
    if int(round(sm**(1/3), 0))**3 == sm:
        print(n)
        break
