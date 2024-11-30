for x in 0,1:
    for y in 0,1:
        for u in 0,1:
            for w in 0,1:
                if ((x <= w) <= (u <= y)) == False:
                    print(x,u,w,y)
