from itertools import product

amount = 0
for e in product('0123456789abc', repeat=7):
    if e[0] != '0' and e.count('5') >= 2:
        s = ''.join(e)
        for p in '2468ac': s = s.replace(p, '0')
        for p in '3579b':  s = s.replace(p, '1')
        if ('00' not in s) and ('11' not in s):
            amount += 1
print(amount)
