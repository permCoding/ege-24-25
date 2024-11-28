def ex_01():
    def f(n):
        k[0] += 1
        # print('*')
        if n >= 1:
            # print('*')
            k[0] += 1
            f(n - 1)
            f(n // 2)

    k = [0]
    f(40)
    print(k)  # 12370

def ex_02():
    def f(n):
        k = 1
        if n >= 1:
            k += 1 + f(n-1) + f(n//2)
        return k

    print(f(40))  # 12370

ex_01()
ex_02()
