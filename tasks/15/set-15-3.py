def f(x, A):
    u1 = ((x in B) == ((x in A) and (x in C)))
    u2 = ((x in C) == ((x in A) and (x in B)))
    return  u1 <= u2

B = [2,5,10,15,17,20,22,25]
C = [2,4,6,8,10,12,15,16,20,25]

A = []
for x in range(1, 26):
    if f(x, A) == False:  # если без него плохо, то добавляем
        A.append(x)

print(sum(A), A)  # ___

"""
тут минимальный - поэтому сначала пустой диапазон и добавляем
https://education.yandex.ru/ege/task/fcd4ef3a-8c80-468a-8217-17f9e35df44d
"""