for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if x and (z <= w) and (not y):
                    print(x,w,z,y)  # xwzy
