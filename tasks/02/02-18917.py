def f(s,r,a,t):
    return (s or (not(r))) and (not(r==a)) and t

for s in 0,1:
    for r in 0,1:
        for a in 0,1:
            for t in 0,1:
                if f(s,r,a,t) == True:
                    print(s,t,a,r)
                    # star