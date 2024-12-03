
f = open('./test.txt')
s = f.read()
for smb in s:
    print(smb, ord(smb))