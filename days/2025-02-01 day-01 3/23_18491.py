def f(a, b):
    if a == b: return 1
    if a > b: return 0
    m = max(int(q) for q in str(a))
    return f(a+3,b) + f(a+m,b)


print(f(10, 24) * f(24, 41))
