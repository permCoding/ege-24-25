from itertools import product

al = 'АБДЕОП'
mx = 0
for i, e in enumerate(product(al, repeat=6), start=1):
    if i%2 == 0:
        if e[0] == 'О':
            if len(set(e)) == 6:
                mx = i
print(mx)  # 38306
