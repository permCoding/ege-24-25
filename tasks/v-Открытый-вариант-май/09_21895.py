k = 0
for e in open('./09_21895.csv'):
    t = sorted(int(w) for w in e.split(','))
    if len(set(t)) == 5:
        if sum(t[3:]) <= sum(t[:3]):
            k += 1

print(k)
