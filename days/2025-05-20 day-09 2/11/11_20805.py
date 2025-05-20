from math import ceil

k = 8  # min=129 .. max=256
n = 248
sn = ceil(k * n / 8)

print(75_600 * sn)
print(16 * 1024 * 1024)
