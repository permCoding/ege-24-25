# https://education.yandex.ru/ege/task/5245b774-6835-45ef-b4e6-0847e41b939e

s = open('./24.txt').readline()
s = s.replace('AA', '##').replace('CC', '##').replace('##', 'p')
for n in range(1, 100):
    if s.find(n*'p') > -1:
        print(n)
        
# 5
