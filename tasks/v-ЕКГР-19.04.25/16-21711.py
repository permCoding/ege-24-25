import sys
sys.setrecursionlimit(9000)
sys.set_int_max_str_digits(30000)

def f(n):
    if n < 20:
        return n
    else:
        return (n-6) * f(n-7)

print( (f(47872) - 290*f(47865)) / f(47858) )

print( (47865-6) * ((47872-6) - 290) )  # 2276939784
