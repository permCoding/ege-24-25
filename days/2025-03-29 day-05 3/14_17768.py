def get(n):
    cnt = 0
    while n > 0:
        if n%4 == 3: cnt += 1
        n //= 4
    return cnt

v = 4**644 + 4**322 + 16**35 - 64**3
print(get(v))  # 61
