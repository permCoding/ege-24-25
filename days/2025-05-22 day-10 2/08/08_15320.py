from itertools import product as p

for i, e in enumerate(p('АПРСУ', repeat=5), start=1):
    if e.count('У') <= 1:
        if 'АА' not in ''.join(e):
            print(i, e)
            break
