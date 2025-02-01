def f(s):
    while '12' in s or '322' in s or '222' in s:
        if '12' in s: s = s.replace('12','2', 1)
        if '322' in s: s = s.replace('322','21', 1)
        if '222' in s: s = s.replace('222','3', 1)
    return sum(int(e) for e in s) == 15

for n in range(3, 100):
    if f('1' + n*'2'):
        print(n)
        # break
