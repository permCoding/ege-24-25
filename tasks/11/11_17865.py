import math
smbs = 10 + 52 + 52 + 963  # 1077
bit_per_smb = 11
n = 257

bytes = math.ceil(n * bit_per_smb / 8)  # bytes
print(bytes * 2_000)
print(693 * 1024)

# print(bts)