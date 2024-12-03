def f(x,y,z,w):
    return ((x == z) <= w) and (w <= (y and x))
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if f(x,y,z,w) == True:
                    print(y,z,x,w)