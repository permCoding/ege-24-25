def f(a, b):
    return int(a)%2 != int(b)%2

amount = 0
for n in range(1000, 10000):
    s = str(n)
    if len(set(list(s))) == 4:
        if f(s[0],s[1]) and f(s[1],s[2]) and f(s[2],s[3]):
            amount += 1
print(amount)  # 720
