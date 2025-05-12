c = 13  # bit/px <== 8192 colors
k = 160
r = 1024 * 960 * c * k  # bit
v = 14_680_064  # bit/sec
# t = ?  # sec

print(r / v)  # 139
