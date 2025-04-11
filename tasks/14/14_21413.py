def f(s, x):
    r, p = 0, 0
    for v in s[::-1]:
        dig = x if v == 'x' else int(v)
        r += dig * 21**p
        p += 1
    return r

def get(x):
    return f('82934x2', x) + f('2924xx7', x) + f('67564x8', x)

for x in range(0, 21):
    r = get(x)
    if r%20 == 0:
        print(r//20)
        break  # 72450445
