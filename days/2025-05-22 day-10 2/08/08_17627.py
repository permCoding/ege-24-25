from itertools import product as p

al = '0123456789ABCDE'
amount = 0
for e in p(al, repeat=5):
    if e[0] != '0':
        if e.count('8') == 1:
            if sum(1 for i in e if i in 'ABCDE') >= 2:
                amount += 1

print(amount)  # 83175
