def f(x, A):
    return (x not in A) <= (((x in P) and (x in Q)) <= (x in R))

P = [2,4,6,8,10,12,14,16,18,20]
Q = [3,6,9,12,15,18,21,24,27,30]
R = [12,24,36,48,60]

A = []
for x in range(1, 62):
    if f(x, A) == False:  # если без него плохо, то добавляем
        A.append(x)

print(len(A), A)  # 6 * 18 = 108

"""
тут минимальный - поэтому сначала пустой диапазон и добавляем
https://education.yandex.ru/ege/task/a44f5179-354c-4844-836a-aa650b38faf4
"""