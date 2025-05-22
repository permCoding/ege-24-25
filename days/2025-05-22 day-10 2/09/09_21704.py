t = [list(map(int , e.split(';'))) for e in open('09_21704.csv')]

for e in t:
    s = sorted(e, reverse=True)
    if s == e:
        if (s[0]+s[-1])/2 > sum(s[1:-1])/5:
            print(sum(e))  # ____
            break
