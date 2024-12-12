t = [int(e) for e in open('./17-ya-01.txt')]

smp = sum(e for e in t if e > 0)
print( abs(smp - abs(sum(t)-smp)) )
# https://education.yandex.ru/ege/task/95518ac1-1c44-49de-b8bf-ff2b02e092a7
