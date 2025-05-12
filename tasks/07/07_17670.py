c = 6  # bit/px => 64 colors
r = 1024 * 960 * c * 32  # bit
v = 1_474_560  # bit/sec
t = 140  # sec

print(r / v)
