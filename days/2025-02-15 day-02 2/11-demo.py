import math

_alph = 10 + 52 + 963  # 11 bit
# print(_alph)
k = 257
s_sn = k * 11
s_sn_byte = math.ceil(s_sn / 8)

print(s_sn_byte)  # 354 byte

n_sn = 2_000
print(n_sn * s_sn_byte / 1_024)
