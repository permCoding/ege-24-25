from re import finditer

# s = '101010778216660911384226316342709330270944'
s = open('./24_19887.txt').readline()

max_len = 0
cur_len = 1
for i in range(0, len(s)-1):
    if int(s[i])%2 != int(s[i+1])%2:
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 1
print(max_len)  # 22
