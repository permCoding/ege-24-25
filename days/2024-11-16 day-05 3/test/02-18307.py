def f(a,b,c,d):
    return ((a or b) <= (not(bool(c)) and a)) and d
for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for d in 0,1:
                if f(a,b,c,d):
                    print(d,b,c,a)