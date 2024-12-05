def f(A, x, y):
    return (x-y>=39) or (y<=x) or (y>=A-20)
A = 500
while A > 0:
    A -= 1
    if all(f(A, x, y) for x in range(1, 200) for y in range(1, 200)):
        print(A)  # 40
        break