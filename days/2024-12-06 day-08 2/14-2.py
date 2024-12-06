for x in '012345678':
    for y in '012345678':  # 9A
        n09 = f'88{x}4{y}'
        n11 = f'7{x}44{y}'
        res = int(n09, 9) + int(n11, 11)
        if res%61 == 0:
            print(res//61)  # 2715
            break

"""
https://inf-ege.sdamgia.ru/problem?id=48384
"""
