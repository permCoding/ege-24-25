from itertools import product

i = 0
for c in product('БЕНРСТЬЯ', repeat=5):
    i += 1
    if i%2==0 and c[0]=='Р' and c.count('Ь')==0:
        print(i, c)
    
