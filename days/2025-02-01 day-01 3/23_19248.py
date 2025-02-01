import sys
##print(sys.getrecursionlimit())
sys.setrecursionlimit(5000)
sys.set_int_max_str_digits(55000)

def f(n):
    if n < 5:
        return n
    else:
        return 2*n*f(n-4)

print( (f(13766)-9*f(13762))/f(13758) )
