s = open('./24_19254.txt').readline()
f = 'FSRQ'
s = f + s + f

a = []
pos = 0
while s.find(f, pos) > -1:
    pos = s.find(f, pos)
    a.append(pos)
    pos += 4

r = [(a[i+81]+3)-(a[i]+1) for i in range(len(a)-81)]
print(max(r))

""" 2379
FSRQ - 80 раз

FSRQ AA FSRQ AA FSRQ AAA FSRQ
0123 45 6789 01 2345 678 9012
0       1       2        3
"""