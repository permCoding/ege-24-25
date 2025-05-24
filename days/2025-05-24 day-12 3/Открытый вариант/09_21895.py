amount = 0
for e in open('./9_21895.csv'):
    t = sorted(map(int, e.split(';')))
    if len(set(t)) == 5:
        if sum(t[3:]) <= sum(t[:3]):
            amount += 1

print(amount)  # 1922
