x = 400
while True:
    x += 1
    v = 16**560 + 16**120 - x
    s = f'{v:x}'
    if s.count('0') == 442:
        print(x)
        break
