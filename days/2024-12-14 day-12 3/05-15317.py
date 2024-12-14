t = []
for n in range(1, 500):
    b = bin(n)[2:]
    if n%2==0:
        b += '01'
    else:
        b = '1' + b + '1'
    r = int(b, 2)
    if r > 156:
        t += [n]
print(min(t))
