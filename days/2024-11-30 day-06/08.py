from itertools import product


def ex_01():
    amount = 0
    al = '0123456789abc'
    for s in product(al, repeat=7):
        if s[0] != '0' and s.count('5') >= 2:
            s = ''.join(s)
            for smb in '02468ac': s = s.replace(smb, '*')
            for smb in '13579b':  s = s.replace(smb, '=')
            if ('**' not in s) and ('==' not in s):
                amount += 1
    print(amount)  # 91581


def ex_02():
    q = '02468ac'
    amount = 0
    for s in product('0123456789abc', repeat=7):
        if s[0] != '0' and s.count('5') >= 2:
            b = True
            for i in range(6): 
                u1 = (s[i] in q) and (s[i+1] in q)
                u2 = (s[i] not in q) and (s[i+1] not in q)
                if (not u1) and (not u2): 
                    b = False
                    break
            if b: amount += 1
    print(amount)  # 91581


ex_01()

# print(13**7)
