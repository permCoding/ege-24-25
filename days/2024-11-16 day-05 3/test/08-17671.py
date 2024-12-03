from itertools import product
a = 'АЙЛМ'
i = 0
for q in product(a, repeat=5):
    i += 1
    if q.count('М') == 0 and q.count('Л') == 0:
        if ''.join(q).find('ЙЙ') == -1:
            print(i, q)  # 274