# https://education.yandex.ru/ege/task/be6320e9-640c-4273-9a51-a8ff2a9863e9

s = open('./24.txt').readline()

k = 0
for i in range(len(s)-2):
    x,y,z = s[i],s[i+1],s[i+2]
    if (x in 'ABC') and (y in 'CDE') and (z in 'BCDF'):
        if len(set([x,y,z])) == 3:
            k += 1
print(k)  # 10102
