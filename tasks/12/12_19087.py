for n in range(4, 10_000):
    s = '2' + n * '7'
    while '27' in s or '777' in s or '377' in s:
        if '27' in s: s = s.replace('27','7',1)
        if '777' in s: s = s.replace('777','3',1)
        if '377' in s: s = s.replace('377','72',1)
    p = 1
    for e in s:
        p *= int(e)
    if p%3==0 and p%10==1:
        print(n, s, p)
