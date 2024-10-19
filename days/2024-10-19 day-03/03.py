
f = open('./test.txt')
s = f.read()

lines = s.split(chr(10))

print(lines)

# for smb in s:
#     print(smb, ord(smb))