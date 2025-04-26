for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if not((x > y) or (z == w) or z):
                    print(z,y,x,w)  # zyxw
