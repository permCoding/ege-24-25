def f(x,y,A):
    return (-(x-2)**2+3 < y) or ((x-1)**2 + y**2 < 7) or (5*x+A > y)

def u(A):
    for x in range(1, 500):
        for y in range(1, 500):
            if f(x/10,y/10,A) == False:
                return False
    return True
    
for A in range(-50, +50):
    if u(A) == True:
        print(A)
        break


"""
x и y - любые положительные
то есть и НЕ целые тоже
A - целые и отрицательные тоже
"""