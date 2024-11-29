for n in range(326782, 965324):
    t = get_d(n)
    if t[0]*t[1]*t[2]==n:
        if p(t[0]) and p[t[1]] and p[t[2]]:
            if max(t)-min(t) <= 12:
                print(n)