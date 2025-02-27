def get(n):
    st = set()
    for d in range(1, int(n**.5)+1):
        if n%d == 0:
            st.add(d)
            st.add(n//d)
    return sorted(st)

for n in range(178965, 178983):
    divs = get(n)
    if len(divs) == 4:
        print(*divs[::-1])
