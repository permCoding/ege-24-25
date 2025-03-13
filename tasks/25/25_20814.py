def get(n):
    st = set()
    for d in range(2, int(n**.5)+1):
        if n%d == 0:
            st.add(d)
            st.add(n//d)
    return sum(st)

n = 500_000
k = 0
while k < 5:
    n += 1
    R = get(n)
    if R % 10 == 9:
        k += 1
        print(n, R)
