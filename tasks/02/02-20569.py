def f(x,y,z,w):
    a = w <= z
    b = x <= (not(y))
    return (a == b) and (x or z)

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                print(z,x,y,w, ' ', f(x,y,z,w))
                # zxyw