for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (not(x <= y)) or (z <= w) or (not z)
                if not(f):
                    print(x,y,z,w)
