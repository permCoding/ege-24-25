def f(A, x):
    return (x&91==0) or ((x&77==0) <= (x&A!=0))

for A in range(0, 100):
    b = True
    for x in range(0, 100):
        if f(A, x) == False:
            b = False
            break
    if b: print(A)

"""
https://education.yandex.ru/ege/task/e4ee1ff0-c06e-478d-b397-be872b454f46
"""
