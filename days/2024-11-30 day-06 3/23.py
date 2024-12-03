def f(a, b):
    if a == 23: return 0
    if a > b: return 0
    if a == b: return 1 
    return f(a+1,b) + f(a+3,b) + f(a*4,b)


print(f(4, 18) * f(18, 35))
