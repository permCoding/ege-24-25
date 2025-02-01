def f(s):
    while '12' in s or '322' in s or '222' in s:
        if '12' in s: s = s.replace('12','2', 1)
        if '322' in s: s = s.replace('322','21', 1)
        if '222' in s: s = s.replace('222','3', 1)
    return s


for n in range(4, 10_000):        
    s = '1' + n*'2'
    r = f(s)
    if sum(int(e) for e in r) == 15:
        print(n)
        break

##s = '345345 12 34645 12 566757'
##s = s.replace('12', '2', 1)
##print(s)


s = '1' + 37*'2'
print(f(s))

# 12:05
