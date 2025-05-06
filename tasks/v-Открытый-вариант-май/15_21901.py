def f(A, x):
    return (((x & 52) != 0) and ((x & 48) == 0)) <= ((x & A) != 0)

for A in range(1, 200):
    if all(f(A,x) for x in range(1, 200)):
        print(A)  # 4
        break
