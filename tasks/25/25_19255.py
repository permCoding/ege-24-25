for n in range(6437, 10**10+1, 6437):
    s = str(n)
    if len(s) >= 7:
        if s[0]=='1' and s[2]=='3' and s[-3:]=='954':
            if '5' in s[3:-3]:
                print(n, n//6437)
    