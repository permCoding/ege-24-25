k = 0
for line in open('./09-20899.csv'):
    t = sorted(int(e) for e in line.split(';'))
    if t[-1] < sum(t[:3]):
        if len(set(t)) == 3:
            k += 1
print(k)  # 138

"""
 2 4 2 3 => 2 4 3
 1 4 2 3 => 1 2 4 3
 2 4 2 4 => 2 4 
 2 2 2 3 => 2 3
"""