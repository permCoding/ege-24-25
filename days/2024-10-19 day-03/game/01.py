# алгоритм бинарного поиска
from random import randint as rnd

comp = rnd(1, 1_000)
money = 1_000  # $
while True:
    n = int(input('введите число - '))
    if comp == n: break
    if comp < n:
        print("- меньше")
    else:
        print("- больше")
    money -= 100

print(f'осталось - {money} $')

"""
500
250
125
62
32
16
8
4
2
1
"""