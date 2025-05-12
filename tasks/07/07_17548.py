c = 11  # bit/px <== 2048 colors
k = 2497  # 2497
r = 1024 * 960 * c * k  # bit
v = 96_468_992  # bit/sec
t = 280  # sec

print(r / v)
