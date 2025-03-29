from math import ceil, log2


len_id = 5

len_al = 10 + 7084
bit_per_smb = ceil(log2(len_al))
bit_per_id = len_id * bit_per_smb
byte_per_id =  ceil(bit_per_id / 8)

print(byte_per_id * 22_528 / 1_024)
