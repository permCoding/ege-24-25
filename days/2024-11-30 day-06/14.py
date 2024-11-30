x = 400
while True:
    x += 1
    r = 16**560 + 16**120 - x
    r = f'{r:x}'
    if r.count('0') == 442:
        print(x)
        break
