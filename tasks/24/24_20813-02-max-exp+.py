from re import finditer

# s = '**9*7**97-890987-89978909-97079**-0*99'
s = open('./24_20813.txt').readline()

num = '(0|[789][0789]*)'
exp = f'{num}([-*]{num})+'

mx_len = 0
for match in finditer(exp, s):  # совпадения
    mx_len = max(mx_len, len(match.group()))

print(mx_len)  # 111
