# https://education.yandex.ru/ege/task/8337d1c9-9cbc-4ff8-ac40-ce04ba5dd256

s = open('./24.txt').readline()
for n in range(1, 100):
    if s.find(n*'Y') > -1:
        print(n)
        
# 'Y' = 11
