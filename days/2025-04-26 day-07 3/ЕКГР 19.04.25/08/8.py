from itertools import product

for i, e in enumerate(product('АБДЕОП', repeat=6), start=1):
    if i%2 == 0 and e[0] == 'О' and len(set(e)) == 6:
        print(i, e)  # 38306