c = 8  # bit/px => 256 colors
r = 1280 * 960 * c * 24  # bit
v = 1_392_640  # bit/sec
t = 180  # sec

print(r / v)
