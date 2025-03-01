def to(n, base=2):
    if n == 0: return '0'
    res = ''
    while n > 0:
        res = str(n%base) + res
        n //= base
    return res


for n in range(1, 10_000):
    
    s = to(n, 5)
    if n%2 == 0:
        s += to(int(s[-1], 5)*3, 5)
    else:
        s = s[-1] + s[1:-1] + s[0] + '1'
    R = s.lstrip('0')
    
    if R.count('0') == 4:
        print(n, R)
        break


# print(to(14))  # 1110

# s = '00024534'
# print(s.lstrip('0'))

# print(str(int(s)))


