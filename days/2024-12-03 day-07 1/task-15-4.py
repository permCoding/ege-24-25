def f(A, x):
    return (x&91==0) or ((x&77==0) <= (x&A!=0))

for A in range(0, 200):
    if all(f(A, x) for x in range(0, 200)):
        print(A)
        break

"""
https://education.yandex.ru/ege/task/e4ee1ff0-c06e-478d-b397-be872b454f46
"""
