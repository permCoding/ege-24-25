for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if (x <= y) and z and (not w):
                    print(y,z,x,w)  # yzxw
 