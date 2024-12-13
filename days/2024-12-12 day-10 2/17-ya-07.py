t = [int(e) for e in open('./17-ya-07.txt')]

lst = []
for i in range(1, len(t)-2):
    a = t[i:i+2]  # внутренние
    b = [t[i-1], t[i+2]]
    if a[0]*a[1] > b[0]*b[1]:
        lst += [a]

print(max(sum(e) for e in lst))  # 19703

avg = sum(t) / len(t)
amount = 0
for pair in lst:
    if pair[0]>avg or pair[1]>avg:
        amount += 1
print(amount)  # 3103
# количество таких из них, в которых есть хотя бы одно число
# большее среднего арифметического всех чисел в файле

# https://education.yandex.ru/ege/task/ad327404-5a19-4231-a238-c95270a529c3
