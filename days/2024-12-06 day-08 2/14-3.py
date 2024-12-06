for x in '0123456789ABCDE':
    a = f'123{x}5'
    b = f'1{x}233'
    res = int(a, 15) + int(b, 15)
    if res%14 == 0:
        print(res//14)  # 8767
        break

"""
https://inf-ege.sdamgia.ru/problem?id=47218
"""
