import sys

def f(n):
    if n == 1:
        return 1
    else:
        return f(n-1)*(n-1)

# print(sys.getrecursionlimit())
sys.setrecursionlimit(2_200)
sys.set_int_max_str_digits(10_000)
print( (f(2024)+2*f(2023)) / f(2022) )  # 4094550
print(2022 * 2025)  # 4094550

"""
f(2024) 
=> (2023 * f(2023) + 2 * f(2023))
=> f(2023) * 2025
=> f(2022) * 2022 * 2025
=> 2022 * 2025 = 4094550

"""