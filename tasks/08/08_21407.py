from itertools import product as p

k = 0
for e in p('ДГИАШЭ', repeat=5):
    if e[0] in 'ДГШ' and e[-1] in 'АИЭ':
        k += 1
print(k)  # 1944