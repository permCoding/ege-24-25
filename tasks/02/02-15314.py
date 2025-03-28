for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (x and (not z)) or (y == z) or (not w)
                if f == False:
                    print(w,y,z,x)  # w_z_
