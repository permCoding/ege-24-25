k = 0
for line in open('./09-17968.csv'):
    t = [int(e) for e in line.split(';')]
    mx = max(t)
    if mx < sum(t)-mx:
        if sum(e for e in t if e%2==0) == sum(e for e in t if e%2!=0):
            k += 1
print(k)  # 13

"""
– наибольшее из четырёх чисел меньше суммы трёх других
– сумма чётных чисел равна сумме нечётных
"""
