from itertools import product

n = 0
al = 'АВНРЬЯ'
for i, e in enumerate(product(al, repeat=5), start=1):
    if e[0] != 'Я':
        if e.count('Ь') <= 1:
            if 'ЯЯ' not in ''.join(e):
                n = i

print(n)  # 6406
