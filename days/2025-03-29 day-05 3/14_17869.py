import sys


def get(n):
    cnt = 0
    while n > 0:
        if n%25 == 0: cnt += 1
        n //= 25
    return cnt


sys.set_int_max_str_digits(20_000)

v = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2025

print(get(v))  # 10

