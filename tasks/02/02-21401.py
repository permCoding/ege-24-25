for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = x and (z <= w) and (not(y))
                if f == True:
                    print(x,w,z,y)  # w_z_
