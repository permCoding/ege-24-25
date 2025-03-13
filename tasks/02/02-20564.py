def f(x,y,z,w):
    return x and ((w <= y) == z)

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                print(z,x,w,y, ' ', int(f(x,y,z,w)))
                # zxwy