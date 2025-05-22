from itertools import product as p

al = '0123456789ABCD'
amount = 0
for e in p(al, repeat=5):
    if e[0] != '0':
        if e.count('9') == 1:
            if sum(1 for i in e if i in 'BCD') <= 3:
                amount += 1

print(amount)  # 133612
