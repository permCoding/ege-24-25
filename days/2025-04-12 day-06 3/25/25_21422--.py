def f(n):
    t = [d for d in range(1, n) if n%d == 0]
    return sorted(e for e in t if e%10==7 and e!=7)


k, n = 0, 1_125_000
while k < 5:
    n += 1
    divs = f(n)
    if len(divs) > 0:
        print(n, divs[0])
        k += 1    
