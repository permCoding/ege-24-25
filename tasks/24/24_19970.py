from re import finditer

# s = '44085*0*97899*0*5+62586+0*16263+6206050*165'
s = open('./24_19970.txt').readline()

num = '(0|5|[1-9][0-9]*[05])'
exp = f'{num}([+*]{num})+'

mx_len = 0
for match in finditer(exp, s):  # совпадения
    mx_len = max(mx_len, len(match.group()))

print(mx_len)
