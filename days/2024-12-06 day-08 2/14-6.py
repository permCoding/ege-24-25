from itertools import product

for cnt in range(1, 9):
    t = []
    for x in range(8):
        for y in product('01234567', repeat=cnt):
            a = int(f'36{x}53', 8)
            b = int(f'4{''.join(y)}3', 8)
            if a-b > 0: t += [a-b]
    if t: print(cnt, min(t))

"""
1 15088
2 12848

https://education.yandex.ru/ege/task/de78f4fe-7180-4347-be54-c0df9f1467d0
"""
