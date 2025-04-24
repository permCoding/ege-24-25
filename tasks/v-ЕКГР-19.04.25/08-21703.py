from itertools import product

a = 'АБДЕОП'
k = 0
for e in product(a, repeat=6):
    k += 1
    if k%2 == 0 and e[0] == 'О' and len(set(e)) == 6:
        print(e, k)  # 38306
        