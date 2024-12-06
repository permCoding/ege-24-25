def f(A, x):
    return ((x%7!=0) and (x%13==0)) <= (x > A-40)

for A in range(900, 0, -1):
    if all(f(A, x) for x in range(1, 900)):
        print(A)  # 52
        break

"""
x = 12
d = 7
print(True if x%d==0 else False)
print(x%d==0)
"""