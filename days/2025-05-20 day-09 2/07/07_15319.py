from math import log2, ceil

al = 7026
k = ceil( log2(7026) )
r = 2764 * 1793 * k
p = 148 * r  # bit
v = 18_349_566  # bit/sec

print(p / v)
