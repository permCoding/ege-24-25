from math import ceil, log2


len_sn = 248

for len_al in range(120, 140):
    bit_per_smb = ceil(log2(len_al))
    byte_per_sn = ceil(bit_per_smb * len_sn / 8)
    byte_all = 75_600 * byte_per_sn
    size = 16 * 1024 * 1024

    print(len_al, byte_all, size)
# 129