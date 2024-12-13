t = [int(e) for e in open('./17-ya-04.txt')]
# макс полож элем — пятизначн оканчивается на 17
mx = max(e for e in t if (e>0) and (len(str(e))==5) and (e%100==17))

lst = []
for i in range(len(t)-2):
    p = t[i:i+3]
    # хотя бы один из трёх элементов оканчивается на 17
    u1 = len([e for e in p if abs(e)%100==17]) >= 1
    # сумма модулей элементов тройки не больше максимального
    u2 = sum([abs(e) for e in p]) <= mx
    if u1 and u2:
        lst += [sum(p)]

print(len(lst), min(lst))  # 243 -99023

# https://education.yandex.ru/ege/task/d5802159-70ca-4d5d-832c-9856d41c15a6
