import re

s = open('./24_21908.txt').readline()

ptn = '[1-9A-D][0-9A-D]*[02468AC]'

ln = 0
for m in re.findall(ptn, s):
    ln = max(ln, len(m))
print(ln)  # 2598
