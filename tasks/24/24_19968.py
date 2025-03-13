from re import finditer

# s = '58+313+1030458*1770E802+693*542*771+4790A*3859'
s = open('./24_19968.txt').readline()

num = '(0|[1-5]+[0-5]*)'
exp = f'{num}([+*]{num})+'

mx_len = 0
for match in finditer(exp, s):  # совпадения
    m = match.group()
    # print(m)
    mx_len = max(mx_len, len(m))

print(mx_len)
