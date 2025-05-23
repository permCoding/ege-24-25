t = [int(e) for e in open('./17_17558.txt')]
x = len([1 for n in t if n%32==0])

k, lst = 0, []
for i in range(len(t)-1):
    if t[i]<0 or t[i+1]<0:
        if t[i] + t[i+1] < x:
            k += 1
            lst.append(t[i] + t[i+1])

print(k, max(lst))  # 4969 299
