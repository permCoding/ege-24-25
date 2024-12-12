t = [int(e) for e in open('./17-ya-02.txt')]

mx = max(e for e in t if e%100==47)

lst = []
for i in range(len(t)-3):
    p = t[i:i+4]
    if sum(p) <= mx:
        if len([e for e in p if e>1_000]) == 2:
            lst += [sum(p)]

print(len(lst), max(lst))  # 154 3946

# https://education.yandex.ru/ege/task/34b173cc-cdfe-4098-bd0d-f7ae3ed241d5
