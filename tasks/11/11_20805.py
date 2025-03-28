import math

alph = 129  # 129 .. 256   128 -> 7 bit
bit_per_smb = 8
n = 248
bytes_per_sn = math.ceil(n * bit_per_smb / 8)

print(bytes_per_sn * 75_600)
print(16 * 1024 * 1024)
