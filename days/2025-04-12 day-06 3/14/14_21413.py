def f(s, x):
    r, s = 0, s[::-1]
    for p in range(len(s)):
        dig = x if s[p] == 'x' else int(s[p], 21)
        r += dig * 21**p
    return r

for x in range(21):
    a = '82934x2'
    b = '2924xx7'
    c = '67564x8'
    sm = f(a, x)+f(b, x)+f(c, x)
    if sm%20 == 0:
        print(sm//20)
        break
