r = 1280 * 960 * 11
max_n = 0
for n in range(1, 5_000):
    p = n * r
    v = 96_468_992
    if p / v <= 132:
        max_n = n
    else:
        break

print(max_n)
