def f(l, r, x):
    return (not(l <= x <= r)) <= ((36 <= x <= 75) == (60 <= x <= 110))

st = 0.1
lst_x = []
x = 36
while x <= 110:
    x += st
    lst_x.append(x)
    
l = 36
while l <= 110:
    l += st

    r = 36
    while r <= 110:
        r += st

    if l<r and all(f(l, r, x) for x in lst_x):
        print(l, r, r-l)  # 74
