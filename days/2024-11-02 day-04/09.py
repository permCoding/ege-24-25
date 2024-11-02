f = open('09.csv')

k = 0
for s in f:
    t = s.split(';')
    nums = [int(e) for e in t]
    np, nn = [], []
    for e in nums:
        if nums.count(e) > 1:
            np.append(e)
        else:
            nn.append(e)
    u1 = (len(np) == 3) and (len(nn)==3)
    u2 = sum(np) > sum(nn)
    if u1 and u2:
        k += 1
print(k)

""" 6 чисел
– в строке только одно число повторяется трижды,
  остальные числа различны;
– квадрат суммы всех повторяющихся чисел строки
  больше квадрата суммы неповторяющихся чисел.
"""
