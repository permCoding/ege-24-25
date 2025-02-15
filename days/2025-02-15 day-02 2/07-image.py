# 20185
s = 6580 * 3240 * 11  # bit
v = 3_964_685 * 8  # bit / sec
t = 510  # sec

n = 68
print(s * n / v)  # 68
print(t * v / s)  # 68

# s = v * t
# s*n / v <= t 

# 19876

s = 3440 * 2880 * 12  # bit
print(s / (8*1_024*1_024))  # 15 Mb

# 19571
k = 8 * 1024 * 1024 * 1024 * 8  # bit
s = 3840 * 2160 * 16 * 2  # bit
n = k // s  # 258 - фото на 1 карту
amount = 2 * n + 45
print(n, amount)  # 57
