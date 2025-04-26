def f(l, r, x):
    return (not(l<=x<=r)) <= ((36<=x<=75) == (60<=x<=110))

lst_A = [n/10 for n in range(350, 1201)]
lst_X = [n/10 for n in range(250, 1801)]

mn = 2**32
for l in lst_A:
    for r in lst_A:
        if l < r:
           if all(f(l,r,x) for x in lst_X):
               mn = min(mn, r-l)
print(mn)
