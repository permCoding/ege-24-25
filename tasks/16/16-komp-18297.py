import sys

def f(n):
    if n < 10: return n-1
    if n%2==0:
        return 3*n - 1 + f(n-3)
    else:
        return 5*n + 2 + f(n-4)

sys.setrecursionlimit(5000)
print(f(4445) - f(4444))  # 8896
