from itertools import product as p

mx = 0
for i,e in enumerate(p('АЙЛМ', repeat=5) , start=1):
    if e.count('М') + e.count('Л') == 0:
        if 'ЙЙ' not in ''.join(e):
            mx = i

print(mx)
