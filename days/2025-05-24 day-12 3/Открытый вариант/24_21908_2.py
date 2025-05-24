from re import findall

s = open('./24_21908.txt').readline()

ptn = '[1-9A-D][0-9A-D]*[02468AC]'

t = []
for e in findall(ptn, s):
    t += [len(e)]

print(max(t))
