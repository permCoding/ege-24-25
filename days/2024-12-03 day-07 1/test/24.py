# https://education.yandex.ru/ege/task/98ae80c8-1e05-4cad-b4cc-4adc1edcc487

s = open('./24.txt').readline()

s = s.replace('SQRP', '****')
for n in range(1, 99):
    if n*'****' in s:
        print(n)  # 12

q = 12*'****'
pos = 0
while s.find(q, pos) > -1:
    pos = s.find(q, pos)
    print(s[pos-4:pos+48+4])
    pos += 48

# QRSP************************************************SQRQ
# ответ: 48+4 = 52