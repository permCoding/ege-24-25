s = 'T' + open('./24_10105.txt').readline() + 'T'

a = []
for i in range(len(s)):
    if s[i] == 'T':
        a.append(i)

mx = 0
for i in range(len(a)-101):
    r = a[i+101] - a[i] - 1
    mx = max(mx, r)

print(mx)  # 133

# 0     1 2   3
# T OOO T T O T
# 0 123 4 5 6 789
# 838