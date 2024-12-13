t = [int(e) for e in open('./17-ya-06.txt')]
# минимальный положительный двузначный элемент последовательности
mn = min(e for e in t if (e>0) and (9<e<100))

lst = []
for i in range(len(t)-1):
    p = t[i:i+2]
    # хотя бы один из элементов не содержит в записи минимальный
    if len([e for e in p if str(mn) not in str(e)]) > 0:
        lst += [abs(p[0]-p[1])]
            
print(len(lst), min(lst))  # 24377 124

# https://education.yandex.ru/ege/task/3394b7d7-51c4-434a-8c09-16c4f01beaa7
