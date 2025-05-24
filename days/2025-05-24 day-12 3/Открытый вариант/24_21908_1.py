s = open('./24_21908.txt').readline()

al = ''.join([chr(i) for i in range(69,91)])
ch = '02468AC'

for e in al: s = s.replace(e, '#')

t = []
for w in s.split('#'):
    e = w.lstrip('0')
    if e != '' and (e[-1] in ch):
        t.append(e)

q = sorted(t, key=lambda x: len(x))
print(q[-1], len(q[-1]))


# res = max(t, key=lambda e: int(e, 14))
# print(res, len(res))




# print(al)
# print(len(s))

# s = '000078969912PMN389BBA700303WWW0ABE000078A69912'
# al = '0123456789ABCD'