def f(x, A):
    return (x not in A) <= (((x in P) and (x in Q)) <= (x in R))

P = set([2,4,6,8,10,12,14,16,18,20])
Q = set([3,6,9,12,15,18,21,24,27,30])
R = set([12,24,36,48,60])

from itertools import product

for e in product(range(1, 62), repeat=2):
    A = set(e)
    if all(f(x, A) for x in range(1, 62)):
        print(len(A), A)  # 18 * 6 = 108



"""
https://education.yandex.ru/ege/task/a44f5179-354c-4844-836a-aa650b38faf4
"""