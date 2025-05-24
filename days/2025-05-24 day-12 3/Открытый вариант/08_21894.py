amount = 0
for n in range(1000, 10_000):
    s = str(n)
    if len(set(s)) == 4:
        u1 = int(s[0])%2 != int(s[1])%2
        u2 = int(s[2])%2 != int(s[1])%2
        u3 = int(s[2])%2 != int(s[3])%2
        if u1 and u2 and u3:
            amount += 1

print(amount)  # 720
