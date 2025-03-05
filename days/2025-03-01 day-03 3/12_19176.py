k = 0
s = 200 * '*'
while '****' in s or '???' in s:
    if "****" in s:
        s = s.replace('****', '???', 1)
        k += 3
    s = s.replace('??', '*', 1)
print(s, k)  # **? 237
