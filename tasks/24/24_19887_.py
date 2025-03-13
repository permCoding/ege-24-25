from re import finditer

# s = '101010778216660911384226316342709330270944'
s = open('./24_19887.txt').readline()

s = s.replace('1','Y').replace('3','Y').replace('5','Y').replace('7','Y').replace('9','Y')
s = s.replace('0','X').replace('2','X').replace('4','X').replace('6','Y').replace('8','X')

# reg = '((XY)+X?)'
# reg = '((YX)+Y?)'
# reg = '(Y?(XY)+X?)'
reg = '(X?(YX)+Y?)'

mx_len = 0
for match in finditer(reg, s):  # совпадения
    m = match.group()
    # print(m)
    mx_len = max(mx_len, len(m))

print(mx_len)
