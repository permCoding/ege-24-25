for x in range(2300, 0, -1):
    r = 7**350 + 7**150 - x
    k = 0
    while r > 0:
        if r%7 == 0: k += 1
        r //= 7
    mx = x
    if k == 200:
        print(x)  # 2001
        break
