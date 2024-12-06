t = list(range(22, 71))
t.remove(26)
t.remove(40)
cnt = 0
for e in t:
    if e//10 + e%10 > 5:
        cnt += 1
print(cnt)  # 40


"""
https://education.yandex.ru/ege/task/0721cb7f-43fe-4b69-ab81-31e482c3e8a9
"""