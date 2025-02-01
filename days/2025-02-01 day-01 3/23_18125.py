import math
def f(a, b):
    if a == b: return 1
    if a < b: return 0
    m = math.floor(a**.5)
    return f(a-4,b) + f(a-7,b) + f(m,b)


print(f(44, 22) * f(22, 3))


##x = 3.78
##print(math.floor(x))
##print(math.trunc(x))
