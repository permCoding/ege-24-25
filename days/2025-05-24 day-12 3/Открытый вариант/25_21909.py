def f(n): 
    st = set()
    for d in range(1, n//2):
        if n%d == 0:
            st.add(d)
            st.add(n//d)
    return sum(st)

k = 0
n = 500_000
while k < 5:
    n += 1
    R = f(n)
    if R%10 == 6:
        k += 1
        print(n, R)

"""
500032 1070356
500035 606816
500039 501456
500050 949716
500052 1333696
"""