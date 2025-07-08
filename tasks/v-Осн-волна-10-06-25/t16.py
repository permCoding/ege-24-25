import sys
sys.setrecursionlimit(4000)

def f(n):
    if n < 10:
        return n
    else:
        return 3*n + f(n-3)
    
print( (f(6250) + 2*f(6244)) / f(6238) )  # 3
