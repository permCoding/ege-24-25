# https://education.yandex.ru/ege/task/cd3c4d7c-cce1-4818-a4fc-b0f79a867e13

s = open('./24.txt').readline()
P = '#'
ln = 0
mx_ln = 0
for i in range(len(s)):
    if s[i] != P:
        ln += 1
        mx_ln = max(mx_ln, ln)
    else:
        ln = 1
    P = s[i]
print(mx_ln)  # 32
