from re import finditer

s = '**9*7**97-890987-89978909-97079**-0*99'

num = r'(0|[789][0789]*)'

mx_len = 0
for match in finditer(num, s):
    mx_len = max(mx_len, len(match.group()))

print(mx_len)
