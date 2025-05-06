for x in range(1, 2300):
    v = 7**350 + 7**150 - x
    k = 0
    while v > 0:
        if v%7 == 0: k += 1
        v //= 7
    if k == 200: print(x)  # 2001
