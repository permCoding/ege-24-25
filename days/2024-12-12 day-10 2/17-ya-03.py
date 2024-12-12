t = [int(e) for e in open('./17-ya-03.txt')]
# квадрат минимального трёхзначного числа, оканчивающегося на 8
q = [e for e in t if len(str(abs(e)))==3 and str(e)[-1]=='8']

kv = min(q)**2

lst = []
for i in range(len(t)-2):
    p = t[i:i+3]
    if len([e for e in p if e**2>kv]) == 2:
        if len([e for e in p if len(str(abs(e)))==3]) > 0:
            lst += [sum(p)]

print(len(lst), max(lst))  # 5312 20235

# https://education.yandex.ru/ege/task/1c1fd299-2d3b-46e0-835d-a8416ecc37c8
