from fnmatch import *

for i in range(2023, 10**10, 2023):
    s = str(i)
    if fnmatch(s, '1?2139*4'):
        print(i, i//2023)

import re 

for i in range(2023, 10**10, 2023):
    if re.match(r'^1.2139.*4$', str(i)):
        print(i, i//2023)
