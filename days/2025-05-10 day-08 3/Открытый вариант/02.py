for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (x and (not(y))) or (y == z) or w
                if f == False:
                    print(x,w,z,y)  # xwzy
