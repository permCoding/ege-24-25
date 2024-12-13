t = [int(e) for e in open('./68279.txt')]

mx = max(e for e in t if e%1_000 == 562)

lst = []
for i in range(len(t)-3):
    p = t[i],t[i+1],t[i+2],t[i+3]
    u1 = any(len(str(e))==5 for e in p) and (len([e for e in p if len(str(e))!=5]) > 1)
    u2 = len([e for e in p if e%3==0]) < len([e for e in p if e%7==0])
    u3 = mx < sum(p) < 2*mx
    if u1 and u2 and u3:
        lst += [sum(p)]

print(len(lst), max(lst))  # 229 154334
