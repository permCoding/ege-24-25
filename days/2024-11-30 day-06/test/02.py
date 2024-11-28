def f(x,y,u,w):
    return (x <= w) <= (u <= y)

for x in 0,1:
    for y in 0,1:
        for u in 0,1:
            for w in 0,1:
                if f(x,y,u,w) == False:
                    print(x,u,w,y)
