# https://education.yandex.ru/ege/task/4a723df3-ea35-4f64-bba3-afda2c8fb879

s = open('./24.txt').readline()
for n in range(1, 100):
    if s.find(n*'Z') > -1:
        print(n)
        
# 'X' = 12 - ответ
# 'Y' = 11
# 'Z' = 11