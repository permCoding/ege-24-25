def f(x,y,z,w):
    return y and (z == (w <= (x or z)))

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if f(x,y,z,w):
                    print(y,x,w,z)
                    # yxwz