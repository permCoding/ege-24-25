def f(a,b,c,d):
    return ((a <= b) <= c) or (not(d))

for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for d in 0,1:
                if f(a,b,c,d) == False:
                    print(d,c,b,a)
                    # dcba