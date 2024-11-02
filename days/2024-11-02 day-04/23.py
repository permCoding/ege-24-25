def f(a, b):
    if a < b: return 0
    if a == b: return 1
    return f(a-2, b) + f(a//2, b)

print(f(38, 16) * f(16, 2))



##def f(a, b):
##    if a > b: return 0
##    if a == b: return 1
##    return f(a+1, b) + f(a*2, b)
##
##print(f(2, 5))


##def summa(n):
##    if n == 0: return 0
##    return summa(n-1) + n
##
##print(summa(5))
