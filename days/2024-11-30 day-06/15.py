def f(A, x, y):
    return (-(x-2)**2+3 < y) or ((x-1)**2 + y**2 < 7) or (5*x+A > y)


def check(A):
    for x in range(1, 100):
        for y in range(1, 100):
            if f(A, x//5, y//5) == False:
                return False
    return True


for A in range(-100, +100):
    if check(A):
        print(A)
        break