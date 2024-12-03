from itertools import product

for i, c in enumerate(product('ДИКМО', repeat=5), start=1):
    if c.count('М') == 2:
        if 'ММ' not in ''.join(c):
            print(i, c)  # 3099 ('О', 'О', 'М', 'О', 'М')
