size = 2_138_400 * 10 * 60  # bit

for n in range(1, 50):
    bit_per_img = 1920 * 1080 * n
    bit_per_pck = bit_per_img * 57
    if bit_per_pck <= size: continue
    print(n)  # 11 bit
    break

"""
10 bit -  513 .. 1024
11 bit - 1025 .. 2048
"""