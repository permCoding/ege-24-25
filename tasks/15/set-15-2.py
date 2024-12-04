def f(x, A):
    return ((x not in Q) <= (x not in A)) and ((x in P) <= (x not in A))

P = [1,2,3,4,5,6,7,10]
Q = [3,5,7,8,30]

# A = list()
# for x in range(1, 32):
#     if f(x, A) == False:
#         A.append(x)
# print(len(A), A)  # 8 [1,2,3,4,5,6,7,10]

A = list(range(1, 32))
for x in range(1, 32):
    if f(x, A) == False:  # если с ним плохо, то убираем
        A.remove(x)
print(len(A), A)  # 2

"""
тут максимальный - поэтому сначала полный диапазон и исключаем
https://education.yandex.ru/ege/task/febc093f-a6e2-4503-9571-1497a1f4d83d
"""