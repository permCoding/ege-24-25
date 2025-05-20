r = 1280 * 960 * 11
for n in range(5_000, 0, -1):
    p = n * r
    v = 96_468_992
    if p / v <= 132:
        print(n)
        break
