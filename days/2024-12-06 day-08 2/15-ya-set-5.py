P = [14,16,18,20,22,24]
Q = [16,19,22,25,28]

A = []
for x in range(1, 256):
    f = (x not in P) or ((x not in Q) <= (x in A))
    if f == False:
        A += [x]
print(A)  # [14, 18, 20, 24]
print(14 * 18 * 20 * 24)  # 120960
"""
https://education.yandex.ru/ege/task/43f3e1bc-ddc6-44a4-84d7-25abf7a35f72
"""
