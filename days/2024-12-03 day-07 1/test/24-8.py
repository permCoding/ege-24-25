# https://education.yandex.ru/ege/task/97e2f438-d6ce-4c55-95f5-8384f58faea4

s = open('./24.txt').readline()

r = ''
mx = 0
for i in range(len(s)):
    if s[i] in '0123456789':
        r += s[i]
        mx = max(mx, int(r))
    else:
        r = ''
print(mx)  # 5763859