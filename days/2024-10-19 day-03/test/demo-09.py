k = 0
for line in open('./demo_2025_9.csv'):
    t = [int(e) for e in line.split(';')]
    t3 = [e for e in t if t.count(e) == 3]
    t1 = [e for e in t if t.count(e) == 1]
    if len(t3) == 3 and len(t1) == 3:
        if sum(t3) > sum(t1): # **2 не обязательно
            k += 1
print(k)


""" 10 35
содержащей в каждой строке шесть натуральных чисел. 
Определите количество строк таблицы, содержащих
числа, для которых выполнены оба условия:
  – в строке только одно число повторяется трижды, 
    остальные числа различны;
  – квадрат суммы всех повторяющихся чисел строки больше 
    квадрата суммы всех её неповторяющихся чисел.
В ответе запишите только число.
"""