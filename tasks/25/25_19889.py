n = 902714
k = 0
while k < 6:
    n += 1
    for d in range(15, n//2+1, 10):
        if n%d==0:
            k += 1
            print(n, d)
            break