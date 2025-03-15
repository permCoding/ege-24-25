for n in range(1, 100):
    b = bin(n)[2:]
    sm = b.count('1')
    if sm % 2 == 0:
        b += '0'
        b = '10' + b[2:]
    else:
        b += '1'
        b = '11' + b[2:]
    r = int(b, 2)
    if r > 19:
        print(n)
        break


# b = '1110101'
# sm = b.count('1')
# print(sm)
# sm = sum(int(e) for e in b)
# print(sm)
