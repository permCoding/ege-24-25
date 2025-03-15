# 2 - product
from itertools import product
from re import search

# cnt = 0
# reg = '[13579]0|0[13579]'

# for tpl in product('012345678', repeat=5):
#     s = ''.join(tpl).lstrip('0')
#     if len(s) == 5 and s.count('0') == 1:
#         if not(search(reg, s)):
#             cnt += 1
# print(cnt)  # 5120

"""
s = '9023404'
reg_l = '.*[13579][0].*'
reg_r = '.*[0][13579].*'
if match(reg_l, s): print('left')
if match(reg_r, s): print('right')
s = '8023407'
reg = '[13579]0|0[13579]'
print(search(reg, s))
"""