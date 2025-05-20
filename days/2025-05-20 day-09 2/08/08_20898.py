from itertools import product

amount = 0
al = '012345678'
for e in product(al, repeat=5):
    if e[0] != '0' and e.count('0') == 1:
        s = ''.join(e) + 'X'
        i = s.index('0')
        if s[i-1] not in '1357' and s[i+1] not in '1357':
            amount += 1

print(amount)
