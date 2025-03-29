# 10 1024
# 11 2048
# 12 4096
# 13 8192
#    7026
n = 13  # bit
bit_per_img = 2764 * 1793 * n
bit_per_pkg = bit_per_img * 148
v = 18_349_566  # bit/sec
t = bit_per_pkg / v
print(t)
