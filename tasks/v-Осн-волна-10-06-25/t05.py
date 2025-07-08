for N in range(1000, 3, -1):
    b = bin(N)[2:]
    if N%3 == 0:
        b += b[-3:]
    else:
        b += bin((N%3)*3)[2:]
    R = int(b, 2)
    if R < 130:
        print(N)  # 31
        break
