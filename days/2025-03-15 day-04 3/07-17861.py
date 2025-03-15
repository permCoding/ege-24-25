for n in range(1, 10_000):
    s = n * 1024 * 768 * 12  # bit
    v = 1_310_720  # bit / sec
    t = s / v
    if t > 300:
        print(n-1)
        break
