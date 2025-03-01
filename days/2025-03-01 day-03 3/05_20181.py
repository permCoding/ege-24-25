for n in range(1, 1_000):

    b = bin(n)[2:]
    if n%2 == 0:
        b += bin(b.count('1'))[2:]
    else:
        b = '1' + b + '101'
    r = int(b, 2)

    if r > 350:
        print(n, r)
        break
