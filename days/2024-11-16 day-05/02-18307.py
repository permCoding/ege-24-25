def f(a,b,c,d):
    return ((a or b) <= ((not bool(c)) and a)) and d

for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for d in 0,1:
                if f(a,b,c,d) == True:
                    print(d,b,c,a)
"""
X НЕ
0 1
1 0
    
X Y AND
0 0 0
0 1 0
1 0 0
1 1 1

X Y OR
0 0 0
0 1 1
1 0 1
1 1 1

X Y XOR
0 0 0
0 1 1
1 0 1
1 1 0

X Y IMP <=
0 0 1
0 1 1
1 0 0
1 1 1

X Y EQ ==
0 0 1
0 1 0
1 0 0
1 1 1
"""
