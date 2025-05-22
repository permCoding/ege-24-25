t = [list(map(int , e.split(';'))) for e in open('09_21895.csv')]

amount = 0
for e in t:
    if len(set(e)) == 5:
        s = sorted(e)
        if sum(s[3:]) <= sum(s[:3]):
            amount += 1
print(amount)  # 1922
