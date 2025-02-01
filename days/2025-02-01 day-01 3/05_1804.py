def  f(n):
    b = bin(2*n)[2:]  # 0b
    bn = bin(n)
    b += str(bn.count('1')%2)
    b += str(b.count('1')%2)
    return int(b, 2)

for n in range(1, 1_000):
    if f(n) > 249:
        print(n)
        break
