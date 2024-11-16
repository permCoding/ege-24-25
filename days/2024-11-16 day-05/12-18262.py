def get(s):
    while ('>3' in s) or ('>2' in s) or ('>0' in s):
        if ('>3' in s): s = s.replace('>3', '22>', 1)
        if ('>2' in s): s = s.replace('>2', '2>', 1)
        if ('>0' in s): s = s.replace('>0', '3>', 1)
    return s

n = 1
while True:
    s = '>' + '0'*17 + '3'*n + '2'*17
    r = get(s)
    sm = sum(int(e) for e in list(r) if e != '>')
    q = sm**.5
    if int(str(q).split('.')[1]) == 0:
        print(n)
        break
    n += 1
