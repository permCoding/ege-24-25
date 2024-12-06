def f(A, x):
    return (x in P) or (x in Q) or (x not in A)


P = [12,23,34,45,56]
Q = [23,35,56,68,89]
A = list(range(10, 95))
for x in range(10, 95):
    if f(A, x) == False:
        A.remove(x)
print(A)  # 8

"""
https://education.yandex.ru/ege/task/ac1394e1-9e24-47fb-a188-a105d55afee7
"""