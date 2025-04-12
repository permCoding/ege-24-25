def f(A, x, y):
    return (5 < y) or (x > 32) or (x+2*y < A)


for A in range(100):
    if all(f(A,x,y) for x in range(100) for y in range(100)):
        print(A)
        break  # 43