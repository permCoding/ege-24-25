def f(n):
    res = ''
    while n > 0:
        res = str(n%4) + res
        n //=4
    return res

r = 4**644 + 4**322 + 16**35 - 64**3
s = f(r)
print(r, s.count('3'))  # 61
