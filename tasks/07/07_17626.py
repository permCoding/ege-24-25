c = 10  # bit/px => 1024 colors
k = 39
r = 1280 * 1024 * c * k  # bit
v = 1_966_080  # bit/sec
t = 280  # sec

print(r / v)
