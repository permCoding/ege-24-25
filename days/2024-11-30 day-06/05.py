
t = []
for n in range(33, 500):
    s = f'{n:b}'
    if n%2 != 0:
        s = '1' + s[:-2] + '10'
    else:
        s = '10' + s[2:] + '1'
    r = int(s, 2)
    t.append(r)
print(min(t))
