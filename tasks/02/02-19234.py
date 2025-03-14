def f(x,y,z,w):
    a = not( ((not x) or y) and (not w) )
    b = not( z and (not(y and w)) )
    return a or b

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if f(x,y,z,w) == False:
                    print(y,x,w,z)
                    # yxwz