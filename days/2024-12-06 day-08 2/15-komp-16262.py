def f(A, x, y):
    u1 = (A<x)  or (x**2-7*x+10>0)
    u2 = (A>=y) or (y**2+7*y+12>0)
    return u1 and u2

res = []
for A in range(-100, +100):
    if all(f(A,x,y) for x in range(-100, +100) for y in range(-100, +100)):
        res.append(A)
print(len(res), res)  # 5
