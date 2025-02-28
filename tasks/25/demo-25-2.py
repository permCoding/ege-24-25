for n in range(1917, 10**10+1, 1917):
    s = str(n)
    if len(s) >= 8:
        if s[0] == '3' and s[2:4] == '12':
            if s[5:7] == '14' and s[-1] == '5':
                print(n, n//1917)