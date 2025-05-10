def f(n, m):
    if n > m or n == 56: return 0
    if n == m: return 1
    return f(n+3, m) + f(n+7, m) + f(n*3, m)

print(f(12, 40)*f(40, 72)*f(72, 89))
