def f(x):
    return x%30==0 or 15%x==0

x = 1
while True:
    x += 1
    if f(x):
        print(x)  # 3
        break
    

"""
https://education.yandex.ru/ege/task/60b92a6e-42d8-4735-ad22-873370e8d5c7
"""