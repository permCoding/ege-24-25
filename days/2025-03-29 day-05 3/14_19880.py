def get(n):
    cnt = 0
    while n > 0:
        if n%25 == 0: cnt += 1
        n //= 25
    return cnt

v = 15625**16 - 3125**3 * 25**19 + 625**4 - 2005
print(get(v))  # 18
