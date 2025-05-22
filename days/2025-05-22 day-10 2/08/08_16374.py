from itertools import product as p

amount = 0
al = '0123456'
for e in p(al, repeat=7):
    if e[0] != '0':
        if sum(1 for i in e if i in '0246') == 2:
            amount += 1

print(amount)
