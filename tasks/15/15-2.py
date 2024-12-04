def f(x, A):
    return (160<=x<=180) <= ((x%35==0)<=(x%A==0))

A = 0
while A <= 900:
    A += 1
    if all(f(x,A) for x in range(1, 900)):
        print(A)  # 6 чисел
    

"""
https://education.yandex.ru/ege/task/bfdcf7a3-606f-4e4d-ac7e-3a26594a79a2
"""