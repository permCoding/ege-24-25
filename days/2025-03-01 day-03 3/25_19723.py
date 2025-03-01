# mask = 10?451*3

# 1 - 1 sec
# for n in range(451, 10**9, 451):
#     s = str(n)
#     if s[:2] == '10' and s[3:6] == '451' and s[-1] == '3':
#         print(n, n//451)

# 2 - 4.5 sec
# from fnmatch import fnmatch

# for n in range(451, 10**9, 451):
#     s = str(n)
#     if fnmatch(s, '10?451*3'):
#         print(n, n//451)

# 3 - 2.4 sec
from re import match

for n in range(451, 10**9, 451):
    s = str(n)
    if match(r'^10.451.*3$', s):
        print(n, n//451)
