for n in range(1, 100):
    b = bin(n)[2:]

    b += str(b.count('1')%2)
    b += str(b.count('1')%2)

    r = int(b, 2)

    if r > 253:
        print(n)  # 64
        break
