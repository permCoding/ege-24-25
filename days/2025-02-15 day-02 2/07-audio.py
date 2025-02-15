# 19697
p = 1 * 18 * 64_000  # bit / sec
t = 68  # sec
s = p * t
v = 204_000  # bit / sec
print(s / v)  # 384 sec

# 19558
s = 4 * 124_000  # bit / sec
v = 840 * 1_024 * 8  # bit / sec
print(v / s)  # bit

# 19556
s = 2 * 48_000 * 18  # bit
f = 196 * 1_024 * 1_024 * 8  # bit
t = f / s
print(t / 60)  # 16

# 18872
t = 7 * 60  # sec
p = 4 * 16 * 48_000  # bit / sec
s = p * t
v = 3 * 1_024 * 8  # bit / sec
print(s / v / 60 / 60)  # 14
