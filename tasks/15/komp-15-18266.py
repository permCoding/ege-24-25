def f(A, x):
    return (x & 57 == 0) or ((x & 23 == 0) <= (x & A != 0))
A = 0
while True:
    A += 1
    if all(f(A, x) for x in range(1, 100)):
        print(A)  # 40
        break
