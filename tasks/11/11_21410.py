from math import ceil

bt = 3  # => 8 символов
sn = 257
byte_on_sn = ceil(sn * bt / 8)
n = 295_740
print(n * byte_on_sn)
print(33*1024*1024)