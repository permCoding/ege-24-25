k = 0
for n in range(1000, 9999+1):
    t = [int(e) for e in str(n)]
    if len(set(t)) == 4:
        u1 = t[0]%2 != t[1]%2
        u2 = t[1]%2 != t[2]%2
        u3 = t[2]%2 != t[3]%2
        if u1 and u2 and u3:
            k += 1
print(k)
