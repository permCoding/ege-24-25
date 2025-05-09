def f(n):
    t = set()
    for d in range(1, n//2):
        if n%d == 0:
            t.add(d)
            t.add(n//d)
    return sum(t)

k = 0
n = 500_000
while k < 5:
    n += 1
    r = f(n)
    if r%10 == 6:
        print(n, r)
        k += 1
"""
500032 1070356
500035 606816
500039 501456
500050 949716
500052 1333696
"""