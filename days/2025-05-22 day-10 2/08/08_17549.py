from itertools import product as p

mx = 0
for i,e in enumerate(p('КОСУФ', repeat=5), start=1):
    if e.count('Ф') == 0:
        if e.count('У') == 2:
            mx = i
print(mx)  # 2313
