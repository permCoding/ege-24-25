for n in range(4, 10_000):
    s = '7' + '8' * n
    while '78' in s or '688' in s or '8888' in s:
        if '78' in s: s = s.replace('78', '8', 1)
        if '688' in s: s = s.replace('688', '87', 1)
        if '8888' in s: s = s.replace('8888', '6', 1)
    if sum(int(e) for e in s) == 61:
        print(n)  # 348
        break
