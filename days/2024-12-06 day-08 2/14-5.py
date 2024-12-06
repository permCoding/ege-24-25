x = 125 + 25**3 + 5**9

cnt = 0
while x > 0:
    if x%5==0: cnt += 1
    x //= 5
print(cnt)

"""
https://inf-ege.sdamgia.ru/problem?id=13362
"""
