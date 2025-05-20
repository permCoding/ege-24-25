from itertools import product

n = 0
al = 'КОСУФ'
for i, e in enumerate(product(al, repeat=5), start=1):
    if e.count('Ф') == 0 and e.count('У') == 2:
        n = i

print(n)  # ____
