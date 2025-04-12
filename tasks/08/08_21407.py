from itertools import product

k = 0
for e in product('ДГИАШЭ', repeat=5):
    if e[0] in 'ДГШ' and e[-1] in 'ИАШ':
        k += 1
print(k)