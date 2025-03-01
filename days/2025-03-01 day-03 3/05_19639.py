lst = []
for n in range(1, 1000):
    b = bin(n)[2:]
    if b.count('0') % 2 == 0:
        b = '1' + b + '1'
    else:
        b = '10' + b
    r = int(b, 2)
    if r < 100:
        lst.append(r)
print(max(lst))
