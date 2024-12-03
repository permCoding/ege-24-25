def get(n, base=12):
    r = ''
    while n > 0:
        o = n%base
        n //= base
        if o < 10:
            r = str(o) + r
        else:
            c = 'A' if o == 10 else 'B'
            r = c + r
    return r

k = 0
n = 0
while True:
    n += 1
    q = get(n)
    if len(q) < 6: continue
    if len(q) > 6: break
    if q[0] != '0':
        if q.count('B') == 1 and q[0] != '0':
            if len([e for e in q if e in '13579B']) == 3:
                k += 1
print(k)  # 297000    
