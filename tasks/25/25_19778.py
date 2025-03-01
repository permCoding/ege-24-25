def get_divs(n):
    st = set()
    for d in range(2, int(n**.5)+1):
        if n%d == 0:
            st.add(d)
            st.add(n//d)
    return st

i = 9_500_000
k = 0
while k < 5:
    i += 1
    divs = [d for d in get_divs(i) if len(get_divs(d))==0]
    F = 0
    if len(divs) > 0:
        F = sum(divs) // len(divs)
        if F % 813 == 0:
            k += 1
            print(i, F)
    