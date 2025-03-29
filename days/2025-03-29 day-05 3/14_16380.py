import sys


def get(n, base=25):
    cnt = 0
    while n > 0:
        if n%base > 10:
            cnt += 1
        n //= base
    return cnt


sys.set_int_max_str_digits(20_000)
v = 4*3125**2019 + 3*625**2020 - 2*125**2021 + 25**2022 - 4*5**2023 - 2024
print(get(v))  # 3030

