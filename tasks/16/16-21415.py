import sys

def f(n):
    if n <= 5: 
        return 1
    else:
        return n + f(n-2)

sys.setrecursionlimit(5000)
print(f(2126) - f(2122))  # ____
