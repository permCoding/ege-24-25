t = [int(e) for e in open('./17.txt')]
m = min(e for e in t if e%2025 == 0)
# print(m)
amount = 0
max_sum = 0
for i in range(len(t)-2):
    if t[i]%m==0 or t[i+1]%m==0 or t[i+2]%m==0:
        sm = t[i]+t[i+1]+t[i+2]
        if 100000<=sm<=999999:
            amount += 1
            max_sum = max(max_sum, sm)
print(amount, max_sum)
