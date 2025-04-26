mx = 0
for x in range(1, 3001):
    dec = 4**210 + 4**110 - x
    cnt0 = 0
    while dec > 0:
        if dec%4 == 0: cnt0 += 1
        dec //=4
    if cnt0 == 105: print(x)
    mx = max(mx, cnt0)
print(mx)
# 1024