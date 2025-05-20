from itertools import product

al = '0123456789AB'
amount = 0
for e in product(al, repeat=5):
    if e[0] != '0':
        u1 = e.count('7') == 1
        u2 = sum(1 for x in e if x in '9AB') <= 3
        if u1 and u2:
            amount += 1

print(amount)  # 67476
