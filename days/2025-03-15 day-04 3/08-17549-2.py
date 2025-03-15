# 2 - КОСУФ - product

from itertools import product

for i, item in enumerate(product('КОСУФ', repeat=5), start=1):
    s = ''.join(item)
    if s.count('Ф') == 0 and s.count('У') == 2:
        print(i, s)
