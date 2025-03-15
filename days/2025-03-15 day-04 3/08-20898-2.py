# 2 - product
from itertools import product

cnt = 0
z = ['10','30','50','70','90','09','07','05','03','01']
for tpl in product('012345678', repeat=5):
    s = ''.join(tpl).lstrip('0')
    if len(s) == 5 and s.count('0') == 1:
        if all((test not in s) for test in z):
            cnt += 1
print(cnt)


# s = '00231'
# print(s)
# print(s.lstrip('0'))