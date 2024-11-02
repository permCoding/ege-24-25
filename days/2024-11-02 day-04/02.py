def f(w,y,x,z):
    return ((w <= y) <= x) or (not z)


for w in 0,1:
    for y in 0,1:
        for x in 0,1:
            for z in 0,1:
                if f(w, y, x, z) == False:
                    print(z, y, w, x)



"""

A НЕ  not
0  1
1  0

A B ИЛИ   or
0 0  0
0 1  1
1 0  1
1 1  1

A B ->  <=   
0 0  1
0 1  1
1 0  0
1 1  1

"""
