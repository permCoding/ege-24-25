from itertools import product as p

k = 0
for e in p('012345678', repeat=5):
    if e[0] != '0':
        if e.count('5') == 1:
            u = True
            for i in range(1, 5):
                if e[i-1] == e[i]:
                    u = False
            if u:
                k += 1

print(k)  # 13377

"""
21456
27272
22133
"""