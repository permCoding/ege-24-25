from itertools import product as p

amount  = 0
for e in p('ДГШИАЭ', repeat=5):
    if e[0] in 'ДГШ' and e[-1] in 'ИАЭ':
        amount += 1

print(amount)  # 1944
