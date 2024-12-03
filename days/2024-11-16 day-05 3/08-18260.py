from itertools import product

k = 0
for c in product('0123456789AB', repeat=6):
    if c.count('B') == 1 and c[0] != '0':
        if len([e for e in c if e in '13579B']) == 3:
            k += 1
print(k)  # 297000    
