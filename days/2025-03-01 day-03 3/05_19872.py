def to(n, base=2):
    res = ''
    while n > 0:
        res = str(n%base) + res
        n //= base
    return res


for n in range(1_000, 0, -1):
    
    svn = to(n, 7)
    if n%2 == 0:
        svn = '52' + svn + '1'
    else:
        svn = svn[-1] + svn[1:-1] + svn[0] + '15'
    R = svn.lstrip('0')
    
    if len(R) == 4:
        print(n, R)
        break


# print(to(14))  # 1110

# s = '00024534'
# print(s.lstrip('0'))

# print(str(int(s)))


