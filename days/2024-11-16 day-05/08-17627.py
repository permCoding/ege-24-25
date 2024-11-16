from itertools import product

k = 0
for q in product('0123456789ABCDE', repeat=5):
    if q.count('8') == 1 and q[0] != '0':
        a = q.count('A')
        b = q.count('B')
        c = q.count('C')
        d = q.count('D')
        e = q.count('E')
        if a+b+c+d+e>=2:
            k += 1
print(k)
