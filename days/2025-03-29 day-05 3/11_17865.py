import math

for len_sn in range(1, 1_000):
    alph = 10 + 52 + 963
    bit_per_smb = math.ceil(math.log2(alph))

    byte_per_sn = math.ceil(len_sn * bit_per_smb / 8)

    if byte_per_sn * 2_000 <= 693 * 1024: continue
    print(len_sn-1)
    break
