from itertools import product as p

amount = 0
for e in p('01234567', repeat=5):
    if e[0] != '0':
        if e[0] not in '1357':
            if e[-1] not in '26':
                if e.count('7') <= 2:
                    amount += 1
print(amount)  # 9135
