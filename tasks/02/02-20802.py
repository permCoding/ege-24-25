def f(x,y,z,w):
    return (w <= (not(z <= x))) or y

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if f(x,y,z,w) == False:
                    print(z,x,y,w)