# https://education.yandex.ru/ege/task/73ae4ec6-cd41-42bb-afd7-e6f2b9768217

s = open('./24.txt').readline()

s = s.replace('DOG', '###')
for n in range(1, 99):
    if n*'###' in s:
        print(n)  # 2

q = 2*'###'
pos = 0
while s.find(q, pos) > -1:
    pos = s.find(q, pos)
    print(s[pos:pos+6+3])
    pos += len(q)

# ######DET
# ответ: 6+1 = 7