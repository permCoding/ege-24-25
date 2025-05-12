c = 13  # bit/px <== 8192 colors
k = 32  # 32
r = 1024 * 960 * c * k  # bit
v = 1_474_560  # bit/sec
t = 280  # sec

print(r / v)
