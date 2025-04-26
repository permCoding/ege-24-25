for e in open('./9_21704.csv'):
    t = list(map(int, e.split(';')))
    s = sorted(t, reverse=True)
    if t == s and (s[0]+s[-1])/2 > sum(s[1:-1])/5:
        print(sum(t))  # 652
        break