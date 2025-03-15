for n in range(1, 10_000):
    s = n * 1280 * 960 * 11  # bit
    v = 96_468_992  # bit / sec
    t = s / v
    if t <= 132: continue
    print(n-1)
    break
