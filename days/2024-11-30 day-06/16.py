def f(n):
    r['amount'] += 1
    # print('*')
    if n >= 1:
        # print('*')
        r['amount'] += 1
        f(n - 1)
        f(n // 2)


r = {'amount': 0}
f(40)
print(r)
