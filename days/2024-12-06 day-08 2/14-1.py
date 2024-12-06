for x in range(1, 10):
    n15 = f'4C{x}4'
    n13 = f'{x}62A'
    res = int(n15, 15) + int(n13, 13)
    if res%121 == 0:
        print(res//121)  # 234
        break


"""
https://inf-ege.sdamgia.ru/problem?id=48394
"""
