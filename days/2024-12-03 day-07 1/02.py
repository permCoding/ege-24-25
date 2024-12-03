n = 0
while True:
    n += 1
    s = f'{n:o}'
    if len(s) == 4:
        b = f'{n:b}'
        if b.count('1') == 6:
            print(s)
            break
