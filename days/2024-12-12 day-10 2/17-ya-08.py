t = [int(e) for e in open('./17-ya-08.txt')]

mx = max(e for e in t if len(str(e))==3)

lst = []
for i in range(len(t)-1):
    p = t[i:i+2]
    if len([e for e in p if len(str(e))==3]) == 1:
        if sum(p)%mx == 0:
            lst += [sum(p)]
            
print(len(lst), max(lst))  # 502 461538

# время решения 5 минут

# https://education.yandex.ru/ege/task/e06271bc-14a7-40fc-8c96-b0648da4b219
