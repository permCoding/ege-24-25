
f = open('./test.txt')
lines = f.readlines()
nums = []
for line in lines:
    nums.append(int(line))
print(nums)

# for smb in s:
#     print(smb, ord(smb))