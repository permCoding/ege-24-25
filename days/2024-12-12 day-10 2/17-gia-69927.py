t = [int(line) for line in open('./69927.txt')]

cnt = len([elm for elm in t if elm%32==0])

amount = 0
mx = -100_000
for i in range(len(t)-1):
    if t[i] < 0 or t[i+1] < 0:
        if t[i] + t[i+1] < cnt:
            amount += 1
            mx = max(mx, t[i]+t[i+1])
print(amount, mx)  # 5897 357
