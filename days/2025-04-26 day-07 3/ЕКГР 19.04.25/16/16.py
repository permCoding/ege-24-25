import sys


def f(n):
    if n < 20:
        return n
    else:
        return (n-6) * f(n-7)
    

sys.setrecursionlimit(7000)
sys.set_int_max_str_digits(40000)
print( (f(47872) - 290*f(47865)) / f(47858) )  # 2276939784
print(47859 * (47866-290))  # 2276939784