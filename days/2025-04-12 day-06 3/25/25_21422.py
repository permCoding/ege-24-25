def f(n):
    st = set()
    for d in range(2, int(n**.5)+1):
        if n%d == 0:
            st.add(d)
            st.add(n//d)
    return [e for e in sorted(st) if e%10==7 and e!=7]


k, n = 0, 1_125_000
while k < 5:
    n += 1
    divs = f(n)
    if len(divs) > 0:
        print(n, divs[0])
        k += 1
    
