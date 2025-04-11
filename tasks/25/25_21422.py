def f(n):
    st = set()
    for d in range(2, int(n**.5)+1):
        if n%d == 0:
            st.add(d)
            st.add(n//d)
    return [e for e in sorted(st) if e%10==7 and e!=7]

k = 0
n = 1_125_000
while k < 5:
    n += 1
    res = f(n)
    if len(res) > 0:
        print(n, res[0])
        k += 1

# 1125003 467
# 1125006 97
# 1125009 17
# 1125011 3187
# 1125012 177