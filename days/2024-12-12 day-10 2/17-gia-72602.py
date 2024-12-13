t = [int(e) for e in open('72602.txt')]
mn, mx = min(t), max(t)

lst = []
for i in range(len(t)-1):
    a, b = t[i], t[i+1]
    if (a%3 == mx%3) or (b%3 == mx%3):
        if (a%7 == mn%7) or (b%7 == mn%7):
            lst += [a+b]

print(len(lst), max(lst))  # 1467 197700
