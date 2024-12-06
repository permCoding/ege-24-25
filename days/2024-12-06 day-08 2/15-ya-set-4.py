def f(x):
    u1 = ((x not in B) and (x in Q)) <= (x in B)
    u2 = ((x not in Q) and (x in P))
    return (x not in R) <= ((x in P) or u1 or u2)

P = [e for e in range(256) if bin(e).count('1')%2==0]
Q = [e for e in range(256) if f'{e:b}'.rjust(8, '0')[:2]=='10']
R = [e for e in range(256) if f'{e:b}'.rjust(8, '0')[5:]=='101']

B = []
for x in range(256):
    if f(x) == False:
        B += [x]
print(len(B), B)

"""
https://education.yandex.ru/ege/task/02da09ba-9555-44ca-936b-b3b73582dffd

00000000   0
00000001   1
...      ...
11111110 254
11111111 255
"""
