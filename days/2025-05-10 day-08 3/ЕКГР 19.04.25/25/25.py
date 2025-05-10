def f1(n):  # 0.6
    s = str(n)
    return s[0]=='4' and s[-1]=='1' and '4736' in s[1:-1]


def f2(n):  # 3.1
    import fnmatch
    s = str(n)
    return fnmatch.fnmatch(s, '4*4736*1')


def f3(n):  # 1.6
    import re
    s = str(n)
    return re.match('^4.*4736.*1$', s)


for n in range(7993, 10**10+1, 7993):
    if f3(n): print(n, n//7993)

        
"""
44736821 5597
4064736241 508537
4303247361 538377
4347368721 543897
4447361151 556407
4473658121 559697
4794736931 599867


"""