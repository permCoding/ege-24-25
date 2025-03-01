import math
ln = 377
bt = 6
byte_on_sn = math.ceil(ln * bt / 8)
print(byte_on_sn)
count_sn = 23_155
print(byte_on_sn * count_sn / 1_024 > 5_536)
print(33)

# 19155

# _ _ _ _ _ => 32

# _ _ _ _ _ _ => 33 .. 64