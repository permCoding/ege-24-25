mx_k = 0
for x in range(1, 3000):
    n = 4**210 + 4**110 - x
    k = 0
    while n > 0:
        ost = n % 4
        if ost == 0: k += 1
        n //= 4
    if k == 105: print(x)
    mx_k = max(mx_k, k)
print(mx_k)
